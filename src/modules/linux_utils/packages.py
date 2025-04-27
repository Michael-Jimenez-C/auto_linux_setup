packages = [
    "flatpak",
    "vim",
    "zsh",
    "zsh-autosuggestions",
    "zsh-syntax-highlighting",
    "python3-venv",
    "python3-pip",
    "git",
    "pipx",
    "make",
    "cmake",
    "unzip",
    "bat",
    "jq",
    "build-essential",
    "ffmpeg",
    "7zip",
    "poppler-utils",
    "imagemagick",
    "libconfig9",
    "libev4",
    "libpcre3",
    "libxcb-composite0",
    "libxcb-xinerama0"
]

desktop_packages = {
    'bspwm':[
        "bspwm",
        "sxhkd",
        "picom",
        "rofi",
        "polybar",
        "feh",
        "gnome-terminal"
        ],
    'gnome':[
        'gnome-shell',
        'ubuntu-desktop-minimal',
        'gnome-tweaks',
        'language-pack-gnome-es',
        'gnome-shell-extensions'
    ]
}


terminal_packages = {
    'gnome-terminal': ['gnome-terminal']
}


aditional_packages = {
    'contendores':['podman'],
    'redes':[
        'nmap',
        'wireshark',
        'bettercap'
    ],
    'web': [
        'wfuzz',
        'whatweb',
        'ffuf'
    ],
    'hash' : ['hashcat','hydra'],
    'db': ['sqlitebrowser','sqlmap'],
    'Directorio Activo': ['smb-client']
}

pipx_packages = {
    'git':['git-dumper'],
    'Directorio Activo': [
        'ensurepath',
        'bloodhound-ce'
        ],
    'python': ['uv'],
    'data': ['dvc']
}

flatpak_packages = {

}

homebrew_packages = {
    'nodejs': ['node@22'],
}


crate_io_packages = {
    'comodidades': ['yazi-fm','yazi-cli', 'wallust']
}