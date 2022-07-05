import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400,500))
clock = pygame.time.Clock()
test_surface = pygame.Surface((100,200))
test_surface.fill((250,120,170))
test_rect = test_surface.get_rect(center = (200,250))																								# pygame.Rect(100,200,100,100)
x_pos = 200
y_pos = 250

while True:
	# draw all our elements
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	screen.fill((175,215,70))
			# screen.fill(pygame.Color('gold'))
			# pygame.draw.rect(screen, pygame.Color('red'), test_rect)
	screen.blit(test_surface, test_rect)
	pygame.display.update()
	clock.tick(60)
