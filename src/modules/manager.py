from .linux_utils.commands import Install
from .linux_utils.packages import packages, desktop_packages
import os
from .commonconstants import HOME

class Manager:
    def __init__(self, config):
        self.config = config

    def run(self):
        self.setUpDirs()
        self.__packages()
        self.__desktop()

        self.__configs()

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
        for i in dirs:
            os.makedirs(i, exist_ok=True)

    def __packages(self):
        Install.install(packages)

    def __desktop(self):
        Install.install(desktop_packages[self.config.desktop])
    
    def __configs(self):
        pass
        