from pyrogram import *

import asyncio

api_id = 1482997
api_hash = '04115d69ede1ded22b48823ad5dadd95'

bot_tok = '1834123008:AAEIgwVgBhmXP_eLZLs6gXUoaqQxRQxhWYY'


plugins = dict(root='plugins')


app = Client('glm', api_id, api_hash, bot_token=bot_tok, plugins=plugins)


app.run()
