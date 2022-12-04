from src.app import App
import os

if __name__ == "__main__":
    path = "/home/{user}/vimwiki/".format(user=os.getlogin())
    App(path).run()
