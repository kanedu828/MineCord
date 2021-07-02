# Isla-Bot-2.0

## Overview

Isla Bot 2.0 takes its focus on the mining game. In this revamp, many more additions and mechanics were added to the mining game to give it more depth. 
The bot is current in its beta state.

You can invite the bot to your server through here: https://discord.com/api/oauth2/authorize?client_id=708417621334163537&permissions=0&scope=bot

## Community Contribution
Commit into the development branch and make a PR. I'll be happy to review them.
Feel free to fix bugs, add anything from Projects, or add more caves and equipment!

### Setup
Create a virtual environment with `$python3 -m venv venv`.\
Activate the venv with `$source venv/bin/activate`.\
Install dependencies with `pip install -r requirements.txt`. (You may need an extra dependency not correctly listed in requirements.txt. Install here: https://github.com/Rapptz/discord-ext-menus) \
Create a `.env` file and populate the fields with the proper values.\
Start bot with `$python3 main.py`

## Commands

`;mine` Mine in the current cave you are in.\
`;cave` List all of your available caves.\
`;cave <cave name>` Switch to the specified cave.\
`;stats` View your stats. i.e Your level, total exp, gold, and mining stats.\
`;equip <equipment name>` Equip your specified equipment.\
`;gear` View all of your equipped equipment.\
`;gear <equipment name>` Display in detail your specified equipment.\
`;inventory` List your inventory.\
`;leaderboard` View the leaderboard based off of total exp.\
`;bonus <equipment name>` Add bonuses to your specified equipment.\
`;reset` Reset your total exp and gain blessings.

## Mining
By using the `;mine` command, you mine your cave in the chance to recieve gold, equipment, or exp. Each cave drops different loot and has different odds to drop loot.

## Caves
Each cave has a level requirement that is needed for someone to enter it. Every cave drops a set amount of exp. For example, the Beginner cave drops 1 exp per mine while the Dark Cave drops 10 exp per mine.\
Cave loot is seperated into 5 categories: Nothing, Common, Rare, Epic, Legendary\
Typically, the latter categories will have a lower chance to drop.\
Additionally, some caves can only be mined a certain amount. For example, if a cave only has 1,000 mines, it can no longer be mined when it is mined a total of 1000 times by all miners. The remaining mines in a cave gets reset periodically. Some caves, however, can be mined an infinite amount of times.\
If you're interested in viewing all available caves, you can find them [here](https://github.com/kanedu828/Isla-Bot-2.0/blob/master/data/caves.py).
If you understand the cave list in that file and you would like to help out, feel free to list the caves in a readable format here with a pull request!

## Equipment
You can find various equipment while mining. There are 6 different types of equipment: Helmet, vest, pants, gloves, pickaxe, and boots.\
Each equipment gives you stats and it is totaled into your total stats, which you can see with ;stats.\
There are two ways you can upgrade your equipment.
1. Star level: You gain a star for each duplicate equipment you have. Increasing your star level only increases the equipment's base stats. For example, if an equipment only has power and speed base stats, only power and speed will be upgraded. The first 5 stars give + 1 to each stat per star, the next 5 stars give +2, and so on.
2. Bonus: You can roll for bonuses with the ;bonus <equipment name> command. You will randomly get random stats. You can recieve up to 5 bonuses for a piece of equipment. Refer to the bonus section for more information.

## Stats
Current there are four different stats for a user: power, speed, exp, luck\
Power: You get x amount of extra gold each time you mine gold.\
Speed: Cooldown for mining reduced by speed / 100. (This stat will most likely be nerfed)\
Exp: You get x amount of extra exp each time you mine exp.\
Luck: Your chances of recieving Epic or Legendary loot is increased by luck / 100 %.\
Your stats can be added raw (+) or added as a percentage (%).\
For example, if you have power + 6, you will get 6 power to your total power stat. If you have ower 6%, you will get an additional 6% of your total power added to your total power.
Your total amount of stats is determined by all of your equipped equipment.

## Bonus
You can give your equipment bonus stats through the `;bonus <equipment name>` command. This will cost 1000 gold.\
Currently you can recieve up to 5 bonus stats. When you first bonus your equipment, you will start off with one bonus. However, if you continue to bonus your equipment, you will reroll your bonuses with the chance to recieve another bonus.\
Here are the odds for getting extra bonuses:\
0 -> 1 bonus stats: 100%\
1 -> 2 bonus stats: 10%\
2 -> 3 bonus stats: 5%\
3 -> 4 bonus stats: 2.5%\
4 -> 5 bonus stats: 1%\
Additionally, the higher level your equipment, the better bonuses it will get.
  
## Blessings
After you reach level 50, you have the opportunity to reset your exp to gain blessings. Every 5 levels after level 50 will give you 1 blessing on a reset. Each blessing will permanently give you 1% exp to your stats.\
For example, if you have level 65, you will gain 3 blessings. If you are level 100, you will gain 10 blessings.

If you have a good understanding of mining and you don't like how things are explained, feel free to create a pull request and edit this README.

