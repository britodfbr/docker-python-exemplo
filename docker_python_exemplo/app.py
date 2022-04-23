from flask import Flask
from redis import Redis

import os

host_redis = os.environ.get('HOST_REDIS', 'redis')
port_redis = os.environ.get('PORT_REDIS', 6379)

app = Flask(__name__)
redis = Redis(host=host_redis, port=port_redis)


@app.route('/')
def hello():
    redis.incr('hits')
    return 'Hello World! %s times' % redis.get('hits')

