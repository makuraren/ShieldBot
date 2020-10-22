# ShieldBot Directory
![ShieldBot Logo](/docs/bot_resize.png)
* [Info](https://github.com/makuraren/ShieldBot/blob/master/README.md#info)
* [Invite Information](https://github.com/makuraren/ShieldBot/blob/master/README.md#invite-information)
* [Commands](https://github.com/makuraren/ShieldBot/blob/master/README.md#commands)
    * [Fun Commands](https://github.com/makuraren/ShieldBot/blob/master/README.md#fun-commands)
        * [[hi]](https://github.com/makuraren/ShieldBot/blob/master/README.md#hi)
        * [[echo]](https://github.com/makuraren/ShieldBot/blob/master/README.md#echo)
        * [[8ball]](https://github.com/makuraren/ShieldBot/blob/master/README.md#8ball)
    * [Info Commands](https://github.com/makuraren/ShieldBot/blob/master/README.md#info-commands)
        * [[stats]](https://github.com/makuraren/ShieldBot/blob/master/README.md#stats)
        * [[directory]](https://github.com/makuraren/ShieldBot/blob/master/README.md#directory)
    * [Moderation Commands](https://github.com/makuraren/ShieldBot/blob/master/README.md#moderation-commands)
        * [[clear]](https://github.com/makuraren/ShieldBot/blob/master/README.md#clear)
        * [[lockdown]](https://github.com/makuraren/ShieldBot/blob/master/README.md#lockdown)
        * [[kick]](https://github.com/makuraren/ShieldBot/blob/master/README.md#kick)
        * [[ban]](https://github.com/makuraren/ShieldBot/blob/master/README.md#ban)
        * [[unban]](https://github.com/makuraren/ShieldBot/blob/master/README.md#unban)
        * [[prefix]](https://github.com/makuraren/ShieldBot/blob/master/README.md#prefix)
    * [Private Commands](https://github.com/makuraren/ShieldBot/blob/master/README.md#private-commands)
        * [[blacklist]](https://github.com/makuraren/ShieldBot/blob/master/README.md#blacklist)
        * [[unblacklist]](https://github.com/makuraren/ShieldBot/blob/master/README.md#unblacklist)
        * [[logout]](https://github.com/makuraren/ShieldBot/blob/master/README.md#logout)
    * [Utility Commands](https://github.com/makuraren/ShieldBot/blob/master/README.md#utility-commands)
        * [[build]](https://github.com/makuraren/ShieldBot/blob/master/README.md#build)
        * [[delete]](https://github.com/makuraren/ShieldBot/blob/master/README.md#delete)
* [Resources](https://github.com/makuraren/ShieldBot/blob/master/README.md#resources)
* [Tasks](https://github.com/makuraren/ShieldBot/blob/master/README.md#tasks)
* [Contact Info](https://github.com/makuraren/ShieldBot/blob/master/README.md#contact-information)
    * [Email](https://github.com/makuraren/ShieldBot/blob/master/README.md#email)
    * [Discord ID](https://github.com/makuraren/ShieldBot/blob/master/README.md#discord-id)

# Info
Since my journey in learning python began with a single college class, I took the liberty in making a new discord bot with a language I feel more comfortable with. Discord.py at least in my opinion works so much better than Discord.js since the ping in between events is insanely low. I hope this bot can one day be full of commands and little nifty tools for gamers and casual chatties can enjoy.

# Invite Information
By clicking this link, you will be prompted to have the bot join your server.

_[click to add me to your discord server](https://discord.com/api/oauth2/authorize?client_id=754876371829784717&permissions=8&scope=bot)_

# Commands
Since this is a new bot with no real method to organize commands right now, most commands are simple and not threatening right now. Keep in mind as I grow this list I will add specific notes to ensure these commands will not fall into the wrong hands.

## Fun Commands

### [hi]  
>**Aliases**  
_{hello}_  
**Format:**  
_(prefix)[command]_  
**Description:**  
_A simple command which says hi to the author._

### [echo]  
>**Format:**  
_(prefix)[command] {message}_  
**Description:**  
_A simple command that repeats the users input back to them._

### [8ball]
>**Format:**  
_(prefix)[command] {question}_  
**Description:**  
_A command that provides you a 8ball response to a question._

## Info Commands

### [stats]  
>**Format:**  
_(prefix)[command]_  
**Description:**  
_A useful command that displays bot statistics._

### [directory]
>**Format:**  
_(prefix)[command]_  
**Description:**  
_Grabs README.md from directory._

## Moderation Commands

### [clear]
>***This will only be available to administrators.***  
**Aliases**  
_{purge}_  
**Format:**  
_(prefix)[command] (num)_  
**Description:**  
_Clears messages_  

### [kick]
>***This will only be available to administrators.***  
**Format:**  
_(prefix)[command] (user) (reason)_  
**Description:**  
_A command that kicks a user_  

### [ban]
>***This will only be available to administrators.***  
**Format:**  
_(prefix)[command] (user) (reason)_  
**Description:**  
_A command that bans a user_  

### [ban]
>***This will only be available to administrators.***  
**Format:**  
_(prefix)[command] (user) (reason)_  
**Description:**  
_A command that unbans a user_  

### [prefix]
>***This will only be available to administrators.***  
**Format:**  
_(prefix)[command] (new prefix)_  
**Description:**  
_Set a custom prefix for a guild_  

## Private Commands

### [blacklist]
>***This is only available to the owner and can not be used by anyone but the owner.***  
**Format:**  
_(prefix)[command] {user id/mention user}_  
**Description:**  
_A command that blacklists a user_  

### [unblacklist]
>***This is only available to the owner and can not be used by anyone but the owner.***  
**Format:**  
_(prefix)[command] {user id/mention user}_  
**Description:**  
_A command that unblacklists a user_  

### [logout]
>***This is only available to the owner and can not be used by anyone but the owner.***  
**Aliases**  
_{disconnect, close, stopbot}_  
**Format:**  
_(prefix)[command]_  
**Description:**  
_Turns off bot_

## Utility Commands

### [build]
>***This will only be available to administrators.***  
**Server Items:**  
_*Channel, Category*_  
**Format:**  
_(prefix)[command] (server item) (role) (name)_  
**Description:**  
_This builds items in the server_  

### [delete]
>***This will only be available to administrators.***  
**Server Items:**  
_*Channel, Category*_  
**Format:**  
_(prefix)[command] (server item) (name) (reason)_  
**Description:**  
_This deletes items in the server_  

# Resources
I have to give a special thanks to the people over at MenuDocs with their Discord.py tutorial videos to help me get started. Please go check them out and their work here:  
*YouTube: [https://www.youtube.com/channel/UCpGGFqJP9vYvzFudqnQ-6IA](https://www.youtube.com/channel/UCpGGFqJP9vYvzFudqnQ-6IA)*  
*GitHub: [https://github.com/MenuDocs](https://github.com/MenuDocs)*  

# Tasks
- [x] offer more moderation control when more aggressive commands are made
- [ ] develop music bot formatting
- [ ] develop more fun commands
- [ ] make a log command

# Contact Information
If you have any inquires or recommendations on what I should do, feel free to send me a message and I will add that to my tasks. This is suppose to be a fun project to keep my free time manageable.
## Email:  
mmclaren1026@gmail.com
## Discord ID:  
マクラレン#7331  
<@300251178107928576>  
