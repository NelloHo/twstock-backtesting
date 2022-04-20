import sys
import pygame as pg
from config import *
from sprites import *
class Game:
	def __init__(self):
		pg.init()
		self.screen=pg.display.set_mode((width,height))
		self.clock=pg.time.Clock()	 
		self.running=True
	def new(self):
		#開始遊戲
		self.playing=True
		self.all_sprites=pg.sprite.LayeredUpdates()
		self.blocks=pg.sprite.LayeredUpdates()
		self.enemies=pg.sprite.LayeredUpdates()
		self.attacks=pg.sprite.LayeredUpdates()
		self.player=Players(self,1,2)
	def event(self):
		#game loop event
		for event in pg.event.get():
			if event.type==pg.QUIT:
				self.playing=False
				self.running=False
	def update(self):
		self.all_sprites.update()
		
	def draw(self):
		self.screen.fill(black)
		self.all_sprites.draw(self.screen)
		self.clock.tick(FPS)
		pygame.display.update()
		
   
	def main(self):
		#game loop
		while self.playing:
			self.event()
			self.update()
			self.draw()
		self.running=False

	def game_over(self):
		pass
	def intro_screen(self):
		pass
g=Game()
g.intro_screen()
g.new()
while g.running:
	g.main()
	g.game_over
pg.QUIT
sys.exit()

		
	
		
		