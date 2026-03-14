import os

from katsuba.wad import Archive # type: ignore


GAME_PATH: str = 'C:/ProgramData/KingsIsle Entertainment/Wizard101'


def get_revision(game_path: str) -> str:
    """Reads the game revision string from revision.dat.

    Args:
        game_path: Absolute path to the game's root installation directory.

    Returns:
        The revision string, or an empty string if the file is missing,
        empty, unreadable, or not valid UTF-8.
    """

    revision_path: str = os.path.join(game_path, 'Bin', 'revision.dat')

    try:
        with open(revision_path, 'r', encoding='utf-8') as revision_file:
            line: str = revision_file.readline().strip()

        if not line:
            print(f'WARNING: revision.dat is empty: {revision_path}')
            return ''

        return line

    except UnicodeDecodeError:
        print(f'ERROR: revision.dat is not valid UTF-8: {revision_path}')

    except OSError as exc:
        print(f'ERROR: Failed to read revision.dat: {exc}')

    return ''


def main() -> None:
    """Extracts all *Messages*.xml files from Root.wad into a versioned output directory."""

    revision: str = get_revision(GAME_PATH)

    root_wad_path: str = os.path.join(GAME_PATH, 'Data', 'GameData', 'Root.wad')
    archive: Archive = Archive.mmap(root_wad_path)

    output_dir: str = os.path.join(revision, 'messages')
    os.makedirs(output_dir, exist_ok=True)

    for file in archive.iter_glob('*Messages*.xml'):
        data: bytes = archive[file]
        output_path: str = os.path.join(output_dir, os.path.basename(file))

        with open(output_path, 'wb') as output_file:
            output_file.write(data)

        print(f'Extracted file: {output_path}')


if __name__ == '__main__':
    main()
