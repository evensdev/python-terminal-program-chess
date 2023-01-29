from tinydb import TinyDB
from controllers.main import MainController as Mc

db = TinyDB('db.json')

if __name__ == "__main__":
    controller = Mc()
    controller.main()
