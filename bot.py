import socket 

def commands(nick,channel,message):
   if message.find(botnick+': how are you!')!=-1:
      ircsock.send('PRIVMSG %s :%s: I am awesome!... How about you?\r\n' % (channel,nick))
   elif message.find(botnick+': show commands!')!=-1:
      ircsock.send('PRIVMSG %s :%s: https://github.com/vipulroxx/iBot/blob/master/Commands\r\n' % (channel,nick))
   elif message.find(botnick+': shut up!')!=-1:
      ircsock.send('PRIVMSG %s :%s: nah!!\r\n' % (channel,nick))
   elif message.find(botnick+': thank you!')!=-1:
      ircsock.send('PRIVMSG %s :%s: I am yours!\r\n' % (channel,nick))
   elif message.find(botnick+': thanks!')!=-1:
      ircsock.send('PRIVMSG %s :%s: I am yours!\r\n' % (channel,nick))
   elif message.find(botnick+': thnx')!=-1:
      ircsock.send('PRIVMSG %s :%s: I am yours!\r\n' % (channel,nick))
   elif message.find(botnick+': thnx!')!=-1:
      ircsock.send('PRIVMSG %s :%s: I am yours!\r\n' % (channel,nick))
   elif message.find(botnick+': ty!')!=-1:
      ircsock.send('PRIVMSG %s :%s: I am yours!\r\n' % (channel,nick))
   elif message.find(botnick+': thanks')!=-1:
      ircsock.send('PRIVMSG %s :%s: I am yours!\r\n' % (channel,nick))
   elif message.find(botnick+': I love you!')!=-1:
      ircsock.send('PRIVMSG %s :%s: Ahh...You guys are full of emotions... But I love you too!\r\n' % (channel,nick))
   elif message.find(botnick+': I luv u!')!=-1:
      ircsock.send('PRIVMSG %s :%s: nah!!\r\n' % (channel,nick))
   elif message.find(botnick+': I owe u!')!=-1:
      ircsock.send('PRIVMSG %s :%s: I know...but I will not ask for anything!\r\n' % (channel,nick))
   elif message.find(botnick+': you rock!')!=-1:
      ircsock.send('PRIVMSG %s :%s: I know.. :)\r\n' % (channel,nick))
   elif message.find(botnick+': where are you!')!=-1:
      ircsock.send('PRIVMSG %s :%s: I am here.. Cant you see me!!' % (channel,nick))
   elif message.find(botnick+': fuck you!')!=-1:
      ircsock.send('PRIVMSG %s :%s: Same to you, Dude :)\r\n' % (channel,nick))
   elif message.find(botnick+': Merry Christmas!')!=-1:
      ircsock.send('PRIVMSG %s :%s: Same to you, Dude :)\r\n' % (channel,nick))
   elif message.find(botnick+': hi!')!=-1:
      ircsock.send('PRIVMSG %s :%s: Hello!\r\n' % (channel,nick))
   elif message.find(botnick+': hey!')!=-1:
      ircsock.send('PRIVMSG %s :%s: Hello!\r\n' % (channel,nick))
   elif message.find(botnick+': bye!')!=-1:
      ircsock.send('PRIVMSG %s :%s: Good Bye, Dude :)\r\n' % (channel,nick))
   elif message.find(botnick+': profile!')!=-1:
      ircsock.send('PRIVMSG %s :%s: I am a bot made by Vipul Sharma. He is still making me (https://github.com/vipulroxx/iBot) . Help me please !!\r\n' % (channel,nick))

      
       
server = "irc.freenode.net" # Server
channel = "#jklmn" # Channel
botnick = "i_bot_" # Your bots nick


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
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :I am a bot made by Vipul Sharma.\n") 
ircsock.send("NICK "+ botnick +"\n")

joinchan(channel) 

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
