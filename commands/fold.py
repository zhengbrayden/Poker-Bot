from commands.header import *

#need to keep track of folded players
async def fold(client, message, player):
    lobby = player.get_lobby()
    res = lobby.fold_player(player)
    fold_res = lib.get_folded_content(res, client, lobby, True)
    content = fold_res[0]
    embed = fold_res[1]
    await lib.ping_msg(message, "".join(content), embed) 