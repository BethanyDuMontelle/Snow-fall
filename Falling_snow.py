import pygame, random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1920, 1080)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Snow Storm")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

star_list = []
for i in range(300):
    x = random.randrange(0, size[0])
    y = random.randrange(0, size[1])
    star_list.append([x, y])
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    for item in star_list:
        item[1] += 10
        item[0] += 5
        pygame.draw.circle(screen, WHITE, item, 2)
        
        #jiggle effect
        number = random.randrange(10)
        if number%2 == 0:
            item[0] += 3
        else:
            item[0] -+ 3
        if item[1] > size[1] or item [0] > size[0]:
            item[1] = random.randrange(-20, -5)
            item[0] = random.randrange(-300, size[0])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()

