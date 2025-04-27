import subprocess
import os
from modules.print_mod import info, error, success
from modules.commonconstants import HOME, USER

class Install:
    @staticmethod
    def update():
        subprocess.run(['sudo', 'apt', 'update'])

    @staticmethod
    def install(packages: list):
        info('Preparandose para instalar los siguientes paquetes: '+' '.join(packages))
        for package in packages:
            if os.path.exists(f"compiled/{package}.deb"):
                info("Se encontró un paquete compilado en compiled, se instalará desde ahí")
                package = f"./compiled/{package}.deb"
            info("Instalando " + package)
            p = subprocess.run(['sudo', 'apt', 'install', '--ignore-missing', '-y', package], capture_output=True)
            if p.returncode != 0:
                error(f"Error instalando {package}")
                continue
            success(f"Se ha instalado {package}")
    
    @staticmethod
    def pipx(packages: list):
        for package in packages:
            info(f"Instalando {package} con pipx")
            p  = subprocess.run(['pipx', 'install', package], capture_output=True)
            if p.returncode != 0:
                error(f"Error instalando {package} con pipx")
                continue
    
    @staticmethod
    def rust():
        info("Instalando rust")
        p = os.system("curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh")
        success("Rust instalado correctamente")
        info("Actualizando rust")
        os.system(f'source {HOME}/.cargo/env')
        os.system("rustup update")

        if p != 0:
            error("Error instalando rust")
            return
        success("Rust instalado correctamente")

    @staticmethod
    def cargo_install(packages: list):
        for package in packages:
            info(f"Instalando {package} con cargo")
            p = os.system(f"{HOME}/.cargo/bin/cargo install {package}")
            if p != 0:
                error(f"Error instalando {package} con cargo")
                continue
            success(f"Se ha instalado {package} con cargo")
    
    @staticmethod
    def homebrew():
        info("Instalando homebrew")
        p = os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
        os.system('export PATH="/home/linuxbrew/.linuxbrew/bin:$PATH"')
        if p != 0:
            error("Error instalando homebrew")
            return
        success("Homebrew instalado correctamente")
    
    @staticmethod
    def homebrew_install(packages: list):
        for package in packages:
            info(f"Instalando {package} con homebrew")
            p = subprocess.run(['brew', 'install', package], capture_output=True)
            if p.returncode != 0:
                error(f"Error instalando {package} con homebrew")
                continue
            success(f"Se ha instalado {package} con homebrew")
    def flatpak(packages: list):
        pass


class linux:
    @staticmethod
    def copy(source, destination):
        info(f"Copiando {source} a {destination}")
        p = subprocess.run(['sudo', 'cp', '-r', source, destination], capture_output=True)
        subprocess.run(['sudo', 'chown', '-R', f'{USER}:{USER}', destination], capture_output=True)
        if p.returncode != 0:
            error(f"Error copiando {source} a {destination}")
            return
        success(f"Se ha copiado {source} a {destination}")
    
    @staticmethod
    def chmod(path, mode):
        info(f"Cambiando permisos de {path} a {mode}")
        p = subprocess.run(['sudo','chmod', mode, path], capture_output=True)
        if p.returncode != 0:
            error(f"Error cambiando permisos de {path} a {mode}")
            return
        success(f"Se ha cambiado permisos de {path} a {mode}")

    @staticmethod
    def wget(url, destination):
        info(f"Descargando {url} como {destination}")
        p = subprocess.run(['wget', url, '-O', destination], capture_output=True)
        if p.returncode != 0:
            error(f"Error descargando {url} a {destination}")
            return
        success(f"Se ha descargado {url} a {destination}")