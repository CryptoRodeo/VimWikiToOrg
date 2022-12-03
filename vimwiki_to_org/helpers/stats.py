#!/usr/bin/env python3

import time

class Stats:

    def __init__(self):
        self._file_names = []
        self._runtime = 0

    def log_file(self, file_name):
        self._file_names.append(file_name)

    def files_converted(self):
        return len(self._file_names)

    def record_runtime(self):
        start_time = time.time()
        self._runtime = (time.time() - start_time)

    def total_runtime(self):
        return ("{0:.10f} seconds".format(self._runtime))
