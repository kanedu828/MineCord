# MineCord

## Overview

MineCord is an idle clicker Discord game. You mine to gain exp and gold to climb the leaderboards or to upgrade your equipment.

You can invite the bot to your server through here: https://discord.com/api/oauth2/authorize?client_id=708417621334163537&permissions=0&scope=bot

Join the official Discord server here! https://discord.gg/d2g6p33

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
By using the `;mine` command, you mine your cave in the chance to recieve gold, equipment, or exp. Each cave drops different loot and has different odds to drop loot. Happy hour is 7 pm EST every day. During happy hour, players gain 2x exp for mining.\
![Mining Example](https://cdn.discordapp.com/attachments/708483256332320788/942244378024476694/unknown.png)
## Drilling
Drilling is basically idle mining. Every 10 minutes, you passively get exp and gold. You can use `;drill` to check your drill for any idle rewards. This is capped at 24 hours worth of rewards.\
Exp and gold rates depend on how much drill exp and drill power you have.\
![Drill Example](https://cdn.discordapp.com/attachments/708483256332320788/942244531896721468/unknown.png)
## Caves
Each cave has a level requirement that is needed for someone to enter it. Every cave drops a set amount of exp, with better caves typically giving more exp.\
![Cave Example](https://cdn.discordapp.com/attachments/708483256332320788/942245019874631740/unknown.png)\
Cave loot is seperated into 5 categories: Nothing, Common, Rare, Epic, Legendary\
Typically, the latter categories will have a lower chance to drop.\
Additionally, some caves can only be mined a certain amount. For example, if a cave only has 1,000 mines, it can no longer be mined when it is mined a total of 1000 times by all miners. The remaining mines in a cave gets reset periodically. Some caves, however, can be mined an infinite amount of times.

## Dungeons
Dungeons do not give any exp or gold per mine. Dungeons have a set amount of durability, and each mine deals damage to its durability. Once its durability hits 0, you are given rewards. Each dungeon drops exp, gold, and a chance to get an item fragments. The more luck stat you have, the higher chance you have to get fragments. Dungeons can either be cleared daily or weekly.\
![image](https://user-images.githubusercontent.com/45084706/153735654-b79f5fce-61fc-43af-87e9-97637b05964b.png)\
![image](https://user-images.githubusercontent.com/45084706/153735649-50f42346-2892-4836-b41f-0d01870d3f19.png)\
Fragments can then be use to forge powerful pieces of equipment.\
Currently, the first dungeon is unlocked at level 75.

## Equipment
You can find various equipment while mining. There are 6 different types of equipment: Helmet, vest, pants, gloves, pickaxe, and boots.\
Each equipment gives you stats and it is totaled into your total stats, which you can see with `;stats`.\
Some equipment also have set bonuses. If you have a certain amount of equipment equipped from that set, you will gain bonuses.\
There are two ways you can upgrade your equipment.
1. Star level: You gain a star for each duplicate equipment you have. Increasing your star level only increases the equipment's base stats. The higher the star level, the more your stats will increase.
2. Bonus: You can roll for bonuses with the `;bonus <equipment name>` command. You will randomly get random stats. You can recieve up to 5 bonuses for a piece of equipment. Refer to the bonus section for more information.\
![image](https://user-images.githubusercontent.com/45084706/153735708-8cee6857-b54e-4b7f-b28e-88f6b2198ffa.png)

## Stats
Current there are six different stats for a user: power, speed, exp, luck, drill exp, drill power\
Power: Grants extra gold each time you mine gold. Additionally, power is used for dungeon mining.\
Speed: Cooldown for mining reduced. Min cooldown is 3 seconds, which is 70 speed.\
Exp: Grants extra exp each time you mine exp.\
Luck: Your chances of recieving Epic or Legendary loot is increased.\
Crit: Increase chance to crit while mining, which provides 2x exp. Crit caps at 100, but any more crit past 100 increases the crit multiplier.\
Drill Power: Gold obtained from drilling.\
Drill EXP: Exp obtaiend from drilling.\
Your stats can be added raw (+) or added as a percentage (%).\
Raw stats increases your stats by that amount. Percentage stats increase your stats by that percentage of your total raw stats.\
Your total amount of stats is determined by all of your equipped equipment.\
![image](https://user-images.githubusercontent.com/45084706/153735819-16ce4eba-cc64-44e5-8673-94b81701779b.png)

## Bonus
You can give your equipment bonus stats through the `;bonus <equipment name>` command. The cost depends on the level of your gear. Higher level gear is more expensive to bonus.\
You can recieve up to 5 bonus stats. When you first bonus your equipment, you will start off with one bonus. However, if you continue to bonus your equipment, you will reroll your bonuses with the chance to recieve another bonus.\
Here are the odds for getting extra bonuses:\
0 -> 1 bonus stats: 100%\
1 -> 2 bonus stats: 10%\
2 -> 3 bonus stats: 5%\
3 -> 4 bonus stats: 2.5%\
4 -> 5 bonus stats: 1%\
Additionally, the higher level your equipment, the better bonuses it will get.
  
## Stars
You can also add stars to your equipment with `;star <equipment name>`. The cost of starring depends on your equipment's level. It gets more expensive the higher star level it is.
  
## Blessings
After you reach level 50, you have the opportunity to reset your exp to gain blessings. The higher level you are, the more blessings you will get. Each blessing will permanently give you 1% exp to your stats.
  
## Terms of Service
  1. Use of scripts to automate miining is not allowed. You may be blacklisted if you are scripting.
  2. Abuse of bugs are not allowed, please report bugs as soon as you can.
  
## Privacy Policy
  #### What information does MineCord collect?
  The only data MineCord collects from users is the user's Discord ID. You may view the bot's (database scheme)[https://github.com/kanedu828/MineCord#database-schema] for a more detailed look on what data MineCord stores.
  #### How does MineCord use your data?
  Minecord uses a user's Discord ID to save save user progress in the game. It is also used to display users on the leaderboard. Only the user's name is displayed on the leaderboard. User tags are omitted.
  #### Will your information be shared with anyone?
  No, anything stored in the database will not be shown to anyone.
  #### How long do we keep your information?
  A user's Discord ID will be stored indefinitely. A user may request to be removed from the database by messaging `kane#6661` on Discord.
  
## Community Contribution
Commit into the development branch and make a PR. I'll be happy to review them.
Feel free to fix bugs, add anything from Projects, or add more caves and equipment!

### Setup
Create a virtual environment with `$python3 -m venv venv`.\
Activate the venv with `$source venv/bin/activate`.\
Install dependencies with `pip install -r requirements.txt`. (You may need an extra dependency not correctly listed in requirements.txt. Install here: https://github.com/Rapptz/discord-ext-menus) \
Create a `.env` file and populate the fields with the proper values.\
Start bot with `$python3 main.py`

#### Database Schema
In order to setup the bot, you need to create a PostgreSQL database with the following tables:
```sql
CREATE TABLE users(
user_id BIGINT PRIMARY KEY NOT NULL,
cave VARCHAR(255) NOT NULL DEFAULT 'Beginner Cave',
dungeon VARCHAR(255) DEFAULT '',
gold INT NOT NULL DEFAULT 0,
exp INT NOT NULL DEFAULT 0,
blessings INT NOT NULL DEFAULT 0,
last_drill TIMESTAMP NOT NULL DEFAULT NOW()
);
```
```sql
CREATE TABLE equipment(
equipment_instance_id SERIAL PRIMARY KEY,
equipment_id INT NOT NULL,
user_id BIGINT NOT NULL,
location VARCHAR(255) NOT NULL,
bonus VARCHAR NOT NULL DEFAULT '',
stars INT NOT NULL DEFAULT 0,

CONSTRAINT fk_user
FOREIGN KEY(user_id)
REFERENCES users(user_id));
```
```sql
CREATE TABLE item(
item_id INT NOT NULL,
user_id BIGINT NOT NULL,
count INT NOT NULL DEFAULT 0,
UNIQUE (item_id, user_id),

CONSTRAINT fk_user
FOREIGN KEY(user_id)
REFERENCES users(user_id));
```
```sql
CREATE TABLE dungeon_instance(
dungeon_name VARCHAR(255),
user_id BIGINT NOT NULL,
durability INT,
clear_rate VARCHAR(255),
UNIQUE (dungeon_name, user_id),

CONSTRAINT fk_user
FOREIGN KEY(user_id)
REFERENCES users(user_id));
```

