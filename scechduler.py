from datetime import datetime
import time
import asyncio
import os
from requests import post
from dotenv import load_dotenv
class scechduler:
    def __init__(self, frenquency=60, activeDuration: (int,int)= (0,24)):
        self.begin = activeDuration[0]
        self.end = activeDuration[1]
        self.frequency = frenquency
        load_dotenv()

    @staticmethod
    def postMethod(path: str, body: {}):
        print("Post method")
        try: 
            post(path, body,timeout = 5)
        except TimeoutError as e:
            print(f"Timeout Error: {e}")
        except Exception as e:
            print(f"Exception: {e}")

    def run(self):
        #runs the scechduler
        while(True):
            if(self.begin <datetime.now().hour < self.end):
                print("here")
                self.postMethod(os.getenv("SEND_MESSAGE"),{"text": f"Message from: {datetime.now()}", "chat_id": "-4576607081"})
                print("------------------------------------------------")
            time.sleep(self.frequency)

