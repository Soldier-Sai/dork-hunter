# 🔍 Dork Hunter

Automated security reconnaissance tool for Google/GitHub/Shodan dorking.

## Features
- Multi-engine support (Google/GitHub/Shodan)
- Domain targeting
- Parallel processing
- Detailed logging

## Installation
git clone https://github.com/Soldier-Sai/dork-hunter.git
cd dork-hunter
pip install -r requirements.txt
Usage
bash
# Google dorks
python3 dorker.py -f example_dorks/google_dorks.txt

# GitHub code search
python3 dorker.py -f example_dorks/github_dorks.txt -e github --domain company

# Shodan scan
python3 dorker.py -f example_dorks/shodan_dorks.txt -e shodan --domain target.com
Legal
Use only on authorized targets. Never use for illegal purposes.

#### **2. requirements.txt**
colorama
requests
