import os
from modules.commonconstants import HOME, PWD

def kittyInstall():
    os.system("curl -L https://sw.kovidgoyal.net/kitty/installer.sh | sh /dev/stdin")
    os.system(f"ln -sf {HOME}/.local/kitty.app/bin/kitty {HOME}/.local/kitty.app/bin/kitten {HOME}/.local/bin/")
    os.system(f"cp {HOME}/.local/kitty.app/share/applications/kitty.desktop {HOME}/.local/share/applications/")
    os.system(f"cp {HOME}/.local/kitty.app/share/applications/kitty-open.desktop {HOME}/.local/share/applications/")
    os.system(f'sed -i "s|Icon=kitty|Icon=$(readlink -f {HOME})/.local/kitty.app/share/icons/hicolor/256x256/apps/kitty.png|g" {HOME}/.local/share/applications/kitty*.desktop')
    os.system(f'sed -i "s|Exec=kitty|Exec=$(readlink -f {HOME})/.local/kitty.app/bin/kitty|g" {HOME}/.local/share/applications/kitty*.desktop')
    os.system(f"echo 'kitty.desktop' > {HOME}/.config/xdg-terminals.list")


def installNvim():
    os.chdir(f'{HOME}/.local')
    os.system("wget https://github.com/neovim/neovim/releases/download/v0.10.4/nvim-linux-x86_64.tar.gz")
    os.system("tar -xzvf nvim-linux-x86_64.tar.gz -C nvim")
    os.system("rm nvim-linux-x86_64.tar.gz")
    os.system(f"ln -s {HOME}/.local/nvim/nvim-linux-x86_64/bin/nvim {HOME}/.local/bin/nvim")
    os.chdir(PWD)
    os.system("git clone https://github.com/NvChad/starter ~/.config/nvim")