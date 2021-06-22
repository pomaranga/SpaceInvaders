class Ship():
    #ShotDirection
    #sprite
    def shot(self, angle):
        fill(25, 255,0)
        rect(0, 20, 20, 20) # tworzymy instancję pocisku i dodajemy do listy sktywnych pocisków ów pocisk
        self.position = 0 # ustawienie pozycji dla pocisku na pozycję statku (self.position)
        self.angle = 180 # ustawienie kierunku ruchu dla pocisku
        self.speed = 3  # ustawienie prędkości ruchu pocisku
def update_shot(self):
    self.position -= 3
    if (random.randint(0, 10)==0): #losowe dodawanie strzału - to już było napisane..
        add.shot() # ale do czego?
    if (self.position == 600):  #usuwanie strzału gdy dotknie krawędzi okna 
        remove # trzebaby usubwać coś konkretnego i z konkretnej kolekcji
 
    def changePosition():
        pass
 
    def sketch_ship(self):
        self.sprite = loadImage('Ship.png') # ta grafika nie została dodana do projektu
 
class Player(Ship):
    #position
    #grafika
    def __init__(self):
        self.sprite = loadImage('Gracz One.png') # teraz trzeba ją w oddzielnej metodzie rysować uwzględniając pozycję
        self.positionH = 400
        self.positionV = 550
    def __init__(self):
        # zmienne potrzebne do porusznia eksplozją
        self.a = 380
        self.b = 260
        self.c = 420
        self.d = 260
        self.e = 380
        self.f = 300
        self.g = 420
        self.h = 300
        self.i = 40
    #grafika - eksplozja_animacja - trzeba uwzględnić pozycję z której ma eksplozja nastąpić
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
 
    def sketch_player(self):
        image(self.sprite, self.positionH, self.positionV)
 
 
 
class Enemy(Ship):
    nextShot = 0
    quantity = 3
    def __init__(self, pos):
        self.positionHorizontal = pos
        self.positionVertical = 15
        self.movementDirection = 1
        self.visability = True
    def changePosition(self):
        pass
    def changeVisability(self):
        self.visability = False # zmina visability
            # sprawdzanie czy wszyscy zestrzeleni (areEnemiesDestroyed)
                # doliczenie punktów
class Bullet():
    def update(self): # movement - metoda
        self.x += 5 # szybkosc lotu pocisku
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
    def update_movement(self, x, y):
        fill(255, 0, 0);
        stroke(0);
        beginShape();
        curveVertex(50+x, 60+y);
        curveVertex(30+x, 30+y);
        curveVertex(75+x, 60+y);
        curveVertex(100+x, 100+y);
        curveVertex(50+x, 120+y);
        curveVertex(30+x, 30+y); 
        curveVertex(80+x, 80+y);
        endShape(CLOSE);

class Shield():
 
    def sketch_shield(shield):
        fill(160, 0, 0)
        stroke(10, 150, 0)
        rect(80,400,120,50)
        rect(340,400,120,50)
        rect(600,400,120,50)
 
        shield.visability = True # to raczej w konstruktorze powinno być
 
    def changeVisability(shield):
        pass
class Interface():
    points = 0
    def bulletIntoYou():
        text ('GameOver', 400,300)# wyświetlenie GameOver
    def areEnemiesDestroyed():
        for enemy in enemyList:
            if enemy.visability == True:
                return False;   
        text("Brawo! Zwycięstwo!", width/3, height/2)
        return True
    def addPoint():
        self.points += 1
    # metoda wyświetlająca bieżącą punktację
 
def setup(): # ta funkcja może występować tylko raz w programie
    size(800, 600)
    loadImage("data\background.png")
    global enemyList, player1
    player1 = Player()
    enemyList = []
    for num, i in enumerate(range(Enemy.quantity)):
        enemyList.append(Enemy(0+num*20))
    # proponuję jeszcze tu listę strzał
def draw():
    # te wyświetlania trzeba jeszcze 'posprzątać' w miejsca docelowe
    player1.sketch_explosion()
    b=Bullet()
    b.sketch_bullet()
    s=Shield()
    s.sketch_shield()
 
    if keyPressed: 
        if key == 'a' or keyCode == 37: #jeżeli strzałka w lewo albo 'a'
            player1.changePosition(True)
        if key == 'd' or keyCode == 39: #jeżeli strzałka w prawo albo 'd'
            player1.changePosition(False)
        if key == " " or key == ENTER or keyCode == 40: # jeżeli spacja lub enter lub strzałka w dół
            bullet_group.add(player1.shot()) # dodać kierunek strzelania jako argument
 
    for enemy in enemyList:
        enemy.changePosition()
 
        enemy.nextShot -= 1 #odliczanie do strzału w pętli
        if enemy.nextShot <= 0: #odliczanie do strzału w pętli
            isShooting = int(random(0,2)) #losowanie czy dany przeciwnik strzela
            enemy.nextShot = 100 #odliczanie do strzału w pętli
            if isShooting == 1: # jeżeli strzał został wylosowany
               enemy.shot(True)
 
 
    # przesunięcie w odpowiednim kierunku pozycji każdego z aktywnych pocisków na ekranie (liście pocisków ekranu)
        # sprawdzenie, czy pozycja vertykalna pocisku jest na wysokości statku - taka jak pozycje vertykalne statków
            # sprawdzenie, czy dotyka gracza lub przeciwnika
                # sprawdzenie, czy kierunek strzały jest zgodny ze statkiem którego dotyka
                    # zależnie od tego którego statku dotyka, wywołanie bulletIntoYou lub zmiana visability wroga
 
    # wyświetlenie aktualnej liczby punktów
