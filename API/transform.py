from .constants import *
from .behavour import Behavour
from .vectors import *
from .logManager import Log

class Transfrom(Behavour):
    def __init__(self) -> None:
        if DEBUG:
            Log("[{}] : Initialized".format(self))

        self.position = Vector3()
        self.rotation = Vector3()
        self.scale = Vector3.once

        return
        
    def Awake(self) -> None:
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

    @property
    def LocalXAxis(self) -> Vector3:
        return Matrix.RotateVector(Vector3.xUnit, self.rotation)

    @property
    def LocalYAxis(self) -> Vector3:
        return Matrix.RotateVector(Vector3.yUnit, self.rotation)

    @property
    def LocalZAxis(self) -> Vector3:
        return Matrix.RotateVector(Vector3.zUnit, self.rotation)

    def Translate(self, delta: Vector3) -> None:
        self.position += delta

    def Rotate(self, delta: Vector3) -> None:
        self.rotation += delta

    def RotateAround(self, axis, angle: float) -> None:
        if   axis == Vector3.Axis["X"]:
            self.Rotate(Vector3(angle, 0, 0))
        elif axis == Vector3.Axis["Y"]:
            self.Rotate(Vector3(0, angle, 0))
        elif axis == Vector3.Axis["Z"]:
            self.Rotate(Vector3(0, 0, angle))
        else:
            return

    def __repr__(self) -> str:
        return "<Transform at {}>".format(hex(id(self)))
