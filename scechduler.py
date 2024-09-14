from datetime import datetime
import time
import asyncio
import os
from typing import Callable
from RequestsWrapper import *
from dotenv import load_dotenv
class scechduler:
    def __init__(self,Update: Callable[[{}],None],FixedUpdate: Callable[[{}],None] = None, frenquency=60, activeDuration: (int,int)= (0,24)):
        self.begin = activeDuration[0]
        self.end = activeDuration[1]
        self.frequency = frenquency
        self.Update = Update
        self.FixedUpdate= FixedUpdate
        self.UpdateId = 0
        load_dotenv()
    def run(self):
        #runs the scechduler
        while(True):
            if(self.begin <datetime.now().hour < self.end):
                path = os.getenv("UPDATES")
                res = getMethod(path, {"chat_id": "-4576607081" , "offset": self.UpdateId})
                if(res):
                    res =res.json()
                    if(len(res["result"])):
                        self.UpdateId = res["result"][-1]["update_id"]
                        self.UpdateId+=1
                        if(self.FixedUpdate):
                            self.FixedUpdate(res)
                    if(self.Update):
                        self.Update(res)
            time.sleep(self.frequency)

