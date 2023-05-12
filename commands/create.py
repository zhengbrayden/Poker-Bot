from commands.header import *

#args = name of lobby
async def create(message, args, Channels):
    channel = lib.get_channel(message, Channels)
    
    if not channel:
        channel_id = message.channel.id
        Channels[channel_id] = Channel(channel_id)
        channel = Channels[channel_id]

    if not len(args):
        await lib.ping_msg(message, 'This command requires an argument!')
        return

    name = ' '.join(args)
    
    member_id = message.author.id
    flag = channel.create_lobby(name, member_id)

    if flag == 0:
        await lib.ping_msg(message, 'A lobby called \'' + name + '\'  already exists.')
    elif flag == 1:
        await lib.ping_msg(message, "You cannot create a lobby when you already in lobby '" + lib.get_lobby_name_by_id(channel, member_id) + "'.")
    else:
        await lib.ping_msg(message, 'Lobby with name \'' + name + '\' has been successfuly created.')
    


