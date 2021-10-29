from pyrogram import *

import asyncio

api_id = API_ID
api_hash = API_HASH

bot_tok = BOT_TOKEN


plugins = dict(root='plugins')


app = Client('S_Name', api_id, api_hash, bot_token=bot_tok, plugins=plugins)


app.run()
