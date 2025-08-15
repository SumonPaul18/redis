from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='192.168.0.207', port=6379, db=0, decode_responses=True)

@app.route('/')
def index():
    r.incr("visitors")  # Increase counter
    count = r.get("visitors")
    return f"<h1>Hello! You are visitor #{count}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)