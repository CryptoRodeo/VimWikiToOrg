#!/usr/bin/env python3
from time import sleep, time


class ProgressBar:

    def __init__(self, total, width=50, msg="[Converting 🦄]:"):
        self.total = total
        self.width = width
        self.start = time()
        self.current_progress = 0
        if msg:
            print(f"{msg}")

    def progress(self):
        sleep(0.01)
        self.current_progress += 1
        bar_width_percent = self.width * ((self.current_progress) / self.total)
        bar = ("#" * int(bar_width_percent)) + ("-" * (self.width - int(bar_width_percent)))
        total_percentage = ((100 / self.width) * bar_width_percent)
        print(
            f"\r|{bar}| {total_percentage:.2f}% "
            f"[{self.current_progress} of {self.total}]",
            end="\r"
        )

    def __enter__(self):
        return self.progress

    def __exit__(self, type, value, traceback):
        end: float = time()
        print(f"\nFinished after {end - self.start: .3f} seconds.")
