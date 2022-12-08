import argparse
from pathlib import Path
from vimwiki_to_org.src.app import App
import os


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('-d',
                        '--wiki-path',
                        help="path to vimwiki directory (optional)",
                        default=f"/home/{os.getlogin()}/vimwiki/",
                        type=str)

    parser.add_argument('-o',
                        '--output-path',
                        help="path to output directory (optional)",
                        default=f"{Path('converted_files').absolute()}",
                        type=str)

    args = parser.parse_args()
    import_path = Path(args.wiki_path).absolute()
    output_path = Path(args.output_path).absolute()
    App(import_path, output_path).run()


if __name__ == "__main__":
    main()
