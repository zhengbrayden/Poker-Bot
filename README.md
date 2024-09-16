```
# Poker-Bot
Overview:  
Bot that allows users to play a text-based texas hold'em poker through the messaged app Discord. Uses discord.py API wrapper.  

Installation:  
Clone the repository  
  
Running the Bot:  
Create a Discord bot ( https://discord.com/developers/docs/intro ) and enter the token into the token.txt file  
run the command "python main.py" from the project top level.  
Your bot is now online!  

Quickstart Guide:
In a server that contains the bot,
Have host create a lobby through command
-create myLobby
Have players join the lobby through command
-join myLobby
Once all players have joined, have host start the lobby through command
-start
Your game has now started! Have fun! And gamble responsibly.

Player Commands:  
-call  
Poker call command  
-create LOBBY  
creates a lobby with name LOBBY (name must be unique)  
-join LOBBY  
joins a lobby with name LOBBY  
-fold  
Poker fold command  
-info_lobby [LOBBY]  
If no argument provided, list all lobbies inside a channel. If argument provided, list players inside lobby LOBBY  
-info  
Receive a DM about your player info from the bot for channel where command is issued  
-raise  
Poker raise command  
-leave  
Leave a lobby  
-start  
Start the poker game of the lobby as the leader  

Implementation Details:  
All poker lobbies are seperated on a discord channel basis, so a player can exist in multiple lobbies within different channels, but only one lobby per channel.  
All rules should be fully implemented including precise tie-breaking, sidepots, and hand evaluation.  

Testing:
To run a test TEST_FILE, use the command python tests/{TEST_FILE} from the project top level
