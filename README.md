# Poker-Bot

## Overview
A Discord bot that allows users to play text-based Texas Hold'em poker through Discord, using the `discord.py` API wrapper.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Poker-Bot
   ```

## Running the Bot
1. [Create a Discord bot](https://discord.com/developers/docs/intro) and copy the bot token.
2. Paste the token into a `token.txt` file in the root directory.
3. Run the bot:
   ```bash
   python main.py
   ```

## Quickstart Guide
1. Create a lobby as the host:
   ```bash
   -create myLobby
   ```
2. Players join the lobby:
   ```bash
   -join myLobby
   ```
3. Once all players have joined, the host starts the game:
   ```bash
   -start
   ```
   
## Player Commands
- `-call`: Call the current bet.
- `-create <LOBBY>`: Create a new lobby with a unique name.
- `-join <LOBBY>`: Join an existing lobby by name.
- `-fold`: Fold your current hand.
- `-info_lobby [LOBBY]`: Show all lobbies or players in a specific lobby.
- `-info`: Get a DM with your player info for the current channel.
- `-raise`: Raise the current bet.
- `-leave`: Leave the current lobby.
- `-start`: Start the game as the host.

## Implementation Details
- Each Discord channel can host multiple lobbies, but a player can only participate in one lobby per channel.
- Full poker rules are implemented, including tie-breaking, sidepots, and hand evaluation.

## Testing
Tests are located in the `tests/` directory. Run a test by using the following command:
```bash
python <path_to_test>
```
