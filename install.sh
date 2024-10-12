#!/bin/bash

apt install git python nodejs -y
git clone https://github.com/STARK-404/Wp-Lock/
cd Wp-Lock/
pip install -r requirment.txt
node index.js
