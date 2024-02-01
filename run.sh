#!/usr/bin/bash
# runs the program

#SDMS_USER='alphonce' SDMS_PWD='sdms_pwd' SDMS_HOST='localhost' SDMS_DB='sdms_db' python3 -m admin.app


SDMS_USER='alphonce' SDMS_PWD='sdms_pwd' SDMS_HOST='localhost' SDMS_DB='sdms_db' python3 -m api.v1.app
