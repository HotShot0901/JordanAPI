from .logManager import Log, LogError
from .constants import DEBUG

class Behavour():
    Awaked = bool()
    Started = bool()

    def __init__(self) -> None:
        self.Awaked = False
        self.Started = False

        if DEBUG:
            Log("[{}] : Initialized".format(self))

        return

    def PreStartCheck(self) -> bool:
        if not self.Awaked:
            LogError("[{}] : Cannot call Start without Awaking the Script.".format(self))
            return False
        
        else:
            return True

    def PreUpdateCheck(self) -> bool:
        if not self.Awaked:
            LogError("[{}] : Cannot call Update without Awaking the Script.".format(self))
            return

        elif not self.Started:
            LogError("[{}] : Cannot call Update without Starting the Script.".format(self))
            return
        
        else:
            return True

    def Awake(self):
        self.Awaked = True

        if DEBUG:
            Log("[{}] : Awaked".format(self))

        return

    def Start(self):
        if not self.PreStartCheck():
            return

        self.Started = True

        if DEBUG:
            Log("[{}] : Started".format(self))

        return

    def Update(self, dt: float):
        if not self.PreUpdateCheck():
            return

        if DEBUG:
            Log("[{}] : Updated".format(self))

        return

    def __repr__(self) -> str:
        return "<Behavour at {}>".format(hex(id(self)))

BehavourTraits = ['Awake', 'Start', 'Update']
# BehavourTraits = dir(Behavour)
