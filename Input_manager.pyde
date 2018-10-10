import Input
#To use the Input moduel, you must first coppy what you see in the built in functions keyPressed() and keyReleased(). due to the fact that these functions will only run in the main moduel, this is the only way to get around it.
#once you create a newControler, you can add 'buttons' to it using the method .addButton("Single string/char", "char/keycode"). This adds a key to the list of keys the newControler object will loop through to check its state to see if its
#being held currently or not.


class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move(self):
        if KEYS.held("w") == True:
            self.y -= 1
        if KEYS.held("a") == True:
            self.x -= 1
        if KEYS.held("s") == True:
            self.y += 1
        if KEYS.held("d") == True:
            self.x += 1
            
    def render(self):
        fill(0, 255, 0)
        rect(self.x, self.y, 20, 20)
        noFill()
        
    def update(self):
        self.move()
        self.render()

def setup():
    global KEYS, user
    KEYS = Input.newControler()
    KEYS.addButton("w", "char")
    KEYS.addButton("a", "char")
    KEYS.addButton("s", "char")
    KEYS.addButton("d", "char")
    #----#
    user = Player(50, 50)
    size(600, 600)
    
def keyPressed():
    global KEYS
    KEYS.updateInput(key, "pressed")
    
def keyReleased():
    global KEYS
    KEYS.updateInput(key, "released")
    
def draw():
    background(255)
    user.update()
    
    