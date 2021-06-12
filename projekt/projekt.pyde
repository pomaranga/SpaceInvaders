'''
grafiki do stworzenia: statku kosmitów, tła, pociski, animacja wybuchu, ew. 'tarcze/przeszkody'
'''
class Ship():
    #ShotDirection
    #sprite
    def shot(self, down):
        # tworzymy instancję pocisku i dodajemy do listy sktywnych pocisków ów pocisk
        # ustawienie pozycji dla pocisku na pozycję statku (self.position)
        # ustawienie kierunku ruchu dla pocisku
        pass
    def changePosition():
        pass
class Player(Ship):
    #position
    #grafika
    def draw() :
    rect (50, 50, 100, 100)
    rect (50, 150, 25, 25)
    rect (125, 150, 25, 25)
    def changePosition(Left):
        if Left:
            pass
            # zmiana pozycji o ileś w lewo (zmniejszenie positionHorizontal)
        else:
            pass
            # zmiana pozycji o ileś w prawo (zwiększenie positionHorizontal)
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
        pass
class Bullet():
    pass
    # position - atrybut
    # direction - atrybut
    # movement - metoda
class Interface():
    points = 0
    def bulletIntoYou():
        # wyświetlenie GameOver
        pass
    def areEnemiesDestroyed():
        pass
        # sprawdzanie po kolei listy wrogów i ich widzialności
            # jeżeli wszyscy zbici to wyświelenie wygranej
    def addPoint():
        self.points += 1
    # metoda wyświetlająca bieżącą punktację
    
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
        # jeżeli spacja lub enter lub strzałka w dół
            player1.shot() # dodać kierunek strzelania jako argument
    for enemy in enemyList:
        enemy.changePosition()
        #losowanie czy dany przeciwnik strzela lub odliczanie do strzału w pętli
            # jeżeli strzał został wylosowany
        enemy.shot(True)
    # przesunięcie w odpowiednim kierunku pozycji każdego z aktywnych pocisków na ekranie (liście pocisków ekranu)
        # sprawdzenie, czy pozycja vertykalna pocisku jest na wysokości statku - taka jak pozycje vertykalne statków
            # sprawdzenie, czy dotyka gracza lub przeciwnika
                # sprawdzenie, czy kierunek strzały jest zgodny ze statkiem którego dotyka
                    # zależnie od tego którego statku dotyka, wywołanie bulletIntoYou lub zmiana visability wroga
        
    # wyświetlenie aktualnej liczby punktów
