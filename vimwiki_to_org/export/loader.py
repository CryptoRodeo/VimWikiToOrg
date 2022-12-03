#!/usr/bin/env python3
import glob, os

EXPORT_DIR = "./converted_files"
PLACEHOLDER = "<^>"
FILE_STORAGE = '{}/{}'.format(EXPORT_DIR, PLACEHOLDER)

class OrgExport:
    def __init__(self):
        self.pending_files = []


    def cache_file_data(self, file_location, content):
        _location = self.__generate_file_location(file_location)
        self.pending_files.append({
            "location": _location,
            "content": content,
        })

    def remove_old_files(self):
        for old_file in glob.glob("./{}/*.org".format(EXPORT_DIR)):
            try:
                os.remove(old_file)
            except OSError as e:
                print(e)

    def __generate_file_location(self, original_location):
        # assumes file location is in the form of /dir/dir/file.wiki
        file_name = original_location.split("/")[-1]
        new_file_name = file_name.replace('.wiki','.org')
        return FILE_STORAGE.replace(PLACEHOLDER, new_file_name)

    def export_files(self):
        for pending_file in self.pending_files:
            with open(pending_file["location"], "a+") as f:
                f.write(pending_file["content"])
