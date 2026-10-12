from __future__ import annotations

import re
from functools import lru_cache

from .common import SCHEMAS, load_json

TYPES = {
    "object": dict, "array": list, "string": str, "boolean": bool, "null": type(None),
}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
URI_RE = re.compile(r"^https?://[^\s/$.?#][^\s]*$")


@lru_cache(maxsize=None)
def load_schema(name: str):
    return load_json(SCHEMAS / name)


def _type_ok(value, t):
    if t == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if t == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    return isinstance(value, TYPES[t]) and not (t != "boolean" and isinstance(value, bool) and TYPES[t] is not bool)


def _resolve_ref(ref, doc_name):
    file, _, frag = ref.partition("#")
    name = file or doc_name
    node = load_schema(name)
    for part in [p for p in frag.split("/") if p]:
        node = node[part]
    return node, name


def validate(value, schema, doc_name, path="$"):
    """Yield (path, message) for every violation."""
    if schema is True or schema == {}:
        return
    if schema is False:
        yield path, "not allowed"
        return
    if "$ref" in schema:
        target, tname = _resolve_ref(schema["$ref"], doc_name)
        yield from validate(value, target, tname, path)
        rest = {k: v for k, v in schema.items() if k != "$ref"}
        if rest:
            yield from validate(value, rest, doc_name, path)
        return
    t = schema.get("type")
    if t is not None:
        ts = t if isinstance(t, list) else [t]
        if not any(_type_ok(value, x) for x in ts):
            yield path, f"expected {'/'.join(ts)}, got {type(value).__name__}"
            return
    if "const" in schema and value != schema["const"]:
        yield path, f"must equal {schema['const']!r}"
    if "enum" in schema and value not in schema["enum"]:
        yield path, f"must be one of {schema['enum']}, got {value!r}"
    if isinstance(value, str):
        if "minLength" in schema and len(value) < schema["minLength"]:
            yield path, f"shorter than {schema['minLength']} characters"
        if "maxLength" in schema and len(value) > schema["maxLength"]:
            yield path, f"longer than {schema['maxLength']} characters"
        if "pattern" in schema and not re.search(schema["pattern"], value):
            yield path, f"{value!r} does not match {schema['pattern']}"
        fmt = schema.get("format")
        if fmt == "date" and not DATE_RE.match(value):
            yield path, f"{value!r} is not a YYYY-MM-DD date"
        if fmt == "uri" and not URI_RE.match(value):
            yield path, f"{value!r} is not an http(s) URL"
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            yield path, f"below minimum {schema['minimum']}"
        if "maximum" in schema and value > schema["maximum"]:
            yield path, f"above maximum {schema['maximum']}"
    if isinstance(value, list):
        if "minItems" in schema and len(value) < schema["minItems"]:
            yield path, f"needs at least {schema['minItems']} item(s)"
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            yield path, f"allows at most {schema['maxItems']} item(s)"
        if schema.get("uniqueItems"):
            seen = []
            for v in value:
                if v in seen:
                    yield path, f"duplicate item {v!r}"
                seen.append(v)
        if "items" in schema:
            for i, v in enumerate(value):
                yield from validate(v, schema["items"], doc_name, f"{path}[{i}]")
    if isinstance(value, dict):
        for r in schema.get("required", []):
            if r not in value:
                yield path, f"missing required field '{r}'"
        props = schema.get("properties", {})
        for k, v in value.items():
            if k in props:
                yield from validate(v, props[k], doc_name, f"{path}.{k}")
            elif "additionalProperties" in schema:
                ap = schema["additionalProperties"]
                if ap is False:
                    yield f"{path}.{k}", "unknown field"
                elif isinstance(ap, dict):
                    yield from validate(v, ap, doc_name, f"{path}.{k}")
    for sub in schema.get("allOf", []):
        yield from validate(value, sub, doc_name, path)
    if "anyOf" in schema:
        if not any(not list(validate(value, s, doc_name, path)) for s in schema["anyOf"]):
            yield path, "does not match any allowed form"
    if "oneOf" in schema:
        n = sum(1 for s in schema["oneOf"] if not list(validate(value, s, doc_name, path)))
        if n != 1:
            yield path, f"must match exactly one allowed form (matched {n})"
    if "if" in schema:
        if not list(validate(value, schema["if"], doc_name, path)):
            if "then" in schema:
                yield from validate(value, schema["then"], doc_name, path)
        elif "else" in schema:
            yield from validate(value, schema["else"], doc_name, path)


def errors(value, schema_name: str):
    return list(validate(value, load_schema(schema_name), schema_name))
