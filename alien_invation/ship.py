import pygame as pg
import sys

class Ship():
	def __init__(self,screen,ai_settings):
		#讓飛船存取螢幕及設置的屬性
		self.screen=screen
		self.ai_settings=ai_settings
		
		#獲取飛船圖片並修剪、設置初位置
		self.image=pg.transform.scale(pg.image.load('images/ship.png'),(90,180)) 
		self.rect=self.image.get_rect()
		self.screen_rect=screen.get_rect()
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom
		self.center = float(self.rect.centerx)
		
		#移動設置
		self.moving_right=False
		self.moving_left=False

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.center -= self.ai_settings.ship_speed
		self.rect.centerx=self.center

	def blitme(self):
		self.screen.blit(self.image,self.rect)
		

