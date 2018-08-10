import math
import pygame, eztext
import PIL.Image

blank_box = 'src/blank_box.png'

class Botao(pygame.sprite.Sprite):
	
	def __init__(self, pos, tam, text, font_size):
		
		self.X_BUTTON = tam[0]
		self.Y_BUTTON = tam[1]
		
		self.weight = tam[0]
		self.height = tam[1]
		
		pygame.font.init()
		font_name = pygame.font.get_default_font()
		game_font = pygame.font.SysFont(font_name, font_size)
		
		image = 'src/button1.png'
		self.image = pygame.image.load(image)
		
		pygame.sprite.Sprite.__init__(self)
		self.text = game_font.render(text, 1, (0, 0, 0))
		self.original = pygame.image.load(image)
		
		#posicao no quadro
		self.rect = self.image.get_rect()
		#posicao relativa
		self.pos_x = pos[0]
		self.pos_y = pos[1]

		self.rect.x = pos[0]
		self.rect.y = pos[1]
		
		#FÓRMULA LINDA MARAVILHOSA QUE EU DESCOBRI QUE CENTRALIZA O TEXTO NO BOTAO
		self.text_x = (self.X_BUTTON-((font_size/2)*len(text)))/2+ self.pos_x
		self.text_y = (self.Y_BUTTON-((font_size/2)))/2 + self.pos_y

	def __str__(self):
		return self.name

	def show(self, screen):
		pygame.draw.rect(screen, (255, 255, 255), (self.pos_x,self.pos_y, self.weight, self.height), 0)
		screen.blit(self.text, [self.text_x,self.text_y])


class InputBox():
	def __init__(self, x, y, text):
		self.pos_x = x
		self.pos_y = y
		self.image = pygame.image.load(blank_box)
		
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
		self.isSelected = False
		
		self.box = eztext.Input(maxlength=45, color=(0,0,0), prompt=text)
		self.box.set_pos(x, y+15)
		
	def set_pos(self, x, y):
		self.box.set_pos(x, y+15)
		self.pos_x = x
		self.pos_y = y
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
		
	def show(self, surface):
		surface.blit(self.image, (self.pos_x, self.pos_y))
		self.box.draw(surface)
	
		
class TextBox:

	def __init__(self, p, t, text, font_size):
		
		pygame.font.init()
		font_name = pygame.font.get_default_font()
		game_font = pygame.font.SysFont(font_name, font_size)
		
		
		self.pos_x = p[0]
		self.pos_y = p[1]
		
		self.weight = t[0]
		self.height = t[1]
		
		j = 0
		self.text = []
		aux = {'value': '','x': 0, 'y':0}
		
		j = 0
		
		for i in text:
		
			aux['value'] = game_font.render(i, 1, (0, 0, 0))
			aux['x'] = (self.weight-((font_size/3)*len(i)))/2+ self.pos_x
			aux['y'] = (self.height-((font_size/2)))/2 + self.pos_y + j*p[0]
			self.text.append(aux)			
			
			j+=1

			
			
	def show(self, screen):
		pygame.draw.rect(screen, (255, 255, 255), (self.pos_x,self.pos_y, self.weight, self.height), 0)
		for i in self.text:
			
			screen.blit(i['value'], [i['x'],i['y']])
	
	

class Cursor(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("cursor.png")
        self.rect  = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.selec = 1


