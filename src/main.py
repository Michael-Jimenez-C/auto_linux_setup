import questionary
from modules.commonconstants import USER, HOME
from modules.print_mod import warning
from modules.linux_utils.packages import aditional_packages, pipx_packages, flatpak_packages, homebrew_packages, crate_io_packages
from modules.manager import Manager


warning(f"Vas a ejecutar este script como {USER}, y todo se instalará en {HOME}")

class Config:
    def __init__(self):
        self.desktop = None
        self.terminal = None
        self.rust = None
        self.rustAlreadyInstalled = False
        self.yazi = None
        self.wallust = None
        self.homebrew = None
        self.homebrewAlreadyInstalled = False
        self.homebrewPackages = []
        self.flatpakPackages = []
        self.aditionalPackages = []
        self.pipxPackages = []
        self.crateIoPackages = []

    def __repr__(self):
        return str(getattr(self, '__dict__'))

class Menu:
    def __init__(self):
        self.config = Config()


    def confirm(self) -> bool:
        return questionary.confirm("¿Quieres continuar?").ask()

    def desktop(self) -> bool:
        self.config.desktop = questionary.select("¿Que entorno de escritorio quieres?",
                                  choices=[
                                      "bspwm",
                                      "gnome",
                                      "Nada"
                                  ]).ask()
        if self.config.desktop == "Nada":
            self.config.desktop = None
    
    def terminal(self) -> bool:
        self.config.terminal = questionary.select("¿Que terminal quieres?",
                                  choices=[
                                      "gnome-terminal",
                                      "kitty"
                                  ]).ask()

    def rust(self):
        self.config.rust = questionary.confirm("¿Quieres instalar rust?").ask()
        if not self.config.rust:
            self.config.rustAlreadyInstalled = questionary.confirm("¿Ya tienes rust instalado?").ask()
    
    def homebrew(self):
        self.config.homebrew = questionary.confirm("¿Quieres instalar homebrew?").ask()
        if not self.config.homebrew:
            self.config.homebrewAlreadyInstalled = questionary.confirm("¿Ya tienes homebrew instalado?").ask()
    
    
    def yazi(self):
        self.config.yazi = questionary.confirm("¿Quieres instalar yazi?").ask()
    
    def wallust(self):
        self.config.wallust = questionary.confirm("¿Quieres instalar wallust?").ask()
    
    def group_packages(self, message: str, packages: list):
        packages_ = []
        for group in packages:
            packages_.extend(questionary.checkbox(f"{message} {group}?",
                choices=packages[group]).ask())
        return packages_

    def additional_packages(self):
        self.config.aditionalPackages = self.group_packages("¿Quieres instalar paquetes adicionales del grupo", aditional_packages)

    def pipx_packages(self):
        self.config.pipxPackages = self.group_packages("¿Quieres instalar paquetes pipx del grupo", pipx_packages)

    def homebrew_packages(self):
        self.config.homebrewPackages = self.group_packages("¿Quieres instalar paquetes homebrew del grupo", homebrew_packages)

    def flatpak_packages(self):
        self.config.flatpakPackages = self.group_packages("¿Quieres instalar paquetes homebrew del grupo", flatpak_packages)

    def crate_io_packages(self):
        self.config.crateIoPackages = self.group_packages("¿Quieres instalar paquetes crate_io del grupo", crate_io_packages)

    def run(self):
        if not self.confirm():
            return
        self.desktop()
        self.terminal()
        self.rust()
        if self.rust:
            self.yazi()
            self.wallust()
            self.crate_io_packages()
        self.homebrew()
        if self.homebrew:
            self.homebrew_packages()
        self.additional_packages()
        self.pipx_packages()
        self.flatpak_packages()

if __name__ == "__main__":
    menu = Menu()
    menu.run()
    inst = Manager(menu.config)
    inst.run()