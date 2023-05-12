from commands.header import *

async def leave(client, message, player, channel, Channels):
    lobby=player.get_lobby()
    old_leader=lobby.get_leader()
    res=channel.delete_player(player)
    flag=res[0]
    content= []
    embed = None
    
    if flag == 3:
        content.append('You have left the lobby \'' + lobby.get_name()  + '\' and will be folded on your turn.')
    else:
        content.append('You have left the lobby \'' + lobby.get_name()  + '\'.')

        if flag == 1:
            content.append("The lobby is empty and has been deleted.")

            if res[1]:
                del Channels[channel.get_id()]
                
        elif flag == 2:
            res = res[1]
            fold_res = lib.get_folded_content(res, client, lobby, True)
            content += fold_res[0]
            embed = fold_res[1]

    if lobby.get_leader() != old_leader:
        content.append("'" + client.get_user(lobby.get_leader()).name + "' has inherited lobby leadership.")

    await lib.ping_msg(message, " ".join(content), embed)
