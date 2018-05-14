#! /usr/bin/python
#author: Noah Tyler
#Curse Chat Bot v1.0

#---------------------------------------------Libraries-----------------------------------------------#

import discord
import ast
import asyncio
import random
import os
import re
import time
import random
import sys
import ast
import operator

#---------------------------------------------Globals-------------------------------------------------#

client = discord.Client()
vServer = discord.Server(id='329432484280270850')
vBotId = 'Curse Chat Bot#8700'

vModRoles = [
	'Lords of Chochi',    #0
	'Knights of Chochi',  #1
	'The King in the Raj' #2    list of mod roles in the server. (who can control the bot)
	]					  
vChatEmojis = [
	':ok_hand:',        #0
	':joy:',            #1
	':thumbsup:',       #2			list of emoji codes to use in the chat
	':punch:',          #3
	':headphones:',     #4
	':fire:',           #5
	':hammer:',	    	#6
	':thinking:',       #7
	':no_entry_sign:',  #8
	':v:'				#9
	]
operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,	#operator set used in calc class
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Invert: operator.neg,
    ast.Mod: operator.mod
    }
#-------------------------------------------Classes-------------------------------------------------------------#
class Calc(ast.NodeVisitor):	#calc class from ast lib, parses a string and calculates it.

    def visit_BinOp(self, node):
         left = self.visit(node.left)
         right = self.visit(node.right)
         return operators[type(node.op)](left, right)

    def visit_Num(self, node):
         return node.n

    def visit_Expr(self, node):
         return self.visit(node.value)

    @classmethod
    def evaluate(cls, expression):
         tree = ast.parse(expression)
         calc = cls()
         return calc.visit(tree.body[0])

#-------------------------------------------Functions--------------------------------------------------------------#

async def joinVoiceChannel(id): #function to join a voice channel
	 channel = client.get_channel(id)
	 await client.join_voice_channel(channel)

#--------------------------------------------On Client Events------------------------------------------------------------#

@client.event
async def on_ready():
	 print('Logged in as')
	 print(client.user.name)
	 print(client.user.id)
	 print('------')
	 await joinVoiceChannel('330522768942563329')

#--------------------------------------------Channel Events------------------------------------------------------------#

@client.event
async def on_channel_update(before, after): #on client event - channel update
	 announcementCH = client.get_channel('329432484280270850')
	 if(before.name != after.name and before.topic != before.topic):
	 	await client.send_message(announcementCH,'The channel '+str(before.name)+' has been renamed to '+str(after.name))
	 	await client.send_message(announcementCH,'The channel '+str(after.name)+'\'s topic has also been changed to '+str(after.topic))
	 elif(before.name != after.name):
	 	await client.send_message(announcementCH,'The channel '+str(before.name)+' has been renamed '+str(after.name))
	 elif(before.topic != before.topic):
	 	await client.send_message(announcementCH,'The channel '+str(after.name)+'\'s topic has been changed to '+str(after.topic))

@client.event
async def on_channel_delete(channel): #on client event - channel delete
	 announcementCH = client.get_channel('329432484280270850')
	 await client.send_message(announcementCH,'The channel'+channel.name+'has been deleted!')

@client.event
async def on_channel_create(channel): #on client event - channel create
	 announcementCH = client.get_channel('329432484280270850') 
	 await client.send_message(announcementCH,'The channel \''+channel.name+'\' has been created!')

#--------------------------------------------Member Events----------------------------------------------------------#

@client.event
async def on_member_join(member): #on client event - member join
	 msg = member.name + " has joined the server! Welcome to " + member.server.name
	 await client.send_message(member.server, msg)

@client.event
async def on_member_remove(member): #on client event - member remove
	 announcementCH = client.get_channel('329432484280270850')	
	 msg = member.name + " has left the server!"
	 await client.send_message(announcementCH, msg)

@client.event
async def on_member_update(before, after): #on client event - member update
	 announcementCH = client.get_channel('329432484280270850')
	 if(before.nick != after.nick):
	 	await client.send_message(announcementCH,''+before.nick+' has changed his name to '+after.nick)
	 elif(before.roles != after.roles):
	 	await client.send_message(announcementCH,''+before.nickname+' roles have been updated to '+after.roles) 

#--------------------------------------------Server Events-------------------------------------------------------------------#

@client.event
async def on_server_update(before, after):#on client event - server update
	 announcementCH = client.get_channel('329432484280270850')
	 if(before.name != after.name):
	 	await client.send_message(announcementCH,'The server\'s name has been changed to '+after.name)

@client.event
async def on_server_role_delete(role):#on client event - server role delete
	 announcementCH = client.get_channel('329432484280270850')
	 await client.send_message(announcementCH,'The role '+role.name+' has been deleted') 

@client.event
async def on_server_role_update(before, after):#on client event - server role update
	 announcementCH = client.get_channel('329432484280270850')
	 if(before.name == 'new role' and before.name != after.name):
	 	 await client.send_message(announcementCH,'The role \''+after.name+'\' has been created.')
	 if(before.name != after.name and before.colour != before.colour):
	 	await client.send_message(announcementCH,'The role '+before.name+'\'s name has been updated to '+after.name)
	 	await client.send_message(announcementCH,'The role '+before.name+'\'s color has also been updated to '+after.colour)
	 elif(before.name != after.name):
	 	await client.send_message(announcementCH,'The role '+before.name+'\'s name has been updated to '+after.name)
	 elif(before.colour != before.colour):
	 	await client.send_message(announcementCH,'The role '+before.name+'\'s color has been updated to '+after.colour)

#---------------------------------------------Message Event----------------------------------------------------------------#

@client.event
async def on_message(message): #on client event - on message
	 strMessageAuthor = str(message.author)
	 messageInLowerCase = message.content.lower()

	 if (messageInLowerCase.startswith('!coms') or message.content.lower().startswith('!help')) and strMessageAuthor != vBotId: #help command
	 	 await client.send_message(message.channel, 'LIST OF COMMANDS\n'
												'-----------------\n'
											'!online - See who is online.\n'
											'!random - Pick a random user.\n'
											'!ban - Ban a user from the server. (MOD only)\n'
											'!unban - Unban a user from the server. (MOD only, must include #???? in the name)\n'
											'!joinvoice - Send me to a voice channel. (need channel id)\n'
											'!kick - Kick a user from the server. (MOD only)\n'
											'!song - I\'ll hit you with a fire song.\n'
											'!addsong - add a song to my playlist. (youtube link)\n'
											'!calc - calculate an equation, supported operators = +, /, -, *, %'
								  			)

	 elif (messageInLowerCase.startswith('!owner') or message.content.lower().startswith('!creator')) and strMessageAuthor != vBotId: #Command to see the owner
 	 	 await client.send_message(message.channel, 'I was created by Mullets in his mom\'s basement. '+vChatEmojis[2])

	 elif messageInLowerCase.startswith('!test') and strMessageAuthor != vBotId: #test command 
	 	 await client.send_message(message.channel, 'Running... no need to worry. '+vChatEmojis[2])

	 elif messageInLowerCase.startswith('!hello') and strMessageAuthor != vBotId: #command to say hello
	 	 reply = 'Hello '+(str(message.author)[:-5])+'!'
	 	 await client.send_message(message.channel, reply)

	 elif messageInLowerCase.startswith('!random') and strMessageAuthor != vBotId: #Command to pick a random user
	 	 members = message.server.members
	 	 memberNames = []

	 	 for member in members:
	 	 	 memberNames.insert(cnt,member.name)

	 	 await client.send_message(message.channel, random.choice(memberNames))

	 elif messageInLowerCase.startswith('!ban') and strMessageAuthor != vBotId and str(message.author.top_role) in vModRoles: #command to ban
 	 	 userName = message.content[5:]
 	 	 try:
 	 	 	 await client.ban(message.server.get_member_named(userName), delete_message_days=6)
 	 	 	 await client.send_message(message.channel, ''+userName+' got hit with the ban hammer!'+vChatEmojis[6])
 	 	 except Exception:
 	 	 	 await client.send_message(message.channel, 'Was unable to ban '+userName+'!')
 
	 elif messageInLowerCase.startswith('!unban') and strMessageAuthor != vBotId and str(message.author.top_role) in vModRoles: #command to unban
	 	 userName = stmessage.content[7:]
	 	 for user in await client.get_bans(server):
		 	 if userName == str(user):		
		 	 	try:
		 	 		 await client.unban(message.server, user)
		 	 		 await client.send_message(message.channel, ''+userName+' was blessed by the gods and given another chance! ')
		 	 	except Exception:
		 	 		 await client.send_message(message.channel, 'Was unable to unban '+userName+'! '+vChatEmojis[7])
	 		 else:
	 		 	 await client.send_message(message.channel, ''+userName+' is not banned.')

	 elif messageInLowerCase.startswith('!online') and strMessageAuthor != vBotId: #command to see online members 
	 	 members = message.server.members
	 	 memberNames = []
	 	 cnt = 0
	 
	 	 for member in members:
	 	 	 if str(member.status) == 'online': 
	 		 	 memberNames.insert(cnt,member.name)
	 		 	 cnt += 1

	 	 await client.send_message(message.channel,'Members online ('+str(cnt)+' online):\n'+"\n".join(memberNames))

	 elif messageInLowerCase.startswith('!joinvoice') and strMessageAuthor != vBotId: #command to join a voice channel 
	 	 channelID = message.author.voice_channel.id
	 	 channel = client.get_channel(channelID)
	 	 await client.move_member(message.server.get_member_named(vBotId), channel)
	 	 await client.send_message(message.channel, 'Joining the '+channel.name+' voice channel...')

	 elif messageInLowerCase.startswith('!kick') and strMessageAuthor != vBotId and str(message.author.top_role) in vModRoles: #command to kick
	 	 if strMessageAuthor not in mods:
	 	 	 await client.send_message(message.channel, 'You do not have the authority. '+vChatEmojis[8])
	 	 else: 
	 	 	 userName = message.content[6:]
	 	 	 try:
	 	 	 	 await client.kick(message.server.get_member_named(userName))
	 	 	 	 await client.send_message(message.channel, ''+userName+' got kicked! '+vChatEmojis[10])
	 	 	 except Exception:
	 	 	 	 await client.send_message(message.channel, 'Was unable to kick '+userName+'! '+vChatEmojis[7])

	 elif messageInLowerCase.startswith('!song') and strMessageAuthor != vBotId: #command for random song
	 	 songs = open('songs.txt','r')
	 	 songlist = songs.readlines()
	 	 songs.close()
	 	 await client.send_message(message.channel, 'This shit bumps!!!\n'+random.choice(songlist))

	 elif messageInLowerCase.startswith('!addsong') and strMessageAuthor != vBotId: #command to addsong
 	 	 songlink = message.content[9:]
 	 	 if 'www.youtube.com' not in songlink:
 	 	 	 await client.send_message(message.channel, 'I only take youtube links. '+vChatEmojis[8])
 	 	 else:
 	 	 	 songs = open("songs.txt", "a")
 	 	 	 songs.write('\n'+songlink)
 	 	 	 songs.close()
 	 	 	 await client.send_message(message.channel, 'That\'s some super hot fire! Song has been added. '+vChatEmojis[4]+' '+vChatEmojis[5])

	 elif messageInLowerCase.startswith('!calc') and strMessageAuthor != vBotId: #command to calculate string
	 	 equation =  message.content[6:]
	 	 try:
	 	 	 await client.send_message(message.channel, 'The answer is '+str(Calc.evaluate(equation)))
	 	 except Exception:
	 	 	 await client.send_message(message.channel, 'I could not calculate '+equation+'! '+vChatEmojis[7])

client.run('MzMyMzM4MzMyODk1OTM2NTIy.DEBBdw.SbkiFNTXc3mcnSSUIdPCbuLs9Qc')