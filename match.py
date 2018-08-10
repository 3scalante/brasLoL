from menu import *
import random, sys, pygame, os
from pygame.locals import *
from sys import exit

clock = pygame.time.Clock()

pygame.init()


"""
i=0
while True:
	clock.tick(1000)
	
	if(i%1000==0 or  i == 0):
		print(i/1000)
		
	
	i+=1
"""

class Dragon():
	def __init__(self):
		self.isAlive = False
		self.spawnIn = 3
		self.bonus = 100
		self.name = 'Dragão'
		
	def att(self, gameTime):
		if (self.spawnIn>0):
			self.spawnIn -= 1
		else:
			self.isAlive = True
		
		if(gameTime%3 == 0 and gameTime != 3):
			self.bonus += 5
			
	def slay(self, gameTime):
		if(gameTime + 6 <= 35):
			self.spawnIn = 6
			self.isAlive = False
		else:
			self.name = 'Dragão Ancião'
			self.spawnIn = 10
			self.isAlive = False
			self.bonus += 100

class Herald():
	def __init__(self):
		self.isAlive = False
		self.spawnIn = 10
		self.bonus = 100
		self.name = 'Arauto do Vale'
		self.slayed = False
		
	def att(self, gameTime):
		if (self.spawnIn>0 ):
			self.spawnIn -= 1
		elif (self.spawnIn <= 0 and not self.slayed):
			self.isAlive = True
			
		if(gameTime >20):
			self.isAlive = False
			
	def slay(self, gameTime):
		self.slayed = True
		self.isAlive =  False
class Baron():
	def __init__(self):
		self.isAlive = False
		self.spawnIn = 20
		self.bonus = 300
		self.name = 'Barão Nashor'
		
	def att(self, gameTime):
		if (self.spawnIn>0):
			self.spawnIn -= 1
		else:
			self.isAlive = True
		
		if(gameTime%3 == 0 and gameTime > 20):
			self.bonus += 5
			
	def slay(self, gameTime):
		self.spawnIn = 7
		self.isAlive = False
		
class Tower():
	
	def __init__(self, life, bonus, name):
		self.isUp = True
		self.bonus = bonus
		self.life = life
		self.name = name
		self.bonus = 300
		
		self.life+=bonus
		
	def hit(self):
		
		if (self.life - 10 > 0):
			self.life-=10
			return False
			
		elif (self.life - 10 == 0):
			self.life-=10
			self.isUp = False
			return True
			
class Inhibitor():
	def __init__(self, lane):
		self.isUp = True
		self.bonus = 400
		self.life = 200
		self.name = 'Inibidor do '+ lane
		self.respawn = 0
		
	def hit(self):
		
		if (self.life - 10 > 0):
			self.life-=10
			return False
			
		elif (self.life - 10 == 0):
			self.life-=10
			self.isUp = False
			self.respawn = 4
			return True
	
	def att(self, x):
		if not self.isUp:
			self.respawn -= 1
			if self.respawn == 0:
				self.isUp= True
				x.respawnInhib()
				
class Nexus():
	def __init__(self):
		self.isUp = True
		self.life = 250
		self.name = 'Nexus'
		
	def hit(self):
		
		if (self.life - 10 > 0):
			self.life-=10
			return False
			
		elif (self.life - 10 == 0):
			self.life-=10
			self.isUp = False
			return True
	
		

class LaneStructures():
	def __init__(self, lane):
		self.structuresUp = 3
		self.lane= lane.lower()
		self.structures = [Inhibitor(lane) , Tower(200, 100, 'Torre de Inibidor do '+ lane), 
												Tower(150, 50, 'T2 do '+ lane), Tower(100, 50, 'T1 do '+ lane)]
		self.down = False
		
	def push(self, team, myStructures):
		
		
		for i in team:
			if self.structures[self.structuresUp].hit(): 
				
				print(self.structures[self.structuresUp].name + ' destruída(o) para '+ team[0].teamObject.name)
				i.advantage += self.structures[self.structuresUp].bonus
				
				
				
				for j in myStructures.structures:
					if j.isUp: j.life += 50
				
				self.structuresUp -= 1 
		
		if (self.structuresUp == -1):
			self.down = True
	
	def att(self, gameTime):
		if gameTime > 10:
			for i in self.structures:
				if i.life > i.bonus and type(i) is Tower:
					i.life -= i.bonus
					
	
	def respawnInhib(self):
		self.structuresUp += 1
		self.down = False
	
		
class BaseStructures():
	def __init__(self):
		self.structuresUp = 2
		self.structures = [Nexus(), Tower(0, 120, 'Torre de Nexus'), Tower(0, 120, 'Torre de Nexus')]
		self.lane = 'base'
		
	def push(self, team):
		
		for i in team:
			if (self.structuresUp>0):
				if self.structures[self.structuresUp].hit(): 
					print(self.structures[self.structuresUp].name + ' destruída(o) para '+ team[0].teamObject.name)
					i.advantage += self.structures[self.structuresUp].bonus
					self.structuresUp -= 1 
			else:
				if self.structures[self.structuresUp].hit(): 
					print(self.structures[self.structuresUp].name + ' destruído para '+ team[0].teamObject.name+ '!\n FIM DO JOGO')
					self.structures[self.structuresUp].isUp = False
					return True

		return False
	
			

class Match():

	
	
	def __init__(self, myTeam, oponent, screen):
	
		background_filename = 'src/bg2.png'
	
		self.background = pygame.image.load(background_filename).convert()
		
		self.myTeam = myTeam
		
		self.oponentTeam = oponent
		
		self.ally_kills = 0
		self.opponent_kills = 0
		self.gameTime = 0
		
		self.dragon = Dragon()
		self.herald = Herald()
		self.baron = Baron()
		
		self.allyMidStructures = LaneStructures('Mid')
		self.allyTopStructures = LaneStructures('Top')
		self.allyBotStructures = LaneStructures('Bot')
		
		self.allyBaseStructures = BaseStructures()
		
		
		self.oponentMidStructures = LaneStructures('Mid')
		self.oponentTopStructures = LaneStructures('Top')
		self.oponentBotStructures = LaneStructures('Bot')
		
		self.oponentBaseStructures = BaseStructures()
		
		self.allLaneStructures = (self.allyMidStructures, self.allyTopStructures, self.allyBotStructures, 
		self.oponentMidStructures, self.oponentTopStructures, self.oponentBotStructures)
		
		self.ally = {'top': {'object': object,  'advantage' : 0},
		'mid' : {'object': object,  'advantage' : 0},
		'support' : {'object': object,  'advantage' : 0},
		'jungler' : {'object': object,  'advantage' : 0},
		'adc' : {'object': object,  'advantage' : 0}
		}
		
		self.oponent = {'top': {'object': object,  'advantage' : 0},
		'mid' : {'object': object,  'advantage' : 0},
		'support' : {'object': object,  'advantage' : 0},
		'jungler' : {'object': object,  'advantage' : 0},
		'adc' : {'object': object,  'advantage' : 0}
		}
		
		
		
		for i in myTeam:
			if 'top' in i.function:
				self.ally['top']['object'] = i 
			if 'mid' in i.function:
				self.ally['mid']['object'] = i 
			if 'support' in i.function:
				self.ally['support']['object'] = i 
			if 'jungler' in i.function:
				self.ally['jungler']['object'] = i 
			if 'adc' in i.function:
				self.ally['adc']['object'] = i 
		
		for i in oponent:
			if 'top' in i.function:
				self.oponent['top']['object'] = i 
			if 'mid' in i.function:
				self.oponent['mid']['object'] = i 
			if 'support' in i.function:
				self.oponent['support']['object'] = i 
			if 'jungler' in i.function:
				self.oponent['jungler']['object'] = i 
			if 'adc' in i.function:
				self.oponent['adc']['object'] = i 		
		
		self.early_Game(myTeam, oponent, screen)
		
		print ('')
		
	def getOponentStructures(self, player, lane):
		if (player.team == self.ally['mid']['object'].team):
			if 'mid' in lane:
				return self.oponentMidStructures
			elif 'top' in lane:
				return self.oponentTopStructures
			elif 'bot' in lane:
				return self.oponentBotStructures
			elif 'base' in lane:
				return self.oponentBaseStructures
		else:
			if 'mid' in lane:
				return self.allyMidStructures
			elif 'top' in lane:
				return self.allyTopStructures
			elif 'bot' in lane:
				return self.allyBotStructures
			elif 'base' in lane:
				return self.allyBaseStructures
	
	def getAllyStructures(self, player, lane):
		if not (player.team == self.ally['mid']['object'].team):
			if 'mid' in lane:
				return self.oponentMidStructures
			elif 'top' in lane:
				return self.oponentTopStructures
			elif 'bot' in lane:
				return self.oponentBotStructures
			elif 'base' in lane:
				return self.oponentBaseStructures
		else:
			if 'mid' in lane:
				return self.allyMidStructures
			elif 'top' in lane:
				return self.allyTopStructures
			elif 'bot' in lane:
				return self.allyBotStructures
			elif 'base' in lane:
				return self.allyBaseStructures	
	
	def getOponents(self, player):
		y = []
		if (player.teamObject == self.ally['mid']['object'].teamObject):
			for x in self.oponentTeam:
				y.append(x)
		else:
			for x in self.myTeam:
				y.append(x)
				
		return y
			
	def getAllys(self, player):
		y = []
		if (player.teamObject == self.ally['mid']['object'].teamObject):
			for x in self.myTeam:
				y.append(x)
		else:
			for x in self.oponentTeam:
				y.append(x)
				
		return y
	
	def gameEnded(self):
		x =  self.allyBaseStructures.structures[0].isUp
		y =  self.oponentBaseStructures.structures[0].isUp
		if not x or not y: return True
		else: return False
		
	def early_Game(self, myTeam, oponent, screen):
		texts = []
		buttons = []
		
		buttons.append(Botao([400,300], [300, 80], 'Passivo', 50))
		buttons.append(Botao([400,420], [300, 80], 'Moderado', 50))
		buttons.append(Botao([400,540], [300, 80], 'Agressivo', 50))
		
		text = ['Como deseja que seja a postura do Jungler?']
		aux = TextBox([200, 100], [800, 80], text, 50)
		texts.append(aux)

		text = ['Como deseja que seja a postura do Top Laner?']
		aux = TextBox([200, 100], [800, 80], text, 50)
		texts.append(aux)

		
		text = ['Como deseja que seja a postura do Mid Laner?']
		aux = TextBox([200, 100], [800, 80], text, 50)
		texts.append(aux)

		
		text = ['Como deseja que seja a postura da Bot Lane?']
		aux = TextBox([200, 100], [800, 80], text, 50)
		texts.append(aux)
		
		
		
		cont = 0
		
		for i in texts:
		
			end = False
			
			while not end:
				
				screen.blit(self.background, [0,0])
				
				for event in pygame.event.get():
					
					if event.type == QUIT:
						exit()
					if event.type == pygame.MOUSEBUTTONUP:
						pos = pygame.mouse.get_pos()
						# get a list of all sprites that are under the mouse cursor
						if buttons[0].rect.collidepoint(pos):
							end = True
							x = 1
						if buttons[1].rect.collidepoint(pos):
	
							end = True
							x = 2
						if buttons[2].rect.collidepoint(pos):
							end = True
							x = 2
					
				i.show(screen)
				for j in buttons:
					j.show(screen)
				
				pygame.display.update()
			
				time_passed = clock.tick(60) 
	
			if cont == 0: self.ally['jungler']['object'].setEarlyAttitude(x)
			if cont == 1: self.ally['top']['object'].setEarlyAttitude(x)
			if cont == 2: self.ally['mid']['object'].setEarlyAttitude(x)
			if cont == 3: 
				self.ally['adc']['object'].setEarlyAttitude(x)
				self.ally['support']['object'].setEarlyAttitude(x)
			
			
			
			cont +=1
			
		x = random.randint(1, 3)
		self.oponent['jungler']['object'].setEarlyAttitude(3)
		
		x = random.randint(1, 3)
		self.oponent['top']['object'].setEarlyAttitude(x)
		
		x = random.randint(1, 3)
		
		self.oponent['mid']['object'].setEarlyAttitude(x)
		
		x = random.randint(1, 3)
		self.oponent['adc']['object'].setEarlyAttitude(x)
		self.oponent['support']['object'].setEarlyAttitude(x)
		
		i=0
		
		end = False
		
		while (not end) and self.gameTime <= 60:
			
			if(i%100==0 or  i == 0):
				
				print(str(self.gameTime)+ '\'')
				
				
				#Primeiramente os jungler jogam
				x = random.randint(0, 1)
				
				if(x == 0 and not end) : 
					self.ally['jungler']['object'].play(0,True, self) 
					if not self.gameEnded():	self.oponent['jungler']['object'].play(0,False, self)
				else: 
					self.oponent['jungler']['object'].play(0,False, self)
					if not self.gameEnded(): self.ally['jungler']['object'].play(0,True, self) 
					
				if self.gameEnded(): end = True
	
				#Depois, os mid
				x = random.randint(0, 1)
				if(x == 0 and not end) : 
					self.ally['mid']['object'].play(0,True, self) 
					if not self.gameEnded(): self.oponent['mid']['object'].play(0,False, self)
				else: 
					self.oponent['mid']['object'].play(0,False, self)
					if not self.gameEnded(): self.ally['mid']['object'].play(0,True, self) 
				
				if self.gameEnded(): end = True
				
				#Depois, os top
				x = random.randint(0, 1)
				if(x == 0 and not end) : 
					self.ally['top']['object'].play(0,True, self) 
					if not self.gameEnded(): self.oponent['top']['object'].play(0,False, self)
				else: 
					self.oponent['top']['object'].play(0,False, self)
					if not self.gameEnded(): self.ally['top']['object'].play(0,True, self) 
				
				if self.gameEnded(): end = True	
					
				#Por último, a bot lane (adc)
				x = random.randint(0, 1)
				if(x == 0 and not end) : 
					self.ally['adc']['object'].play(0,True, self) 
					if not self.gameEnded(): self.oponent['adc']['object'].play(0,False, self)
				else: 
					self.oponent['adc']['object'].play(0,False, self)
					if not self.gameEnded(): self.ally['adc']['object'].play(0,True, self) 
				
				if self.gameEnded(): end = True		
					
				#Supps
				x = random.randint(0, 1)
				if(x == 0) : 
					self.ally['support']['object'].play(0,True, self) 
					if not self.gameEnded(): self.oponent['support']['object'].play(0,False, self)
				else: 
					self.oponent['support']['object'].play(0,False, self)
					if not self.gameEnded(): self.ally['support']['object'].play(0,True, self) 	
				
				if self.gameEnded(): end = True	
				
				if not self.allyMidStructures.structures[0].isUp: self.allyMidStructures.structures[0].att(self.allyMidStructures)
				if not self.allyTopStructures.structures[0].isUp: self.allyTopStructures.structures[0].att(self.allyTopStructures)
				if not self.allyBotStructures.structures[0].isUp: self.allyBotStructures.structures[0].att(self.allyBotStructures)
				
				if not self.oponentMidStructures.structures[0].isUp: self.oponentMidStructures.structures[0].att(self.oponentMidStructures)
				if not self.oponentTopStructures.structures[0].isUp: self.oponentTopStructures.structures[0].att(self.oponentTopStructures)
				if not self.oponentBotStructures.structures[0].isUp: self.oponentBotStructures.structures[0].att(self.oponentBotStructures)	
					
				self.dragon.att(self.gameTime)
				self.herald.att(self.gameTime)
				self.baron.att(self.gameTime)
				
				for x in self.allLaneStructures:
					x.att(self.gameTime)
					
				self.gameTime +=1
				
				print('')
				
			if(i%1000*int(self.gameTime/10)==0):
				#ressuscita e 
				for player in self.myTeam:
					
					if player.dead:
						player.dead = False
				
				for player in self.oponentTeam:
					
					if player.dead:
						player.dead = False
							
		
			i+=1

			clock.tick(1000)
			
		print(myTeam[0].teamObject.name)
		for player in myTeam:
			print(player.nickname+' '+player.get_Score() + ' ' + str(player.farm) + ' CS')

		print('')
		
		print(oponent[0].teamObject.name)
		for player in oponent:
			print(player.nickname+' '+player.get_Score() + ' ' + str(player.farm) + ' CS')
		
		valMvp = 0
		mvp = ''
		
		for player in self.myTeam:
			if player.mvp > valMvp:
				valMvp = player.mvp
				mvp = player.nickname
			
		for player in self.oponentTeam:
			if player.mvp > valMvp:
				valMvp = player.mvp
				mvp = player.nickname
				
		print(mvp+' foi o MVP!!')
			

	
			
		
		
