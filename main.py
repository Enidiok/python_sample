import time
import asyncio
import threading


def timeout():
    print("1st timeout is started again")
    time.sleep(5)
    print("1st timeout is finished")

def timeout():
    print("2nd timeout ")