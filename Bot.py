import socket 

def commands(nick,channel,message):
   if message.find(botnick+': shellium')!=-1:
      ircsock.send('PRIVMSG %s :%s: Shellium is awesome!\r\n' % (channel,nick))
   elif message.find(botnick+': help')!=-1:
      ircsock.send('PRIVMSG %s :%s: My other command is shellium.\r\n' % (channel,nick))

       
server = "irc.freenode.net" # Server
channel = "#mifos" # Channel
botnick = "iBot" # Your bots nick


def ping(): 
  ircsock.send("PONG :pingis\n")  

def sendmsg(chan , msg):
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n") 

def joinchan(chan): 
  ircsock.send("JOIN "+ chan +"\n")

def hello(): 
  ircsock.send("PRIVMSG "+ channel +" :Hello!\n")
                  
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) 
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :I am a bot made by Vipul.\n") # user authentication
ircsock.send("NICK "+ botnick +"\n") 

joinchan(channel

while 1: 
  ircmsg = ircsock.recv(2048) 
  ircmsg = ircmsg.strip('\n\r')
  print(ircmsg) 
  if ircmsg.find(' PRIVMSG ')!=-1:
     nick=ircmsg.split('!')[0][1:]
     channel=ircmsg.split(' PRIVMSG ')[-1].split(' :')[0]
     commands(nick,channel,ircmsg)
  if ircmsg.find(":Hello "+ botnick) != -1: 
    hello()

  if ircmsg.find("PING :") != -1: 
    ping()
