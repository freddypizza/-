from pygame import *
import pygame.sprite
font.init()
font1 = font.SysFont('Arial', 80)
lose1 = font1.render("PLAYER 1 LOSE", True, (247, 5, 5))
lose2 = font1.render("PLAYER 2 LOSE", True, (247, 5, 5))
img_rocket = 'png-klev-club-p-raketka-png-1.png'
img_back = 'download.png'
img_ball = 'images.jpg'
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
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

raket1 = Player(img_rocket, 5, 100, 80, 100, 5)
raket2 = Player(img_rocket, 600, 100, 80, 100, 5)
ball = GameSprite(img_ball, 100, 100, 20, 20, 5)
clock = time.Clock()

finish = False
game = True
speed_x = 3
speed_y = 3
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish: 
        window.blit(background, (0,0))
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(raket1, ball) or sprite.collide_rect(raket2, ball):
            speed_x *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x > 700:
            finish = True
            window.blit(lose2, (200, 200))
        raket1.reset()
        raket1.update_l()
        raket2.reset()
        raket2.update_r()
        display.update()
        clock.tick(20) 
