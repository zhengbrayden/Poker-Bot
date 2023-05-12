from commands.header import *

#need to keep track of folded players
async def call(client, message, player):
    lobby = player.get_lobby()
    res = lobby.call_player(player)
    flag = res[0]

    if flag == 0:
        await lib.ping_msg(message, f"Cannot call as the lobby '{lobby.get_name()}' has not started")
    elif flag == 1:
        await lib.ping_msg(message, f"Cannot call as it is not your turn!")
    elif flag == 2:
        bet_amount = res[1]
        content = [f"You have bet ${bet_amount}"]
        #cycle player
        res = res[2]
        cycle_res = lib.get_cycle_content(res, client, lobby)
        content += cycle_res[0]
        embed = cycle_res[1]
        await lib.ping_msg(message, "".join(content), embed)