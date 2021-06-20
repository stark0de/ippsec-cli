# ippsec-cli

This a simple tool to query the awesome ippsec.rocks website from your terminal

[![demo](https://asciinema.org/a/K2Y3sHcUC1MHhpiaiiZfYEfnh.svg)](https://asciinema.org/a/K2Y3sHcUC1MHhpiaiiZfYEfnh?autoplay=1)

## Installation and usage
```
cd /opt
git clone https://github.com/stark0de/ippsec-cli
cd ippsec-cli
pip3 install -r requirements.txt
chmod +x ippsec-cli.py
python3 -W ignore ippsec-cli.py <keyword>

Note: optionally you can go to /home/$USER/.bashrc and add this line so u can just launch it putting ippsec-cli in your terminal:

vim /home/$USER/.bashrc
alias ippsec-cli="python3 -W ignore /opt/ippsec-cli.py"
source /home/$USER/.bashrc
```

Credits to @HexF_me,  @Shell_ock and of course to the awesome Ippsec ;)

Note: I've set the string size limit to 100 characters in order to make sure tabulate can print it correctly, you can modify that if your screen is bigger
