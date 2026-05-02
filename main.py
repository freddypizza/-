from pygame import *
import pygame.sprite
font.init()
font1 = font.SysFont('Arial', 80)
lose = font1.render("YOU LOSE", True, (247, 5, 5))
img_rocket = 'png-klev-club-p-raketka-png-1.png'
img_back = 'download.png'
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
class GameSprite(sprite.Sprite):
    #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#класс главного игрока
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.x += self.speed
raket1 = Player(img_rocket, 5, 100, 80, 100, 5)
clock = time.Clock()

finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish: 
        window.blit(background, (0,0))
        raket1.reset()
        raket1.update_l()
        display.update()
        clock.tick(20) 