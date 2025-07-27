from configs import ids, edit_version, build_dir
from theme_edits import ThemeEdits
import os
import shutil
import subprocess

if __name__ == "__main__":
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir)
    edit_version()

    theme_edits = ThemeEdits()
    for cfg in ids:
        theme_edits.download(theme_edits.get_link(cfg), cfg)

    folders = (".config", ".fonts", ".local", ".var")
    files = (".fonts.conf", ".p10k.zsh", ".zshrc")
    os.makedirs(build_dir + "/etc/skel")

    for folder in folders:
        shutil.copytree(folder, f"{build_dir}/etc/skel/{folder}")
    for file in files:
        shutil.copy(file, f"{build_dir}/etc/skel/{file}")

    shutil.copytree("DEBIAN", build_dir + "/DEBIAN")

    subprocess.run(["dpkg-deb", "--build", build_dir])
    shutil.rmtree(build_dir)
