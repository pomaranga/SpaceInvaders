class Ship:

    def shot(self, isUp, posH, posV):
        b = Bullet(isUp, posH, posV) # tworzymy instancję pocisku
        bullet_group.add(b) # dodajemy do listy sktywnych pocisków ów pocisk
        self.speed = 3  # ustawienie prędkości ruchu pocisku


class Player(Ship):
nextShot = 100
shotcount = 5
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
    def sketch_explosion(self): #player1.sketch_explosion()
        self.sprite = loadImage("explosion.png")
        image(self.sprite, self.positionH - 15, self.positionV - 15)

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

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN-100:
           self.cool_down_counter = 0
        else: 
            self.cool_down_counter+=1
            
            
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
    def __init__(self):
        self.visability = False
        self.sprite = loadImage("RepairKit.png")  # to tylko załadowanie grafiki, nie rysowanie, powinno dziać się raz, nie co klatkę
        
    def sketch_RepairKit(self):
         self.positionH = 30
         self.positionV = 490
        if self.visability == True:
            image(self.sprite, self.positionH, self.positionV)
        self.value = 20
        
    def RepairKitCollision(self):
        if player1.positionH == self.positionH:
            self.visability = False
            return True
        return False
        
    def RepairKitSpawn(self):
        if Interface.points >= 1:
            if Interface.health <= 80:
                self.visability = True
                return True
        return False

    def RepairProcedure(self):
        if (self.RepairKitCollision() and self.RepairKitSpawn()) == True:
            Interface.health += self.value
            text("naprawiono", height/4, width/4)


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
        rect(550, 550, Interface.health * 2, 30)
        textSize(30)
        text("Health: " + str(Interface.health), 550, 540)

                    
    def bulletOrShipIntoYou(self): #2 
        Interface.health -= 10
        if Interface.health <= 0:
            image(loadImage("gameover.png"), 300, 100)# wyświetlenie GameOver
            fill(255, 0, 0)
            text("Twoje punkty to " + str(Interface.points), width / 3, 350)
            player1.sketch_explosion()
            noLoop() 
        
    def areEnemiesDestroyed(self):
        for enemy in enemyList:
            if enemy.visability == True:
                return False
        image(loadImage("victory.png"), 0, 165)
        noLoop()
        return True

    def addPoint(self):
        Interface.points += 1

    def showScore(self):
        textSize(30)
        text("Score:" + str(Interface.points), 5, 50)  # metoda wyświetlająca bieżącą punktację    

        
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
    
    #meteoryty
    fill(200, 100, 0)
    rect(30, 200, 50, 50)
    fill(250, 100, 0)
    rect(300, 500, 30, 30)
    fill(200, 100, 0)
    rect(200, 30, 30, 30)
    fill(250, 100, 0)
    rect(400, 200, 50, 50)
    fill(250, 100, 0)
    rect(50, 70, 30, 30)
    fill(200, 100, 0)
    rect(500, 500, 30, 30)
    fill(250, 100, 0)
    rect(100, 30, 70, 70)
    
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
    
    #grafiki do tła (planety) 
    stroke(19,26,60)
    fill(19,26,60)
    ellipse(400, 100, 100, 100)
    ellipse(400, 100, 200, 50)
    stroke(14,19,47)
    fill(14,19,47)
    ellipse(400, 81, 90, 60)
    stroke(47,79,79)
    fill(47,79,79)
    ellipse(400, 300, 70, 70)
    stroke (90, 90, 70)
    fill(90, 90, 70)
    ellipse(500, 400, 30, 30)

    # wyjście z gry (exit)
    fill(220,0,190,130)
    rect(720, 10, 70, 40)
    text('exit', 727,40)
    
    fill(220,0,190,130)
    rect(605, 10, 100, 40)
    text('restart', 607,40)
    
    player1.nextShot += 1
    
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
      
        if player1.positionH < 0:
            player1.positionH = 0
        if player1.positionH > 700:
            player1.positionH = 700
            
            def keyTyped():
if key == " " or key == ENTER: # jeżeli spacja lub enter lub strzałka w dół
if player1.shotcount > 0 and player1.nextShot > 100:
player1.shotcount -= 1
player1.nextShot = 0
player1.shot(True, player1.positionH, player1.positionV)

            
    for enemy in enemyList:
        enemy.changePosition()
        if enemy.positionVertical >=player1.positionV-15:
            interface.bulletOrShipIntoYou()
        enemy.sketch_ship()
        enemy.nextShot -= 1  # loop countdown to shot
        if enemy.nextShot <= 0:  # loop countdown to shot
            isShooting = int(random(0, 2))  # drawing whether the opponent shoots
            enemy.nextShot = random (65,100)  # loop countdown to shot
            if isShooting == 1:  # if the shot is drawn
                enemy.shot(False , enemy.positionHorizontal, enemy.positionVertical)

    for bullet in bullet_group:
        bullet.update()
        bullet.update_movement() # przesunięcie w odpowiednim kierunku pozycji każdego z aktywnych pocisków na ekranie (liście pocisków ekranu)
        bullet.sketch_bullet()
        
        if(bullet.isUp == True): # Jezeli pocisk leci w gore to:
            for ememy in list(enemyList): # Przelatujemy przez cala liste wrogow i:
                if (inBounds(bullet.positionH, bullet.positionV, bullet.width, bullet.height, ememy.positionHorizontal, enemy.positionVertical, enemy.width, enemy.height) == True): # Jezeli wrog i pocisk sie zderzaja to:
                    image(loadImage("explosion.png"), ememy.positionHorizontal, enemy.positionVertica, enemy.width, enemy.heigh)
                    enemyList.remove(ememy) # To usuwamy wroga z listy wrogow.
                    interface.addPoint() #dodawnie punktów jeśli zestrzeli się przeciwnika
                    repairKit.RepairKitSpawn()
        
        if(bullet.isUp == False): # Jezeli pocisk leci w dol to:
            if (inBounds(bullet.positionH, bullet.positionV, bullet.width, bullet.height, player1.positionH, player1.positionV, player1.width, player1.height) == True): # Jezeli gracz i pocisk sie zderzaja to:
                interface.bulletOrShipIntoYou() # Powiadamiamy interfejs ze cos przywalilo w nasz statek
                bullet_group.remove(bullet)     # Usuwamy pocisk z gry
                
    repairKit.RepairProcedure()
    interface.showScore() # wyświetlenie aktualnej liczby punktów
    interface.draw_health()
    interface.areEnemiesDestroyed() #wywołanie metody żeby sprawdzić czy się grało czy nie
    
def keyTyped(): 
    if key == " " or key == ENTER: # jeżeli spacja lub enter lub strzałka w dół
        player1.shot(True, player1.positionH, player1.positionV)
        
def mouseClicked():
    if mouseX >720 and mouseX<790:
        if mouseY <50 and mouseY >10:
            exit()
            
    if mouseX >605 and mouseX < 707:
        if mouseY <50 and mouseY >10:
            setup()

    
            
