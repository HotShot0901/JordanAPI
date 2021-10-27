from .behavour import Behavour
from .transform import Transfrom
from .constants import ARROW_RIGHT

class GameObject():
    def __init__(self, name: str, sceneID: int) -> None:
        self.name = name
        
        self.__components : list      = []
        self.__transform  : Transfrom = Transfrom()
        self.sceneId      : int       = sceneID

        self.__components.append(self.__transform)

    @property
    def transform(self) -> Transfrom:
        return self.__transform

    def AddComponent(self, component: Behavour) -> None:
        if isinstance(component, Behavour) and component not in self.__components and not isinstance(component, Transfrom):
            self.__components.append(component)

    def AddComponentByType(self, _type: Behavour) -> None:
        if _type is Transfrom:
            return

        component = _type()
        self.AddComponent(component)

    def RemoveComponentByType(self, _type: Behavour) -> None:
        for component in self.__components:
            if isinstance(component, _type):
                self.__components.remove(component)
                break

    def RemoveComponentsByType(self, _type: Behavour) -> None:
        for component in self.__components:
            if isinstance(component, _type):
                self.__components.remove(component)

    def RemoveComponentByReferance(self, _component: Behavour) -> None:
        if isinstance(_component, Behavour) and (_component in self.__components):
            self.__components.remove(_component)

    def GetComponentOfType(self, _type: Behavour) -> Behavour:
        for component in self.__components:
            if isinstance(component, _type):
                return component

    def GetComponentsOfType(self, _type: Behavour) -> list:
        components = []

        for component in self.__components:
            if isinstance(component, _type):
                components.append(component)

        return components

    def HasComponent(self, _type: Behavour) -> bool:
        for component in self.__components:
            if isinstance(component, _type):
                return True

        return False

    def Awake(self):
        for component in self.__components:
            component.Awake()

    def Start(self):
        for component in self.__components:
            if not component.Awaked:
                component.Awake()

            component.Start()

    def Update(self, dt: float):
        for component in self.__components:
            if not component.Awaked:
                component.Awake()
                
            if not component.Started:
                component.Start()

            component.Update(dt)

    def __repr__(self) -> str:
        s = ""

        s += "<GameObject at {}>\n".format(hex(id(self)))
        
        compTypes = []
        for component in self.__components:
            comp = str(type(component))
            comp = comp[8:len(comp)-2]

            compTypes.append(comp)

        s += " {} Number of Components Attached : {}\n".format(ARROW_RIGHT, len(compTypes))
        s += " {} Components Attached : {}\n".format(ARROW_RIGHT, compTypes)
        s += " {} Scene ID : {}\n".format(ARROW_RIGHT, self.sceneId)

        return s
