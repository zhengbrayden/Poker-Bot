import discord
from commands import * 
import lib
import os.path

client = discord.Client(intents=discord.Intents.all())
#contains channel objects with Lobbies and Players attributes.
Channels = {}
cmds = {'call', 'join', 'create', 'fold', 'info', 'ping', 'start', 'raise', 'leave'} #set of all possible commands
@client.event
async def on_ready():
    print("Poker is the greatest!")

@client.event
async def on_message(message):
    if (message.author == client.user) or (not message.content.startswith('-')) or message.author.bot or not message.guild:
        return
    else:
        args = message.content.split()
        cmd = args[0][1:]
        args.pop(0)

        if cmd not in cmds:
            #we dont want to do anything if not a cmd.
            return
        
        if cmd == "ping":
            await ping(message, Channels)
        elif cmd == 'info':
            #display info about a lobby or a channel (if no args given)
            await info(message, client, args, Channels)
        elif cmd == 'create':
            await create(message, args, Channels)
        else:
            
            #check if channel is valid for poker
            channel = lib.get_channel(message, Channels)
            
            if not channel:
                await lib.ping_msg(message, 'unfortunately, THIS CHANNEL HAS NO POKER LOBBIES')
                return

            if cmd == 'join':
                await enter(message, args, channel)
            else:
                #check if user is a player
                player = channel.get_player(message.author.id)

                if not player:
                    await lib.ping_msg(message, 'unfortunately, you are not in a lobby.')
                    return

                if cmd == 'leave':
                    await leave(client, message, player, channel, Channels)
                elif cmd == 'start':
                    await start(client, message, player)
                elif cmd == 'call': 
                    await call(client, message, player)
                elif cmd == 'raise': 
                    await raise_(client, message, args, player)
                elif cmd == 'fold': 
                    await fold(client, message, player)

assert os.path.isfile('token.txt'), "must define a token inside of token.txt file"
with open('token.txt', 'r') as f:
    token = f.read()

client.run(token)
