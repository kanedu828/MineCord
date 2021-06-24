from discord.ext import commands

class CustomCooldownMapping(commands.CooldownMapping):
    def __init__(self, factory):
        super().__init__(commands.Cooldown(1, 10, commands.BucketType.user))
        self._factory = factory

    def copy(self):
        ret = DynamicCooldownMapping(self._factory, self._type)
        ret._cache = self._cache.copy()
        return ret

    @property
    def valid(self):
        return True


    async def get_bucket(self, message, current=None):
        if self._cooldown.type is commands.BucketType.default:
            return self._cooldown
        self._verify_cache_integrity(current)
        key = self._bucket_key(message)
        if key not in self._cache:
            bucket = await self._factory(message)
            self._cache[key] = bucket
        else:
            bucket = self._cache[key]

        return bucket
