import pygame
from pygame.sprite import Sprite


class alien(Sprite):
    """表示單個外星人的類"""
	def __init__(self,ai_setting,screen):
	 """初始化外星人並設置其起始位置"""
		super().__init__()
		self.screen = screen
		self.ai_setting = ai_setting
		# 載入外星人圖像，並設置其rect屬性
		
		
		