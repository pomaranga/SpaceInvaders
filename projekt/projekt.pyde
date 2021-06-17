'''
grafiki do stworzenia: statku kosmitów, tła, pociski, animacja wybuchu, ew. 'tarcze/przeszkody'
'''
class Ship():
    #ShotDirection
    #sprite
    def shot(self, angle):
        fill(25, 255,0)
        rect(0, 20, 20, 20) # tworzymy instancję pocisku i dodajemy do listy sktywnych pocisków ów pocisk
        self.position = x0ship # ustawienie pozycji dla pocisku na pozycję statku (self.position)
        self.angle = 180 # ustawienie kierunku ruchu dla pocisku
        self.speed = 3    # ustawienie prędkości ruchu pocisku
        pass
    def changePosition():
        pass
    def sketch_ship(self):
        fill(0,0,0)
        rect (0,150,10,40)
        rect (10,150,120,10)
        rect (120,150,10,40)
        rect (20,160,90,10)
        rect (30,170,10,10)
        rect (90,170,10,10)
        rect (40,180,10,10)
        rect (80,180,10,10)
        rect (10,140,30,10)
        rect (90,140,30,10)
        rect (50,140,30,10)
        rect (20,130,20,10)
        rect (90,130,20,10)
        rect (50,130,30,10)
        rect (30,120,70,10)
        rect (40,110,50,10)
        rect (50,100,10,10)
        rect (70,100,10,10)
        rect (40,90,10,10)
        rect (80,90,10,10)
class Player(Ship):
    #position
    #grafika
    
    #grafika - eksplozja_animacja:
    def __init__(self):
        self.a = 380
        self.b = 260
        self.c = 420
        self.d = 260
        self.e = 380
        self.f = 300
        self.g = 420
        self.h = 300
        self.i = 40
    def sketch_explosion(self):
        self.a = self.a - 5
        self.b = self.b - 5
        self.c = self.c + 5
        self.d = self.d - 5
        self.e = self.e - 5
        self.f = self.f + 5
        self.g = self.g + 5
        self.h = self.h + 5
        fill(255, 150, 0)
        stroke(255, 150, 0)
        rect(self.a, self.b, self.i, self.i)
        rect(self.c, self.d, self.i, self.i)
        rect(self.e, self.f, self.i, self.i)
        rect(self.g, self.h, self.i, self.i)
        
 class Shield():
    
    def sketch_shield(shield):
        fill(160, 0, 0)
        stroke(10, 150, 0)
        rect(80,400,120,50)
        rect(340,400,120,50)
        rect(600,400,120,50)
            
        shield.visability = True
        def changeVisability(shield):
            pass
        

    
    def changePosition(Left):
        if Left:
            pass
            self.positionHorizontal -= 3
        else:
            pass
            self.positionHorizontal += 3
class Enemy(Ship):
    doNastepnegoStrzalu = 0
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
    # position - atrybut
    # direction - atrybut
    # movement - metoda
    def sketch_bullet(self):
        fill(255, 0, 0);
        stroke(0);
        beginShape();
        curveVertex(50, 60);
        curveVertex(30, 30);
        curveVertex(75, 60);
        curveVertex(100, 100);
        curveVertex(50, 120);
        curveVertex(30, 30); 
        curveVertex(80, 80);
        endShape(CLOSE);
class Interface():
    points = 0
    def bulletIntoYou():
        # wyświetlenie GameOver
        pass
    def areEnemiesDestroyed():
        global enemies
    for enemy in enemyList:
        if enemy.visible:
            return False
    return True
    # sprawdzanie po kolei listy wrogów i ich widzialności
            # jeżeli wszyscy zbici to wyświelenie wygranej
        
    def addPoint():
        self.points += 1
    # metoda wyświetlająca bieżącą punktację
    
def setup(): # ta funkcja może występować tylko raz w programie
    size(800, 600)
    global enemyList, player1
    player1 = Player()
    enemyList = []
    for num, i in enumerate(range(Enemy.quantity)):
        enemyList.append(Enemy(0+num*20))
def draw():
    background(60)
    player1.sketch_explosion()
    player1.sketch_ship()
    b=Bullet()
    b.sketch_bullet()
    s=Shield()
    s.sketch_shield()
    
    if keyPressed: 
        #jeżeli strzałka w lewo albo 'a'
        if key == 'a' or keyCode == 37:
            player1.changePosition(True)
        #jeżeli strzałka w prawo albo 'd' 
        if key == 'd' or keyCode == 39:
            player1.changePosition(False)
        # jeżeli spacja lub enter lub strzałka w dół
        if key == " " or key == ENTER or keyCode == 40: 
            player1.shot() # dodać kierunek strzelania jako argument }
            
    for enemy in enemyList:
        enemy.changePosition()
    
        #losowanie czy dany przeciwnik strzela lub odliczanie do strzału w pętli
        enemy.doNastepnegoStrzalu -= 1
        if(enemy.doNastepnegoStrzalu <= 0):
            czyStrzela = int(random(0,2))
            enemy.doNastepnegoStrzalu = 100
        # jeżeli strzał został wylosowany
            if(czyStrzela == 1):
                enemy.shot(True)

    # przesunięcie w odpowiednim kierunku pozycji każdego z aktywnych pocisków na ekranie (liście pocisków ekranu)
        # sprawdzenie, czy pozycja vertykalna pocisku jest na wysokości statku - taka jak pozycje vertykalne statków
            # sprawdzenie, czy dotyka gracza lub przeciwnika
                # sprawdzenie, czy kierunek strzały jest zgodny ze statkiem którego dotyka
                    # zależnie od tego którego statku dotyka, wywołanie bulletIntoYou lub zmiana visability wroga
        
    # wyświetlenie aktualnej liczby punktów
