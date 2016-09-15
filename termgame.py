"""
Pygame framework taken by Lukas Peraza for 15-112 F15 Pygame Optional Lecture, 11/11/15

More citations at the bottom of code. 

My link to the youtube video: https://youtu.be/5eoVDhVCx-Y

"""

import random
import pygame
from pygame.locals import *

###############
### BUTTONS ### 
###############

class fightButton(pygame.sprite.Sprite): 
	def __init__(self,x,y):
		super(fightButton,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load\
								("images/fight.png").convert_alpha(),(100,40))
		self.width,self.height = self.image.get_size()
		self.updateRect() 

	def updateRect(self):
		self.rect = pygame.Rect(self.x-self.width/2,self.y-self.height/2,\
								self.width,self.height)

class trainButton(pygame.sprite.Sprite): 
	def __init__(self,x,y): 
		super(trainButton,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load\
								("images/train.png").convert_alpha(),(100,40))
		self.width,self.height = self.image.get_size()
		self.updateRect()

	def updateRect(self): 
		self.rect = pygame.Rect(self.x-self.width/2,\
							self.y-self.height/2,self.width,self.height)
	
class restButton(pygame.sprite.Sprite): 
	def __init__(self,x,y):
		super(restButton,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load\
								("images/rest.png").convert_alpha(),(100,40))
		self.width,self.height = self.image.get_size()
		self.updateRect() 

	def updateRect(self): 
		self.rect = pygame.Rect(self.x-self.width/2,\
							self.y-self.height/2,self.width,self.height)

class titleLogo(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(titleLogo,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load\
								("images/title.png").convert_alpha(),(300,120))
		self.width,self.height = self.image.get_size()
		self.updateRect() 

	def updateRect(self): 
		self.rect = pygame.Rect(self.x-self.width/2,\
							self.y-self.height/2,self.width,self.height)

class menuBackground(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(menuBackground,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load\
								("images/cutout.png").convert_alpha(),(900,350))
		self.width,self.height = self.image.get_size()
		self.updateRect() 

	def updateRect(self): 
		self.rect = pygame.Rect(self.x-self.width/2,\
							self.y-self.height/2,self.width,self.height)

class playButton(pygame.sprite.Sprite):
	def __init__(self,x,y): 
		super(playButton,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load\
							("images/playbutton.png").convert_alpha(),(100,40))
		self.width,self.height = self.image.get_size()
		self.updateRect() 

	def updateRect(self): 
		self.rect = pygame.Rect(self.x-self.width/2,\
							self.y-self.height/2,self.width,self.height)

class instructButton(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(instructButton,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load\
							("images/instruct.png").convert_alpha(),(270,40))
		self.width,self.height = self.image.get_size()
		self.updateRect() 
	def updateRect(self): 
		self.rect = pygame.Rect(self.x-self.width/2,\
							self.y-self.height/2,self.width,self.height)

class editorButton(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(editorButton,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load\
								("images/editor.png").convert_alpha(),(120,40))
		self.width,self.height = self.image.get_size()
		self.updateRect() 
	def updateRect(self): 
		self.rect = pygame.Rect(self.x-self.width/2,\
							self.y-self.height/2,self.width,self.height)

class backToMenu(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(backToMenu,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load\
							("images/menuwhite.png").convert_alpha(),(80,30))
		self.width,self.height = self.image.get_size()
		self.updateRect() 
	def updateRect(self): 
		self.rect = pygame.Rect(self.x-self.width/2,self.y-self.height/2,
								self.width,self.height)

######################
## "TRAIN" ELEMENTS ## 
######################

class Portal (pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(Portal,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load
											("images/crate.png").
			convert_alpha(),(100,80))
		self.width,self.height = self.image.get_size()
		self.updateRect()
	def updateRect(self):
		self.rect = pygame.Rect(self.x-self.width/2,self.y,
								self.width,self.height)

class Ledge (pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(Ledge,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load
											("images/cloudvector.png").
			convert_alpha(),(120,50))
		self.width,self.height = self.image.get_size()
		self.updateRect()

	def draw(self,screen): 
		screen.blit(self.image,(self.x-self.width/2,self.y-self.height/2))

	def updateRect(self):
		self.rect = pygame.Rect(self.x-self.width/2,self.y,self.width-20,20)

class Platform (pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(Platform,self).__init__()
		self.x = x 
		self.y = y 

		self.image = pygame.transform.scale(pygame.image.load(\
			"images/cloudplatleft.png").
			convert_alpha(),(300,110))
		self.width,self.height = self.image.get_size()
		self.updateRect()

	def draw(self,screen): 
		screen.blit(self.image,(self.x-self.width/2, self.y-self.height/2))

	def updateRect(self):
		self.rect = pygame.Rect(self.x-self.width/2,self.y+10,self.width,30)

class Bullet (pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(Bullet,self).__init__()
		self.x = x 
		self.y = y 
		self.speed = 10 
		self.image = pygame.transform.scale(pygame.image.load
							("images/snowball1.png").convert_alpha(),(30,30))
		self.width,self.height = self.image.get_size()
		self.updateRect() 

	def updateRect(self):  
		self.rect = pygame.Rect(self.x-self.width/2,self.y-self.height/2,
								self.width,self.height)

class BossBullet (pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(BossBullet,self).__init__()
		self.x = x 
		self.y = y 
		self.speed = 10 
		self.image = pygame.transform.scale(pygame.image.load
							("images/attackball.png").convert_alpha(),(30,30))
		self.width,self.height = self.image.get_size()
		self.updateRect() 

	def updateRect(self):  
		self.rect = pygame.Rect(self.x-self.width/2,self.y-self.height/2,
							self.width,self.height)

class Background (pygame.sprite.Sprite): 
	def __init__(self,x,y): 
		super(Background,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load(\
			"images/trainingback.png").convert_alpha(),(900,600))
		self.width, self.height = self.image.get_size()
		self.updateRect()
	def updateRect(self):
		self.rect = pygame.Rect(self.x-self.width/2,self.y-self.height/2,
							self.width,self.height)

class MapIcon (pygame.sprite.Sprite): 
	def __init__(self,x,y):
		super(MapIcon,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load(\
			"images/mapicon.PNG").convert_alpha(),(50,55))
		self.width, self.height = self.image.get_size()
		self.updateRect()
	def updateRect(self):
		self.rect = pygame.Rect(self.x-self.width/2,self.y-self.height/2,
								self.width,self.height)

class TokenAttack (pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(TokenAttack,self).__init__()
		self.x = x 
		self.y = y 
		self.speed = 3 
		self.image = pygame.transform.scale(pygame.image.load
											("images/token1.png").
			convert_alpha(),(25,28))
		self.width, self.height = self.image.get_size()
		self.updateRect()
	def updateRect(self):
		self.rect = pygame.Rect(self.x-self.width/2,self.y-self.height/2,
								self.width,self.height)

class TokenAgility (pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(TokenAgility,self).__init__()
		self.x = x 
		self.y = y 
		self.speed = 3
		self.image = pygame.transform.scale(pygame.image.load
											("images/token2.png").
			convert_alpha(),(25,25))
		self.width, self.height = self.image.get_size()
		self.updateRect()
	def updateRect(self):
		self.rect = pygame.Rect(self.x-self.width/2,self.y-self.height/2,
								self.width,self.height)

class TokenDefense(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(TokenDefense,self).__init__()
		self.x = x 
		self.y = y
		self.speed = 3
		self.image = pygame.transform.scale(pygame.image.load
											("images/token3.png").
			convert_alpha(),(25,25))
		self.width, self.height = self.image.get_size()
		self.updateRect()
	def updateRect(self):
		self.rect = pygame.Rect(self.x-self.width/2,self.y-self.height/2,
								self.width,self.height)

class AttackBackground(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(AttackBackground,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load
											("images/results.png").
			convert_alpha(),(1200,600))
		self.width, self.height = self.image.get_size()
		self.updateRect()

	def updateRect(self): 
		self.rect = pygame.Rect(self.x-self.width/2,self.y-self.height/2,
								self.width,self.height)

class AgilityBackground(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(AgilityBackground,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load
											("images/trainingback2.png").
			convert_alpha(),(1200,700))
		self.width, self.height = self.image.get_size()
		self.updateRect()
	def updateRect(self): 
		self.rect = pygame.Rect(self.x-self.width/2,self.y-self.height/2,
								self.width,self.height)

class nextButton(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(nextButton,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load
							("images/nextstage.png").convert_alpha(),(300,35))
		self.width,self.height = self.image.get_size()
		self.updateRect() 

	def updateRect(self):
		self.rect = pygame.Rect(self.x-self.width/2,self.y-self.height/2,
								self.width,self.height)

class nextStage(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(nextStage,self).__init__()
		self.x = x
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load
							("images/nextstage.png").convert_alpha(),(300,35))
		self.width,self.height = self.image.get_size()
		self.updateRect()

	def updateRect(self):
		self.rect = pygame.Rect(self.x-self.width/2,self.y-self.height/2,
							self.width,self.height)

class DefenseBackground(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(DefenseBackground,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load
											("images/trainingback3.jpg").
			convert_alpha(),(1200,750))
		self.width, self.height = self.image.get_size()
		self.updateRect()
	def updateRect(self): 
		self.rect = pygame.Rect(self.x-self.width/2,self.y-self.height/2,
								self.width,self.height)

class Frostbite(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(Frostbite,self).__init__()
		self.x = x 
		self.y = y 
		self.speed = 3
		self.image = pygame.transform.scale(pygame.image.load
							("images/frostbite.png").convert_alpha(),(30,34))
		self.width,self.height = self.image.get_size()
		self.updateRect() 

	def updateRect(self):  
		self.rect = pygame.Rect(self.x-self.width/2,self.y-self.height/2,
							self.width,self.height+5)


######################
## "FIGHT" ELEMENTS ## 
######################

class BattleBackground(pygame.sprite.Sprite): 
	def __init__(self,x,y):
		super(BattleBackground,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load
										("images/battleground.jpg").
				convert_alpha(),(960,600))
		self.width, self.height = self.image.get_size()
		self.updateRect()

	def updateRect(self): 
		self.rect = pygame.Rect(self.x-self.width/2,self.y-self.height/2,
								self.width,self.height)

class FrozenLedge(pygame.sprite.Sprite): 
	def __init__(self,x,y):
		super(FrozenLedge,self).__init__()
		self.x = x 
		self.y = y 
		self.speed = 3
		self.image = pygame.transform.scale(pygame.image.load(\
			"images/frozenledge.png").
			convert_alpha(),(120,60))
		self.width,self.height = self.image.get_size()
		self.updateRect()

	def draw(self,screen): 
		screen.blit(self.image,(self.x-self.width/2, self.y-self.height/2))

	def updateRect(self):
		self.rect = pygame.Rect(self.x-self.width/2,self.y-10,self.width,20)

class FrozenPlatform(pygame.sprite.Sprite): 
	def __init__(self,x,y):
		super(FrozenPlatform,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load(\
			"images/snowwall.png").
			convert_alpha(),(300,100))
		self.width,self.height = self.image.get_size() 
		self.updateRect()
	def draw(self,screen): 
		screen.blit(self.image,(self.x-self.width/2, self.y-self.height/2))
	def updateRect(self): 
		self.rect = pygame.Rect(self.x-self.width/2,self.y+12,self.width,2)

class SavePuffle(pygame.sprite.Sprite): 
	def __init__(self,x,y): 
		super(SavePuffle,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load(\
			"images/bluepufflesad.png").
			convert_alpha(),(50,50))
		self.width,self.height = self.image.get_size()
		self.updateRect() 
	def draw(self,screen): 
		screen.blit(self.image,(self.x-self.width/2, self.y-self.height/2))
	def updateRect(self): 
		self.rect = pygame.Rect(self.x-self.width/2,self.y+12,self.width,2)

class Cage(pygame.sprite.Sprite): 
	def __init__(self,x,y): 
		super(Cage,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load(\
			"images/netfront.png").convert_alpha(),(130,80))
		self.width,self.height = self.image.get_size()
		self.updateRect() 
	def draw(self,screen): 
		screen.blit(self.image,(self.x-self.width/2, self.y-self.height/2))
	def updateRect(self): 
		self.rect = pygame.Rect(self.x-self.width/2,self.y+12,self.width,2)

#####################
## "REST" ELEMENTS ## 
#####################

class IglooBackground(pygame.sprite.Sprite): 
	def __init__(self,x,y):
		super(IglooBackground,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load
											("images/betterigloo.png").
				convert_alpha(),(760,400))
		self.width, self.height = self.image.get_size()
		self.updateRect()

	def updateRect(self): 
		self.rect = pygame.Rect(self.x-self.width/2,self.y-self.height/2,
								self.width,self.height)

class mapBackground(pygame.sprite.Sprite):
	def __init__(self,x,y): 
		super(mapBackground,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load
											("images/cpmap.jpg").
			convert_alpha(),(840,640))
		self.width,self.height = self.image.get_size()
		self.updateRect()

	def updateRect(self):
		self.rect = pygame.Rect(self.x-self.width/2,self.y-self.height/2,
								self.width,self.height)

class igloo(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(igloo,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load
											("images/startgame.jpeg").
			convert_alpha(),(1000,590))
		self.width,self.height = self.image.get_size()
		self.updateRect()
	def updateRect(self):
		self.rect = pygame.Rect(self.x-self.width/2,self.y-self.height/2,
								self.width,self.height)

##################
### CHARACTERS ### 
##################

class redPuffle(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(redPuffle,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load
							("images/puffle2.png").convert_alpha(),(100,80))
		self.width,self.height = self.image.get_size()
		self.updateRect() 

	def updateRect(self): 
		self.rect = pygame.Rect(self.x-self.width/2,self.y-self.height/2,
							self.width,self.height)

class greenPuffle(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(greenPuffle,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load
							("images/redpuffle.png").convert_alpha(),(70,70))
		self.width,self.height = self.image.get_size()
		self.updateRect() 
	def updateRect(self): 
		self.rect = pygame.Rect(self.x-self.width/2,self.y-self.height/2,
								self.width,self.height)

class BigBoss(pygame.sprite.Sprite):
	def __init__(self,x,y): 
		super(BigBoss,self).__init__()
		self.x = x 
		self.y = y 
		self.speed = 5
		self.image1 = pygame.transform.scale(pygame.image.load
											 ("images/bossflip.png").
				convert_alpha(),(125,125))
		self.image2 = pygame.transform.scale(pygame.image.load
											 ("images/boss.png").
				convert_alpha(),(125,125))
		self.width1,self.height1 = self.image1.get_size()
		self.width2,self.height2 = self.image2.get_size()
		self.width,self.height = self.width1,self.height1
		self.updateRect(False)

	def draw(self,screen,reverseBoss): 
		if reverseBoss: 
			screen.blit(self.image1,(self.x-self.width1/2,
									 self.y-self.height1/2))
		else: #Image one, facing right
			screen.blit(self.image2,(self.x-self.width2/2,
									 self.y-self.height2/2))
		self.updateRect(reverseBoss)

	def updateRect(self,reverseBoss): 
		if reverseBoss: 
			self.rect = pygame.Rect(self.x-self.width1/2,
								self.y-self.height1/2,self.width1,self.height1)
		else: 
			self.rect = pygame.Rect(self.x-self.width2/2,
								self.y-self.height2/2,self.width2,self.height2)

class Boss(pygame.sprite.Sprite):
	def __init__(self,x,y): 
		super(Boss,self).__init__()
		self.x = x 
		self.y = y 
		self.speed = 5
		self.image1 = pygame.transform.scale(pygame.image.load(\
			"images/badpuffle5.png").convert_alpha(),(100,110))
		self.image2 = pygame.transform.scale(pygame.image.load
											("images/badpuffle5flip.png").
			convert_alpha(),(100,110))
		self.width1, self.height1 = self.image1.get_size()
		self.width2, self.height2 = self.image2.get_size()
		self.updateRect(False)

	def draw(self,screen,reverse): 
		if reverse: 
			screen.blit(self.image1,(self.x-self.width1/2,
									 self.y-self.height1/2))
		else: 
			screen.blit(self.image2,(self.x-self.width2/2,
									 self.y-self.height2/2))

	def updateRect(self,reverse):
		if reverse:
			self.rect = pygame.Rect(self.x-self.width1/2-20,
						self.y-self.height1/2,self.width1-20,self.height1)
		else: 
			self.rect = pygame.Rect(self.x-self.width2/2-20,
						self.y-self.height2/2,self.width2-20,self.height2)

class Puffle (pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(Puffle,self).__init__()
		self.x = x 
		self.y = y
		self.lastMove = True #Left 
		self.image1 = pygame.transform.scale(pygame.image.load
											 ("images/puffleleft.png").
				convert_alpha(),(70,54))
		self.image2 = pygame.transform.scale(pygame.image.load
											 ("images/puffleright.png").
				convert_alpha(),(60,48))
		self.image3 = pygame.transform.scale(pygame.image.load
											 ("images/pufflehurtleft.png").
				convert_alpha(),(50,50))
		self.image4 = pygame.transform.scale(pygame.image.load
											 ("images/pufflehurtright.png").
				convert_alpha(),(50,50))
		self.images = [self.image1, self.image2, self.image3, self.image4]
		self.currentImage = self.images[0]

		self.width1,self.height1 = self.image1.get_size()
		self.width2,self.height2 = self.image2.get_size()
		self.width3,self.height3 = self.image3.get_size()
		self.width4,self.height4 = self.image4.get_size()

		self.updateRect(False,False)
		self.topCollide = False
		self.rightCollide = False
		self.leftCollide = False
		self.bottomCollide = False

	def updateRect(self,turnRight,gotHit):
		if gotHit and not turnRight:
			self.rect = pygame.Rect(self.x-self.width3/2,
							self.y-self.height3/2,self.width3,self.height3)
		elif gotHit and turnRight: 
			self.rect = pygame.Rect(self.x-self.width4/2,
							self.y-self.height4/2,self.width4,self.height4)
		else: 
			if turnRight and not gotHit: 
				self.rect = pygame.Rect(self.x-self.width2/2,
							self.y-self.height2/2,self.width2,self.height2)
			elif not turnRight and not gotHit: 
				self.rect = pygame.Rect(self.x-self.width1/2,
							self.y-self.height1/2,self.width1,self.height1)
			Game.hitTimer = 0
		
	def draw(self,screen,turnRight,gotHit): 
		if gotHit and not turnRight: 
			self.currentImage = self.images[2]
			screen.blit(self.image3,
						(self.x-self.width3/2,self.y-self.height3/2))
		elif gotHit and turnRight: 
			self.currentImage = self.images[3]
			screen.blit(self.image4,
						(self.x-self.width4/2,self.y-self.height4/2))
		else: 
			if turnRight: 
				self.currentImage = self.images[1]
				screen.blit(self.currentImage,
							(self.x-self.width2/2,self.y-self.height2/2))
			elif not turnRight: 
				self.currentImage = self.images[0]
				screen.blit(self.currentImage,
							(self.x-self.width1/2,self.y-self.height1/2))
			Game.hitTimer = 0
			
		self.updateRect(turnRight,gotHit)

class BossTwo (pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(BossTwo,self).__init__()
		self.x = x 
		self.y = y 
		self.speed = 5 
		self.image = pygame.transform.scale(pygame.image.load
											("images/badpuffle4.png").
			convert_alpha(),(100,130))
		self.width, self.height = self.image.get_size()
		self.updateRect()

	def draw(self,screen): 
		screen.blit(self.image,(self.x-self.width/2, self.y-self.height/2))

	def updateRect(self):
		self.rect = pygame.Rect(self.x-self.width/2-20,
								self.y-self.height/2,self.width-20,self.height)

class Potion (pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(Potion,self).__init__()
		self.x = x 
		self.y = y 
		self.speed = 3 
		self.image = pygame.transform.scale\
			(pygame.image.load("images/potion.png").
			convert_alpha(),(50,60))
		self.width, self.height = self.image.get_size()
		self.updateRect()
	def updateRect(self):
		self.rect = pygame.Rect(self.x-self.width/2-20,
								self.y-self.height/2,self.width-20,self.height)

class BadPuffle (pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(BadPuffle,self).__init__()
		self.x = x 
		self.y = y 
		self.speed = 5 
		self.image = pygame.transform.scale(pygame.image.load
											("images/angrypuffle.png").
			convert_alpha(),(55,55))
		self.width, self.height = self.image.get_size()
		self.updateRect()

	def draw(self,screen): 
		screen.blit(self.image,(self.x-self.width/2, self.y-self.height/2))

	def updateRect(self):
		self.rect = pygame.Rect(self.x-self.width/2-20,self.y-self.height/2,
							self.width-20,self.height)

##################
### MAIN CLASS ### 
##################

class Game(object):
	#General variables to reference throughout the game
	healthPoints = 100 
	attack = 1 
	defense = 0 
	agility = 3 
	timer = 0
	hitTimer = 0

	def __init__(self,mode):
		self.width = 800
		self.height = 600
		self.mode = mode

		self.puffWidth = 50 #Where the puffle starts on the screen
		self.puffHeight = 550

		self.fps = 50

		pygame.init() #Initialize 
		self.screen = pygame.display.set_mode((self.width,self.height))	

		#Initialize all variables and sprites
		self.Background = pygame.sprite.Group()
		self.Background.add(Background(self.width/2,self.height/2))

		self.BattleBackground = pygame.sprite.Group() 
		self.BattleBackground.add(BattleBackground(self.width/2,self.height/2))

		self.AttackBackground = pygame.sprite.Group()
		self.AttackBackground.add(AttackBackground(self.width/2,self.height/2))

		self.AgilityBackground = pygame.sprite.Group()
		self.AgilityBackground.add(AgilityBackground
								   (self.width/2,self.height/2))

		self.DefenseBackground = pygame.sprite.Group()
		self.DefenseBackground.add(DefenseBackground
								   (self.width/2,self.height/2))

		self.IglooBackground = pygame.sprite.Group()
		self.IglooBackground.add(IglooBackground
								 (self.width/2,self.height/2))

		self.MapIcon = pygame.sprite.Group()
		self.MapIcon.add(MapIcon(50,50))

		self.Puffles = pygame.sprite.Group()
		if self.mode == "Train" or self.mode == "Fight":
			self.Puffles.add(Puffle(self.puffWidth, self.puffHeight)) 
			self.ground = self.puffHeight 
		elif self.mode == "Rest":
			self.Puffles.add(Puffle(200,400))
			self.ground = 400

		self.nextButton = pygame.sprite.Group()
		self.nextButton.add(nextButton(420,400))
		self.nextStage = pygame.sprite.Group()
		self.nextStage.add(nextStage(420,400))

		self.Bullets = pygame.sprite.Group()
		self.BossBullets = pygame.sprite.Group()
		self.Potion = pygame.sprite.Group() 
		
		self.Boss = pygame.sprite.Group()
		self.BossTwo = pygame.sprite.Group()
		if self.mode == "Train":
			self.Boss.add(Boss(350,250))
			self.BossTwo.add(BossTwo(625,425))

		# KEYPRESS RESPONSES for right/left arrow keys
		self.pressLeft = False
		self.pressRight = False 
		self.turnRight = False
		self.turnLeft = False
		self.pressUp = False
		self.pressDown = False

		# KEYPRESS RESPONSES FOR up/down arrow keys 
		self.doJump = False
		self.falling = False

		self.counter = 0

		#Initialize training ground features
		self.Platforms = pygame.sprite.Group()
		self.Ledges = pygame.sprite.Group()
		self.Portal = pygame.sprite.Group()
		self.BadPuffleOne = pygame.sprite.Group() 
		self.Frostbite = pygame.sprite.Group()

		#Initial positions of frozen ledges 
		self.posAx, self.posAy, self.posA = 200,515,True
		self.posBx, self.posBy, self.posB = 380,480,False
		self.posCx, self.posCy, self.posC = 560,445,False
		self.posDx, self.posDy, self.posD = 380,390,False
		self.posEx, self.posEy, self.posE = 200,335,False
		self.posFx, self.posFy, self.posF = 670,180,False
		
		if self.mode == "Train": 
			self.Platforms.add(Platform(625,470)) #Last in indexing 
			self.Platforms.add(Platform(350,300))
			self.Platforms.add(Platform(650,75)) #First in indexing 
			self.Ledges.add(Ledge(180,525))
			self.Ledges.add(Ledge(355,500))
			self.Ledges.add(Ledge(750,420))
			self.Ledges.add(Ledge(600,350))
			self.Ledges.add(Ledge(100,250))
			self.Ledges.add(Ledge(250,175))
			self.Ledges.add(Ledge(400,100))
			self.Portal.add(Portal(700,25))
			self.BadPuffleOne.add(BadPuffle(180,515))
			self.Frostbite.add(Frostbite(60,200))
			self.Frostbite.add(Frostbite(330,130))
			self.Frostbite.add(Frostbite(650,300))
			self.Frostbite.add(Frostbite(200,425))

		self.FrozenLedges = pygame.sprite.Group()
		self.FrozenPlatforms = pygame.sprite.Group()
		self.BigBoss = pygame.sprite.Group() 
		self.SavePuffles = pygame.sprite.Group() 
		self.Cages = pygame.sprite.Group()

		if self.mode == "Fight": 
			self.FrozenLedges.add(FrozenLedge(self.posAx,self.posAy))
			self.FrozenLedges.add(FrozenLedge(self.posBx,self.posBy))
			self.FrozenLedges.add(FrozenLedge(self.posCx,self.posCy))
			self.FrozenLedges.add(FrozenLedge(self.posDx,self.posDy))
			self.FrozenLedges.add(FrozenLedge(self.posEx,self.posEy))
			self.FrozenLedges.add(FrozenLedge(self.posFx,self.posFy))
			self.FrozenPlatforms.add(FrozenPlatform(450,230))
			self.BigBoss.add(BigBoss(450,200))
			self.SavePuffles.add(SavePuffle(670,150))
			self.Cages.add(Cage(670,100))

		self.hitCounter = 0
		self.bossPoints = 100 #HP for Big Boss in "Fight" Mode 
		self.doKill = False
		self.timeCount = 0 

		#Displays the health bars & icons
		self.icon = pygame.transform.scale(pygame.image.load
										   ("images/puffleleft.png").
			convert_alpha(),(40,35))
		self.bossIcon = pygame.transform.scale(pygame.image.load
											   ("images/boss.png").
			convert_alpha(),(40,40))
		self.loseScreen = pygame.transform.scale(pygame.image.load
												 ("images/losescreen.jpg").
			convert_alpha(),(960,600))
		self.winScreen = pygame.transform.scale(pygame.image.load
												("images/winscreen.png").
			convert_alpha(),(800,500))

		self.attackIcon = pygame.transform.scale(pygame.image.load
												 ("images/token1.png").
			convert_alpha(),(40,40))
		self.agilityIcon = pygame.transform.scale(pygame.image.load
												  ("images/token2.png").
			convert_alpha(),(40,40))
		self.defenseIcon = pygame.transform.scale(pygame.image.load
												  ("images/token3.png").
			convert_alpha(),(40,40))
		self.igloo = pygame.sprite.Group() 
		self.igloo.add(igloo(400,290))

		self.backToMenu = pygame.sprite.Group()
		self.backToMenu.add(backToMenu(50,575))
		self.pressBack = False

		self.TokenAttack = pygame.sprite.Group()
		self.TokenAgility = pygame.sprite.Group()
		self.TokenDefense = pygame.sprite.Group()
		if self.mode != "Fight":
			self.TokenAttack.add(TokenAttack(670,75))
			self.TokenDefense.add(TokenDefense(680,75))
			self.TokenAgility.add(TokenAgility(670,75))

		self.crate = True #Crate will be there when you draw 
		self.jumpCount = 0 #For bad puffle
		self.badFall = False
		self.badJump = True

		self.hitCounter1 = 0 
		self.doKill1 = False 
		self.hitCounter2 = 0 
		self.doKill2 = False 
		self.hitCounter3 = 0 
		self.doKill3 = False

		self.newCount = 0
		self.gotHit = False
		self.hitTimer = 0 
		self.attackTimer = 0 
		self.gotAttack = False
		self.agilityTimer = 0 
		self.gotAgility = False
		self.defenseTimer = 0
		self.gotDefense = False
		self.attackCount = 0
		self.agilityCount = 0
		self.defenseCount = 0 

		self.reverse = False
		self.reverseBoss = False

	def jump(self): #Allows puffle to jump
		# If there is a platform above the puffle
		if self.Puffles.sprites()[0].topCollide == True: 
			self.doJump = False
		if self.doJump == True: 
			self.Puffles.sprites()[0].y -= 5
			self.counter += 1
			if self.counter > 15: 
				self.doJump = False 
				self.falling = True
				self.counter = 0

	def fall(self): #Allows puffle to fall after jumping (simulated gravity)
		#If the puffle doesn't have a platform below him
		if not self.Puffles.sprites()[0].bottomCollide == True:
			#If the puffle is above the ground, move toward ground 
			if self.Puffles.sprites()[0].y < self.ground:
				self.Puffles.sprites()[0].y += 5
			#Otherwise, puffle is not falling
			else: 
				self.falling = False
				self.Puffles.sprites()[0].y = self.ground

	def keyPressed(self,key):
		# PUFFLE MAIN CHARACTER MOVEMENT
		if key == pygame.K_LEFT:
			self.pressLeft = True
			self.turnLeft = True 
			self.turnRight = False
			self.Puffles.sprites()[0].lastMove = True

		elif key == pygame.K_RIGHT:
			self.pressRight = True
			self.turnRight = True
			self.turnLeft = False
			self.Puffles.sprites()[0].lastMove = False

		elif key == pygame.K_SPACE: #Can jump if not falling 
			if not self.falling or self.Puffles.sprites()[0].bottomCollide \
				or not self.Puffles.sprites()[0].topCollide:
				self.doJump = True

		elif key == pygame.K_UP and self.mode == "Rest": 
			self.pressUp = True

		elif key == pygame.K_DOWN and self.mode == "Rest": 
			self.pressDown = True 
	
		# Checks the bounds of window, if puffle goes off-screen
		if self.mode == "Train":
			if self.Puffles.sprites()[0].y < 35:
				self.Puffles.sprites()[0].y = 35
			elif self.Puffles.sprites()[0].y > 565:
				self.Puffles.sprites()[0].y = 565
		elif self.mode == "Rest":
			if self.Puffles.sprites()[0].y < 150:
				self.Puffles.sprites()[0].y = 150
			elif self.Puffles.sprites()[0].y > 475:
				self.Puffles.sprites()[0].y = 475

		# BULLET MOVEMENT; if you press b, snowballs will come out 
		if key == pygame.K_b: 
			bullet = Bullet(self.Puffles.sprites()[0].x,
							self.Puffles.sprites()[0].y)
			if self.Puffles.sprites()[0].lastMove: #If the puffle faces right
				bullet.speed *= -1 #Change bullet direction 
			self.Bullets.add(bullet)

	def keyReleased(self,key):
		if key == pygame.K_LEFT:
			self.pressLeft = False
		elif key == pygame.K_RIGHT:
			self.pressRight = False
		elif key == pygame.K_UP: 
			self.pressUp = False
		elif key == pygame.K_DOWN: 
			self.pressDown = False

	def move(self): #Moves the puffle, called in timer fired function
		if self.mode == "Train" or self.mode == "Fight" or \
						self.mode == "AgilityGame":
			if self.pressLeft and self.Puffles.sprites()[0].x > 37 and \
								not self.Puffles.sprites()[0].leftCollide:
								 #Not off-screen
				self.Puffles.sprites()[0].x -= Game.agility
				self.Puffles.update()
			elif self.pressRight and self.Puffles.sprites()[0].x < 763 and \
								not self.Puffles.sprites()[0].rightCollide: 
				self.Puffles.sprites()[0].x += Game.agility
				self.Puffles.update()
		else: #It's in "rest" mode; make sure puffle doesn't go outside igloo 
			if self.pressLeft and self.Puffles.sprites()[0].x > 100 and \
								not self.Puffles.sprites()[0].leftCollide: 
				self.Puffles.sprites()[0].x -= Game.agility
				self.Puffles.update()
			elif self.pressRight and self.Puffles.sprites()[0].x < 700 and \
								not self.Puffles.sprites()[0].rightCollide:
				self.Puffles.sprites()[0].x += Game.agility
				self.Puffles.update()
			elif self.pressUp and self.Puffles.sprites()[0].y > 350: 
				self.Puffles.sprites()[0].y -= Game.agility
			elif self.pressDown and self.Puffles.sprites()[0].y < 450: 
				self.Puffles.sprites()[0].y += Game.agility

	def timerFired(self):
		Game.timer += 1 #Acts like our clock 
		for bullet in self.Bullets.sprites(): 
			bullet.x += bullet.speed
			bullet.updateRect()
		margin = 2

		Game.hitTimer += 1 #Reset timer to show puffle damage
		if self.gotHit and Game.hitTimer > 10: 
			self.gotHit = False 
			Game.hitTimer = 0

		self.attackTimer += 1
		if self.gotAttack and self.attackTimer > 500: 
			self.gotAttack = False
			if self.attackCount == 1: 
				Game.attack -= 1
				self.attackCount = 0
			elif self.attackCount > 1:
				Game.attack -= self.attackCount
				self.attackCount = 0
			self.attackTimer = 0

		self.agilityTimer += 1 
		if self.gotAgility and self.agilityTimer > 500: 
			self.gotAgility = False
			if self.agilityCount == 1: 
				Game.agility -= 1
				self.agilityCount = 0
			elif self.agilityCount > 1:
				Game.agility -= self.agilityCount
				self.agilityCount = 0
			self.agilityTimer = 0

		self.defenseTimer += 1
		if self.gotDefense and self.defenseTimer > 500: 
			self.gotDefense = False
			if self.defenseCount == 1: 
				Game.defense -= 1
				self.defenseCount = 0
			elif self.defenseCount > 1:
				Game.defense -= self.defenseCount
				self.defenseCount = 0
			self.defenseTimer = 0
		
		for puff in self.Puffles.sprites():
			puff.updateRect(self.turnRight,self.gotHit)
	
		#Increases Big Boss bullets if he is dying 
		for bossBullet in self.BossBullets.sprites():
			if(bossBullet.x < self.Puffles.sprites()[0].x):
				bossBullet.x += margin
			if(bossBullet.x >= self.Puffles.sprites()[0].x): 
				bossBullet.x -= margin
			if(bossBullet.y < self.Puffles.sprites()[0].y):
				bossBullet.y += margin
			if(bossBullet.y >= self.Puffles.sprites()[0].y):
				bossBullet.y += margin
			if self.bossPoints <= 70: margin = 2
			if self.bossPoints <= 50: margin = 3 
			if self.bossPoints <= 20: margin = 4 
			bossBullet.updateRect()

		#Allows "Train" bosses to keep moving along platform
		for boss in self.Boss.sprites():
			boss.x += boss.speed 
			if boss.x == self.Platforms.sprites()[0].x - self.Platforms.sprites()[0].width/2 \
				or boss.x == 200:
				boss.speed *= -1
			if boss.speed < 0: 
				self.reverse = True
			else:
				self.reverse = False
			boss.updateRect(self.reverse)

		for boss in self.BossTwo.sprites():
			boss.x += boss.speed 
			if boss.x == self.Platforms.sprites()[0].x - self.Platforms.sprites()[0].width/2 \
				or boss.x == self.Platforms.sprites()[0].x + \
									self.Platforms.sprites()[0].width/2:
				boss.speed *= -1
				if boss.speed < 0: 
					boss.x = self.Platforms.sprites()[0].x + \
									self.Platforms.sprites()[0].width/2
				else: 
					boss.x == self.Platforms.sprites()[0].x - self.Platforms.sprites()[0].width/2 

			boss.updateRect()

		# Allows movement for big boss along platform
		for big in self.BigBoss.sprites(): 
			big.x += big.speed
			if big.x == self.FrozenPlatforms.sprites()[0].x - \
							self.FrozenPlatforms.sprites()[0].width/2 \
				or big.x == self.FrozenPlatforms.sprites()[0].x + \
									self.FrozenPlatforms.sprites()[0].width/2:
				big.speed *= -1
				if big.speed < 0: 
					self.reverseBoss == True
				else: 
					self.reverseBoss == False
			# Increases difficulty of boss as he starts to die (shoots more bullets)
			if self.bossPoints >= 70 and self.bossPoints <= 100 \
					and self.timeCount %100 == 0:
				bullet = BossBullet(self.BigBoss.sprites()[0].x,
									self.BigBoss.sprites()[0].y)
				self.BossBullets.add(bullet)
			if self.bossPoints >= 50 and self.bossPoints < 70 and \
									self.timeCount % 80 == 0:
				bullet = BossBullet(self.BigBoss.sprites()[0].x,
									self.BigBoss.sprites()[0].y)
				self.BossBullets.add(bullet)
			if self.bossPoints >= 30 and self.bossPoints < 50 and\
									self.timeCount % 30 == 0:
				bullet = BossBullet(self.BigBoss.sprites()[0].x,
									self.BigBoss.sprites()[0].y)
				self.BossBullets.add(bullet)
			if self.bossPoints >= 0 and self.bossPoints < 30 and \
									self.timeCount % 10 == 0:
				bullet = BossBullet(self.BigBoss.sprites()[0].x,
									self.BigBoss.sprites()[0].y)
				self.BossBullets.add(bullet)

			big.updateRect(self.reverseBoss)

		for frost in self.Frostbite.sprites():
			frost.x += frost.speed 
			self.newCount += 1 
			if self.newCount > 80: 
				frost.speed *= -1 
				self.newCount = 0
			frost.updateRect()

		if self.timeCount%200 == 0: #Drops random potions 
			xValuePot = random.randint(40,750) 
			pot = Potion(xValuePot,0) 
			self.Potion.add(pot)
			pot.updateRect()

		for pot in self.Potion.sprites(): #Potions will fall down at speed
			pot.y += pot.speed
			pot.updateRect()

		if self.timeCount%50 == 0 and\
			self.timeCount != 0 and self.mode == "Fight":#Drops random powerups
			index = random.randint(0,2)
			xValue = random.randint(40,750)
			if index == 0: 
				atk = TokenAttack(xValue,0)
				self.TokenAttack.add(atk)
			elif index == 1:
				agil = TokenAgility(xValue,0)
				self.TokenAgility.add(agil)
			else: 
				defn = TokenDefense(xValue,0)
				self.TokenDefense.add(defn)
		if self.mode == "Fight":
			for move in self.TokenAttack.sprites():
				move.y += move.speed 
				move.updateRect()
			for move in self.TokenAgility.sprites():
				move.y += move.speed
				move.updateRect()
			for move in self.TokenDefense.sprites():
				move.y += move.speed
				move.updateRect()

		for badPuff in self.BadPuffleOne.sprites(): 
			ground = 515 
			if self.badJump == True and self.badFall == False:
				badPuff.y -= badPuff.speed
				self.jumpCount += 1
				if self.jumpCount > 10: 
					self.badFall = True 
					self.badJump = False
					self.jumpCount = 0	
			elif badPuff.y < ground: 
				badPuff.y += badPuff.speed
			elif badPuff.y >= ground: 
				self.badJump = True
				self.badFall = False
			badPuff.updateRect()

		self.move()
		if self.doJump: self.jump()
		elif self.doJump == False and self.falling: self.fall()

		#Collision functions 
		platResult = pygame.sprite.groupcollide(self.Puffles,self.Platforms,
												False,False)
		froPlatResult = pygame.sprite.groupcollide(self.Puffles,
											self.FrozenPlatforms,False,False)
		frozenResult = pygame.sprite.groupcollide(self.Puffles,
											self.FrozenLedges,False,False)
		ledResult = pygame.sprite.groupcollide(self.Puffles,
											   self.Ledges,False,False)
		bossResult = pygame.sprite.groupcollide(self.Bullets,self.BigBoss,
												True,False)
		hitResult = pygame.sprite.groupcollide(self.Puffles,self.Boss,
											   False,False)
		killResult = pygame.sprite.groupcollide(self.Puffles,self.BigBoss,
												False,False)
		bossHitResult = pygame.sprite.groupcollide(self.Puffles,
												   self.BossBullets,False,True)
		portResult = pygame.sprite.groupcollide(self.Bullets,self.Portal,
												True,True)
		sameBulletResult = pygame.sprite.groupcollide(self.BossBullets,
													  self.Bullets,True,True)
		bulletResult = pygame.sprite.groupcollide(self.Boss,self.Bullets,
												  self.doKill1,True)
		puffleResult = pygame.sprite.groupcollide(self.Bullets,
										self.BadPuffleOne,True,self.doKill2)
		nextResult = pygame.sprite.groupcollide(self.BossTwo,self.Bullets,
										self.doKill3,True)
		frostResult = pygame.sprite.groupcollide(self.Puffles,
										self.Frostbite,False,False)
		badPuffResult = pygame.sprite.groupcollide(self.Puffles,
										self.BadPuffleOne,False,False)
		bossTwoResult = pygame.sprite.groupcollide(self.Puffles,
										self.BossTwo,False,False)
		potionResult = pygame.sprite.groupcollide(self.Puffles,
										self.Potion,False,True)
		attackResult = pygame.sprite.groupcollide(self.Puffles,
										self.TokenAttack,False,True)
		defendResult = pygame.sprite.groupcollide(self.Puffles,
										self.TokenDefense,False,True)
		agilityResult = pygame.sprite.groupcollide(self.Puffles,
										self.TokenAgility,False,True)

		if len(bulletResult) > 0: #If puffle's bullets hit "Train" small bosses
			for key in bulletResult.keys():
				if self.mode == "Train":
					self.hitCounter1 += 1 
					if self.hitCounter1 > 5:  
						self.doKill1 = True
		if len(portResult) > 0: #Hit crate portal with bullets for next stage
			for key in portResult.keys():
				self.crate = False
		if len(potionResult) > 0: #If puffle collides with health potion
			for key in potionResult.keys():
				if self.mode == "Fight":
					Game.healthPoints += 10 
		if len(frostResult) > 0: #If puffle collides with frostbite, puffle die 
			for key in frostResult.keys():
				if self.mode == "AgilityGame":
					Game.healthPoints -=10
		if len(bossHitResult) > 0: #Puffle and Boss Bullets collision
			for key in bossHitResult.keys():
				if self.mode == "Fight":
					Game.healthPoints -= 10-2*Game.defense
					#If puffle is hit, then will lose 10 HP
					self.gotHit = True
					if Game.defense > 5: Game.defense = 4 
		elif len(attackResult) > 0: 
			for key in attackResult.keys():
				if self.mode == "Fight":
				
					Game.attack += 1
					self.gotAttack = True
			self.attackCount += 1 
		elif len(agilityResult) > 0: 
			for key in agilityResult.keys():
				if self.mode == "Fight":
			
					Game.agility += 1 
					self.gotAgility = True
			self.agilityCount += 1 
		elif len(defendResult) > 0: 
			for key in defendResult.keys():
				if self.mode == "Fight":
				
					Game.defense += 1
					self.gotDefense = True
			self.defenseCount += 1
		elif len(froPlatResult) > 0: #If puffle collides with platform
			for key in froPlatResult.keys(): 
				if self.mode == "Fight":
					self.collisionEffect(key,froPlatResult[key])
		elif len(frozenResult) > 0: #If puffle falls/walks on frozen ledges 
			for key in frozenResult.keys():
				if self.mode == "Fight":
					self.collisionEffect(key,frozenResult[key])
		elif len(platResult) > 0: #If puffle collides with regular platforms
			for key in platResult.keys():
				if not self.mode == "Fight" and not self.mode == "Rest":
					self.collisionEffect(key,platResult[key])
		elif len(ledResult) > 0: #If puffle collides with regular ledges 
			for key in ledResult.keys():
				if not self.mode == "Fight" and not self.mode == "Rest":
					self.collisionEffect(key,ledResult[key])
		elif len(nextResult) > 0: #If puffle bullets hit bossTwo, bossTwo die
			for key in nextResult.keys():
				if not self.mode == "Fight" and not self.mode == "Rest":
					self.hitCounter3 += 1 
					if self.hitCounter3 > 5:
						self.doKill3 = True
		elif len(puffleResult) > 0: #If puffle bullets hit bad puffle,
			for key in puffleResult.keys():
				if not self.mode == "Fight" and not self.mode == "Rest":
					self.hitCounter2 += 1
					if self.hitCounter2 > 5: 
						self.doKill2 = True
		elif len(sameBulletResult) > 0: #If puffle and boss's bullets collide 
			for key in sameBulletResult.keys():
				if self.mode == "Fight":
					self.collisionEffect(key,sameBulletResult[key])
		elif len(killResult) > 0:
			#If puffle hits the Big boss, accelerated death
			for key in killResult.keys():
				if self.mode == "Fight":
					Game.healthPoints -= 20
		elif len(hitResult) > 0: #If puffle hits small boss, accelerated death
			for key in hitResult.keys(): 
				if not self.mode == "AgilityGame" and not self.mode == "Fight"\
					and not self.mode == "Rest":
					Game.healthPoints -= 10
					print("hello")
		elif len(bossTwoResult) > 0: #If puffle collides with boss #2
			for key in bossTwoResult.keys():
				if not self.mode == "AgilityGame" and not self.mode == "Fight"\
					and not self.mode == "Rest":
					Game.healthPoints -= 10 
		elif len(badPuffResult) > 0: #If puffle collides with bad puffle
			for key in badPuffResult.keys():
				if not self.mode == "AgilityGame" and not self.mode == "Fight"\
					and not self.mode == "Rest":
					Game.healthPoints -=10 
		elif len(bossResult) > 0: #If puffle bullets hits big Boss, damage done
			for key in bossResult.keys(): 
				if self.mode == "Fight":
					self.bossPoints -= Game.attack
		else: #Otherwise, the puffle did not collide with anything
			self.Puffles.sprites()[0].topCollide = False
			self.Puffles.sprites()[0].rightCollide = False
			self.Puffles.sprites()[0].leftCollide = False
			self.Puffles.sprites()[0].bottomCollide = False
		for puff in self.Puffles.sprites():
			puff.updateRect(self.turnRight,self.gotHit)

		self.timeCount += 1 

	def collisionEffect(self,key,entry):
		puffle = key 
		platform = entry[0]
		if puffle.x < platform.x - platform.width/2: 
			self.rightCollide = False
		elif puffle.x > platform.x + platform.width/2: 
			self.leftCollide = False
		elif puffle.y > platform.y: 
			puffle.topCollide = True
			self.falling = True
		elif puffle.y < platform.y: 
			puffle.bottomCollide = True

	def gameDraw(self): # "TRAIN MODE"
		if Game.healthPoints > 0:
			self.Background.draw(self.screen)
			for plat in self.Platforms.sprites(): 
				plat.draw(self.screen)
			for land in self.Ledges.sprites(): #Small blue clouds
				land.draw(self.screen)
			self.TokenAttack.draw(self.screen)
			self.TokenDefense.draw(self.screen)
			self.Portal.draw(self.screen)
			
			for boss in self.Boss.sprites():
				boss.draw(self.screen,self.reverse) 
			self.Bullets.draw(self.screen)
			self.MapIcon.draw(self.screen)

			subfont = pygame.font.Font(None,25)
			attack = subfont.render("ATTACK:%d"%Game.attack,1,(255,255,255))
			self.screen.blit(attack,(275,40))
			defense = subfont.render("DEFENSE:%d"%Game.defense,1,(255,255,255))
			self.screen.blit(defense,(275,55))
			agility = subfont.render("AGILITY:%d"%Game.agility,1,(255,255,255))
			self.screen.blit(agility,(275,70))

			self.screen.blit(self.icon,(220,10))
			font = pygame.font.Font(None, 30)
			player = font.render("HP:%d" % Game.healthPoints,1,(178,34,34))
			self.screen.blit(player,(275,20))

			station = font.render("TRAINING:",1,(178,34,34))
			self.screen.blit(station,(570,555))
			attack = font.render("ATTACK",1,(255,255,255))
			self.screen.blit(attack,(680,555))
			defense = font.render("DEFENSE",1,(255,255,255))
			self.screen.blit(defense,(680,576))

			for puff in self.Puffles.sprites(): 
				puff.draw(self.screen,self.turnRight,self.gotHit)

			for badPuff in self.BadPuffleOne.sprites():
				badPuff.draw(self.screen)

			for boss in self.BossTwo.sprites():
				boss.draw(self.screen)

			self.crate = True

		if Game.healthPoints <= 0: #Puffle died 
			self.screen.blit(self.loseScreen,(0,0))
			self.image = pygame.transform.scale(pygame.image.load
												("images/failtraining.png").
				convert_alpha(),(500,40))
			self.image2 = pygame.transform.scale(pygame.image.load
												("images/pufflescared.png").
				convert_alpha(),(150,150))
			self.screen.blit(self.image,(170,200))
			self.screen.blit(self.image2,(330,300))
			self.MapIcon.draw(self.screen)
		
	def attackDraw(self): #This is the splash screen moving to the next stage 
		self.AttackBackground.draw(self.screen)
		self.image = pygame.transform.scale(pygame.image.load
											("images/stageone.png").
				convert_alpha(),(400,40))
		self.screen.blit(self.image,(220,150))

		self.image1 = pygame.transform.scale(pygame.image.load
											 ("images/completed.png").
				convert_alpha(),(400,40))
		self.screen.blit(self.image1,(220,200))
		self.MapIcon.draw(self.screen)

		font = pygame.font.Font(None, 40)
		attack = font.render("ATTACK +1",1,(178,34,34))
		defense = font.render("DEFENSE +1",1,(178,34,34))
		self.screen.blit(attack,(350,300))
		self.screen.blit(defense,(340,340))

		self.screen.blit(self.icon,(220,10))
		font = pygame.font.Font(None, 30)
		player = font.render("HP:%d" % Game.healthPoints,1,(178,34,34))
		self.screen.blit(player,(275,20))
		subfont = pygame.font.Font(None,25)
		attack = subfont.render("ATTACK:%d" % Game.attack,1,(255,255,255))
		self.screen.blit(attack,(275,40))
		defense = subfont.render("DEFENSE:%d" % Game.defense,1,(255,255,255))
		self.screen.blit(defense,(275,55))
		agility = subfont.render("AGILITY:%d" % Game.agility,1,(255,255,255))
		self.screen.blit(agility,(275,70))
		self.nextButton.draw(self.screen)

	def gameTwoDraw(self): #Agility Training Ground
		if Game.healthPoints > 0:
			self.AgilityBackground.draw(self.screen) 
			for plat in self.Platforms.sprites(): 
				plat.draw(self.screen)
			for land in self.Ledges.sprites(): 
				land.draw(self.screen)
			self.Frostbite.draw(self.screen)
		
			self.TokenAgility.draw(self.screen)
			self.Portal.draw(self.screen)
			self.Bullets.draw(self.screen)

			subfont = pygame.font.Font(None,25)
			font = pygame.font.Font(None,30)

			self.MapIcon.draw(self.screen)
			self.screen.blit(self.icon,(220,10))
			if Game.healthPoints >= 80: 
				player = font.render("HP:%d" % Game.healthPoints,1,(61,145,64))
			elif Game.healthPoints >= 40 and Game.healthPoints < 80: 
				player = font.render("HP:%d" % Game.healthPoints,1,(255,255,0))
			elif Game.healthPoints >= 0 and Game.healthPoints < 40: 
				player = font.render("HP:%d" % Game.healthPoints,1,(178,34,34))
			self.screen.blit(player,(275,20))

			subfont = pygame.font.Font(None,25)
			attack = subfont.render("ATTACK:%d" % Game.attack,1,(255,255,255))
			self.screen.blit(attack,(275,40))
			defense = subfont.render("DEFENSE:%d"%Game.defense,1,(255,255,255))
			self.screen.blit(defense,(275,55))
			agility = subfont.render("AGILITY:%d"%Game.agility,1,(255,255,255))
			self.screen.blit(agility,(275,70))
			station = font.render("TRAINING:",1,(178,34,34))
			self.screen.blit(station,(570,575))
			attack = font.render("AGILITY",1,(255,255,255))
			self.screen.blit(attack,(680,576))

			self.crate = True

			for puff in self.Puffles.sprites(): 
				puff.draw(self.screen,self.turnRight,self.gotHit)
			

		if Game.healthPoints <= 0: #Puffle died 
			self.screen.blit(self.loseScreen,(0,0))
			self.image = pygame.transform.scale(pygame.image.load
												("images/failtraining.png").
				convert_alpha(),(500,40))
			self.image2 = pygame.transform.scale(pygame.image.load
												 ("images/pufflescared.png").
				convert_alpha(),(150,150))
			self.screen.blit(self.image,(170,200))
			self.screen.blit(self.image2,(330,300))
			self.MapIcon.draw(self.screen)

	def agilityDraw(self): #This is the splash screen moving to the next stage
		self.AttackBackground.draw(self.screen)
		self.MapIcon.draw(self.screen)
		self.screen.blit(self.icon,(220,10))
		font = pygame.font.Font(None, 30)
		if Game.healthPoints >= 80: 
			player = font.render("HP:%d" % Game.healthPoints,1,(61,145,64))
		elif Game.healthPoints >= 40 and Game.healthPoints < 80: 
			player = font.render("HP:%d" % Game.healthPoints,1,(255,255,0))
		elif Game.healthPoints >= 0 and Game.healthPoints < 40: 
			player = font.render("HP:%d" % Game.healthPoints,1,(178,34,34))
		self.screen.blit(player,(275,20))

		subfont = pygame.font.Font(None,25)
		attack = subfont.render("ATTACK:%d" % Game.attack,1,(255,255,255))
		self.screen.blit(attack,(275,40))
		defense = subfont.render("DEFENSE:%d" % Game.defense,1,(255,255,255))
		self.screen.blit(defense,(275,55))
		agility = subfont.render("AGILITY:%d" % Game.agility,1,(255,255,255))
		self.screen.blit(agility,(275,70))

		self.image1 = pygame.transform.scale(pygame.image.load
											 ("images/completed.png").
				convert_alpha(),(400,40))
		self.screen.blit(self.image1,(220,200))
		self.MapIcon.draw(self.screen)

		self.image = pygame.transform.scale(pygame.image.load
											("images/stagetwo.png").
				convert_alpha(),(400,40))
		self.screen.blit(self.image,(220,150))

		self.image3 = pygame.transform.scale(pygame.image.load
											 ("images/traincomplete.png").
			convert_alpha(),(400,25))
		self.screen.blit(self.image3,(220,350))

		newFont = pygame.font.Font(None, 40)
		attack = newFont.render("AGILITY +1",1,(178,34,34))
		self.screen.blit(attack,(350,300))

	def fightDraw(self): #Draws game elements onto  screen for the "FIGHT" mode
		if Game.healthPoints > 0 and self.bossPoints > 0:
		#Both puffle & boss alive
			self.BattleBackground.draw(self.screen)
			for land in self.FrozenLedges.sprites():
				land.draw(self.screen)
			for plat in self.FrozenPlatforms.sprites():
				plat.draw(self.screen)
			for puff in self.Puffles.sprites(): 
				puff.draw(self.screen,self.turnRight,self.gotHit)
			for save in self.SavePuffles.sprites(): 
				save.draw(self.screen)
			self.MapIcon.draw(self.screen)
			self.Bullets.draw(self.screen)
			self.BossBullets.draw(self.screen)
			self.Cages.draw(self.screen)
			for big in self.BigBoss.sprites():
				big.draw(self.screen,self.reverseBoss)

			#Draws small icons 
			self.screen.blit(self.icon,(220,10))
			self.screen.blit(self.bossIcon,(480,10))

			if self.gotAttack:
				self.screen.blit(self.attackIcon,(750,20))
			if self.gotAgility: 
				self.screen.blit(self.agilityIcon,(750,70))
			if self.gotDefense:
				self.screen.blit(self.defenseIcon,(750,120))

			#Draws HP  
			font = pygame.font.Font(None, 30)

			if Game.healthPoints >= 80: 
				player = font.render("HP:%d" % Game.healthPoints,1,(61,145,64))
			elif Game.healthPoints >= 40 and Game.healthPoints < 80: 
				player = font.render("HP:%d" % Game.healthPoints,1,(255,255,0))
			elif Game.healthPoints >= 0 and Game.healthPoints < 40: 
				player = font.render("HP:%d" % Game.healthPoints,1,(178,34,34))
			self.screen.blit(player,(275,20))

			if self.bossPoints >= 80: 
				enemy = font.render("HP:%d" % self.bossPoints,1,(61,145,64))
			elif self.bossPoints >= 40 and self.bossPoints < 80: 
				enemy = font.render("HP:%d" % self.bossPoints,1,(255,255,0))
			elif self.bossPoints >= 0 and self.bossPoints < 40: 
				enemy = font.render("HP:%d" % self.bossPoints,1,(178,34,34))
			self.screen.blit(enemy,(550,20))

			#Draws puffle stats 
			subfont = pygame.font.Font(None,25)
			attack = subfont.render("ATTACK:%d" % self.attack,1,(74,74,74))
			self.screen.blit(attack,(275,40))
			defense = subfont.render("DEFENSE:%d" % self.defense,1,(74,74,74))
			self.screen.blit(defense,(275,55))
			agility = subfont.render("AGILITY:%d" % self.agility,1,(74,74,74))
			self.screen.blit(agility,(275,70))

			self.Potion.draw(self.screen)
			self.TokenAttack.draw(self.screen)
			self.TokenAgility.draw(self.screen)
			self.TokenDefense.draw(self.screen)

		if Game.healthPoints <= 0: #Puffle died 
			self.screen.blit(self.loseScreen,(0,0))
			self.image = pygame.transform.scale(pygame.image.load
												("images/lostpuffle.png").
				convert_alpha(),(500,40))
			self.image2 = pygame.transform.scale(pygame.image.load
												 ("images/pufflescared.png").
				convert_alpha(),(150,150))
			self.screen.blit(self.image,(170,200))
			self.screen.blit(self.image2,(330,300))
			self.backToMenu.draw(self.screen)

		if self.bossPoints <= 0: #Puffle won! 
			self.screen.blit(self.winScreen,(0,0))
			self.image = pygame.transform.scale(pygame.image.load
												("images/happypufflesave.png").
				convert_alpha(),(150,150))
			self.image2 = pygame.transform.scale(pygame.image.load
												 ("images/bluepufflesave.png").
				convert_alpha(),(150,150))
			self.image3 = pygame.transform.scale(pygame.image.load
												 ("images/yourpuffle.png").
				convert_alpha(),(400,40))
			self.image4 = pygame.transform.scale(pygame.image.load
												 ("images/saveday.png").
				convert_alpha(),(400,40))
			self.image5 = pygame.transform.scale(pygame.image.load
												 ("images/menublue.png").
				convert_alpha(),(80,30))
			self.screen.blit(self.image,(100,200))
			self.screen.blit(self.image2,(250,300))
			self.screen.blit(self.image3,(275,75))
			self.screen.blit(self.image4,(275,125))
			self.backToMenu.draw(self.screen)
			self.screen.blit(self.image5,(25,550))
			
	def restDraw(self): #Draws game elements onto the screen for "REST" mode
		self.igloo.draw(self.screen)
		self.IglooBackground.draw(self.screen)
		self.image5 = pygame.transform.scale(pygame.image.load
											 ("images/armchair.png").
			convert_alpha(),(150,150))
		self.screen.blit(self.image5,(300,250))
		for puff in self.Puffles.sprites(): 
			puff.draw(self.screen,self.turnRight,self.gotHit)
		self.MapIcon.draw(self.screen)
		self.screen.blit(self.icon,(220,10))
		font = pygame.font.Font(None, 30)
		player = font.render("HP:%d" % Game.healthPoints,1,(178,34,34))
		self.screen.blit(player,(275,20))

		subfont = pygame.font.Font(None,25)
		attack = subfont.render("ATTACK:%d" % self.attack,1,(74,74,74))
		self.screen.blit(attack,(275,40))
		defense = subfont.render("DEFENSE:%d" % self.defense,1,(74,74,74))
		self.screen.blit(defense,(275,55))
		agility = subfont.render("AGILITY:%d" % self.agility,1,(74,74,74))
		self.screen.blit(agility,(275,70))
		if self.mode == "Rest" and Game.timer%150 == 0 \
				and Game.healthPoints<=90:
			Game.healthPoints += 5
			font = pygame.font.Font(None,70) 
			rest = font.render("+5",1,(178,34,34))
			if Game.timer%100 < 40: 
				self.screen.blit(rest,(self.Puffles.sprites()[0].x-25,
									   self.Puffles.sprites()[0].y-60))
			
	def run(self):
		clock=pygame.time.Clock()
		playing = True
		while playing:
			self.timerFired()
			for event in pygame.event.get(): #Loops through all events 
				if event.type == pygame.QUIT:
					playing = False
				elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					pos = pygame.mouse.get_pos()
					for maps in self.MapIcon.sprites(): 
						if maps.rect.collidepoint(pos): 
							self.mode = "Map"
							if Game.healthPoints <= 0: Game.healthPoints = 100
							mapGame = Mode(Game.healthPoints,Game.attack,
										   Game.agility,Game.defense)
							pygame.mixer.music.load("bmusic.ogg")
							pygame.mixer.music.play(-1,1.5)
							mapGame.run()
					for menu in self.backToMenu.sprites():
						if menu.rect.collidepoint(pos):
							self.pressBack = True
							self.mode = "Back"
							Game.healthPoints = 100
							Game.attack = 1 
							Game.agility = 3
							Game.defense = 0
							back = Menu(Game.healthPoints,Game.attack,
										Game.agility,Game.defense)
							pygame.mixer.music.load("bmusic.ogg")
							pygame.mixer.music.play(-1,1.5)
							back.run()
					#When you click the token behind the crate 
					for atk in self.TokenAttack.sprites():
						if atk.rect.collidepoint(pos) and self.mode == "Train": 
							Game.attack += 1
							Game.defense += 1 
							self.mode = "AttackSplash" 
							self.Portal.add(Portal(700,25))
					for dnd in self.TokenDefense.sprites():
						if dnd.rect.collidepoint(pos) and self.mode == "Train":
							Game.attack += 1 
							Game.defense += 1 
							self.mode = "AttackSplash" 
							self.Portal.add(Portal(700,25))
					for button in self.nextButton.sprites():
						if button.rect.collidepoint(pos) and \
										self.mode == "AttackSplash":
							self.mode = "AgilityGame"
							self.Puffles.sprites()[0].x = self.puffWidth
							self.Puffles.sprites()[0].y = self.puffHeight
							#Reset position
					for agile in self.TokenAgility.sprites():
						if agile.rect.collidepoint(pos) and \
										self.mode == "AgilityGame":
							Game.agility += 1 
							self.mode = "AgilitySplash"
							self.Portal.add(Portal(700,25))
					for buttonNext in self.nextStage.sprites():
						if buttonNext.rect.collidepoint(pos) and \
										self.mode == "AgilitySplash":
							self.mode = "DefenseGame"
					
				elif event.type == pygame.KEYDOWN: 
					self.keyPressed(event.key)
				elif event.type == pygame.KEYUP: 
					self.keyReleased(event.key)

			self.screen.fill((255,255,255))
			if self.mode == "Train":
				self.gameDraw() #this is game 1, for attack 
			elif self.mode == "Fight": 
				self.fightDraw()
			elif self.mode == "Rest":
				self.restDraw()
			elif self.mode == "AttackSplash":
				self.attackDraw()
			elif self.mode == "AgilityGame":
				self.gameTwoDraw()
			elif self.mode == "AgilitySplash": 
				self.agilityDraw()
			elif self.mode == "DefenseGame":
				self.gameThreeDraw()
			pygame.display.flip()
		pygame.quit()

class Mode(object): #This gives the "map" for player to choose where to go 
	def __init__(self,hp,attack,agility,defense): 
		self.mode = "Map" 
		self.width = 800
		self.height = 600
		self.fps = 50
		self.defense = defense
		self.agility = agility
		self.attack = attack
		self.prevHP = hp 

		pygame.init()
		self.screen = pygame.display.set_mode((self.width,self.height))	

		self.mapBackground = pygame.sprite.Group()
		self.mapBackground.add(mapBackground(400,300))

		self.fightButton = pygame.sprite.Group()
		self.fightButton.add(fightButton(400,200))
		self.pressFight = False

		self.trainButton = pygame.sprite.Group()
		self.trainButton.add(trainButton(400,300))
		self.pressTrain = False

		self.restButton = pygame.sprite.Group()
		self.restButton.add(restButton(400,400))
		self.pressRest = False

		self.backToMenu = pygame.sprite.Group()
		self.backToMenu.add(backToMenu(50,575))
		self.pressBack = False

	def mousePressed(self,key): 
		if self.mode == "Map": mapMousePressed(self,key)
	
	def mapMousePressed(self,key): 
		if self.pressFight: self.mode = "Fight"
		elif self.pressTrain: self.mode = "Train"
		elif self.pressRest: self.mode = "Rest"
		elif self.pressBack: self.mode = "Back"

	def modeRun(self): 
		self.mapBackground.draw(self.screen)
		self.fightButton.draw(self.screen)
		self.trainButton.draw(self.screen)
		self.restButton.draw(self.screen)
		self.backToMenu.draw(self.screen)

	def timerFired(self):
		pass

	def run(self):
		clock=pygame.time.Clock()
		playing = True
		while playing:
			self.timerFired()
			time = clock.tick(self.fps)
			for event in pygame.event.get(): #Loops through all events 
				if event.type == pygame.QUIT: #Quits game if exited 
					playing = False
				elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
					pos = pygame.mouse.get_pos() #gives (x,y)
					for fight in self.fightButton.sprites(): 
						if fight.rect.collidepoint(pos): 
							self.pressFight = True
							self.mode = "Fight"
							fight = Game(self.mode)
							pygame.mixer.music.load("bossmusic.ogg")
							pygame.mixer.music.play(-1,0.0)
							fight.run()
					for train in self.trainButton.sprites():
						if train.rect.collidepoint(pos): 
							self.pressTrain = True 
							self.mode = "Train"
							train = Game(self.mode) #Runs the training ground
							pygame.mixer.music.load("battlemusic.ogg")
							pygame.mixer.music.play(-1,0.0) 
							train.run()	
					for rest in self.restButton.sprites():
						if rest.rect.collidepoint(pos):
							self.pressRest = True
							self.mode = "Rest"
							rest = Game(self.mode)
							pygame.mixer.music.load("restmode.ogg")
							pygame.mixer.music.play(-1,0.0) 
							rest.run()
					for menu in self.backToMenu.sprites():
						if menu.rect.collidepoint(pos):
							self.pressBack = True
							self.mode = "Back"
							Game.attack = 1
							Game.healthPoints = 100
							Game.agility = 3 
							Game.defense = 0 
							back = Menu(Game.healthPoints,Game.attack,
										Game.agility,Game.defense)
							back.run()

			self.screen.fill((255,255,255))
			self.modeRun()
			pygame.display.flip()

		pygame.quit()

class ForwardButton(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super(ForwardButton,self).__init__()
		self.x = x 
		self.y = y 
		self.image = pygame.transform.scale(pygame.image.load
											("images/nextwhite.png").
			convert_alpha(),(80,30))
		self.width,self.height = self.image.get_size()
		self.updateRect() 

	def updateRect(self):
		self.rect = pygame.Rect(self.x-self.width/2,self.y-self.height/2,
								self.width,self.height)

		self.updateRect()
	def updateRect(self):
		self.rect = pygame.Rect(self.x-self.width/2,self.y-self.height/2,
								self.width,self.height)

class Instructions (object): 
	def __init__(self): 
		self.width = 800 
		self.height = 600 
		self.fps = 50 

		pygame.init()
		self.screen = pygame.display.set_mode((self.width,self.height))

		self.instructButton = pygame.sprite.Group()
		self.instructButton.add(instructButton(400,50))

		self.ForwardButton = pygame.sprite.Group()
		self.ForwardButton.add(ForwardButton(750,575))
		self.pressNext = False

		self.menuBackground = pygame.sprite.Group() 
		self.menuBackground.add(menuBackground(350,450))

		self.backToMenu = pygame.sprite.Group()
		self.backToMenu.add(backToMenu(50,575))
		self.pressBack = False

	def timerFired(self): 
		pass

	def instructDraw(self):
		self.menuBackground.draw(self.screen)
		self.backToMenu.draw(self.screen)
		self.instructButton.draw(self.screen)
		self.ForwardButton.draw(self.screen)

		font = pygame.font.Font(None,40)
		one = font.render("Objective: save the puffle!",1,(0,128,128))
		self.screen.blit(one,(100,100))

		two = font.render("- Use arrow keys to move",1,(0,128,128))
		self.screen.blit(two,(375,175))

		three = font.render("- Spacebar to jump",1,(0,128,128))
		self.screen.blit(three,(375,225))

		four = font.render("- Press 'b' to shoot",1,(0,128,128))
		self.screen.blit(four,(375,275))
		self.imageBlue = pygame.transform.scale(pygame.image.load
												("images/bluepufflesad.png").
			convert_alpha(),(70,70))
		self.screen.blit(self.imageBlue,(590,300))
		self.imagePurple = pygame.transform.scale(pygame.image.load
												  ("images/puffleleft.png").
			convert_alpha(),(90,75))
		self.screen.blit(self.imagePurple,(100,300))
		self.imageKeys = pygame.transform.scale(pygame.image.load
												("images/arrow_keys.png").
			convert_alpha(), (150,150))
		self.screen.blit(self.imageKeys,(200,150))

	def run(self):
		clock=pygame.time.Clock()
		playing = True
		while playing:
			self.timerFired()
			time = clock.tick(self.fps)
			for event in pygame.event.get(): #Loops through all events 
				if event.type == pygame.QUIT: #Quits game if exited 
					playing = False
				elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
					pos = pygame.mouse.get_pos() #gives (x,y)
					for menu in self.backToMenu.sprites():
						if menu.rect.collidepoint(pos):
							self.pressBack = True
							self.mode = "Back"
							Game.attack = 1
							Game.healthPoints = 100
							Game.agility = 3 
							Game.defense = 0 
							back = Menu(Game.healthPoints,Game.attack,
										Game.agility,Game.defense)
							back.run()
					for new in self.ForwardButton.sprites():
						if new.rect.collidepoint(pos):
							self.pressNext = True
							self.mode = "Next"
							new = PageTwo()
							new.run()
			self.screen.fill((255,255,255))
			self.instructDraw()
			pygame.display.flip()

		pygame.quit()

class PageTwo(object):
	def __init__(self): 
		self.width = 800 
		self.height = 600 
		self.fps = 50 

		pygame.init()
		self.screen = pygame.display.set_mode((self.width,self.height))

		self.menuBackground = pygame.sprite.Group() 
		self.menuBackground.add(menuBackground(350,450))

		self.instructButton = pygame.sprite.Group()
		self.instructButton.add(instructButton(400,50))

		self.backToMenu = pygame.sprite.Group()
		self.backToMenu.add(backToMenu(50,575))
		self.pressBack = False

		self.ForwardButton = pygame.sprite.Group()
		self.ForwardButton.add(ForwardButton(750,575))
		self.pressNext = False

	def timerFired(self): 
		pass

	def pageTwoDraw(self):
		self.menuBackground.draw(self.screen)
		self.backToMenu.draw(self.screen)
		self.instructButton.draw(self.screen)
		self.ForwardButton.draw(self.screen)

		font = pygame.font.Font(None,40)
		one = font.render("1. Fight Mode: Battle against the boss",1,
						  (0,128,128))
		self.screen.blit(one,(100,100))

		three = font.render("- Kill boss with puffle snowballs",1,(0,128,128))
		self.screen.blit(three,(150,150))

		four = font.render("- Obtain temporary powerups to boost stats",1,
						   (0,128,128))
		self.screen.blit(four,(150,200))

		five = font.render("- Jump on ledges to reach boss",1,(0,128,128))
		self.screen.blit(five,(150,250))

		self.imageArrow = pygame.transform.scale(pygame.image.load
												 ("images/arrow.png").
			convert_alpha(),(75,75))
		self.screen.blit(self.imageArrow,(50,400))

		self.imageBoss = pygame.transform.scale(pygame.image.load
												("images/boss.png").
			convert_alpha(),(150,150))
		self.screen.blit(self.imageBoss,(50,250))
		two = font.render("BOSS",1,(255,99,71))
		self.screen.blit(two,(45,475))

		self.imageBullet = pygame.transform.scale(pygame.image.load
												  ("images/attackball.png").
			convert_alpha(),(30,30))
		self.screen.blit(self.imageBullet,(225,300))

		self.imageLedge = pygame.transform.scale(pygame.image.load
												 ("images/frozenledge.png").
			convert_alpha(), (190,110))
		self.screen.blit(self.imageLedge,(250,450))

		self.screen.blit(self.imageArrow,(180,490))
		six = font.render("LEDGES",1,(255,99,71))
		self.screen.blit(six,(125,560))

		self.powerImage1 = pygame.transform.scale(pygame.image.load
												  ("images/token1.png").
			convert_alpha(),(30,30))
		self.screen.blit(self.powerImage1,(500,400))

		seven = font.render("ATTACK +1",1,(0,128,128))
		self.screen.blit(seven,(550,400))

		self.powerImage2 = pygame.transform.scale(pygame.image.load
												  ("images/token2.png").
			convert_alpha(),(30,30))
		self.screen.blit(self.powerImage2,(500,450))

		eight = font.render("AGILITY +1",1,(0,128,128))
		self.screen.blit(eight,(550,450))

		self.powerImage3 = pygame.transform.scale(pygame.image.load
												  ("images/token3.png").
			convert_alpha(),(30,30))
		self.screen.blit(self.powerImage3,(500,500))
		nine = font.render("DEFENSE +1",1,(0,128,128))
		self.screen.blit(nine,(550,500))

		self.potionImage = pygame.transform.scale(pygame.image.load
												  ("images/potion.png").
			convert_alpha(),(30,35))
		self.screen.blit(self.potionImage,(500,350))
		ten = font.render("POTION HP +10",1,(0,128,128))
		self.screen.blit(ten,(550,350))

		eleven = font.render("- Watch your HP!",1,(0,128,128))
		self.screen.blit(eleven,(300,300))

	def run(self):
		clock=pygame.time.Clock()
		playing = True
		while playing:
			self.timerFired()
			time = clock.tick(self.fps)
			for event in pygame.event.get(): #Loops through all events 
				if event.type == pygame.QUIT: #Quits game if exited 
					playing = False
				elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
					pos = pygame.mouse.get_pos() #gives (x,y)
					for menu in self.backToMenu.sprites():
						if menu.rect.collidepoint(pos):
							self.pressBack = True
							self.mode = "Back"
							Game.attack = 1
							Game.healthPoints = 100
							Game.agility = 3 
							Game.defense = 0 
							back = Menu(Game.healthPoints,Game.attack,
										Game.agility,Game.defense)
							back.run()
					for new in self.ForwardButton.sprites():
						if new.rect.collidepoint(pos):
							self.pressNext = True
							self.mode = "Next"
							new = PageThree()
							new.run()
			self.screen.fill((255,255,255))
			self.pageTwoDraw()
			pygame.display.flip()

		pygame.quit()

class PageThree(object):
	def __init__(self):
		self.width = 800 
		self.height = 600 
		self.fps = 50 
		pygame.init() 

		self.screen = pygame.display.set_mode((self.width,self.height))
		self.menuBackground = pygame.sprite.Group() 
		self.menuBackground.add(menuBackground(350,450))

		self.instructButton = pygame.sprite.Group()
		self.instructButton.add(instructButton(400,50))

		self.backToMenu = pygame.sprite.Group()
		self.backToMenu.add(backToMenu(50,575))
		self.pressBack = False

		self.ForwardButton = pygame.sprite.Group()
		self.ForwardButton.add(ForwardButton(750,575))
		self.pressNext = False

	def timerFired(self): 
		pass

	def pageThreeDraw(self):
		self.menuBackground.draw(self.screen)
		self.backToMenu.draw(self.screen)
		self.instructButton.draw(self.screen)
		self.ForwardButton.draw(self.screen)

		font = pygame.font.Font(None,40)
		one = font.render\
			("1. Training Mode: Train to increase stats permanently",
			 1,(0,128,128))
		self.screen.blit(one,(50,100))
		two = font.render("- Press 'b' to shoot & kill training bosses",
						  1,(0,128,128))
		self.screen.blit(two,(100,150))
		three = font.render("- Jump on ledges to reach crate",1,(0,128,128))
		self.screen.blit(three,(100,200))
		four = font.render("- Attack crate to obtain tokens for next stage",1,
						   (0,128,128))
		self.screen.blit(four,(100,250))
		five = font.render("- Stage 1: Attack & Defense",1,(0,128,128))
		self.screen.blit(five,(100,300))
		six = font.render("- Stage 2: Agility",1,(0,128,128))
		self.screen.blit(six,(100,350))
		seven = font.render(" - Avoid the frostbite!",1,(0,128,128))
		self.screen.blit(seven,(150,400))

		self.image1 = pygame.transform.scale(pygame.image.load
											 ("images/frostbite.png").
			convert_alpha(),(30,33))
		self.screen.blit(self.image1,(450,390))

	def run(self):
		clock=pygame.time.Clock()
		playing = True
		while playing:
			self.timerFired()
			time = clock.tick(self.fps)
			for event in pygame.event.get(): #Loops through all events 
				if event.type == pygame.QUIT: #Quits game if exited 
					playing = False
				elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
					pos = pygame.mouse.get_pos() #gives (x,y)
					for menu in self.backToMenu.sprites():
						if menu.rect.collidepoint(pos):
							self.pressBack = True
							self.mode = "Back"
							Game.attack = 1
							Game.healthPoints = 100
							Game.agility = 3 
							Game.defense = 0 
							back = Menu(Game.healthPoints,Game.attack,
										Game.agility,Game.defense)
							back.run()
					for new in self.ForwardButton.sprites():
						if new.rect.collidepoint(pos):
							self.pressNext = True
							self.mode = "Next"
							new = PageFour()
							new.run()
			self.screen.fill((255,255,255))
			self.pageThreeDraw()
			pygame.display.flip()
		pygame.quit()

class PageFour(object):
	def __init__(self): 
		self.width = 800 
		self.height = 600 
		self.fps = 50 

		pygame.init() 
		self.screen = pygame.display.set_mode((self.width,self.height))
		self.menuBackground = pygame.sprite.Group() 
		self.menuBackground.add(menuBackground(350,450))

		self.instructButton = pygame.sprite.Group()
		self.instructButton.add(instructButton(400,50))

		self.backToMenu = pygame.sprite.Group()
		self.backToMenu.add(backToMenu(50,575))
		self.pressBack = False

		self.ForwardButton = pygame.sprite.Group()
		self.ForwardButton.add(ForwardButton(750,575))
		self.pressNext = False

	def timerFired(self): 
		pass

	def pageFourDraw(self):
		self.menuBackground.draw(self.screen)
		self.backToMenu.draw(self.screen)
		self.instructButton.draw(self.screen)

		font = pygame.font.Font(None,40)
		one = font.render("1. Rest Mode: Puffle's home",1,(0,128,128))
		self.screen.blit(one,(100,100))

		two = font.render("- Take a break and restore HP",1,(0,128,128))
		self.screen.blit(two,(150,150))

		three = font.render("- Increases +5 HP every couple of seconds",1,
							(0,128,128))
		self.screen.blit(three,(150,200))


	def run(self):
		clock=pygame.time.Clock()
		playing = True
		while playing:
			self.timerFired()
			time = clock.tick(self.fps)
			for event in pygame.event.get(): #Loops through all events 
				if event.type == pygame.QUIT: #Quits game if exited 
					playing = False
				elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
					pos = pygame.mouse.get_pos() #gives (x,y)
					for menu in self.backToMenu.sprites():
						if menu.rect.collidepoint(pos):
							self.pressBack = True
							self.mode = "Back"
							Game.attack = 1
							Game.healthPoints = 100
							Game.agility = 3 
							Game.defense = 0 
							back = Menu(Game.healthPoints,Game.attack,
										Game.agility,Game.defense)
							back.run()
			self.screen.fill((255,255,255))
			self.pageFourDraw()
			pygame.display.flip()
		pygame.quit()

class Menu(object): 
	def __init__(self,hp,attack,agility,defense): 
		self.width = 800 
		self.height = 600 
		self.fps = 50 
		self.attack = attack
		self.agility = agility
		self.defense = defense
		self.newHP = hp 
		self.mode = "Menu"

		pygame.init() 

		self.screen = pygame.display.set_mode((self.width,self.height))

		self.redPuffle = pygame.sprite.Group()
		self.redPuffle.add(redPuffle(600,400))

		self.greenPuffle = pygame.sprite.Group()
		self.greenPuffle.add(greenPuffle(170,350))

		self.titleLogo = pygame.sprite.Group()
		self.titleLogo.add(titleLogo(400,100))

		self.menuBackground = pygame.sprite.Group() 
		self.menuBackground.add(menuBackground(350,450))

		self.playButton = pygame.sprite.Group()
		self.playButton.add(playButton(400,250))
		self.pressPlay = False

		self.instructButton = pygame.sprite.Group() 
		self.instructButton.add(instructButton(400,350))
		self.pressInstruct = False

	def mousePressed(self,key):
		if self.mode == "Menu": menuMousePressed(self,key)

	def timerFired(self): 
		pass

	def menuMousePressed(self,key):
		if self.pressPlay: self.mode == "Play"
		elif self.pressInstruct: self.mode = "Instruct" 

	def menuRun(self):
		self.titleLogo.draw(self.screen)
		self.menuBackground.draw(self.screen)
		self.playButton.draw(self.screen)
		self.instructButton.draw(self.screen)
		self.redPuffle.draw(self.screen)
		self.greenPuffle.draw(self.screen)

	def run(self):
		clock=pygame.time.Clock()
		playing = True
		pygame.mixer.music.load("bmusic.ogg")
		pygame.mixer.music.play(-1,1.5)
		while playing:
			self.timerFired()
			time = clock.tick(self.fps)
			for event in pygame.event.get(): #Loops through all events 
				if event.type == pygame.QUIT: #Quits game if exited 
					playing = False
				elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
					pos = pygame.mouse.get_pos() #gives (x,y)
					for play in self.playButton.sprites(): 
						if play.rect.collidepoint(pos): 
							self.pressPlay = True
							self.mode = "Play"
							play = Mode(Game.healthPoints,Game.attack,
										Game.agility,Game.defense)
							play.run()
					for instruct in self.instructButton.sprites():
						if instruct.rect.collidepoint(pos): 
							self.pressInstruct = True 
							self.mode = "Instruct"
							instruct = Instructions()
							instruct.run()
			self.screen.fill((255,255,255))
			self.menuRun()
			pygame.display.flip()
		pygame.quit()

game1 = Menu(Game.healthPoints,Game.attack,Game.agility,Game.defense)
#Starts with mode right now
game1.run()

"""
Citations (media files)

Font taken from: 
	http://fontmeme.com/club-penguin-font/
Penguin cutouts, background, and puffles taken from: 
	http://cutoutcp.blogspot.com/p/blog-page_21.html
	http://cpcutout.blogspot.co.uk/p/penguins.html
	http://yourclubpenguincutouts.blogspot.com/p/beta-page.html
Club penguin map taken from: 
	https://mrzero3cp.files.wordpress.com/2015/03/screen-shot-2015-03-26-at
	-9-37-30-pm.png
Music credits:
	Music by Sophonic Media, http://instrumentalsfree.com
Start mode background music: 
	https://www.youtube.com/watch?v=nRy0W3jpk7Q
Arrow key image taken from: 
	http://www.stereomaster.net/Images/arrow_keys.gif
	http://i.stack.imgur.com/M8X6e.png
Potion image taken from: 
	http://es.clubpenguin.wikia.com/wiki/Archivo:409px-Medieval_2013_Potions
	_The_Vanishing.png
Various accessory images taken from: 
	http://clubpenguin.wikia.com/wiki/Category:Furniture
Map icon taken from: 
	http://www.clubpenguinwiki.info/static/images/www/thumb/1/16/Map.PNG/
	300px-Map.PNG
"""
