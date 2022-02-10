# MineCord

## Overview

MineCord is an idle clicker Discord game. You mine to gain exp and gold to climb the leaderboards or to upgrade your equipment.

You can invite the bot to your server through here: https://discord.com/api/oauth2/authorize?client_id=708417621334163537&permissions=0&scope=bot

Join the official Discord server here! https://discord.gg/GHEhKR3 

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
`;reset` Reset your total exp and gain blessings.\
`;shop <optional: item name>` View the shop. Provide the item name to view a detailed description of the item.\
`;buy <item name>` Buy the item. It must be in the shop.\
`;drill` CLaim your idle rewards.\
`;dungeon` View details of your current dungeon.\
`;dungeon <dungeon name>` Switch to the specified dungeon\
`;dmine` Mine your current dungeon\
`;fragments` Check your current fragments\
`;forge` Look at the available items to forge with fragments\
`;forge <item name>` For an item.\
`;lookup <item name>` Look up details on an item.

## Mining
By using the `;mine` command, you mine your cave in the chance to recieve gold, equipment, or exp. Each cave drops different loot and has different odds to drop loot. Happy hour is 7 pm EST every day. During happy hour, players gain 2x exp for mining

## Drilling
Drilling is basically idle mining. Every 10 minutes, you passively get exp and gold. You can use `;drill` to check your drill for any idle rewards. This is capped at 24 hours worth of rewards.\
Exp and gold rates depend on how much drill exp and drill power you have.

## Caves
Each cave has a level requirement that is needed for someone to enter it. Every cave drops a set amount of exp. For example, the Beginner cave drops 1 exp per mine while the Dark Cave drops 10 exp per mine.\
Cave loot is seperated into 5 categories: Nothing, Common, Rare, Epic, Legendary\
Typically, the latter categories will have a lower chance to drop.\
Additionally, some caves can only be mined a certain amount. For example, if a cave only has 1,000 mines, it can no longer be mined when it is mined a total of 1000 times by all miners. The remaining mines in a cave gets reset periodically. Some caves, however, can be mined an infinite amount of times.\
If you're interested in viewing all available caves, you can find them [here](https://github.com/kanedu828/Isla-Bot-2.0/blob/master/data/caves.py).
If you understand the cave list in that file and you would like to help out, feel free to list the caves in a readable format here with a pull request!

## Dungeons
Dungeons do not give any exp or gold per mine. Dungeons have a set amount of durability, and each mine deals damage to its durability. Once its durability hits 0, you are given rewards. Each dungeon drops exp, gold, and a chance to get an item fragments. You get an aditionally roll to get a fragment per 100 luck. Dungeons can either be cleared daily or weekly.\
Fragments can then be use to forge powerful pieces of equipment.\
Currently, the first dungeon is unlocked at level 75.

## Equipment
You can find various equipment while mining. There are 6 different types of equipment: Helmet, vest, pants, gloves, pickaxe, and boots.\
Each equipment gives you stats and it is totaled into your total stats, which you can see with ;stats.\
Some equipment also have set bonuses. If you have a certain amount of equipment equipped from that set, you will gain bonuses.\
There are two ways you can upgrade your equipment.
1. Star level: You gain a star for each duplicate equipment you have. Increasing your star level only increases the equipment's base stats. For example, if an equipment only has power and speed base stats, only power and speed will be upgraded. The first 5 stars give + 1 to each stat per star, the next 5 stars give +2, and so on.
2. Bonus: You can roll for bonuses with the ;bonus <equipment name> command. You will randomly get random stats. You can recieve up to 5 bonuses for a piece of equipment. Refer to the bonus section for more information.\


## Stats
Current there are four different stats for a user: power, speed, exp, luck\
Power: You get x amount of extra gold each time you mine gold.\
Speed: Cooldown for mining reduced. Max cooldown is 3 seconds, which is 70 speed.\
Exp: You get x amount of extra exp each time you mine exp.\
Luck: Your chances of recieving Epic or Legendary loot is increased.\
Crit: Increase chance to crit while mining, which provides 2x exp. Crit caps at 100, but any more crit increases crit %.\
Drill Power: Gold obtained from drilling.\
Drill EXP: Exp obtaiend from drilling.\
Your stats can be added raw (+) or added as a percentage (%).\
For example, if you have power + 6, you will get 6 power to your total power stat. If you have ower 6%, you will get an additional 6% of your total power added to your total power.
Your total amount of stats is determined by all of your equipped equipment.\

## Bonus
You can give your equipment bonus stats through the `;bonus <equipment name>` command. This will cost 1000 gold.\
Currently you can recieve up to 5 bonus stats. When you first bonus your equipment, you will start off with one bonus. However, if you continue to bonus your equipment, you will reroll your bonuses with the chance to recieve another bonus.\
Here are the odds for getting extra bonuses:\
0 -> 1 bonus stats: 100%\
1 -> 2 bonus stats: 10%\
2 -> 3 bonus stats: 5%\
3 -> 4 bonus stats: 2.5%\
4 -> 5 bonus stats: 1%\
Additionally, the higher level your equipment, the better bonuses it will get.\
  
## Stars
You can also manually add stars to your equipment with `;star`. This typically costs a hefty amount of gold and there is no guarantee that your equipment will be starred. It gets more expensive the higher star level it is.
  
## Blessings
After you reach level 50, you have the opportunity to reset your exp to gain blessings. Every 5 levels after level 50 will give you 1 blessing on a reset. Each blessing will permanently give you 1% exp to your stats.\
For example, if you have level 65, you will gain 3 blessings. If you are level 100, you will gain 10 blessings.

If you have a good understanding of mining and you don't like how things are explained, feel free to create a pull request and edit this README.
  
## Terms of Service
  Don't cheat

