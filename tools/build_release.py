#!/usr/bin/env python3
import shutil
import subprocess
import sys
import zipfile

import _cli
from archive_lib.common import BUNDLES, ROOT
from importer_app import APP_VERSION

NAME = "Teyvat Importer"
INCLUDE = ["sillytavern", "config", "data/indexes/character-index.json", "art/README.md", "LICENSE", "NOTICE", "README.md"]


def build_exe():
    build = ROOT / "build"
    ui = ROOT / "tools" / "importer_ui"
    subprocess.run([sys.executable, "-m", "PyInstaller", "--noconfirm", "--onefile", "--noconsole", "--name", NAME,
                    "--icon", str(ui / "icon.ico"), "--add-data", f"{ui}{';' if sys.platform == 'win32' else ':'}importer_ui",
                    "--paths", str(ROOT / "tools"), "--distpath", str(build / "dist"), "--workpath", str(build / "work"),
                    "--specpath", str(build), str(ROOT / "tools" / "importer_app.py")], check=True)
    exe = build / "dist" / (NAME + (".exe" if sys.platform == "win32" else ""))
    shutil.copy2(exe, ROOT / exe.name)
    return exe


def make_zip(exe):
    BUNDLES.mkdir(exist_ok=True)
    out = BUNDLES / f"Teyvat-Importer-v{APP_VERSION}-windows.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        z.write(exe, f"Teyvat Archive/{exe.name}")
        for item in INCLUDE:
            p = ROOT / item
            files = [p] if p.is_file() else sorted(x for x in p.rglob("*") if x.is_file())
            for f in files:
                z.write(f, f"Teyvat Archive/{f.relative_to(ROOT).as_posix()}")
    return out


def main():
    exe = build_exe()
    out = make_zip(exe)
    print(f"exe: {ROOT / exe.name}\nrelease zip: {out} ({out.stat().st_size / 1e6:.1f} MB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
