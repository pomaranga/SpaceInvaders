class Ship:
    # sprite

    def shot(self, isUp, posH, posV):
        fill(25, 255, 0)
        b = Bullet(isUp, posH, posV) # tworzymy instancję pocisku
        bullet_group.add(b) # dodajemy do listy sktywnych pocisków ów pocisk
        rect(0, 20, 20, 20) # to zostawiam w celach debugowych 
        self.speed = 3  # ustawienie prędkości ruchu pocisku


class Player(Ship):

    # poczatkowa pozycja
    def __init__(self):
        self.positionH = 350
        self.positionV = 475
        self.sprite = loadImage("Gracz One.png")
        self.width = 100 # Szerokosc statku
        self.height = 80 # Wysokosc statku
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
        self.cc = self.cc + 0.15
        self.dd = self.dd + 5
        self.ee = self.ee + 5
        
        if (self.aa > 800) or (self.bb > 600):
            self.aa = random(0,300)
            self.bb = random(0,400)
            self.cc = 1
        if (self.dd > 800) or (self.ee > 600):
            self.dd = random(0,300)
            self.ee = random(0,400)
            self.cc = 1
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
        #player1.sketch_explosion()

    def changePositionH(self, offset):
        self.positionH = self.positionH + offset

    def changePositionV(self, offset):
        self.positionV = self.positionV + offset

    def sketch_player(self):
        image(self.sprite, self.positionH, self.positionV, 100, 80)
        # POKAZANIE OBSZARU KOLIZJI
        stroke(100)
        noFill()
        rect(self.positionH, self.positionV, self.width, self.height) # Obszak ktory obejmuje statek.
        noStroke()
        # KONIEC POKAZYWANIE OBSZARU KOLIZJI

class Enemy(Ship):
    nextShot = 0
    quantity = 6

    def __init__(self, pos):
        self.positionHorizontal = pos
        self.positionVertical = 15
        self.movementDirection = 1
        self.visability = True
        self.sprite = loadImage("Ship.png")
        self.width = 80 # Szerokosc statku
        self.height = 50 # Wysokosc statku

    def changePosition(self):
        if self.positionHorizontal < 0:
            self.positionVertical += 50
            self.movementDirection = 1
        if self.positionHorizontal > 700:
            self.positionVertical += 50
            self.movementDirection = 0
        if self.movementDirection == 0:
            self.positionHorizontal -= 1.7
        if self.movementDirection == 1:
            self.positionHorizontal += 1.7
    def changeVisability(self):
        self.visability = False  # zmina visability
        # sprawdzanie czy wszyscy zestrzeleni (areEnemiesDestroyed)
        # doliczenie punktów

    def sketch_ship(self):
        image(self.sprite, self.positionHorizontal, self.positionVertical)
        # POKAZANIE OBSZARU KOLIZJI
        stroke(100)
        noFill()
        rect(self.positionHorizontal, self.positionVertical, self.width, self.height) # Obszak ktory obejmuje statek.
        noStroke()
        # KONIEC POKAZYWANIE OBSZARU KOLIZJI
       
        
    
class Bullet:
    def __init__(self, isUp, posH, posV):
        self.positionH = posH
        self.positionV = posV
        self.isUp = isUp # Zmienna przechowujaca informacje czy pocisk leci do gory
        self.sprite= loadImage("arrow.png")
        self.width = 80 # Szerokosc pocisku
        self.height = 50 # Wysokosc pocisku

    def update(self):  # movement - metoda
        if self.isUp == False: # Jezeli pocisk nie leci do gory
            self.positionV += 5  # szybkosc lotu pocisku
            if self.positionV >= 600:
                bullet_group.remove(self)
        if self.isUp == True: # Jezeli pocisk leci do gory
            self.positionV -= 5
            if self.positionV <= 0:
                bullet_group.remove(self)
                
    def sketch_bullet(self):
        image(self.sprite, self.positionH, self.positionV)

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
        
        # POKAZANIE OBSZARU KOLIZJI
        stroke(100)
        noFill()
        rect(self.positionH, self.positionV, self.width, self.height) # Obszak ktory obejmuje pocisk.
        noStroke()
        # KONIEC POKAZYWANIE OBSZARU KOLIZJI

    def update_movement(self):
        self.positionV
        self.positionH 
        


class RepairKit:
    def sketch_RepairKit(self):
        self.sprite = loadImage("RepairKit.png")  # to tylko załadowanie grafiki, nie rysowanie, powinno dziać się raz, nie co klatkę
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
        image(loadImage("gameover.png"), 300,400)# wyświetlenie GameOver
        player1.sketch_explosion()
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
    global enemyList, player1, ship1, bullet_group, tlo, s, repairKit, interface
    tlo = loadImage("background.jpg")
    player1 = Player()
    enemyList = []
    for num, i in enumerate(range(Enemy.quantity)):
        enemyList.append(Enemy(0 + num * 100))
    bullet_group = set()
    s = Shield()
    interface = Interface()
    repairKit = RepairKit()

# Funkcja wykrywajaca czy zachodzi kolizja pomiedzy dwoma prostokatami
def inBounds (posX1, posY1, width1, height1, posX2, posY2, width2, height2):
    if (posX1 < posX2 + width2 and posX1 + width1 > posX2 and posY1 < posY2 + height2 and posY1 + height1 > posY2):
        return True
    return False

def draw():
    image(tlo, 0, 0)
    player1.sketch_player()
    player1.shooting_stars()
    s.sketch_shield()
    repairKit.sketch_RepairKit()
    
    #galaktyka-tło-grafika-orbita
    stroke(255,255,255)
    fill(0, 0, 0, 0)
    ellipse(2, 2, 500, 500)
    stroke(255,247,0)
    fill(255,250,87)
    ellipse(2, 2, 200, 200)
    stroke (255, 255, 255)
    fill(255, 255, 255)
    ellipse(250, 30, 30, 30)
    stroke (255, 255, 255)
    fill(168, 168, 168)
    ellipse(207, 150, 50, 50)
    stroke (81, 81, 81)
    fill(81, 81, 81)
    ellipse(207, 150, 4, 4)
    stroke (81, 81, 81)
    fill(81, 81, 81)
    ellipse(225, 150, 4, 4)
    stroke (81, 81, 81)
    fill(81, 81, 81)
    ellipse(190, 150, 4, 4)
    stroke (81, 81, 81)
    fill(81, 81, 81)
    ellipse(207, 134, 4, 4)
    stroke (81, 81, 81)
    fill(81, 81, 81)
    ellipse(207, 165, 4, 4)

    
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
            player1.shot(True, player1.positionH, player1.positionV)
      
    for enemy in enemyList:
        enemy.changePosition()
        if enemy.positionVertical >=player1.positionV-15:
            interface.bulletOrShipIntoYou()
        enemy.sketch_ship()
        enemy.nextShot -= 1  # loop countdown to shot
        if enemy.nextShot <= 0:  # loop countdown to shot
            isShooting = int(random(0, 2))  # drawing whether the opponent shoots
            enemy.nextShot = 100  # loop countdown to shot
            if isShooting == 1:  # if the shot is drawn
                enemy.shot(False , enemy.positionHorizontal, enemy.positionVertical)

    for bullet in bullet_group:
        bullet.update()
        bullet.update_movement() # przesunięcie w odpowiednim kierunku pozycji każdego z aktywnych pocisków na ekranie (liście pocisków ekranu)
        bullet.sketch_bullet2()
        bullet.sketch_bullet()
        
        if(bullet.isUp == True): # Jezeli pocisk leci w gore to:
            for ememy in list(enemyList): # Przelatujemy przez cala liste wrogow i:
                if (inBounds(bullet.positionH, bullet.positionV, bullet.width, bullet.height, ememy.positionHorizontal, enemy.positionVertical, enemy.width, enemy.height) == True): # Jezeli wrog i pocisk sie zderzaja to:
                    enemyList.remove(ememy) # To usuwamy wroga z listy wrogow.
        
        if(bullet.isUp == False): # Jezeli pocisk leci w dol to:
            if (inBounds(bullet.positionH, bullet.positionV, bullet.width, bullet.height, player1.positionH, player1.positionV, player1.width, player1.height) == True): # Jezeli gracz i pocisk sie zderzaja to:
                interface.bulletOrShipIntoYou() # Powiadamiamy interfejs ze cos przywalilo w nasz statek
                bullet_group.remove(bullet)     # Usuwamy pocisk z gry
        
        if bullet.positionV == player1.positionV: # sprawdzenie, czy pozycja pocisku pokrywa się z tą gracza w pionie
            if bullet.positionH == player1.positionH: # sprawdzenie, czy pozycja pocisku pokrywa się z tą gracza w poziomie
                pass # to do uzupełnienia
         
    # sprawdzenie, czy kierunek strzały jest zgodny ze statkiem którego dotyka
    # zależnie od tego którego statku dotyka, wywołanie bulletIntoYou lub zmiana visability wroga

    interface.showScore() # wyświetlenie aktualnej liczby punktów
    interface.draw_health()
