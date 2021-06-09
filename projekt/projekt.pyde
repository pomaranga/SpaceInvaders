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
    #ShotDirection
    #sprite
    def shot():
        pass
    def changePosition():
        pass
class Player(Ship):
    def changePosition(czyLewo):
        if czyLewo:
            pass
            # zmiana pozycji o ileś w lewo (zmniejszenie positionHorizontal)
        else:
            pass
            # zmiana pozycji o ileś w prawo (zwiększenie positionHorizontal)
    # strzelanie spacją
class Enemy(Ship):
    quantity = 3
    def __init__(self, pos):
        self.positionHorizontal = pos
        self.positionVertical = 15
        self.movementDirection = 1
        self.visability = 1
    def changePosition(self):
        pass
    #strzelanie
    pass
class Bullet():
    pass
    # position
    # movement
class Interface():
    points = 0
    def bulletIntoYou():
        pass
    
def setup():
    size(800,600)
    global enemyList, player1
    enemyList = []
    for num, i in enumerate(range(Enemy.quantity)):
        enemyList.append(Enemy(0+num*20))
    player1 = Player()
def draw():
    if keyPressed:
        pass
        # jeżeli spacja
          # metoda od strzelania
        # jeżeli strzałka w lewo albo 'a'
          # changePosition(True)
    for enemy in enemyList:
        enemy.changePosition()
        #losowanie czy dany przeciwnik strzela
            #ustawienie pozycji na pozycję wroga dla ewentualnej strzały
            #ustawienie kierunku dla strzały
    # przesunięcie w odpowiednim kierunku każdej ze strzał na ekranie
    # sprawdzenie czy są na wysokości gracza lub przeciwnika
    # sprawdzenie czy dotyka gracza lub przeciwnika
    # sprawdzenie czy kierunek strzały jest zgodny z statkiem którego dostyka (czy ma go zwalczać)
        #utrata życia lub zabicie, czyli np. ustawienie visability na 0

        
    #wyświetlanie liczby punktów na ekranie
    #sprawdzanie, czy liczba punktów się zmieniła w tej klatce
