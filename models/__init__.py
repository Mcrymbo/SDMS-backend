#!/usr/bin/python3
"""
Initialize storage
"""
from models.engine.db_storage import DBStorage
storage = DBStorage()
storage.reload()
