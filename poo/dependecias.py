from abc import ABC

class Writer:

    def __init__(self, name):
        self.name = name
        self.__tools = None

    @property
    def getTools(self):
        return self.__tools

    @getTools.setter
    def setTool(self, tool):
        self.__tools = tool


class Tool(ABC):

    def __init__(self, name):
        self.name = name

    def message(self):
        return f"I am use the tool {self.name}!"

class Pen(Tool):
    def __init__(self, name="pen"):
        super().__init__(name)

class TypeWriter(Tool):

    def __init__(self, name="typeWhiter"):
        super().__init__(name)


if __name__ == '__main__':
    pass