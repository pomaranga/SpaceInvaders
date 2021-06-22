def setup():
    size(600, 600);
    
class pocisk():
    def draw():
        rect(100, 100, 10, 10)
        rect(90, 110, 10, 10)
        rect(100, 110, 10, 10)
        rect(110, 110, 10, 10)
        rect(80, 120, 10, 10)
        rect(90, 120, 10, 10)
        rect(100, 120, 10, 10)
        rect(110, 120, 10, 10)
        rect(120, 120, 10, 10)
        rect(90, 130, 10, 10)
        rect(100, 130, 10, 10)
        rect(110, 130, 10, 10)
        rect(100, 140, 10, 10)
        rect(100, 150, 10, 10)
        noStroke()
        fill(255, 0, 0);
    def __init__(self, pos):
        self.position = position.ship
        self.direction = 0
    def update(self):
        self.position.y+4
        self.size-=0.4
        if (self.position.y==100):
            game.remove(self)
