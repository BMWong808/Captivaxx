import pygame

pygame.init()

win = pygame.display.set_mode((1000,600))
 
pygame.display.set_caption("Muddy Puddles")

bg = pygame.image.load('C:/Python27/Tests/Hack/back.png')
peps = pygame.image.load('C:/Python27/Tests/Hack/peppa.png')
mud = pygame.image.load('C:/Python27/Tests/Hack/puddle.png')
mudtwo = pygame.image.load('C:/Python27/Tests/Hack/puddletwo.png')
x = 820
y = 300
width = 40
height = 50
vel = 5

isjump = False
jumpcount = 10


def newdraw():
        win.blit(bg,(0,0))
        win.blit(mud,(100,400))
        win.blit(mudtwo,(600,475))
        win.blit(peps,(x,y))

        pygame.display.update()


running = True

while running:
        pygame.time.delay(100)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x > vel:
            x -= vel

        if keys[pygame.K_RIGHT] and x < 1000 - width - vel:
            x += vel
        if not(isjump):
                if keys[pygame.K_UP] and y > vel:
                        y -= vel
                if keys[pygame.K_DOWN] and y < 600 - height - vel:
                        y += vel
                if keys[pygame.K_SPACE]:
                        isjump = True
        else:
                if jumpcount >= -10:
                        minus = 1
                        if jumpcount < 0:
                                minus = -1
                        y -= (jumpcount ** 2) / 2 * minus
                        jumpcount -= 1

                else:
                        isjump = False
                        jumpcount = 10
        newdraw()



        
        
pygame.quit()




