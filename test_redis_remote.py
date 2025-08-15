# test_redis_remote.py
import redis
from dotenv import load_dotenv
import os

load_dotenv()
r = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    password=os.getenv("REDIS_PASSWORD")
)

try:
    if r.ping():
        print("✅ Connected to Redis on DockerHost!")

    r.set("machine:base-pc", "Connected from 192.168.0.93")
    value = r.get("machine:base-pc")
    print("💡 Value:", value.decode())

except Exception as e:
    print("❌ Failed to connect:", e)