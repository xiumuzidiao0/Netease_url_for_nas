#!/bin/bash
export AUTOREMOVE=true
export AUTO_DELETE_TIME=60
export WEBDL=false
source .venv/bin/activate
python main.py > flask_log.txt 2>&1
