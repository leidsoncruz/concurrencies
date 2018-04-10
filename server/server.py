import json
import os
import time
import asyncio

from quart import Quart
from flask import Flask


app = Quart(__name__)

@asyncio.coroutine
def load_json(show):
    with open('{0}/server/fixtures/{1}.json'.format(os.getcwd(), show)) as data:
        data_json = json.load(data)
        yield from asyncio.sleep(2)
        return json.dumps(data_json)

@app.route("/<show>")
async def get_show(show):
    return await load_json(show)


app.run()
