from commands.header import *
#takes no args
async def start(client, message, player):

    #perform the check inside like a good boy
    lobby = player.get_lobby()

    if player.get_id() == lobby.get_leader():
        res = lobby.start()
    else:
        await lib.ping_msg(message, 'You cannot start the lobby because you are not the leader!')
        return False

    flag = res[0]
    
    if flag == 0:
        await lib.ping_msg(message, 'You need atleast 2 players to start a lobby.')
    elif flag == 1:
        await lib.ping_msg(message, 'The lobby \'' + lobby.get_name() + '\' has already been started')
    else: 
        players = lobby.get_unfolded_list()
        player_ids = [player.get_id() for player in players]
        cur_player = lobby.get_cur_player()
        little = res[1]
        big = res[2]
        embed = discord.Embed()

        player_names = []

        if len(player_ids) == 1:
            return client.get_user(player_ids[i]).name
        
        for i in range(len(player_ids) - 1):
            player_names.append(client.get_user(player_ids[i]).name)
            player_names.append(' => ')

        player_names.append(client.get_user(player_ids[-1]).name)
        player_names = "".join(player_names)
        embed.add_field(value = player_names, name = "Player Order")
        embed.add_field(value = f'{lib.mention(cur_player.get_id())}\'s turn', name = "Current Player")
        embed.add_field(value = f"{client.get_user(big).name}.\n{client.get_user(little).name}", name = "Big blind/Little blind")

        hand_str_list = [lib.compose_hand_str(player.get_hand()) for player in players]
        users_list = [client.get_user(player_id) for player_id in player_ids]
        await lib.ping_msg(message, 'Starting lobby.', embed)
        
        #send each player their hand
        for user, hand in zip(users_list, hand_str_list):
            dm_channel = await client.create_dm(user)
            await dm_channel.send(hand)