from pygame import *
from random import randint

font.init()
font1 = font.Font(None, 26)
font2 = font.Font(None, 60)

win_widht = 700
win_heidht = 500

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, sise_x, sise_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (sise_x, sise_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_widht - 80:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet('en.jpg', self.rect.centerx, self.rect.top, 35, 40, -15)
        bullets.add(bullet)

lost = 0 
score = 0

class Enemy(GameSprite):
   def update(self):
       self.rect.y += self.speed
       global lost
       if self.rect.y > win_heidht:
           self.rect.x = randint(80, win_widht - 80)
           self.rect.y = 0
           lost = lost + 1
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
       #исчезает, если дойдет до края экрана
        if self.rect.y < 0:
           self.kill()

bullets = sprite.Group()

ship = Player('rocket.png', 300, 420, 70, 70, 3)
hoz_1 = Enemy('frametamer.jpg', randint(80, 620),0, 70, 70, randint(1, 3))
hoz_2 = Enemy('frametamer.jpg', randint(80, 620),0, 70, 70,randint(1, 3))
hoz_3 = Enemy('frametamer.jpg', randint(80, 620),0, 70, 70,randint(1, 3))
hoz_4 = Enemy('fpd.jpg', randint(80, 620),0, 70, 70,randint(1, 3))
hoz_5 = Enemy('fpd.jpg', randint(80, 620),0, 70, 70,randint(1, 3))
monsters = sprite.Group()
monsters.add(hoz_1)
monsters.add(hoz_2)
monsters.add(hoz_3)
monsters.add(hoz_4)
monsters.add(hoz_5)
Finish = False
run = True

win_widht = 700
win_heidht = 500
window = display.set_mode((win_widht, win_heidht))
display.set_caption('Никто не узнает секрет карпового озера')
background = transform.scale(image.load('galaxy.jpg'),(win_widht, win_heidht))
mixer.init()
mixer.music.load('tabletka.ogg')
mixer.music.play()



clock = time.Clock()
FPS = 60
finish = False
game = True 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship.fire()
    if finish != True:

        sprites_list = sprite.groupcollide(monsters, bullets, True, True)
        for el in sprites_list:
            num = randint(1, 2)
            if num == 1:
                monster = Enemy('frametamer.jpg',randint(80, 620),0, 80, 60, randint(1, 3))
                monsters.add(monster)
            else:
                monster2 = Enemy('fpd.jpg',randint(80, 620),0, 80, 60, randint(1, 3))
                monsters.add(monster2)
            score += 1
            
        text_lose = font1.render('Пропущено: ' + str(lost), 1, (255, 255, 255))
        text_score = font1.render('Счет: ' + str(score), 1, (255, 255, 255))

        window.blit(background,(0,0))
        window.blit(text_score, (20, 50))
        window.blit(text_lose,(20, 20))
        ship.update()
        ship.reset()
        bullets.draw(window)
        bullets.update()
        monsters.draw(window)
        monsters.update()
        if score > 15:
            text_win = font2.render('СИГМА', 1, (0, 255, 100))
            window.blit(text_win,(250,200))
            finish = True

        if lost > 3:
            end = font2.render('БОЖ УДАЛИ ИГРУ ОЛУХ', 1, (0, 255, 100))
            window.blit(end,(100,200))
            finish = True
        display.update()
        clock.tick(FPS)
