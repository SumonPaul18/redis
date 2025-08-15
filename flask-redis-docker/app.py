from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis (now named 'redis' in Docker network)
r = redis.Redis(
    host='redis',  # This is the service name in docker-compose
    port=6379,
    db=0,
    decode_responses=True,
    socket_connect_timeout=5
)

@app.route('/')
def index():
    try:
        r.incr('visitors')
        count = r.get('visitors')
        return f"<h1 style='text-align: center; margin-top: 50px;'>🌍 You are visitor #{count}!</h1>"
    except Exception as e:
        return f"<h1>Redis connection failed: {e}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)