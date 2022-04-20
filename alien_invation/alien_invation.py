import pygame as pg
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_function as gf


def run_game():
	pg.init() 
	pg.display.set_caption("Alien Invasion")
	
	ai_settings=Settings()
	screen=pg.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) 
	ship=Ship(screen,ai_settings)
	bullets=Group()
	
	# 開始遊戲的主迴圈
	while True: 
	
		#檢查遊戲輸入
		gf.check_event(ai_settings,screen,ship,bullets)
		ship.update()
		gf.update_bullet(bullets)
		gf.update_screen(ai_settings,screen,ship,bullets)	
run_game() 




