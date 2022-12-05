from src.app import App
import os

if __name__ == "__main__":
    path = f"/home/{os.getlogin()}/vimwiki/"
    App(path).run()
