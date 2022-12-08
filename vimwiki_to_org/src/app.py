#!/usr/bin/env python3
#
import os
from vimwiki_to_org.src.converters.vimwiki_to_org import convert
from vimwiki_to_org.src.helpers.progress_bar import ProgressBar
from vimwiki_to_org.src.converters.helpers.prevention_tag import PREVENTION_TAG
from pathlib import Path


class App:

    def __init__(self, wiki_dir_path: Path, output_path: Path):
        # Keep the path object for globbing
        self.output_path = output_path
        # create regular path text for output directory
        self.output_dir = str(output_path) + os.sep

        self.cached_file_data = []
        self.files = [wiki for wiki in wiki_dir_path.glob('*.wiki')]

    def run(self):
        self.cleanup()

        with ProgressBar(len(self.files)) as progress:
            for file_location in self.files:
                with open(file_location, 'r') as wiki:
                    converted_content = convert(wiki.read())
                    file_name = os.path.basename(file_location)
                    self.cache_file_data(file_name, converted_content)

                    progress()

        self.export_files()

    def cache_file_data(self, file_name, content):
        # change file type
        _fname = file_name.replace('.wiki', '.org')
        # remove --converted tag
        content = content.replace(PREVENTION_TAG, '')
        self.cached_file_data.append({
            "location": (self.output_dir + _fname),
            "content": content,
        })

    def cleanup(self):
        for old_file in self.output_path.glob("*.org"):
            try:
                os.remove(old_file)
            except OSError as e:
                print(e)

    def export_files(self):
        for new_file in self.cached_file_data:
            with open(new_file["location"], "a+") as f:
                f.write(new_file["content"])
