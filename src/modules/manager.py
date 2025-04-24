from .linux_utils.commands import Install, linux
from .linux_utils.packages import packages, desktop_packages
import os
from .external_packages import kittyInstall, installNvim
from .commonconstants import HOME, PWD
from .print_mod import info, error, success

class Manager:
    def __init__(self, config):
        self.config = config

    def run(self):
        self.setUpDirs()
        self.__packages()
        os.system("chsh -s /usr/bin/zsh")
        installNvim()
        self.__desktop()

        self.__configs()

        self.__terminal()

        Install.install(self.config.aditionalPackages)
        Install.pipx(self.config.pipxPackages)
        Install.flatpak(self.config.flatpakPackages)
        
        if self.config.rust:
            Install.rust()
        if (self.config.rust or self.config.rustAlreadyInstalled):
            if self.config.yazi:
                Install.cargo_install(['yazi-fm', 'yazi-cli'])
            if self.config.wallust:
                Install.cargo_install(['wallust'])
            Install.cargo_install(self.config.crateIoPackages)

        if self.config.homebrew:                
            Install.homebrew()
        if self.config.homebrewAlreadyInstalled or self.config.homebrew:
            Install.homebrew_install(self.config.homebrewPackages)
        

    def setUpDirs(self):
        dirs = [
            f"{HOME}/.local",
            f"{HOME}/.local/bin",
            f"{HOME}/.local/share",
            f"{HOME}/.local/share/fondos/",
            f"{HOME}/.local/nvim",
            f"{HOME}/.config"
        ]
        os.system("mkdir -p "+" ".join(dirs))
        os.system("sudo mkdir -p /usr/share/fonts/truetype")

    def __packages(self):
        Install.install(packages)

    def __desktop(self):
        Install.install(desktop_packages[self.config.desktop])
    
    def __terminal(self):
        if self.config.terminal == "gnome-terminal":
            Install.install(self.config.terminalPackages['gnome-terminal'])
        if self.config.terminal == "kitty":
            kittyInstall()

    def __configs(self):
        info("Configurando el entorno")
        if self.config.desktop == "bspwm":
            for i in ['bspwm','picom','polybar', 'rofi', 'sxhkd']:
                linux.copy(f"dotfiles/{i}", f"{HOME}/.config")
            linux.chmod(f"{HOME}/.config/rofi/powermenu/powermenu.sh", "774")
            linux.chmod(f"{HOME}/.config/polybar/launch.sh", "774")
            tmp_= open(f"{HOME}/.config/sxhkd/sxhkdrc", "r").read()
            with open(f"{HOME}/.config/sxhkd/sxhkdrc", "w") as file:
                file.write(tmp_.replace("gnome-terminal", self.config.terminal))
                file.close()

        if self.config.terminal == "gnome-terminal":
            os.system(f"dconf load /org/gnome/terminal/ < {PWD}/dotfiles/terminal/gnome-terminal")
        if self.config.terminal == "kitty":
            os.system(f'git clone https://github.com/d3vjh/Dotfiles.git d3vjh_df')
            linux.copy('d3vjh_df/kitty', f'{HOME}/.config/')

        linux.copy("background/fondo.png", f"{HOME}/.local/share/fondos")
        linux.copy("dotfiles/.zshrc", f"{HOME}/.zshrc")




        info("Descargando fuentes de nerd fonts")
        linux.wget('https://github.com/ryanoasis/nerd-fonts/releases/download/v3.3.0/Meslo.zip', 'Meslo.zip')
        os.system(f"unzip Meslo.zip -d /tmp/meslo")
        linux.copy("/tmp/meslo/MesloLGSNerdFontMono-Regular.ttf", "/usr/share/fonts/truetype")
        linux.copy("/tmp/meslo/MesloLGSNerdFont-Regular.ttf", "/usr/share/fonts/truetype")

        info("Instalando powerlevel10k")
        os.system(f"git clone --depth=1 https://github.com/romkatv/powerlevel10k.git {HOME}/powerlevel10k")
        os.system(f"echo 'source {HOME}/powerlevel10k/powerlevel10k.zsh-theme' >>{HOME}/.zshrc")

