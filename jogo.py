import pygame, sys, eztext, os
from match import *
from pygame.locals import *
from Team import *
from sys import exit
from menu import *

pygame.init()
 
screen = pygame.display.set_mode((1280, 720), 0, 32)

background_filename = 'src/bg2.png'
background = pygame.image.load(background_filename).convert()

pygame.display.set_caption('BrasLuL')

#carrega os times
teams = []
players = []


play_button = Botao([600,300],[200,90], 'JOGAR',70)
load_button = Botao([600,400],[200, 90], 'CARREGAR',50)
clock = pygame.time.Clock()


def loadTeams():
	path = 'Times/'
	teamsLocal = os.listdir(path)
	
	for i in teamsLocal:
		i += '/' + i + '.txt'
		teams.append(Team(path+i))

	
loadTeams()

def loadPlayers():
	
	mid_Laners = {'path': 'players/mid/', 'players': []}
	mid_Laners['players'] = os.listdir(mid_Laners['path'])
	
	top_Laners = {'path': 'players/top/', 'players': []}
	top_Laners['players'] = os.listdir(top_Laners['path'])
	
	junglers = {'path': 'players/jungler/', 'players': []}
	junglers['players'] = os.listdir(junglers['path'])
	
	support = {'path': 'players/support/', 'players': []}
	support['players'] = os.listdir(support['path'])
	
	adc = {'path': 'players/adc/', 'players': []}
	adc['players'] = os.listdir(adc['path'])
	
	for i in mid_Laners['players']:
		if i not in "photos":
			players.append(Mid_Laner(mid_Laners['path']+i))
	
			
	for i in top_Laners['players']:
		if i not in "photos":
			players.append(Top_Laner(top_Laners['path']+i))

			
	for i in junglers['players']:
		if i not in "photos":
			players.append(Jungler(junglers['path']+i))
			
	for i in support['players']:
		if i not in "photos":
			players.append(Support(support['path']+i))
			
	for i in adc['players']:
		if i not in "photos":
			players.append(Adc(adc['path']+i))
	
	for i in players:
		for j in teams:
			if i.team == j.code:
				j.addPlayer(i)

loadPlayers()

game = Match(teams[0].players, teams[1].players, screen)

for j in teams:
	print(j.name + ":")
	j.listPlayers()

def mainMenu():
	
	while True:
		screen.blit(background, [0,0])
		
		for event in pygame.event.get():
			
			if event.type == QUIT:
				exit()
			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				# get a list of all sprites that are under the mouse cursor
				if play_button.rect.collidepoint(pos):
					newGame()
				if load_button.rect.collidepoint(pos):
					i = ''
			
		
		
		play_button.show(screen)
		load_button.show(screen)
		
		pygame.display.update()
		
	time_passed = clock.tick(60) 

def newGame():
	
	
	screen.blit(background, [0,0])
	teste = TextBox([600, 100], [200, 500], ["opa 1 aa solado maluco"], 40)
	teste2 = TextBox([600, 100], [600, 600], ["opa 2 aa solado maluco"], 40)
	
	getName = InputBox(400,300, "NOME: " )
	
	
	while True:
		getName.show(screen)
		teste.show(screen)
		teste2.show(screen)
		
		events = pygame.event.get()
		
		
		for event in events:
			if event.type == QUIT:
				exit()
			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				# get a list of all sprites that are under the mouse cursor
				if getName.rect.collidepoint(pos):
					getName.isSelected = True
					
				if not(getName.rect.collidepoint(pos)):
					getName.isSelected = False
					
					
		if getName.isSelected:
			getName.box.update(events)
			# blit txtbx on the sceen
			
		
		pygame.display.update()
		
	time_passed = clock.tick(60) 

mainMenu()
