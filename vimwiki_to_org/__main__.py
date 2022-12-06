from src.app import App
import argparse
from pathlib import Path
import os


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('-d',
                        '--wiki-path',
                        help="absolute path to vimwiki directory (optional)",
                        default=f"/home/{os.getlogin()}/vimwiki/",
                        type=str)

    parser.add_argument('-o',
                        '--output-path',
                        help="absolute path to output directory (optional)",
                        default="converted_files/",
                        type=str)

    args = parser.parse_args()
    import_path = Path(args.wiki_path).absolute()
    output_path = str(Path(args.output_path).absolute()) + os.sep
    App(import_path, output_path).run()


if __name__ == "__main__":
    main()
