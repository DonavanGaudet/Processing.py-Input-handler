
class Key():
    def __init__(self, keyChar, type):
        self.keyChar = keyChar
        self.type = type
        self.active = False
        
    def updateState(self, state):
        if state == "pressed":
            self.active = True
        elif state == "released":
            self.active = False
        
class newControler():
    def __init__(self):
        self.temp = 0
        self.buttons = []
        
    def addButton(self, keyChar, type):
        self.temp = Key(keyChar, type)
        self.buttons.append(self.temp)
        self.temp = 0
        
    def updateInput(self, curKey, state):
        for i in self.buttons:
            if i.keyChar == curKey:
                i.updateState(state)
            
    def held(self, requestKey):
        for i in self.buttons:
            if i.keyChar == requestKey:
                return(i.active)