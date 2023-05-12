from commands.header import *

#args = name of lobby
async def enter(message, args, channel):

    if not len(args):
        await lib.ping_msg(message, 'This command requires an argument!')
        return

    name = ' '.join(args)
    flag = channel.create_player(name, message.author.id)

    if flag == 0:
        await lib.ping_msg(message, 'A lobby called \'' + name + '\' does not exist.')
    elif flag == 1:
        await lib.ping_msg(message, 'You cannot join a lobby when you are already in lobby \'' + lib.get_lobby_name_by_id(channel, message.author.id) + '\'.')
    elif flag == 2:
        await lib.ping_msg(message, 'The game of lobby \'' + name + '\' has already started.')
    else:
        await lib.ping_msg(message, "You have joined \'" + name + '\'.')