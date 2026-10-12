# Your art (optional)

The Teyvat Archive ships **no images**: character art belongs to HoYoverse. You can add your own pictures here for
your local SillyTavern, and the importer uses them automatically. Nothing in this folder is committed to git.

```
art/
  characters/
    arlecchino/        any .png, .jpg, .jpeg or .webp; if there are several, the newest one is used
    hu-taos-father/
  backgrounds/         chat backgrounds, copied into SillyTavern's backgrounds as they are
```

Folder names are the character's id without its prefix, in lowercase with hyphens (`character.arlecchino` ->
`arlecchino`, `npc.hu-taos-father` -> `hu-taos-father`). The easiest way is the **quill → Portrait** panel in the
desktop importer: it finds pictures, lets you crop them, and saves them in the right folder for you.

Character cards are PNG files, so JPEG/WebP pictures are converted to PNG by the importer (or by Pillow, if installed,
when you use the command-line installer).
