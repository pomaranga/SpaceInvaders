class Ship:
    # ShotDirection
    # sprite

    def shot(self, angle):
        fill(25, 255, 0)
        rect(0, 20, 20, 20)  # tworzymy instancję pocisku i dodajemy do listy sktywnych pocisków ów pocisk
        self.position = 0  # ustawienie pozycji dla pocisku na pozycję statku (self.position)
        self.angle = 180  # ustawienie kierunku ruchu dla pocisku
        self.speed = 3  # ustawienie prędkości ruchu pocisku

    def update_shot(self):  # to powinno być w strzelaniu, a nie statku
        self.position = player1.position
        if self.position == 600:  # usuwanie strzału gdy dotknie krawędzi okna
            remove  # trzebaby usubwać coś konkretnego i z konkretnej kolekcji


class Player(Ship):
    # position
    # grafika

    # poczatkowa pozycja
    def __init__(self):
        self.positionH = 350
        self.positionV = 475
        self.sprite = loadImage(
            "Gracz One.png"
        )  # teraz trzeba ją w oddzielnej metodzie rysować uwzględniając pozycję
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
        # zmienne spadających gwiazd
        self.aa = 5
        self.bb = 5
        self.cc = 1
        self.dd = 100
        self.ee = 300

    # grafika - spadające_gwiazdy_animacja
    def shooting_stars(self):
        self.aa = self.aa + 5
        self.bb = self.bb + 5
        self.cc = self.cc + 0.05
        self.dd = self.dd + 5
        self.ee = self.ee + 5

        fill(255, 255, 100)
        stroke(255, 255, 200)
        rect(self.aa, self.bb, self.cc, self.cc)
        rect(self.dd, self.ee, self.cc, self.cc)

    # grafika - eksplozja_animacja - trzeba uwzględnić pozycję z której ma eksplozja nastąpić
    def sketch_explosion(self):
        self.sprite = loadImage("explosion.png")
        if (self.positionV < 440 and self.positionV > 320) and (
            (
                self.positionH > 40 and self.positionH < 160
            )  # utrudnienie - eksplozja gracza po wleceniu w tarcze
            or (self.positionH > 280 and self.positionH < 420)
            or (self.positionH > 540 and self.positionH < 680)
        ):
            image(self.sprite, self.positionH - 15, self.positionV - 15)

    def changePositionH(self, offset):
        self.positionH = self.positionH + offset

    def changePositionV(self, offset):
        self.positionV = self.positionV + offset

    def sketch_player(self):
        self.sprite = loadImage("Gracz One.png")
        image(self.sprite, self.positionH, self.positionV, 100, 80)


class Enemy(Ship):
    nextShot = 0
    quantity = 6

    def __init__(self, pos):
        self.positionH = pos
        self.positionV = 15
        self.movementDirection = 1
        self.visability = True
        self.sprite = loadImage(
            "Ship.png"
        )  # 4tys px to zdecydowanie za dużo, grafika powinna być raczej rozmiaru 30... poprawiłam, bo nie nadążało ładować i rzucało out of memory, zmieniłąm też kolor, bo nie było widać na tle

    def changePosition(self):
        if self.positionH < 0:
            self.positionV += 50
            self.movementDirection = 1

        if self.positionH > 700:
            self.positionV += 50
            self.movementDirection = 0

        if self.movementDirection == 0:
            self.positionH -= 1.7

        if self.movementDirection == 1:
            self.positionH += 1.7

    def changeVisability(self):
        self.visability = False  # zmina visability
        # sprawdzanie czy wszyscy zestrzeleni (areEnemiesDestroyed)
        # doliczenie punktów

    def sketch_ship(self):
        image(self.sprite, self.positionH, self.positionV)


class Bullet:
    def __init__(self, posH, posV):  # tu powinna być przekazana pozycja statku
        self.positionH = posH
        self.positionV = posV
        self.direction = 0

    def update(self):  # movement - metoda
        self.positionV += 5  # szybkosc lotu pocisku
        if self.positionV >= 600:
            bullet_group.pop(self.bullet)

    def update2(self): # movement - metoda
        Vspeed = 4
        bullet_group.push(self.update_movement())
        Bullet().changePositionH = False 
        self.positionV -= Vspeed # szybkosc lotu pocisku
        bullet_group.pop(self.update_movement())
        if (self.positionV>=100):
             bullet_group.pop(self.bullet)
			 
    def sketch_bullet(self):
        fill(255, 0, 0)
        stroke(0)
        beginShape()
        curveVertex(50, 60)
        curveVertex(30, 30)
        curveVertex(75, 60)
        curveVertex(100, 100)
        curveVertex(50, 120)
        curveVertex(30, 30)
        curveVertex(80, 80)
        endShape(CLOSE)

    def sketch_bullet2(self):
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

    def update_movement(self):
        fill(255, 0, 0)
        stroke(0)
        beginShape()
        curveVertex(50 + self.positionH, 60 + self.positionV)
        curveVertex(30 + self.positionH, 30 + self.positionV)
        curveVertex(75 + self.positionH, 60 + self.positionV)
        curveVertex(100 + self.positionH, 100 + self.positionV)
        curveVertex(50 + self.positionH, 120 + self.positionV)
        curveVertex(30 + self.positionH, 30 + self.positionV)
        curveVertex(80 + self.positionH, 80 + self.positionV)
        endShape(CLOSE)


class RepairKit:
    def sketch_RepairKit(self):
        self.sprite = loadImage("RepairKit.png")  # to tylko załadowanie grafiki, nie rysowanie, powinnodziać isę raz, nie co klatkę
        self.positionH = 0
        self.positionV = 500
        image(self.sprite, self.positionH, self.positionV)
        self.visability = False


class Shield:
    def sketch_shield(self):
        fill(102, 255, 255)
        stroke(10, 150, 0)
        rect(80, 400, 120, 50)
        rect(340, 400, 120, 50)
        rect(600, 400, 120, 50)

        self.visability = True  # to raczej w konstruktorze powinno być

    def changeVisability(shield):
        pass


class Interface:
    points = 0
    health = 100

    def draw_health(self):

        fill(255, 0, 0)
        rect(550, 550, self.health * 2, 30)

        textSize(30)
        text("Health: " + str(self.health), 550, 540)

    def bulletOrShipIntoYou(self):
        self.health -= 10
        text("GameOver", 400, 300)  # wyświetlenie GameOver

    def areEnemiesDestroyed(self):
        for enemy in enemyList:
            if enemy.visability == True:
                return False
        text("Brawo! Zwycięstwo!", width / 3, height / 2)
        return True

    def addPoint(self):
        Interface.points += 1

    def showScore(self):
        textSize(30)
        text(
            "Score:" + str(Interface.points), 5, 50
        )  # metoda wyświetlająca bieżącą punktację


def setup():  # ta funkcja może występować tylko raz w programie
    size(800, 600)
    global enemyList, player1, ship1, bullet_group, tlo, s, RepairKit, interface
    tlo = loadImage("background.jpg")  # rozdzielczość 300 ustawiamy dla wydruków, do wyświetlania 72...
    player1 = Player()
    enemyList = []
    for num, i in enumerate(range(Enemy.quantity)):
        enemyList.append(Enemy(0 + num * 100))
    # proponuję jeszcze tu listę strzał
    bullet_group = set()
    s = Shield()

    interface = Interface()

    RepairKit = RepairKit()


def draw():
    # te wyświetlania trzeba jeszcze 'posprzątać' w miejsca docelowe
    image(tlo, 0, 0)
    player1.sketch_player()
    player1.shooting_stars()
    player1.sketch_explosion()  # to powinno się dziać po trafieniu w gracza pociskiem
    b = Bullet(player1.positionH, player1.positionV)  # to powinno się dziac  w moemncie stzelenia
    s.sketch_shield()
    RepairKit.sketch_RepairKit()
    interface.showScore()
    interface.draw_health()
    if keyPressed:
        if key == "a" or keyCode == 37:  # jeżeli strzałka w lewo albo 'a'
            player1.changePositionH(-5)
        if key == "d" or keyCode == 39:  # jeżeli strzałka w prawo albo 'd'
            player1.changePositionH(5)
'''
        if key == "w" or keyCode == 38:  # jeżeli strzałka w gore albo 'w'
            player1.changePositionV(-5)
        if key == "s" or keyCode == 40:  # jeżeli strzałka w dol albo 's'
            player1.changePositionV(5)
'''
        if key == " " or key == ENTER: # jeżeli spacja lub enter lub strzałka w dół
            bullet_group.add(player1.shot(0)) # dodawać do listy tzeba wewnątz metody shot, nie tutaj
			
    for enemy in enemyList:
        enemy.changePosition()
        enemy.sketch_ship()
        enemy.nextShot -= 1  # loop countdown to shot
        if enemy.nextShot <= 0:  # loop countdown to shot
            isShooting = int(random(0, 2))  # drawing whether the opponent shoots
            enemy.nextShot = 100  # loop countdown to shot
            if isShooting == 1:  # if the shot is drawn
                enemy.shot(True)

    for bullet in bullet_group:
        bullet.sketch_bullet()
    # przesunięcie w odpowiednim kierunku pozycji każdego z aktywnych pocisków na ekranie (liście pocisków ekranu)
    # sprawdzenie, czy pozycja vertykalna pocisku jest na wysokości statku - taka jak pozycje vertykalne statków
    # sprawdzenie, czy dotyka gracza lub przeciwnika
    # sprawdzenie, czy kierunek strzały jest zgodny ze statkiem którego dotyka
    # zależnie od tego którego statku dotyka, wywołanie bulletIntoYou lub zmiana visability wroga

    # wyświetlenie aktualnej liczby punktów
