from commands.header import *

#need to keep track of folded players
async def raise_(client, message, args, player):
    #raise amount must be an int. improvement would be to have a minimum raise restriction as well
    try:
        raise_amount = int(args[0])
    except:
        lib.ping_msg("Raise amount must be an integer")

    #can't raise an amount greater than what they have
    lobby = player.get_lobby()
    res = lobby.raise_player(player, raise_amount)
    flag = res[0]

    if flag == 0:
        await lib.ping_msg(message, f"Cannot raise as the lobby '{lobby.get_name()}' has not started")
    elif flag == 1:
        await lib.ping_msg(message, f"Cannot raise as it is not your turn!")
    elif flag == 2:
        await lib.ping_msg(message, f"You cannot raise a negative amount!")
    elif flag == 3:
        await lib.ping_msg(message, f"You do not have enough to raise that amount")
    elif flag == 4:
        bet_amount = res[1]
        content = [f"You have bet ${bet_amount}."]
        #cycle player
        bet_amount = res[1]
        res = res[2]
        cycle_res = lib.get_cycle_content(res, client, lobby)
        content += cycle_res[0]
        embed = cycle_res[1]
        await lib.ping_msg(message, "".join(content), embed)