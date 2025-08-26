import redis

r = redis.Redis(decode_responses=True)

r.set('food', 'Fried chicken') #food stores Fried chicken

r.close()
