import time
import datetime
from tqdm import tqdm

filename = __file__.replace(".py", "")
problemNumber = filename.replace("problem", "")

scratchpad = open("./"+filename+"_scratchpad.euler", "a+")

def pad (string):
    scratchpad.write(string+"\n")


##########################################

def run () :
    global problemNumber
    start = time.time()
    pad(
        "\n\n"+
        str(datetime.datetime.now())+"\n"
        "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    )

    pad("^^^^^^^PROJECT EULER PROBLEM "+problemNumber+"^^^^^^^\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

    finish = time.time()
    pad("This took "+str(finish - start)+" s")

run()