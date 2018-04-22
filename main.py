from gui import SimGUI
from log import Log
import time

start_time = time.time()

if __name__=="__main__":
    Log.comment('Launching simulation.')
    SimGUI()
    stop_time = time.time()
    Log.comment('Simulation finished after {} seconds.'.format(stop_time - start_time))
