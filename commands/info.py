async def info(message, client, args, Channels):

    if message.channel.id not in Channels:
        await message.channel.send('This channel contains no lobbies')
        return
    
    channel = Channels[message.channel.id]

    if len(args) == 0:
        #output the channel info
        lobbies = channel.get_lobbies()
        content=["List of Lobbies:"]

        for lobby in lobbies:
            content.append(lobby.get_name())

        await message.channel.send('\n'.join(content))
        return
    
    name = " ".join(args)
    lobby = channel.get_lobby(name)

    if not lobby:
        await message.channel.send("'" + name + "' is not a lobby in this channel!")
        return
    
    #output lobby info (players inside)
    content=["List of Players:"]

    for player in lobby.get_players():
        id=player.get_id()
        content.append(client.get_user(id).name)

    await message.channel.send('\n'.join(content))
