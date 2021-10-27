from .vectors import *
from .logManager import *
from .behavour import Behavour
from .gameObject import GameObject

from time import sleep, time
from threading import Thread

class Scene():
    def __init__(self, name: str, sceneID: int=0) -> None:
        self.objects : list = []
        self.name    : str  = name
        self.sceneID : int  = sceneID

        self.deltaTime = 1 / 60
        self.lastTime = time()

        self.gameloopThread = None
        
        self.isRunning: bool = True
        self.frames: int = 0
        
    def NewObject(self, name: str, *componentsToAttach) -> GameObject:
        _object = GameObject(name, self.sceneID)

        for i in componentsToAttach:
            _object.AddComponentByType(i)

        self.AddObject(_object)
        return _object

    def AddObject(self, _object: GameObject) -> None:
        if isinstance(_object, GameObject) and _object not in self.objects:
            self.objects.append(_object)

    def Destroy(self, _object: GameObject, delay: float=0) -> None:
        def des(l: list, obj: GameObject, dt: float):
            sleep(dt)
            l.remove(obj)

        if delay == 0:
            self.objects.remove(_object)
        else:
            t = Thread(target=des, args=(self.objects, _object, delay))
            t.start()

    def GetObjectByType(self, _type: Behavour) -> GameObject:
        for _object in self.objects:
            if _object.HasComponent(_type):
                return _object

    def GetObjectsByTypes(self, _type: Behavour) -> list:
        objects: list = []

        for _object in self.objects:
            if _object.HasComponent(_type):
                objects.append(_object)

        return objects

    def Awake(self) -> None:
        for _object in self.objects:
            _object.Awake()

    def Start(self) -> None:
        for _object in self.objects:
            _object.Start()

    def Update(self, dt: float) -> None:
        for _object in self.objects:
            self.frames += 1
            _object.Update(dt)

    def startGameLoop(self) -> Thread:
        def loop(_scene):
            while _scene.isRunning:
                _scene.Update(_scene.deltaTime)

                currentTime = time()
                _scene.deltaTime = currentTime - _scene.lastTime
                _scene.lastTime = currentTime

        self.gameloopThread = Thread(target=loop, args=(self,))
        self.gameloopThread.start()

        return self.gameloopThread
