#!/usr/bin/python3
"""initialize magic method for models dir"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
