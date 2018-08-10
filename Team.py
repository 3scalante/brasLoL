import pygame, random
from match import *


def toList(texto):
		
		line_Brake = '\n'
		
		for i in range(len(texto)):
			x = texto[i].split('\n')
			texto[i] = x[0]
				
		return texto

class Team():

	def __init__(self, archive):
		arq = open(archive, 'r')
		texto = arq.readlines()
		caracteristicas = toList(texto)
		arq.close()
		self.code = 0
		self.name = ''
		
		#características
		
		for x in caracteristicas:
			
			if("self.logo" in x):
				
				v = x.split('= ')
				logo = v[1]
				self.image = pygame.image.load(logo)
				
			if("self.code" in x):
				
				v = x.split('= ')
				self.code = int(v[1])
				
			if("self.name" in x):
				
				v = x.split('= ')
				self.name = v[1]
		
			if("self.coach" in x):
				
				v = x.split('= ')
				self.coach = v[1]
				
			if("self.entaglement" in x):
				
				v = x.split('= ')
				self.entaglement = int(v[1])
			
			if("self.income" in x):
				
				v = x.split('= ')
				self.income = int(v[1])
		
			if("self.cash" in x):
				
				v = x.split('= ')
				self.cash = int(v[1])
		
		#forças gerais
		self.strength_Total = 0
		self.strength_Early_Game = 0
		self.strength_Mid_Game = 0
		self.strength_Late_Game = 0
		#forças em jogadas
		self.strength_Siege = 0
		self.strength_Gank = 0
		self.strength_Dragons = 0
		self.strength_Baron = 0
		self.strength_inLane = 0
		self.strength_Attack = 0
		self.strength_Defense = 0
		
		self.players = []
		
		
	def showName(self):
		print (self.name)
		
	def showLogo(self,screen, x, y):
		logo_image = pygame.image.load(self.logo).convert_alpha()
		screen.blit(logo_image, [x, y])
		
	def addPlayer(self, object):
		object.teamObject = self
		self.players.append(object)
		
	def listPlayers(self):
		for x in self.players:
			print (x.fullName)
		
class Person ():
	def __init__(self):
		self.code = 0
		self.name = ""
		self.image = ""
		self.last_Name = ''
		self.age = ''
		self.team = ''
		
class Player (Person):

	def __init__(self):
		
		Person.__init__(self)	
		self.teamObject = object
		self.code = 0
		self.nickname = ""
		self.function = ""
		self.mechanics = 0
		self.game_Vision = 0
		self.team_Play = 0
		self.aggressivity = 0
		self.passivity = 0
		self.especiatility = 0
		self.motivation = 0
		
		self.dead = False
		self.kills = 0
		self.deaths = 0
		self.assists = 0
		self.farm = 0
		self.strength_inGame = 0
		self.mvp = 0
		self.advantage = 0
		self.respawnTime = 0
		
		self.attitude = 0
		self.protectBonus = 0
		self.roamBonus = 0
		self.aggressivityBonus = 0
		self.earlyStrength = 0
		
	def get_Score(self):
		
		return(str(self.kills) + '/' + str(self.deaths) + '/' + str(self.assists))
			
			
def fight(ally, oponent):
	i=0
	allyTeamPlay = 0
	oponentTeamPlay = 0
	for player in ally:
		allyTeamPlay += player.team_Play
		i+=1
		
	if(i>0):
		allyTeamPlay /= i
	
	i = 0
	
	for player in oponent:
		oponentTeamPlay += player.team_Play
		i+=1
		
	if(i>0):
		oponentTeamPlay /= i

		
	if(len(ally)==1):
		
		for player in ally:
			if not player.dead:
				if player.advantage > 0: x =  random.randint(int((player.strength+player.advantage)/player.advantage/100+1), 100 + player.advantage)
				else: x =  random.randint(int((player.strength+player.advantage)/100), 100)
				
				for player2 in oponent:
					if player2.advantage > 0: y =  random.randint(int(player2.strength+player2.advantage/player2.advantage/100), 100 + player2.advantage)
					else: y =  random.randint(int((player2.strength+player2.advantage)/100), 100)
					if(x + player.aggressivityBonus > y+player2.protectBonus and not player2.dead):
						
						player2.dead = True
						player2.deaths += 1
						player2.mvp -= 15
						player2.advantage -=8
						
						player.kills +=1
						player.mvp+=10
						player.advantage +=10
						
						print(player.nickname+' matou '+player2.nickname+'!')
					elif(x + player.aggressivityBonus < y+player2.protectBonus and  not player.dead and not player2.dead ):
						
						player.dead = True
						player.deaths += 1
						player.mvp -= 15
						player.advantage -=8
						
						player2.advantage += 10
						player2.kills +=1
						player2.mvp+=10
						
						print(player2.nickname+' matou '+player.nickname+'!')
	else:
		assistentes = ''
		for player in ally:
			if not player.dead:
				if player.advantage > 0: x =  random.randint(int((player.strength+oponentTeamPlay+player.advantage)/player.advantage/100+1), 100 + player.advantage)
				else: x =  random.randint(int((player.strength+oponentTeamPlay+player.advantage)/100), 100)
				for player2 in oponent:
					if player2.advantage > 0: y =  random.randint(int((player2.strength+oponentTeamPlay+player2.advantage)/player2.advantage/100+1), 100 + player2.advantage)
					else: y =  random.randint(int((player2.strength+oponentTeamPlay+player2.advantage)/100), 100)
					if(x + player.aggressivityBonus > y+player2.protectBonus and not player2.dead):
						
						player2.dead = True
						player2.deaths += 1
						player2.mvp -= 15
						player2.advantage -=8
						
						player.kills +=1
						player.mvp+=10
						player.advantage +=10
						
						#assistencias
						for assist in ally:
							if(assist != player):
								assist.assists+=1
								assist.mvp +=5
								assistentes += assist.nickname + ' '
						
						print(player.nickname+' matou '+player2.nickname+'! Assist: '+assistentes)
					elif(x + player.aggressivityBonus < y+player2.protectBonus and not player.dead  and not player2.dead ):
						
						player.dead = True
						player.deaths += 1
						player.mvp -= 15
						player.advantage -=8
						
						player2.advantage += 10
						player2.kills +=1
						player2.mvp+=10
						
						#assistencias
						if(len(oponent)>1):
							for assist in oponent:
								if(assist != player2):
									assist.assists+=1
									assist.mvp += 5
									assist.advantage += 5
									assistentes += assist.nickname + ' '
							
							print(player2.nickname+' matou '+player.nickname+'! Assist: '+assistentes)
						else:
							print(player2.nickname+' matou '+player.nickname+'! ')
					assistentes = ''
	
def teamFight(allAllys, allOponents):
	
	allys = []
	
	for i in allAllys:
		x = random.randint(0,200)
		if (x<i.game_Vision+i.advantage):
			if not i.dead:
				allys.append(i)
	
	oponents = []
	
	for i in allOponents:
		x = random.randint(0,200)
		if (x<i.game_Vision+i.advantage):
			if not i.dead:
				oponents.append(i)
	
			
	if len(oponents)>0 and len(allys) > 0:			
		fight(allys, oponents)	
			
def smite(ally, oponent):
	if(random.randint(0, ally) > random.randint(0, oponent)):
		return True
	else:
		return False
						
def tryMonster(player, match, monster):
	totalAllyAdvantage = 0
	totalOponentAdvantage = 0
	
	#tenta chamar aliados para fazer o drag e verifica quem está vivo
	allyJunglerSmite = 30 #smite começa como 30, para caso o jungler n venha ajudar
	allAllys = match.getAllys(player)
	allys = []
	allys.append(player)
	
	for i in allAllys:
		x = random.randint(0,200)
		if (x<i.game_Vision+i.advantage):
			if not i.dead and i!=player:
				allys.append(i)
				totalAllyAdvantage += i.advantage
			if i.function in 'jungle':
				allyJunglerSmite = i.smite	
				

	#carrega os inimigos
	allOponents = match.getOponents(player)
	oponents = []
	#chama top ou mid para contestar
	oponentJunglerSmite = 20 #smite começa como 20, para caso o jungler n venha contestar
	for i in allOponents:
		x = random.randint(0,200)
		if (x<i.game_Vision+i.advantage):
			if not i.dead:
				oponents.append(i)
				totalOponentAdvantage += i.advantage
			if i.function in 'jungle':
				oponentJunglerSmite = i.smite
	#verifica se tem vantagem para fazer monster
	if(totalAllyAdvantage > totalOponentAdvantage + 10 or len(oponents) == 0):
		
		monster.slay(match.gameTime)
		
		winner = allys
		looser = oponents
		
		print(allys[0].teamObject.name+ ' matou o ' + monster.name + '!') 
		
	elif(totalAllyAdvantage < totalOponentAdvantage + 10):
	
		monster.slay(match.gameTime)
		
		winner = oponents
		looser = allys
		
		print(oponents[0].teamObject.name+ ' roubou o ' + monster.name + '!') 
		
	else:
		decision = smite(allyJunglerSmite, oponentJunglerSmite)
		if decision:
			
			monster.slay(match.gameTime)
			winner = allys
			looser = oponents
			
			print(allys[0].teamObject.name+ ' matou o ' + monster.name + '!') 
			
		else:
			
			monster.slay(match.gameTime)
			winner = oponents
			looser = allys

			print(oponents[0].teamObject.name+ ' roubou o ' + monster.name + '!') 
		
	for i in winner:
		i.advantage += monster.bonus

	for i in looser :
		i.advantage -= monster.bonus + 5
		
def choosePlay(n):
	
	x= random.randint(0,100)
	
	if n == 1:
		if(x<=80):
			play = 1
		elif(x > 80 and x <= 90):
			play = 2
		else:
			play = 3
	
	if n == 2:
		if(x<=80):
			play = 2
		elif(x > 80 and x <= 90):
			play = 1
		else:
			play = 3
	
	if n == 3:
		if(x<=80):
			play = 3
		elif(x > 80 and x <= 90):
			play = 1
		else:
			play = 2	
			
	return play
					
def teamPlay(player, advantage, match, laneStructures):
	
	x = (random.randint(1, 3))
	
	if x == 3: laneStructures = match.getOponentStructures(player, 'top')
	
	if x == 2: laneStructures = match.getOponentStructures(player, 'mid')
	
	if x == 1: laneStructures = match.getOponentStructures(player, 'bot')
			
	if not player.dead:
				

		if(random.randint(0, 10000)<200): teamFight(match.getAllys(player), match.getOponents(player))
		
		if not laneStructures.down:
			
			if not player.dead: laneStructures.push(match.getAllys(player), match.getAllyStructures(player, laneStructures.lane))
			
		else:

			if not player.dead: match.getOponentStructures(player, 'base').push(match.getAllys(player))
	
	if(random.randint(0, 100) < player.game_Vision):
		
		if not player.dead:
		
			x = random.randint(0, 1000 + 1000 - advantage)
				
			if(x<player.game_Vision+player.advantage and not player.dead and match.herald.isAlive):
				tryMonster(player, match, match.herald)
			elif(x<player.game_Vision+player.advantage and not player.dead and match.baron.isAlive):
				tryMonster(player, match, match.baron)
			elif(x<player.game_Vision+player.advantage and not player.dead and match.dragon.isAlive):
				tryMonster(player, match, match.dragon)

					
class Mid_Laner(Player):
	
	def __init__(self, archive):
		Player.__init__(self)
		self.roaming = 0
		self.farming = 0
		arq = open(archive, 'r')
		texto = arq.readlines()
		
		caracteristicas = toList(texto)
		
		arq.close()
		
		
		
		for x in range(len(caracteristicas)):
			
			if("self.image" in caracteristicas[x]):
				
				v = caracteristicas[x].split('= ')
				image = v[1]
				self.image = pygame.image.load(image)
			
			if("self.code" in caracteristicas[x]):
				
				v = caracteristicas[x].split('= ')
				self.code = v[1]
			
			if("self.function" in caracteristicas[x]):
				
				v = caracteristicas[x].split('= ')
				self.function = v[1]
				
			if("self.name" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.name = v[1]
			
			if("self.nickname" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.nickname = v[1]
				
			if("self.last_Name" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.last_Name = v[1]
				
			if("self.team = " in caracteristicas[x]):
				
				v = caracteristicas[x].split('= ')
				self.team = int(v[1])
			
			if("self.especiatility" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.especiatility = v[1]	
				
			if("self.mechanics" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.mechanics = int(v[1])	
				
			if("self.game_Vision" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.game_Vision = int(v[1])	
				
			if("self.team_Play" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.team_Play = int(v[1])		
				
			if("self.aggressivity" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.aggressivity = int(v[1])		
				
			if("self.passivity" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.passivity = int(v[1])		
				
			if("self.roaming" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.roaming = int(v[1])		
				
			if("self.farming" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.farming = int(v[1])		
				
			if("self.motivation" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.motivation = int(v[1])		
		
		
		self.strength = (self.aggressivity + self.mechanics + self.game_Vision)/3
		self.fullName = self.name + ' \"' + self.nickname + '\" ' + self.last_Name  
		
	def play(self, game_phase, isAlly, match):
			
		
		#verifica se é do time do usuário	
		if isAlly:
			self.ally = match.ally
			self.oponent = match.oponent
		else:
			self.ally = match.oponent
			self.oponent = match.ally

			
		game_phase = 0		
		
		laneStructures = match.getOponentStructures(self, 'mid')
		baseStructures = match.getOponentStructures(self, 'base')
		
		x = random.randint(0, 100)
		
		play = choosePlay(self.attitude)
		
		allys = []
		
		allys.append(self)
			
		if self.advantage > 1000:
			advantage = 1000 - self.oponent['mid']['object'].advantage
		else:
			advantage = self.advantage - self.oponent['mid']['object'].advantage
		
		if(random.randint(0, 1000) > match.gameTime*10+200 and not laneStructures.down):	
		
			if play == 1:#passivo
				
				
				x = random.randint(0, 1000 + 1000 - advantage)
				self.farm+= int(self.farming/10)+1
				self.mvp += 1
				self.advantage += int(self.farm/10)
					
				#se obter sucesso, ganha farm e força
				if(x<self.earlyStrength):
					fight( [self],[self.oponent['mid']['object']] )
					self.farm -= 2	
				
				if(x<(self.earlyStrength + self.roamBonus )):
					self.farm-=2
					x = random.randint(1, 2)
					
					if (x==1):
						fight([self.ally['top']['object'], self],[self.oponent['top']['object']] )
						laneStructures = match.getOponentStructures(self, 'top')
						allys.append(self.ally['top']['object'])
						
						
					elif (x==2):
						fight([self.ally['adc']['object'],self.ally['support']['object'], self],[self.oponent['adc']['object'], self.oponent['support']['object']] )
						laneStructures = match.getOponentStructures(self, 'bot')
						allys.append(self.ally['adc']['object'])
						allys.append(self.ally['support']['object'])
					
			elif play == 2:

				x = random.randint(0, 1000 + 1000 - advantage)
				self.farm+= int(self.farming/10)
				self.advantage += int(self.farm/10)
				self.mvp += 1
					
				#se obter sucesso, ganha farm e força e tenta dar roaming
					
				x = random.randint(0, 1000 + 1000 - advantage)
				if(x<(self.earlyStrength + self.roamBonus + self.advantage)/12):
					self.farm-=2
					x = random.randint(1, 2)
					
					if (x==1):
						fight([self.ally['top']['object'], self],[self.oponent['top']['object']] )
						laneStructures = match.getOponentStructures(self, 'top')
						allys.append(self.ally['top']['object'])
						
						
					elif (x==2):
						fight([self.ally['adc']['object'],self.ally['support']['object'], self],[self.oponent['adc']['object'], self.oponent['support']['object']] )
						laneStructures = match.getOponentStructures(self, 'bot')
						allys.append(self.ally['adc']['object'])
						allys.append(self.ally['support']['object'])
					
					
			elif play == 3:
				
				x = random.randint(0, 1000 + 1000 - advantage)
				self.farm+= int(self.farming/10)
				self.advantage += int(self.farm/10)
				#se obter sucesso, ganha farm e força e tenta solar
				
				if(x<self.earlyStrength):
					fight( [self],[self.oponent['mid']['object']] )
					self.farm -= 1
					
				if(x<(self.earlyStrength + self.roamBonus )/2):
					self.farm -=2
					x = random.randint(1, 2)
				
					if (x==1):
						fight([self.ally['top']['object'], self],[self.oponent['top']['object']] )
						laneStructures = match.getOponentStructures(self, 'top')
						allys.append(self.ally['top']['object'])
						
					elif (x==2):
						fight([self.ally['adc']['object'],self.ally['support']['object'], self],[self.oponent['adc']['object'], self.oponent['support']['object']] )
						laneStructures = match.getOponentStructures(self, 'bot')
						allys.append(self.ally['adc']['object'])
						allys.append(self.ally['support']['object'])
						
			if not self.dead and x < self.game_Vision : 
				if not laneStructures.down:
					laneStructures.push(allys, match.getAllyStructures(self, laneStructures.lane))
				else:
					baseStructures.push(allys)
			
		else:
			teamPlay(self, advantage, match, laneStructures)					

	def setEarlyAttitude(self, n):
		if (n==1):
			self.attitude = n
			self.protectBonus = 20
			self.roamBonus = 0
			self.aggressivityBonus = 0
			self.earlyStrength = (self.passivity + self.farming +self.game_Vision)/3
			
		elif (n==2):
			self.attitude = n
			self.protectBonus = 5
			self.roamBonus = 10
			self.aggressivityBonus = 5
			self.earlyStrength = (self.aggressivity + self.roaming + self.farming +  self.team_Play + self.game_Vision)/5
		
		elif (n==3):
			self.attitude = n
			self.protectBonus = 0
			self.roamBonus = 0
			self.aggressivityBonus = 20
			self.earlyStrength = (self.aggressivity + self.mechanics + self.game_Vision)/3
					
						
		
class Top_Laner(Player):
	
	def __init__(self, archive):
		Player.__init__(self)
		
		self.roaming = 0
		self.farming = 0
		
		arq = open(archive, 'r')
		texto = arq.readlines()
		
		caracteristicas = toList(texto)
		
		arq.close()
		
		for x in range(len(caracteristicas)):
			
			if("self.image" in caracteristicas[x]):
				
				v = caracteristicas[x].split('= ')
				image = v[1]
				self.image = pygame.image.load(image)
			
			if("self.code" in caracteristicas[x]):
				
				v = caracteristicas[x].split('= ')
				self.code = v[1]
			
			if("self.function" in caracteristicas[x]):
				
				v = caracteristicas[x].split('= ')
				self.function = v[1]
				
			if("self.name" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.name = v[1]
			
			if("self.nickname" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.nickname = v[1]
				
			if("self.last_Name" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.last_Name = v[1]
				
			if("self.team = " in caracteristicas[x]):
				
				v = caracteristicas[x].split('= ')
				self.team = int(v[1])
			
			if("self.especiatility" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.especiatility = v[1]	
				
			if("self.mechanics" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.mechanics = int(v[1])	
				
			if("self.game_Vision" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.game_Vision = int(v[1])	
				
			if("self.team_Play" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.team_Play = int(v[1])		
				
			if("self.aggressivity" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.aggressivity = int(v[1])		
				
			if("self.passivity" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.passivity = int(v[1])		
				
			if("self.roaming" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.roaming = int(v[1])		
				
			if("self.farming" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.farming = int(v[1])		
				
			if("self.motivation" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.motivation = int(v[1])		
				
		self.strength = (self.aggressivity + self.mechanics + self.game_Vision)/3
		
		self.fullName = self.name + ' \"' + self.nickname + '\" ' + self.last_Name  
		
	def play(self, game_phase, isAlly, match):
				
		#verifica se é do time do usuário	
		if isAlly:
			self.ally = match.ally
			self.oponent = match.oponent
		else:
			self.ally = match.oponent
			self.oponent = match.ally

			
		play = choosePlay(self.attitude)
		
		laneStructures = match.getOponentStructures(self, 'top')
		baseStructures = match.getOponentStructures(self, 'base')
		
		allys = []
		
		if self.advantage > 1000:
			advantage = 1000 - self.oponent['top']['object'].advantage
		else:
			advantage = self.advantage - self.oponent['top']['object'].advantage
		
		if(random.randint(0, 1000) > match.gameTime*10+200 and not laneStructures.down):
			
			if play == 1:#passivo
				
				
				x = random.randint(0, 1000 + 1000 - advantage)
				self.farm+= int(self.farming/10)+1
				self.mvp += 1
				self.advantage += int(self.farm/10)
					
				#se obter sucesso, ganha farm e força
				if(x<(self.earlyStrength)/2):
					fight( [self],[self.oponent['top']['object']] )
					self.farm -= 2	
				
				if(x<(self.earlyStrength + self.roamBonus)/2):
					self.farm-=2
					x = random.randint(1, 2)
					
					if (x==1):
						fight([self.ally['mid']['object'], self],[self.oponent['mid']['object']] )
						laneStructures = match.getOponentStructures(self, 'mid')
						allys.append(self.ally['mid']['object'])
						
					elif (x==2):
						fight([self.ally['adc']['object'],self.ally['support']['object'], self],[self.oponent['adc']['object'], self.oponent['support']['object']] )
						laneStructures = match.getOponentStructures(self, 'bot')
						allys.append(self.ally['adc']['object'])
						allys.append(self.ally['support']['object'])
						
			elif play == 2:
				
				x = random.randint(0, 1000 + 1000 - advantage)
				self.farm+= int(self.farming/10)
				self.mvp += 1
				self.advantage += int(self.farm/10)
				#se obter sucesso, ganha farm e força e tenta dar roaming
				if(x<(self.earlyStrength + self.roamBonus)/2):
					self.farm-=2
					x = random.randint(1, 2)
					
					if (x==1):
						fight([self.ally['mid']['object'], self],[self.oponent['mid']['object']] )
						laneStructures = match.getOponentStructures(self, 'mid')
					elif (x==2):
						fight([self.ally['adc']['object'],self.ally['support']['object'], self],[self.oponent['adc']['object'], self.oponent['support']['object']] )
						laneStructures = match.getOponentStructures(self, 'bot')
						allys.append(self.ally['adc']['object'])
						allys.append(self.ally['support']['object'])
						
			elif play == 3:
				
				x = random.randint(0, 1000 + 1000 - advantage)
				self.farm+= int(self.farming/10)
				self.mvp += 1
				self.advantage += int(self.farm/10)
				#se obter sucesso, ganha farm e força e tenta solar
				
				if(x<self.earlyStrength):
					fight( [self],[self.oponent['top']['object']] )
					self.farm -= 2	
					
				if(x<(self.earlyStrength + self.roamBonus)/2):
					x = random.randint(1, 2)
					
					if (x==1):
						fight([self.ally['mid']['object'], self],[self.oponent['mid']['object']] )
						laneStructures = match.getOponentStructures(self, 'mid')
						allys.append(self.ally['mid']['object'])
						
					elif (x==2):
						fight([self.ally['adc']['object'],self.ally['support']['object'], self],[self.oponent['adc']['object'], self.oponent['support']['object']] )
						laneStructures = match.getOponentStructures(self, 'bot')
						allys.append(self.ally['adc']['object'])
						allys.append(self.ally['support']['object'])
						
			if not self.dead and x < self.game_Vision: 
				if not laneStructures.down:
					laneStructures.push(allys, match.getAllyStructures(self, laneStructures.lane))
				else:
					baseStructures.push(allys)
		else:
			teamPlay(self, advantage, match, laneStructures)

	def setEarlyAttitude(self, n):
		if (n==1):
			self.attitude = n
			self.protectBonus = 20
			self.roamBonus = 0
			self.aggressivityBonus = 0
			self.earlyStrength = (self.passivity + self.farming +self.game_Vision)/3
			
		elif (n==2):
			self.attitude = n
			self.protectBonus = 5
			self.roamBonus = 10
			self.aggressivityBonus = 5
			self.earlyStrength = (self.aggressivity + self.roaming + self.farming +  self.team_Play + self.game_Vision)/5
		
		elif (n==3):
			self.attitude = n
			self.protectBonus = 0
			self.roamBonus = 0
			self.aggressivityBonus = 20
			self.earlyStrength = (self.aggressivity + self.mechanics + self.game_Vision)/3
					
					
		
class Jungler(Player):
	def __init__(self, archive):
		Player.__init__(self)
		self.gank_effectivity = 0
		self.smite = 0
		self.farming = 0
		
		arq = open(archive, 'r')
		texto = arq.readlines()
		
		caracteristicas = toList(texto)
		
		arq.close()
		
		for x in range(len(caracteristicas)):
			
			if("self.image" in caracteristicas[x]):
				
				v = caracteristicas[x].split('= ')
				image = v[1]
				self.image = pygame.image.load(image)
			
			if("self.code" in caracteristicas[x]):
				
				v = caracteristicas[x].split('= ')
				self.code = v[1]
			
			if("self.function" in caracteristicas[x]):
				
				v = caracteristicas[x].split('= ')
				self.function = v[1]
				
			if("self.name" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.name = v[1]
			
			if("self.nickname" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.nickname = v[1]
				
			if("self.last_Name" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.last_Name = v[1]
				
			if("self.team = " in caracteristicas[x]):
				
				v = caracteristicas[x].split('= ')
				self.team = int(v[1])
			
			if("self.especiatility" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.especiatility = v[1]	
				
			if("self.mechanics" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.mechanics = int(v[1])	
				
			if("self.game_Vision" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.game_Vision = int(v[1])	
				
			if("self.team_Play" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.team_Play = int(v[1])		
				
			if("self.aggressivity" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.aggressivity = int(v[1])		
				
			if("self.passivity" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.passivity = int(v[1])		
				
			if("self.gank_effectivity" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.gank_effectivity = int(v[1])	
				
			if("self.smite" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.smite = int(v[1])	
				
			if("self.farming" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.farming = int(v[1])		
				
			if("self.motivation" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.motivation = int(v[1])		
		
		self.strength = (self.aggressivity + self.mechanics + self.game_Vision)/3
		self.fullName = self.name + ' \"' + self.nickname + '\" ' + self.last_Name  
		
	def play(self, game_phase, isAlly, match):
		
		
		#verifica se é do time do usuário	
		if isAlly:
			self.ally = match.ally
			self.oponent = match.oponent
		else:
			self.ally = match.oponent
			self.oponent = match.ally

		play = choosePlay(self.attitude)
		
		laneStructures = object
		baseStructures = match.getOponentStructures(self, 'base')
		
		allys = []
		
		if self.advantage > 500:
			advantage = 500 - self.oponent['jungler']['object'].advantage
		else:
			advantage = self.advantage - self.oponent['jungler']['object'].advantage
			
		if(random.randint(0, 1000) > match.gameTime*10+200 ):
			if play == 1:#passivo

				x = random.randint(0, 1000 + 1000 - advantage)
				
				#se obter sucesso, ganha farm e força
				
				self.farm+= int(self.farming/15)
				self.mvp += 3
				self.advantage += int(self.farm)
					
				if(x<(self.earlyStrength+self.roamBonus)):
					
					x = random.randint(1, 3)
		
					if (x==1):
						
						fight([self.ally['top']['object'], self],[self.oponent['top']['object']] )
						laneStructures = match.getOponentStructures(self, 'top')
						allys.append(self.ally['top']['object'])
						
						
					elif (x==2):
						
						fight([self.ally['adc']['object'],self.ally['support']['object'], self],[self.oponent['adc']['object'], self.oponent['support']['object']] )
						laneStructures = match.getOponentStructures(self, 'bot')
						allys.append(self.ally['adc']['object'])
						allys.append(self.ally['support']['object'])	
							
					elif (x==3):
						fight([self.ally['mid']['object'], self],[self.oponent['mid']['object']] )
						laneStructures = match.getOponentStructures(self, 'mid')
						allys.append(self.ally['mid']['object'])
						
					x = random.randint(0, 1000 + 1000 - advantage)
					
					
					if(x<self.game_Vision+self.advantage and not self.dead and match.herald.isAlive):
						tryMonster(self, match, match.herald)
					elif(x<self.game_Vision+self.advantage and not self.dead and match.dragon.isAlive):
						tryMonster(self, match, match.dragon)
					
			elif play == 2:
				
				self.farm+= int(self.farming/18)
				self.advantage += int(self.farm)
				self.mvp += 2
				
				#se obter sucesso, ganha farm, força e tenta gankar
					
				x = random.randint(0, 1000 + 1000 - advantage)
				if(x<(self.earlyStrength+self.roamBonus)):
					
					x = random.randint(1, 3)
					
					if (x==1):
						fight([self.ally['top']['object'], self],[self.oponent['top']['object']] )
						laneStructures = match.getOponentStructures(self, 'top')
						allys.append(self.ally['top']['object'])
							
					elif (x==2):
						fight([self.ally['adc']['object'],self.ally['support']['object'], self],[self.oponent['adc']['object'], self.oponent['support']['object']] )
						laneStructures = match.getOponentStructures(self, 'bot')
						allys.append(self.ally['adc']['object'])
						allys.append(self.ally['support']['object'])
						
					elif (x==3):
						fight([self.ally['mid']['object'], self],[self.oponent['mid']['object']])
						laneStructures = match.getOponentStructures(self, 'mid')
						allys.append(self.ally['mid']['object'])
						
					x = random.randint(0, 1000 + 1000 - advantage)
					
					if(x<self.game_Vision+self.advantage and not self.dead and match.herald.isAlive):
						tryMonster(self, match, match.herald)
					elif(x<self.game_Vision+self.advantage and not self.dead and match.dragon.isAlive):
						tryMonster(self, match, match.dragon)
					
					
			elif play == 3:
				
				x = random.randint(0, 1000 + 1000 - advantage)
					
				self.farm+= int(self.farming/20)
				self.advantage += int(self.farm)
				self.mvp += 2
					
				#se obter sucesso, ganha farm e força e tenta dar roaming
				if(x<(self.earlyStrength+self.roamBonus)):
					
					x = random.randint(1, 3)

					if (x==1):
						
						fight([self.ally['top']['object'], self],[self.oponent['top']['object']] )
						laneStructures = match.getOponentStructures(self, 'top')
						allys.append(self.ally['top']['object'])
						
					elif (x==2):
						fight([self.ally['adc']['object'],self.ally['support']['object'], self],[self.oponent['adc']['object'], self.oponent['support']['object']] )
						laneStructures = match.getOponentStructures(self, 'bot')						
						allys.append(self.ally['adc']['object'])
						allys.append(self.ally['support']['object'])
						
					elif (x==3):
						fight([self.ally['mid']['object'], self],[self.oponent['mid']['object']])	
						laneStructures = match.getOponentStructures(self, 'mid')
						allys.append(self.ally['mid']['object'])
						
			if not self.dead and x < self.game_Vision and isinstance(laneStructures, LaneStructures): 
				if not laneStructures.down:
					laneStructures.push(allys, match.getAllyStructures(self, laneStructures.lane))
				else:
					baseStructures.push(allys)
		elif isinstance(laneStructures, LaneStructures):
			teamPlay(self, advantage, match, laneStructures)
					 
				
	def setEarlyAttitude(self, n):
		if (n==1):
			self.attitude = n
			self.protectBonus = 20
			self.roamBonus = 0
			self.aggressivityBonus = 0
			self.earlyStrength = (self.passivity + self.farming + self.gank_effectivity)/3
			
		elif (n==2):
			self.attitude = n
			self.protectBonus = 5
			self.roamBonus = 10
			self.aggressivityBonus = 5
			self.earlyStrength = (self.passivity + self.gank_effectivity + self.game_Vision +  self.team_Play + self.aggressivity)/5
		
		elif (n==3):
			self.attitude = n
			self.protectBonus = 0
			self.roamBonus = 5
			self.aggressivityBonus = 15
			self.earlyStrength = (self.aggressivity + self.mechanics + self.gank_effectivity + self.game_Vision)/4	
		
class Support(Player):
	def __init__(self, archive):
		Player.__init__(self)
		
		self.protect = 0
		self.warding = 0
		self.gank_effectivity = 0
		
		arq = open(archive, 'r')
		texto = arq.readlines()
		
		caracteristicas = toList(texto)
		
		arq.close()
		
		for x in range(len(caracteristicas)):
			
			if("self.image" in caracteristicas[x]):
				
				v = caracteristicas[x].split('= ')
				image = v[1]
				self.image = pygame.image.load(image)
			
			if("self.code" in caracteristicas[x]):
				
				v = caracteristicas[x].split('= ')
				self.code = v[1]
			
			if("self.function" in caracteristicas[x]):
				
				v = caracteristicas[x].split('= ')
				self.function = v[1]
				
			if("self.name" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.name = v[1]
			
			if("self.nickname" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.nickname = v[1]
				
			if("self.last_Name" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.last_Name = v[1]
				
			if("self.team = " in caracteristicas[x]):
				
				v = caracteristicas[x].split('= ')
				self.team = int(v[1])
			
			if("self.especiatility" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.especiatility = v[1]	
				
			if("self.mechanics" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.mechanics = int(v[1])	
				
			if("self.game_Vision" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.game_Vision = int(v[1])	
				
			if("self.team_Play" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.team_Play = int(v[1])		
				
			if("self.aggressivity" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.aggressivity = int(v[1])		
				
			if("self.passivity" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.passivity = int(v[1])		
				
			if("self.gank_effectivity" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.gank_effectivity = int(v[1])		
				
				
			if("self.warding" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.warding = int(v[1])		
				
			if("self.protect" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.protect = int(v[1])		
				
			if("self.motivation" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.mechanis = int(v[1])		
		
		self.strength = (self.aggressivity + self.mechanics + self.game_Vision + self.protect)/4
		self.fullName = self.name + ' \"' + self.nickname + '\" ' + self.last_Name  
		
	def play(self, game_phase, isAlly, match):
		
		#verifica se é do time do usuário	
		if isAlly:
			self.ally = match.ally
			self.oponent = match.oponent
		else:
			self.ally = match.oponent
			self.oponent = match.ally	
		
			
		laneStructures = match.getOponentStructures(self, 'bot')
		baseStructures = match.getOponentStructures(self, 'base')
		
		play = choosePlay(self.attitude)	
		
		allys = []
		
		allys.append(self)
		allys.append(self.ally['adc']['object'])
		
		if self.advantage > 1000:
			advantage = 1000 - self.oponent['support']['object'].advantage
		else:
			advantage = self.advantage - self.oponent['support']['object'].advantage
			
			
		if(random.randint(0, 1000) > match.gameTime*10+200 and not laneStructures.down):	
		
			if play == 1:#passivo
				
				x = random.randint(0, 1000 + 1000 - advantage)
				self.mvp += 3
				self.advantage += 5
				#se obter sucesso, ganha farm e força
				if(x<self.earlyStrength + self.advantage):
					
					self.ally['adc']['object'].advantage += 2 
					
				
			elif play == 2:
				
				x = random.randint(0, 1000 + 1000 - advantage)
				
				self.advantage += 5
				self.mvp += 2
				
				#se obter sucesso, ganha farm, força e tenta gankar

				if(x<(self.earlyStrength + self.roamBonus)/12):
					x = random.randint(1, 2)
						
					if (x==1):
						fight([self.ally['top']['object'], self],[self.oponent['top']['object']] )
						laneStructures = match.getOponentStructures(self, 'top')
						allys.append(self.ally['top']['object'])
						
					elif (x==2):
						fight([self.ally['mid']['object'], self],[self.oponent['mid']['object']] )
						laneStructures = match.getOponentStructures(self, 'mid')
						allys.append(self.ally['mid']['object'])

			elif play == 3:
				
				x = random.randint(0, 1000 + 1000 - advantage)
				
				self.advantage += 5
				self.mvp += 2
				
				if(x<self.earlyStrength):
					fight([self.ally['adc']['object'],self.ally['support']['object'], self],[self.oponent['adc']['object'], self.oponent['support']['object']] )
			
			if not self.dead and x < self.game_Vision :
				if not laneStructures.down:
					laneStructures.push(allys, match.getAllyStructures(self, laneStructures.lane))
				else:
					baseStructures.push(allys)
		else:
			teamPlay(self, advantage, match, laneStructures)

				
	def setEarlyAttitude(self, n):
		if (n==1):
			self.attitude = n
			self.protectBonus = 20
			self.roamBonus = 0
			self.aggressivityBonus = 0
			self.earlyStrength = (self.passivity + self.protect + self.warding)/3
		elif (n==2):
			self.attitude = n
			self.protectBonus = 5
			self.roamBonus = 10
			self.aggressivityBonus = 5
			self.earlyStrength = (self.passivity + self.gank_effectivity+ self.protect +  self.team_Play + self.aggressivity)/5
		
		elif (n==3):
			self.attitude = n
			self.protectBonus = 0
			self.roamBonus = 0
			self.aggressivityBonus = 20
			self.earlyStrength = (self.aggressivity + self.mechanics + self.protect)/3		
		
					
class Adc(Player):
	def __init__(self, archive):
		Player.__init__(self)
		self.kiting = 0
		self.poisicion = 0
		self.farming = 0
		
		arq = open(archive, 'r')
		texto = arq.readlines()
		
		caracteristicas = toList(texto)
		
		arq.close()
		
		for x in range(len(caracteristicas)):
			
			if("self.image" in caracteristicas[x]):
				
				v = caracteristicas[x].split('= ')
				image = v[1]
				self.image = pygame.image.load(image)
			
			if("self.code" in caracteristicas[x]):
				
				v = caracteristicas[x].split('= ')
				self.code = v[1]
			
			if("self.function" in caracteristicas[x]):
				
				v = caracteristicas[x].split('= ')
				self.function = v[1]
				
			if("self.name" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.name = v[1]
			
			if("self.nickname" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.nickname = v[1]
				
			if("self.last_Name" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.last_Name = v[1]
				
			if("self.team = " in caracteristicas[x]):
				
				v = caracteristicas[x].split('= ')
				self.team = int(v[1])
			
			if("self.especiatility" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.especiatility = v[1]	
				
			if("self.mechanics" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.mechanics = int(v[1])	
				
			if("self.game_Vision" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.game_Vision = int(v[1])	
				
			if("self.team_Play" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.team_Play = int(v[1])		
				
			if("self.aggressivity" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.aggressivity = int(v[1])		
				
			if("self.passivity" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.passivity = int(v[1])		
				
			if("self.kiting" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.kiting = int(v[1])		
				
			if("self.protect" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.protect = int(v[1])	
				
			if("self.farming" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.farming = int(v[1])		
				
			if("self.motivation" in caracteristicas[x]):
				v = caracteristicas[x].split('= ')
				self.motivation = int(v[1])		
		
		self.strength = (self.aggressivity + self.mechanics + self.game_Vision)/3
		self.fullName = self.name + ' \"' + self.nickname + '\" ' + self.last_Name  
		
	def play(self, game_phase, isAlly, match):
		
		
		#verifica se é do time do usuário	
		if isAlly:
			self.ally = match.ally
			self.oponent = match.oponent
		else:
			self.ally = match.oponent
			self.oponent = match.ally
		
		play = choosePlay(self.attitude)
		
		laneStructures = match.getOponentStructures(self, 'bot')
		baseStructures = match.getOponentStructures(self, 'base')
		
		allys = []
			
		allys.append(self)
		allys.append(self.ally['adc']['object'])
			
		if self.advantage > 1000:
			advantage = 1000 - self.oponent['adc']['object'].advantage
		else:
			advantage =  self.advantage - self.oponent['adc']['object'].advantage
		
		if(random.randint(0, 1000) > match.gameTime*10+200 and not laneStructures.down):			
			
			if play == 1:#passivo
				
				x = random.randint(0, 1000 + 1000 - advantage)
				
				self.farm += int(self.farming/10)+1
				self.mvp += 3
				self.advantage += int(self.farm/10)
				self.ally['support']['object'].advantage += 2
				
				#tenta lutar
				if(x<(self.earlyStrength+self.advantage)/32):
					fight([self.ally['adc']['object'],self.ally['support']['object'], self],[self.oponent['adc']['object'], self.oponent['support']['object']] )
					
					x = random.randint(0, 1000 + 1000 - advantage)
					
					if(x<self.game_Vision+self.advantage and not self.dead and match.dragon.isAlive):
						tryMonster(self, match, match.dragon)
				
				if(x<(self.earlyStrength + self.roamBonus)):
					x = random.randint(1, 2)
						
					if (x==1):
						fight([self.ally['top']['object'], self],[self.oponent['top']['object']] )
						laneStructures = match.getOponentStructures(self, 'top')
						allys.append(self.ally['top']['object'])
						
					elif (x==2):
						fight([self.ally['mid']['object'], self],[self.oponent['mid']['object']] )
						laneStructures = match.getOponentStructures(self, 'mid')
						allys.append(self.ally['mid']['object'])
						
					x = random.randint(0, 1000 + 1000 - advantage)
					
				
			elif play == 2:
			
				x = random.randint(0, 1000 + 1000 - advantage)
								
				self.farm += int(self.farming/10)
				self.mvp += 2
				self.advantage += int(self.farm/10)
				self.ally['support']['object'].advantage += 1
				
				#tenta lutar
				if(x<(self.earlyStrength)):
					fight([self.ally['adc']['object'],self.ally['support']['object'], self],[self.oponent['adc']['object'], self.oponent['support']['object']] )
					
					x = random.randint(0, 1000 + 1000 - advantage)
					
					if(x<self.game_Vision+self.advantage and not self.dead and match.dragon.isAlive):
						tryMonster(self, match, match.dragon)
					
				if(x<(self.earlyStrength + self.roamBonus)):
					x = random.randint(1, 2)
						
					if (x==1):
						fight([self.ally['top']['object'], self],[self.oponent['top']['object']] )
						laneStructures = match.getOponentStructures(self, 'top')
						allys.append(self.ally['top']['object'])
						
					elif (x==2):
						fight([self.ally['mid']['object'], self],[self.oponent['mid']['object']] )
						laneStructures = match.getOponentStructures(self, 'mid')
						allys.append(self.ally['mid']['object'])
						
					x = random.randint(0, 1000 + 1000 - advantage)
					
				
			elif play == 3:
				
				self.earlyStrength = (self.game_Vision + self.team_Play + self.aggressivity)/3
				
				x = random.randint(0, 1000 + 1000 - advantage)
				
				self.farm += int(self.farming/10)-1
				self.mvp += 1
				self.advantage += int(self.farm/10)
				self.ally['support']['object'].advantage += 1
				
				#tenta lutar
				if(x<(self.earlyStrength)):
					fight([self.ally['adc']['object'],self.ally['support']['object'], self],[self.oponent['adc']['object'], self.oponent['support']['object']] )
				
					x = random.randint(0, 1000 + 1000 - advantage)
					
				if(x<(self.earlyStrength + self.roamBonus)):
					x = random.randint(1, 2)
						
					if (x==1):
						fight([self.ally['top']['object'], self],[self.oponent['top']['object']] )
						laneStructures = match.getOponentStructures(self, 'top')
						allys.append(self.ally['top']['object'])
						
					elif (x==2):
						fight([self.ally['mid']['object'], self],[self.oponent['mid']['object']] )
						laneStructures = match.getOponentStructures(self, 'mid')
						allys.append(self.ally['mid']['object'])
						
					x = random.randint(0, 1000 + 1000 - advantage)
					
					
					if(x<self.game_Vision+self.advantage and not self.dead and match.dragon.isAlive):
						tryMonster(self, match, match.dragon)
						

			if not self.dead and x < self.game_Vision:
				if not laneStructures.down:
					laneStructures.push(allys, match.getAllyStructures(self, laneStructures.lane))
				else:
					baseStructures.push(allys)
				#tenta levar estruturas		
			
			
		else:
			teamPlay(self, advantage, match, laneStructures)
			
	def setEarlyAttitude(self, n):
		if (n==1):
			self.attitude = n
			self.protectBonus = 20
			self.roamBonus = 0
			self.aggressivityBonus = 0
			self.earlyStrength = (self.passivity + self.team_Play + self.game_Vision)/3
		elif (n==2):
			self.attitude = n
			self.protectBonus = 5
			self.roamBonus = 10
			self.aggressivityBonus = 5
			self.earlyStrength = (self.game_Vision + self.team_Play + self.aggressivity)/3
		elif (n==3):
			self.attitude = n
			self.protectBonus = 0
			self.roamBonus = 0
			self.aggressivityBonus = 20
			self.earlyStrength = (self.game_Vision + self.team_Play + self.aggressivity)/3
			
class Coach (Person):
					
	def __init__(self):

		self.game_Vision = 0
		self.game_Knowledge = 0
		self.leadership = 0
