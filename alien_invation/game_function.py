import sys
import pygame as pg
from bullet import Bullet

def check_event(ai_settings,screen,ship,bullets):
	for event in pg.event.get():
#是否關閉? 
		if event.type == pg.QUIT:
			sys.exit()
#按下按鍵?
		elif event.type == pg.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
			
#放開按鍵?
		elif event.type == pg.KEYUP:
			check_keyup_events(event,ai_settings,screen,ship,bullets)
			

def check_keydown_events(event,ai_settings,screen,ship,bullets):
	if event.key == pg.K_RIGHT:# →
		ship.moving_right = True
		
	if event.key == pg.K_LEFT:# ←
		ship.moving_left = True
		
	if event.key == pg.K_SPACE:# _
		fire_bullet(ai_settings,screen,ship,bullets)
	
	if event.key == pg.K_q:# Q
		sys.exit()

		
def check_keyup_events(event,ai_settings,screen,ship,bullets):
	if event.key == pg.K_RIGHT:
		ship.moving_right = False
		
	if event.key == pg.K_LEFT:
		ship.moving_left = False
		
def fire_bullet(ai_settings,screen,ship,bullets):
	if len(bullets) < ai_settings.bullet_allowed:
			new_bullet = Bullet(ai_settings, screen, ship)
			bullets.add(new_bullet)
		
def update_bullet(bullets):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	

def update_screen(ai_settings, screen, ship, bullets):
	 # 讓最近繪製的螢幕可見
	screen.fill(ai_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	ship.blitme()
	pg.display.flip()