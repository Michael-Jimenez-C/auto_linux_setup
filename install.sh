sudo apt update
sudo apt install -y git curl python3 python3-venv

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cd src
python3 main.py