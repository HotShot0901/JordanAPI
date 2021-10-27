from .PyLogger import *

logManager: Logger = Logger(saveLog=False, program="Jordan Scripting API", timestamp=True)

def Log(s: str) -> None:
    logManager.log(s)

def LogWarn(s: str) -> None:
    logManager.logWarning(s)

def LogError(s: str) -> None:
    logManager.logError(s)

def StopLogging() -> None:
    logManager.stop()

def HaltLogging() -> None:
    logManager.halt()
