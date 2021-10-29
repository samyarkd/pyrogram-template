from pyrogram import *
import asyncio


@Client.on_message(group=1)
async def help(client, message):
         await message.reply('Bot is Working !')
