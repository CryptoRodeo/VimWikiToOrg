#!/usr/bin/env python3
#
import glob
import os
from src.transformers.vimwiki_to_org import convert
from src.helpers.progress_bar import ProgressBar

EXPORT_DIR = "./converted_files/"
PLACEHOLDER = "<^>"


class App:

    def __init__(self, wiki_dir_path):
        _glob_pattern = (wiki_dir_path + "*.wiki")
        self.cached_file_data = []
        self.files = [wiki for wiki in glob.glob(_glob_pattern)]

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
        _fname = file_name.replace('.wiki', '.org')
        self.cached_file_data.append({
            "location": (EXPORT_DIR + _fname),
            "content": content,
        })

    def cleanup(self):
        for old_file in glob.glob(f"{EXPORT_DIR}/*.org"):
            try:
                print(old_file)
                os.remove(old_file)
            except OSError as e:
                print(e)

    def export_files(self):
        for new_file in self.cached_file_data:
            with open(new_file["location"], "a+") as f:
                f.write(new_file["content"])
