import asyncpg
import asyncio


class DBUtil:

    def __init__(self, pool):
        self.pool = pool

    def get_conn(self):
        return self.pool.acquire()

    async def get_all_users(self):
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                stmt = await conn.prepare("SELECT * FROM users")

    async def insert_user(self, id: int):
        '''
            Inserts a user into the database.
            Columns: user_id, exp, cave, gold
        '''
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                stmt = await conn.prepare("INSERT INTO users(user_id) VALUES ($1) RETURNING *")
                result = await stmt.fetch(id)
                return result

    async def get_user(self, id: int):
        '''
            Retrieves an user and returns the columns and values as a dictionary.
            If the user is not in the database, the user is first inserted and then returned.
        '''
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                stmt = await conn.prepare("SELECT * FROM users WHERE user_id=$1")
                result = await stmt.fetch(id)
                if not result:
                    result = await insert_user(id)
                user_data = {}
                for field, value in result[0].items():
                    user_data[field] = value
                return user_data

    async def update_user_exp(self, user_id: int, amount: int):
        '''
            Adds amount to the user's exp. Returns a record object.
        '''
        await self.get_user(user_id)
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                stmt = await conn.prepare("UPDATE users SET exp=exp + $2 WHERE user_id=$1 RETURNING *")
                result = await stmt.fetch(user_id, amount)
                return result

    async def set_user_exp(self, user_id: int, amount: int):
        '''
            Set amount to the user's exp. Returns a record object.
        '''
        await self.get_user(user_id)
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                stmt = await conn.prepare("UPDATE users SET exp=$2 WHERE user_id=$1 RETURNING *")
                result = await stmt.fetch(user_id, amount)
                return result

    async def set_user_last_drill(self, user_id: int, dt):
        '''
            Set amount to the user's exp. Returns a record object.
        '''
        await self.get_user(user_id)
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                stmt = await conn.prepare("UPDATE users SET last_drill=$2 WHERE user_id=$1 RETURNING *")
                result = await stmt.fetch(user_id, dt)
                return result

    async def update_user_gold(self, user_id: int, amount: int):
        '''
            Adds amount to the user's gold. Returns a record object.
        '''
        await self.get_user(user_id)
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                stmt = await conn.prepare("UPDATE users SET gold=gold + $2 WHERE user_id=$1 RETURNING *")
                result = await stmt.fetch(user_id, amount)
                return result

    async def set_user_gold(self, user_id: int, amount: int):
        '''
            Set amount to the user's gold. Returns a record object.
        '''
        await self.get_user(user_id)
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                stmt = await conn.prepare("UPDATE users SET gold=$2 WHERE user_id=$1 RETURNING *")
                result = await stmt.fetch(user_id, amount)
                return result

    async def update_user_blessings(self, user_id: int, amount: int):
        '''
            Adds amount to the user's gold. Returns a record object.
        '''
        await self.get_user(user_id)
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                stmt = await conn.prepare("UPDATE users SET blessings=blessings + $2 WHERE user_id=$1 RETURNING *")
                result = await stmt.fetch(user_id, amount)
                return result

    async def update_user_cave(self, user_id: int, cave: str):
        '''
            Updates an user's cave. Returns a record object.
        '''
        await self.get_user(user_id)
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                stmt = await conn.prepare("UPDATE users SET cave=$2 WHERE user_id=$1 RETURNING *")
                result = await stmt.fetch(user_id, cave)
                return result

    async def update_user_dungeon(self, user_id: int, dungeon: str):
        '''
            Updates an user's cave. Returns a record object.
        '''
        await self.get_user(user_id)
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                stmt = await conn.prepare("UPDATE users SET dungeon=$2 WHERE user_id=$1 RETURNING *")
                result = await stmt.fetch(user_id, dungeon)
                return result

    async def get_top_users_for_exp(self, amount: int):
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                stmt = await conn.prepare("SELECT * FROM users ORDER BY exp DESC LIMIT $1")
                result = await stmt.fetch(amount)
                user_list = []
                for r in result:
                    user_data = {}
                    for field, value in r.items():
                        user_data[field] = value
                    user_list.append(user_data)
                return user_list

    async def insert_equipment(self, user_id: int, equipment_id: int, location: str):
        await self.get_user(user_id)
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                stmt = await conn.prepare("""
                    INSERT INTO equipment(equipment_id, user_id, location)
                    VALUES ($1, $2, $3)
                    RETURNING equipment_instance_id, equipment_id, user_id, location, bonus, stars""")
                result = await stmt.fetch(equipment_id, user_id, location)
                return result

    async def get_equipment_for_user(self, user_id: int):
        '''
            Gets all equipment attatched to a user id. Returns as a list of dictionaries.
        '''
        await self.get_user(user_id)
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                stmt = await conn.prepare("SELECT * FROM equipment WHERE user_id=$1")
                result = await stmt.fetch(user_id)
                equipment_data_list = []
                for r in result:
                    equipment_data = {}
                    for field, value in r.items():
                        equipment_data[field] = value
                    equipment_data_list.append(equipment_data)
                return equipment_data_list

    async def update_equipment_location(self, user_id: int, equipment_id: int, location: str):
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                stmt = await conn.prepare("UPDATE equipment SET location=$3 WHERE user_id=$1 AND equipment_id=$2 RETURNING *")
                result = await stmt.fetch(user_id, equipment_id, location)
        return result

    async def update_equipment_stars(self, user_id: int, equipment_id: int, amount: int):
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                stmt = await conn.prepare("UPDATE equipment SET stars=stars + $3 WHERE user_id=$1 AND equipment_id=$2 RETURNING *")
                result = await stmt.fetch(user_id, equipment_id, amount)
        return result

    async def update_equipment_bonus(self, user_id: int, equipment_id: int, bonus: str):
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                stmt = await conn.prepare("UPDATE equipment SET bonus=$3 WHERE user_id=$1 AND equipment_id=$2 RETURNING *")
                result = await stmt.fetch(user_id, equipment_id, bonus)
        return result

    async def update_item_count(self, user_id, item_id, amount):
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                result = await conn.fetch(
                    'SELECT * FROM item WHERE user_id=$1 AND item_id=$2',
                    user_id,
                    item_id
                )
                if result:
                    if result[0]['count'] + amount < 0:
                        amount = -result['count']
                    result = await conn.fetch(
                        '''UPDATE item
                        SET count=count + $1
                        WHERE user_id=$2 AND item_id=$3
                        RETURNING *''',
                        amount,
                        user_id,
                        item_id
                    )
                elif amount >= 0:
                    result = await conn.fetch(
                        '''INSERT INTO item(item_id, user_id, count)
                        VALUES ($1, $2, $3)
                        RETURNING *''',
                        item_id,
                        user_id,
                        amount
                    )
                return result

    async def update_dungeon_durability(self, user_id, dungeon_name, amount):
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                result = await conn.fetch(
                    '''UPDATE dungeon_instance
                    SET durability=durability + $1
                    WHERE user_id=$2 AND dungeon_name=$3
                    RETURNING *''',
                    amount,
                    user_id,
                    dungeon_name
                )
                return result

    async def get_dungeon_instance(self, user_id, dungeon_name):
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                result = await conn.fetch(
                    'SELECT * FROM dungeon_instance WHERE user_id=$1 AND dungeon_name=$2',
                    user_id,
                    dungeon_name
                )
                return result

    async def insert_dungeon_instance(self, user_id, dungeon_name, durability, clear_rate):
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                result = await conn.fetch(
                    '''INSERT INTO dungeon_instance(dungeon_name, user_id, durability, clear_rate)
                    VALUES ($1, $2, $3, $4)
                    RETURNING *''',
                    dungeon_name,
                    user_id,
                    durability,
                    clear_rate
                )
                return result
