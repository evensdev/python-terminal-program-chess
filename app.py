from datetime import datetime
import re
from tinydb import TinyDB, Query, where

db = TinyDB('db.json')


"""---------------------------------------------------CONTROLLERS--------------------------------------------------------"""
from controllers.main import MainController as MC


if __name__ == "__main__":
    controller = MC()
    controller.main()