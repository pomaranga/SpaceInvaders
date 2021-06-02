'''
statek
 strzelanie
 poruszanie w poziomie
 przegrana - utrata życia
 sterowanie przez gracza
kosmici
 gromada
 poruszanie gromadą
 nadlatywanie
 umieranie
punktacja
tło
grafiki: statku kosmitów, tła, pociski, animacja wybuchu
'''
class Ship():
    position = 0
    #ShotDirection
    #sprite
    def shot():
        pass
    def changePosition():
        pass
class Player(Ship):
    pass
    # sterowanie
class Enemy(Ship):
    def __init__(pos):
        self.position = pos
    #ilosc
    position
    #poruszanie
    #strzelanie
    pass
class Bullet():
    pass
class Interface():
    points = 0
    def bulletIntoYou():
        pass
    
def setup():
    size(800,600)
    enemyList = Enemy()
def draw():
    pass
