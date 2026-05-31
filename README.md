# Messages-Extractor

Extracts `*Messages*.xml` files from Wizard101's `Root.wad` archive into a local, revision-versioned directory.

## Requirements

- Python 3.13+
- [`katsuba`](https://github.com/vbe0201/katsuba) >= 0.4.0 — WAD archive reading
- [`uv`](https://github.com/astral-sh/uv) (recommended)

## Setup

With uv:

```bash
uv sync
```

Or with pip:

```bash
pip install katsuba>=0.4.0
```

## Usage

Set `GAME_PATH` in `main.py` to your Wizard101 installation directory, then run:

```bash
uv run main.py
```

Or with Python directly:

```bash
python main.py
```

Extracted files are written to `<revision>/messages/`, where `<revision>` is read from `Bin/revision.dat`.
