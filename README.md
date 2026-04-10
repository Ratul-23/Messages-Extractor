# Messages-Extractor

Extracts `*Messages*.xml` files from Wizard101's `Root.wad` archive into a local, revision-versioned directory.

## Requirements

- Python 3.x
- [`katsuba`](https://github.com/vbe0201/katsuba) — WAD archive reading

Install dependencies:

```bash
pip install katsuba
```

## Usage

Set `GAME_PATH` in `Main.py` to your Wizard101 installation directory, then run:

```bash
python main.py
```

Extracted files are written to `<revision>/messages/`, where `<revision>` is read from `Bin/revision.dat`.
