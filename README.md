# ShieldBot for Discord

[click to add me to your discord server](https://discord.com/api/oauth2/authorize?client_id=754876371829784717&permissions=8&scope=bot)

# Info
Since my journey in learning python began with a single college class, I took the liberty in making a new discord bot with a language I feel more comfortable with. Discord.py at least in my opinion works so much better than Discord.js since the ping in between events is insanely low. I hope this bot can one day be full of commands and little nifty tools for gamers and casual chatties can enjoy.
# Tasks
- [ ] make cogs for command handlers
- [ ] make cogs for event handlers
- [x] figure out how to hide the key more efficiently
- [x] modify the debugger menu
- [ ] offer more moderation control when more aggressive commands are made
- [x] update markdown
- [x] get bot up and running

# Commands
Since this is a new bot with no real method to organize commands right now, most commands are simple and not threatening right now. Keep in mind as I grow this list I will add specific notes to ensure these commands will not fall into the wrong hands.

## Owner-Specific Commands
### While few in numbers these do exist:

#### [blacklist command]
**Format:**  
_(prefix)[command] {user id/mention user}_  
**Description:**  
_This command does absolutely nothing other than placing the persons id into a json file._  

>If the user's id is inside this document in Ver 0.1.1, they are still allowed to use regular commands.

#### [unblacklist command]  
**Format:**  
_(prefix)[command] {user id/mention user}_  
**Description:**  
_This command removes the user's id from the blacklist json file._  

>If the user's id is inside this document in Ver 0.1.1, they are still allowed to use regular commands.

#### [logout command]
**Aliases**  
_{disconnect, close, stopbot}_  
**Format:**  
_(prefix)[command]_  
**Description:**  
_If the user running the command owns the bot then this will disconnect the bot from discord._  

>This is only available to the owner and can not be used by anyone but the owner.

## User-Specific Commands
### These commands are made entirely for the user to enjoy. While most of my really fun ones are in a previous version not available for viewing, I will implement these when I begin to organize cogs into the bot. For now, here are a few commands active as of Ver 0.1.1:  

#### [hi command]  
**Aliases**  
_{hello}_  
**Format:**  
_(prefix)[command]_  
**Description:**  
_A simple command which says hi to the author._

#### [stats command]  
**Format:**  
_(prefix)[command]_  
**Description:**  
_A useful command that displays bot statistics._

#### [echo command]  
**Format:**  
_(prefix)[command] {message}_  
**Description:**  
_A simple command that repeats the users input back to them._

# Contact Information
If you have any inquires or recommendations on what I should do, feel free to send me a message and I will add that to my tasks. This is suppose to be a fun project to keep my free time manageable.
## Email:  
mmclaren1026@gmail.com
## Discord ID:  
マクラレン#7331  
<@300251178107928576>  
