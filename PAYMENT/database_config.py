from redisorm import redis
import configs

redis_connection = redis.Redis(
    host = configs.HOST,
    password = configs.PASSWORD,
    port = configs.PORT,
    decode_responses = True
)