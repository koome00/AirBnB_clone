#!/usr/bin/python3
""" Create a unique file storage for your application"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
storage.reload()
all_classes = {"BaseModel": BaseModel}
