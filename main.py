import sys
import pygame
from player import Player
from constants import *
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
    pygame.init()
    print("Starting Asteroids!")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()    

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    asteroid_field = AsteroidField()

    player = Player(
        x=SCREEN_WIDTH / 2,
        y=SCREEN_HEIGHT / 2
    )

    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game Over")
                sys.exit()
        
        screen.fill("black")
        
        for entity in drawable:
            entity.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
