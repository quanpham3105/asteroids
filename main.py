import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable,drawable)

    gameOn = True
    pygame.init() 
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT]) 
    pygameClock = pygame.time.Clock()
    dt = 0 
    currentPlayer = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    newField = AsteroidField()

    while gameOn:
        for event in pygame.event.get(): #Check to see if user closed tab or not
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        for player in drawable:
            player.draw(screen)
        updatable.update(dt)
        
        for asteroid in asteroids: # Check for player and asteroid collision
            if currentPlayer.collisionCheck(asteroid):
                print("Game Over!")
                return
            
        for asteroid in asteroids:
            for shot in shots:
                if shot.collisionCheck(asteroid):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()

        dt = pygameClock.tick(60)/1000 # Limit framerate to 60

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
if __name__ == "__main__":
    main()
