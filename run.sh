#!/usr/bin/bash
# runs the program

tmux new-session -d 'SDMS_USER='alphonce' SDMS_PWD='sdms_pwd' SDMS_HOST='localhost' SDMS_DB='sdms_db' python3 -m admin.app'

tmux new-session -d 'SDMS_USER='alphonce' SDMS_PWD='sdms_pwd' SDMS_HOST='localhost' SDMS_DB='sdms_db' python3 -m api.v1.app'
