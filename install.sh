#!/bin/bash
# Readme Generator Installer
# Created by Anoop Macharla (149@holbertonschool.com) 08/25/17

if [ "$(id -u)" != "0" ]; then
	echo "Sorry, your not root!"
	echo "Rerun with: sudo ./install.sh"
	exit 1
fi

README_GENERATOR="readme4me"
APP_PATH="/opt/readme4me"
BIN_PATH="/usr/local/bin"

echo -e "Installing ReadMeGenerator Version 1"
echo -e "Installing Beauitful Soup 4 Python Library"

sudo apt-get update
sudo apt-get install python3-bs4

mkdir -p "${APP_PATH}"
cp "${README_GENERATOR}.py" "${APP_PATH}/${README_GENERATOR}"
chmod +x "${APP_PATH}/${README_GENERATOR}"
ln -s "${APP_PATH}/${README_GENERATOR}" "${BIN_PATH}/${README_GENERATOR}"

echo -e "--------------------------"
echo -e "Enjoy -Anoop M."
echo -e "Use: readme4me [README.MD]"
