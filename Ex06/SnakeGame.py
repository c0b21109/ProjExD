import pygame as pg
from pygame.locals import *                                                                          #Importing Star Variable

def Draw_Block():
    surface.fill((16, 67, 52))                                                                      #Color of the Block
    surface.blit(block, (block_x, block_y))                                                          #BlockSize
    pg.display.update()                                                                              #Updating Display

if __name__ == "__main__":
    pg.init()                                                                                       #Initializing PYGAME
    pg.display.set_caption("SNAKE GAME")                                                            #Setting Title 
    surface = pg.display.set_mode((1280,1128))                                                      #Initializing WINDOW/DISPLAY
    surface.fill((16,67,52))
    block_x, block_y = 100, 100                                                                     #CoordinatesOrSize
    block = pg.image.load("Ex06/Pics/SnakeBlock.png").convert()                                     #UploadingBlockImage
    surface.blit(block, (block_x, block_y))                                                         #Draws The Block onto this Surface

    
    clock = pg.time.Clock()
    running = True                                                                                  #InfiniteLoop
    while running:                                                                                  #Starting Coditional Code
        for event in pg.event.get():            
            if event.type == KEYDOWN:                                                               #Conditional code that ends the inifiniteloop/event if the 'KEYDOWN' is pressed
                if event.key == K_ESCAPE:                                                           #Conditional code that ends the inifiniteloop/event if the 'K_ESCAPE' is pressed
                    running = False
                if event.key == K_LEFT:                                                             #Moves to the left side
                    block_x -= 10
                    Draw_Block()
                if event.key == K_RIGHT:                                                            #Moves to the Right side
                    block_x += 10
                    Draw_Block()
                if event.key == K_UP:                                                               #Moves to the Up side
                    block_y -= 10
                    Draw_Block()
                if event.key == K_DOWN:                                                             #Moves to the Down side
                    block_y += 10
                    Draw_Block()

            elif event.type == QUIT:
                running = False
        pg.display.update()                                                                             #UpdatingPreviousCode
        
        clock.tick(1000)
    
                  








