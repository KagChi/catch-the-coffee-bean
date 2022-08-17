import pygame, sys, math, time
from pygame.locals import *
from player import Player
from background import Background
from utils import checkCollisions

def main():
    pygame.init()
    pygame.time.Clock().tick(60)
    display = pygame.display.set_mode((640, 480), 0, 32)
    pygame.display.set_caption('Catch the coffee bean')
    pygame.display.set_icon(pygame.image.load('./assets/images/coffee_bag.png'))

    font_small = pygame.font.Font('./assets/fonts/font.otf', 32)

    pygame.display.update()
    pygame.time.delay(10)

    titleScreen = True
    running = False
    
    background = [Background(), Background(), Background()]

    menu_theme = pygame.mixer.Sound.play(pygame.mixer.Sound("./assets/sfx/menu.mp3"), loops = -1, fade_ms = 600)

    while titleScreen:
        mouseX,mouseY = pygame.mouse.get_pos()  
        clicked = False
        keys = pygame.key.get_pressed()
        
        button = pygame.image.load('./assets/images/button.png')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
                pygame.quit()
                break

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    titleScreen = False
                    running = True
                    menu_theme.stop()
        if (clicked and checkCollisions(mouseX, mouseY, 3, 3, display.get_width() / 2 - button.get_width()/2, 288, button.get_width(), button.get_height())):
            clicked = False
            pygame.mixer.Sound.play(pygame.mixer.Sound("./assets/sfx/click.wav"))
            menu_theme.stop()
            titleScreen = False
            running = True
    
        logo = pygame.transform.scale(pygame.image.load('./assets/images/logo.png'), (1080, 480))
        display.fill((255, 255, 255))

        for bg in background:
            bg.setSprite(3.88 / 100)
            display.blit(bg.sprite, (0, bg.position))

        display.blit(logo, (display.get_width() / 2 - logo.get_width() / 2, display.get_height() / 4 - logo.get_height() / 4 + math.sin(time.time() * 5) * 5 - 25))
        display.blit(button, (display.get_width()/2 - button.get_width()/2, 288))
        startMessage = font_small.render("START", True, (0, 0, 0))
        display.blit(startMessage, (display.get_width() / 2 - startMessage.get_width() / 2, 292))
        pygame.display.flip()
        print((display.get_width() / 2 - startMessage.get_width() / 2, 292))

    gameSprites = pygame.sprite.Group()
    player = Player()
    
    gameSprites.add(player)

    pygame.mixer.Sound.play(pygame.mixer.Sound("./assets/sfx/theme.mp3"), loops = -1, fade_ms = 600)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    break
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    pygame.mixer.Sound.play(pygame.mixer.Sound("./assets/sfx/move.wav"))
                    player.dButtonClicked(5)
                    break
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    pygame.mixer.Sound.play(pygame.mixer.Sound("./assets/sfx/move.wav"))
                    player.aButtonClicked(5)
                    break
                break
            if event.type == pygame.TEXTINPUT:
                if event.text == "a":
                    player.aButtonClicked(15)
                    break
                if event.text == "d":
                    player.dButtonClicked(15)
                    break
    
        
        gameSprites.update()

        display.fill((255, 255, 255))

        for bg in background:
            bg.setSprite(3.88 / 100)
            display.blit(bg.sprite, (0, bg.position))

        gameSprites.draw(display)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()