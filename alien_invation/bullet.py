import pygame as pg
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self,ai_settings,screen,ship):
	 #在飛船所處的位置創建一個子彈物件
		super().__init__()
		self.screen=screen

	#在(0,0)處創建一個表示子彈的矩形，再設置正確的位置
		self.rect=pg.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
		self.rect.centerx=ship.rect.centerx
		self.rect.top=ship.rect.top
	#存儲用小數表示的子彈位置
		self.y=float(self.rect.y)

		self.color = ai_settings.bullet_color 
		self.speed_factor = ai_settings.bullet_speed_factor
		

	def update(self):
	#向上移動子彈
		self.y-=self.speed_factor
	#更新表示子彈位置的小數值
		self.rect.y=self.y

	def draw_bullet(self):
	#在螢幕上畫出子彈
		pg.draw.rect(self.screen,self.color,self.rect)
		