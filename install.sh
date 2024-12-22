#!/bin/bash


if [[ -n "$TERMUX_VERSION" ]]; then
        clear
        pkg update
        pkg install python3 nodejs npm -y
        pip install rich 
        npm install 
        python3 main.py
elif [[ -f "/data/data/com.termux/files/usr/bin/bash" ]]; then
        clear
        pkg update
        pkg install python3 nodejs npm -y
        pip install rich 
        npm install 
        python3 main.py
else
   
    if [[ "$(uname -o)" == "GNU/Linux" ]]; then
        clear
        sudo apt update
        sudo apt install python3 nodejs npm -y
        pip install rich 
        npm install 
        python3 main.py

    else
        echo "Unknown environment."
    fi
fi




