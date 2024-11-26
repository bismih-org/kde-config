from configs import ids
from theme_edits import ThemeEdits
import os
if __name__ == "__main__":
    os.removedirs("usr")
    theme_edits = ThemeEdits()
    for cfg in ids:
        theme_edits.download(theme_edits.get_link(cfg), cfg)