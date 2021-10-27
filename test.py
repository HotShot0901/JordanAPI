from API.logManager import Log, StopLogging
from API import *
from testComponent import TestComponent

s = Scene("Test Scene")

s.NewObject("Test 1")
_s = time()
s.startGameLoop()

sleep(1)
s.NewObject("Test 2")

sleep(1)

s.isRunning = False
e = time()

fps = s.frames / (e - _s)

sleep(0.1)

Log(f"FPS: {fps}")
Log(f"Total Frames Rendered: {s.frames}")
Log(f"Total Time Taken: {e - _s}")

sleep(0.1)
StopLogging()
