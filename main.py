import os
from modules.data import Data
from modules.networking import Networking
from dotenv import load_dotenv

load_dotenv()


class main:
    def __init__(self):
        self.networking = Networking(os.getenv("SERVER_IP"), os.getenv("SERVER_PORT"))

    def update():
        pass
    
    def run(self):
        while True:
            self.update()
    
    
if __name__ == "__main__":
    main_instance = main()
    main_instance.run()