#!/usr/bin/env python3
#
import re, glob, os,sys,time
from transformers.vimwiki_to_org import convert
from helpers.stats import Stats

EXPORT_DIR = "./converted_files/"
PLACEHOLDER = "<^>"

class App:
    def __init__(self, wiki_dir_path):
        self._path_pattern = (wiki_dir_path + "*.wiki")
        self.cached_file_data = []
        self.stats = Stats()
        self.files = self.get_files()


    def run(self):
        self.remove_old_files()
        for progress_left in self.progressbar(self.files):
            self._perform_conversion()

        self.export_files()

    def log_file(self, file_name):
        self.stats.log_file(file_name)

    def _perform_conversion(self):
        for file_location in self.files:
            with open(file_location, 'r') as wiki:
                converted_content = convert(wiki.read())
                file_name = os.path.basename(file_location)
                self.cache_file_data(file_name, converted_content)

    def stats_data(self):
        return {
            "files_converted": self.stats.files_converted(),
            "total_runtime": self.stats.total_runtime(),
        }

    def get_files(self):
        return [ wiki for wiki in glob.glob(self._path_pattern) ]


    def cache_file_data(self, file_name, content):
        _location = self.__generate_file_export_location(file_name)
        self.cached_file_data.append({
            "location": _location,
            "content": content,
        })


    def remove_old_files(self):
        for old_file in glob.glob("./{}/*.org".format(EXPORT_DIR)):
            try:
                os.remove(old_file)
            except OSError as e:
                print(e)


    def __generate_file_export_location(self, file_name):
        # assumes file location is in the form of /dir/dir/file.wiki
        new_file_name = file_name.replace('.wiki','.org')
        return (EXPORT_DIR + new_file_name)


    def export_files(self):
        for pending_file in self.cached_file_data:
            with open(pending_file["location"], "a+") as f:
                f.write(pending_file["content"])


    def progressbar(self, total_files, prefix="[Converting 🦄]: ", size=60, out=sys.stdout):
        total_file_count = len(total_files)
        initial_idx = 0
        def display(file_idx):
            # Ensures that we never go over the specified size if
            # the number of items is greater than the size.
            size_limit = int( size * file_idx / total_file_count)
            files_done = ("#" * int(size*file_idx/total_file_count))
            files_left = ("."*(size-size_limit))

            output = "{}[{}{}] {}/{} files".format(prefix, files_done, files_left, file_idx, total_file_count)
            print(output, end='\r', file=out, flush=True)

        display(initial_idx)
        for idx, converted_file in enumerate(total_files):
            yield converted_file
            display(idx+1)

        # Prevent status bar from disappearing
        print("\nConversion complete 🫡", flush=True, file=out)
#


path = "/home/{user}/vimwiki/".format(user=os.getlogin())
App(path).run()
