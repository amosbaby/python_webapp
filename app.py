#!/usr/bin/dev/python3
# -*- coding:utf-8 -*-
import logging; logging.basicConfig(level=logging.INFO)
import asyncio,os,json,time
from datetime import datetime
from aiohttp import web

from aiohttp import web
#入口方法
async def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'),content_type='text/html')


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    app.router.add_route('GET','/hello/{name}',hello)
    srv = await loop.create_server(app.make_handler(),'127.0.0.1',8000)
    print('Server started at http://localhost:8000....')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()


