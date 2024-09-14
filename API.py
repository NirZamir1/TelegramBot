from requests import get
from dotenv import load_dotenv
import os
from scechduler import scechduler

def main():
    scech = scechduler(activeDuration=(0,20))
    scech.run()

if __name__ == "__main__":
    main()