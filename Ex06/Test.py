import pygame as pg
from pygame.locals import *     #Importing Star Variable

def Block():
    surface.fill((110, 110, 5))                     #Color of the Block
    surface.blit(block, (block_x, block_y))         #BlockSize
    pg.display.update()                             #Updating Display

    

if __name__ == "__main__":
    pg.init()                                       #Initializing PYGAME
    surface = pg.display.set_mode((500,500))        #Initializing WINDOW/DISPLAY
    surface.fill((110,255,255))                     #BackGroundColor
    pg.display.flip()                               #UpdatingPreviousCode
    block_x, block_y = 100, 100                     #CoordinatesOrSize
    block = pg.image.load("Ex06/SnakeBlock.png").convert()      #UploadingBlockImage
    surface.blit(block, (block_x, block_y))         #Draws The Block onto this Surface
    

    running = True                           #InfiniteLoop
    while running:                                 #Starting Coditional Code
        for event in pg.event.get():            
            if event.type == KEYDOWN:           #Conditional code that ends the inifiniteloop/event if the 'KEYDOWN' is pressed
                if event.key == K_ESCAPE:       #Conditional code that ends the inifiniteloop/event if the 'K_ESCAPE' is pressed
                    running = False
                if event.key == K_LEFT:         #Moves to the left side
                    block_x -= 10
                    block()
                if event.key == K_RIGHT:        #Moves to the Right side
                    block_x += 10
                    block()
                if event.key == K_UP:           #Moves to the Up side
                    block_y -= 10
                    block()
                if event.key == K_DOWN:         #Moves to the Down side
                    block_y += 10
                    block()

            elif event.type == QUIT:
                running = False
    
                  








