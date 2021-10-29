from pyrogram import *
import asyncio
import random

ansTF = [":| you too.... bitch", 'برو جناب خدا روزیتو جای دیگ بده تو مال این حرفا نیستی',
         'فحش یادت دادن جوون', "i don't give a shit :)", '(•ˋ _ ˊ•)', '🖕']
aksTF = ['fuck you bitch', 'کیرم تو کونت', 'fuck you',
         'فاک غلام', 'حالت خوش نیست', 'کوبص نگو', 'کص نگو', 'نکص', '🖕']

tasA = ['تاس بنداز', 'غلام تاس بنداز', 'تاس', 'غلام تاسی',
        'غلام بتاس', 'تاس غلام', 'تاس میخوام غلام']
tasS = [1, 2,  6, 'نمیندازم', 'نه', 'حوصله == 0', 'ولم کن ', 'ولم کن ', 'ولم کن ', 'حال داری جناب ',
        'دوباره بگو نشنیدم', 3, 4, 5, ':))))))))', '🎲', 'سطحت پایین تر از این حرفاست', 'حوصله صفر']


@Client.on_message(filters.text, group=7)
async def help(client, message):

    try:

        if (message.text in aksTF) & (message.reply_to_message.from_user.username == 'samyartestbot'):
            await message.reply(ansTF[random.randint(0, 5)])
    except Exception as e:
        print(e)
    if message.text in tasA:
        await message.reply(tasS[random.randint(0, tasS.__len__() - 1)])
