import discord
import commands.header
import lib
async def info(client, message, player):
    #give info on a player about bank, cards, and bet
    #if not started, player won't have cards
    bank = player.get_bank()
    lobby = player.get_lobby()
    embed = discord.Embed()
    embed.add_field(value=f"${bank}", name = "Bank")

    if not lobby.has_started:
        dm_channel = await client.create_dm(message.author)
        await dm_channel.send(embed = embed)
        return

    bet = player.get_bet()
    hand = player.get_hand()
    embed.add_field(value=f"${bet}", name = "Bet")
    embed.add_field(value=lib.compose_hand_str(hand), name = "Hand")
    dm_channel = await client.create_dm(message.author)
    await dm_channel.send(embed = embed)
    