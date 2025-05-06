# 🔍 Dork Hunter [![GitHub stars](https://img.shields.io/github/stars/Soldier-Sai/dork-hunter?style=social)](https://github.com/Soldier-Sai/dork-hunter)

Advanced multi-engine dorking tool for security researchers and bug bounty hunters.

![Demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDk0dW1mY2V6dW5yY3V1eW5jZ3B5eGx4bGZ6dHhqZ2Z1dWx6ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xT5LMHxhOfscxPfIfm/giphy.gif)

## Features
- **Multi-engine support**: Google, GitHub, Shodan
- **Smart domain targeting**: Auto-adapts syntax per engine
- **Parallel processing**: Threaded execution for speed
- **Comprehensive logging**: Tracks all executed dorks
- **Proxy support**: Route through Burp/ZAP

## Installation
```bash
git clone https://github.com/Soldier-Sai/dork-hunter.git
cd dork-hunter
pip install -r requirements.txt
```

## Usage
```bash
# Basic Google dorking
python3 dorker.py -f dorks/google.txt

# GitHub code search (domain as keyword)
python3 dorker.py -f dorks/github.txt -e github --domain acme-corp

# Shodan host scan
python3 dorker.py -f dorks/shodan.txt -e shodan --domain target.com

# Advanced options
python3 dorker.py -f dorks/custom.txt \
  -e google \
  --delay 2 \
  --threads 8 \
  --proxy http://127.0.0.1:8080
```

## Dork Examples
### Google
```
site:example.com ext:pdf "confidential"
intitle:"index of" "database.sql"
```

### GitHub
```
filename:.env "API_KEY"
org:acme-corp "password" extension:json
```

### Shodan
```
http.title:"Admin Login"
ssl:"target.com" port:443
```

## Configuration
Edit `config.ini` to set:
```ini
[API_KEYS]
github = your_github_token
shodan = your_shodan_key

[SETTINGS]
default_delay = 1.5
max_threads = 5
```

## Legal & Ethics
⚠️ **Use Responsibly**
- Only test systems you own or have permission to scan
- Never use for illegal purposes
- Respect robots.txt and terms of service

Report vulnerabilities responsibly using:
- [HackerOne](https://hackerone.com)
- [Bugcrowd](https://bugcrowd.com)

## Contributing
1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Support
Found this useful? Give it a ⭐!  
Have questions? Open an issue.

## License
[MIT](LICENSE) © [Soldier-Sai](https://github.com/Soldier-Sai)

---

[![GitHub contributors](https://img.shields.io/github/contributors/Soldier-Sai/dork-hunter)](https://github.com/Soldier-Sai/dork-hunter/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/Soldier-Sai/dork-hunter)](https://github.com/Soldier-Sai/dork-hunter/issues)
[![GitHub forks](https://img.shields.io/github/forks/Soldier-Sai/dork-hunter)](https://github.com/Soldier-Sai/dork-hunter/network)
