#!/usr/bin/python3
__all__ = ["storage"]
from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
