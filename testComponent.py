from API import Behavour
from API.logManager import *
from API.vectors.vector import Vector3

class TestComponent(Behavour):
    def __init__(self) -> None:
        Log("[{}] : Initialized".format(self))

    def Awake(self):
        self.Awaked = True
        Log("[{}] : Awaked".format(self))
        return

    def Start(self):
        if not self.PreStartCheck():
            return

        self.Started = True
        Log("[{}] : Started".format(self))
        return

    def Update(self, dt: float):
        if not self.PreUpdateCheck():
            return
            
        Log("[{}] : Updated".format(self))
        return
        
    def __repr__(self) -> str:
        return "<TestComponent at {}>".format(hex(id(self)))
