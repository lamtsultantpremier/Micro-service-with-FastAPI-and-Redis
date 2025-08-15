from redis_om import get_redis_connection
import configs
import redis

redis_connection = redis.Redis(
    host = configs.HOST,
    port = configs.PORT,
    password = configs.PASSWORD,
    decode_responses = True
)