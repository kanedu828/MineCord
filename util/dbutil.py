import asyncpg
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

PSQL_CONNECTION_URL = os.getenv('PSQL_CONNECTION_URL')

async def get_all_users():
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("SELECT * FROM users")
    #print(await stmt.fetch())
    await conn.close()

async def insert_user(id: int):
    '''
        Inserts a user into the database.
        Columns: user_id, exp, cave, gold
    '''
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("INSERT INTO users(user_id) VALUES ($1) RETURNING user_id, exp, cave, gold")
    result = await stmt.fetch(id)
    await conn.close()
    return result

async def get_user(id: int):
    '''
        Retrieves an user and returns the columns and values as a dictionary.
        If the user is not in the database, the user is first inserted and then returned.
    '''
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("SELECT * FROM users WHERE user_id=$1")
    result = await stmt.fetch(id)
    if not result:
        result = await insert_user(id)
    await conn.close()
    user_data = {}
    for field, value in result[0].items():
        user_data[field] = value
    return user_data

async def update_user_exp(user_id: int, amount: int):
    '''
        Adds amount to the user's exp. Returns a record object.
    '''
    await get_user(user_id)
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("UPDATE users SET exp=exp + $2 WHERE user_id=$1 RETURNING user_id, exp, cave, gold")
    result = await stmt.fetch(user_id, amount)
    await conn.close()
    return result

async def set_user_exp(user_id: int, amount: int):
    '''
        Set amount to the user's exp. Returns a record object.
    '''
    await get_user(user_id)
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("UPDATE users SET exp=$2 WHERE user_id=$1 RETURNING user_id, exp, cave, gold")
    result = await stmt.fetch(user_id, amount)
    await conn.close()
    return result


async def update_user_gold(user_id: int, amount: int):
    '''
        Adds amount to the user's gold. Returns a record object.
    '''
    await get_user(user_id)
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("UPDATE users SET gold=gold + $2 WHERE user_id=$1 RETURNING user_id, exp, cave, gold")
    result = await stmt.fetch(user_id, amount)
    await conn.close()
    return result

async def set_user_gold(user_id: int, amount: int):
    '''
        Set amount to the user's gold. Returns a record object.
    '''
    await get_user(user_id)
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("UPDATE users SET gold=$2 WHERE user_id=$1 RETURNING user_id, exp, cave, gold")
    result = await stmt.fetch(user_id, amount)
    await conn.close()
    return result

async def update_user_cave(user_id: int, cave: str):
    '''
        Updates an user's cave. Returns a record object.
    '''
    await get_user(user_id)
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("UPDATE users SET cave=$2 WHERE user_id=$1 RETURNING user_id, exp, cave, gold")
    result = await stmt.fetch(user_id, cave)
    await conn.close()
    return result

async def get_top_users_for_exp(amount: int):
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("SELECT * FROM users ORDER BY exp DESC LIMIT $1")
    result = await stmt.fetch(amount)
    await conn.close()
    user_list = []
    for r in result:
        user_data = {}
        for field, value in r.items():
            user_data[field] = value
        user_list.append(user_data)
    return user_list

async def insert_equipment(user_id: int, equipment_id: int, location: str):
    await get_user(user_id)
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("INSERT INTO equipment(equipment_id, user_id, location) VALUES ($1, $2, $3) RETURNING equipment_instance_id, equipment_id, user_id, location, bonus, stars")
    result = await stmt.fetch(equipment_id, user_id, location)
    await conn.close()
    return result

async def get_equipment_for_user(user_id: int):
    '''
        Gets all equipment attatched to a user id. Returns as a list of dictionaries.
    '''
    await get_user(user_id)
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("SELECT * FROM equipment WHERE user_id=$1")
    result = await stmt.fetch(user_id)
    await conn.close()
    equipment_data_list = []
    for r in result:
        equipment_data = {}
        for field, value in r.items():
            equipment_data[field] = value
        equipment_data_list.append(equipment_data)
    return equipment_data_list

async def update_equipment_location(user_id: int, equipment_id: int, location: str):
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("UPDATE equipment SET location=$3 WHERE user_id=$1 AND equipment_id=$2 RETURNING *")
    result = await stmt.fetch(user_id, equipment_id, location)
    await conn.close()
    return result

async def update_equipment_stars(user_id: int, equipment_id: int, amount: int):
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("UPDATE equipment SET stars=stars + $3 WHERE user_id=$1 AND equipment_id=$2 RETURNING *")
    result = await stmt.fetch(user_id, equipment_id, amount)
    await conn.close()
    return result

async def update_equipment_bonus(user_id: int, equipment_id: int, bonus: str):
    conn = await asyncpg.connect(PSQL_CONNECTION_URL)
    stmt = await conn.prepare("UPDATE equipment SET bonus=$3 WHERE user_id=$1 AND equipment_id=$2 RETURNING *")
    result = await stmt.fetch(user_id, equipment_id, bonus)
    await conn.close()
    return result


if __name__ == '__main__':
    #print(asyncio.get_event_loop().run_until_complete(update_user_cave(124668192948748288, 'Beginner Cave')))
    #print(asyncio.get_event_loop().run_until_complete(get_equipment_for_user(124668192948748288)))
    print(asyncio.get_event_loop().run_until_complete(insert_equipment(124668192948748288, 6400, 'inventory')))
