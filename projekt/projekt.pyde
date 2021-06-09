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
        # tworzymy dodajemy do listy sktywnych strzał strzałę
        # ustawienie pozycji dla strzały na pozycję statku
        # ustawienie kierunku ruchu dla strzały
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
        self.visability = True
    def changePosition(self):
        pass
    def changeVisability(self):
        # zmina visability
        # sprawdzanie czy wszyscy zestrzeleni (areEnemiesDestroyed)
        # doliczenie punktów
    #strzelanie
    pass
class Bullet():
    pass
    # position
    # direction
    # movement
class Interface():
    self.points = 0
    def bulletIntoYou():
        # wyświetlenie GameOver
    def areEnemiesDestroyed():
        pass
        # sprawdzanie po kolei listy wrogów i ich widzialności
            # jeżeli wszyscy zbici to wyświelenie wygranej
    def addPoint():
        self.points += self.points
    
def setup():
    size(800, 600)
    global enemyList, player1
    player1 = Player()
    enemyList = []
    for num, i in enumerate(range(Enemy.quantity)):
        enemyList.append(Enemy(0+num*20))
def draw():
    if keyPressed:
        # jeżeli strzałka w lewo albo 'a'
            player1.changePosition(True)
        # jeżeli strzałka w prawo albo 'd'
            player1.changePosition(False)
        # jeżeli spacja
            player1.shot()
    for enemy in enemyList:
        enemy.changePosition()
        #losowanie czy dany przeciwnik strzela
            # jeżeli się wylosował strzał
            enemy.shot()
    # przesunięcie w odpowiednim kierunku pozycji każdej ze strzał na ekranie (liście strzał ekranu)
    # sprawdzenie, czy pozycja vertykalna strzały jest  na wysokości gracza - taka jak pozycje vertykalne statków
    # sprawdzenie, czy dotyka gracza lub przeciwnika
    # sprawdzenie, czy kierunek strzały jest zgodny ze statkiem którego dotyka
        # zależnie od tego którego statku dotyka, wywołanie bulletIntoYou lub zmiana visability wroga
        
    # wyświetlenie aktualnej liczby punktów
