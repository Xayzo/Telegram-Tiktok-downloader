from aiogram import types
from bot import dp, bot
from bot.api import MobileTikTokAPI, TikTokAPI


platforms = [MobileTikTokAPI(), TikTokAPI()]


@dp.message_handler()
async def get_message(message: types.Message):
    lol = await message.reply("Mengunduh video...")
    for api in platforms:
        if videos := [v for v in await api.handle_message(message) if v and v.content]:
            for video in videos:
                lol = await message.reply("Mengunggah video...")
                await bot.send_video(
                    message.chat.id, video.content, reply_to_message_id=message.message_id
                )
                await lol.delete()
            break

@dp.message_handler(commands=['start'], commands_prefix='!/&')
async def start(message: types.Message):
    await message.reply("Hai, aku adalah Tiktok Downloader Bot, bot Telegram yang diciptakan untuk mendownload video dari Tiktok tanpa watermark\n\n By @DionProjects")

@dp.message_handler(commands=['help'], commands_prefix='!/&')
async def start(message: types.Message):
    await message.reply("Untuk mengunduh video dari Tiktok, cukup kirimkan tautan video tiktok anda disini")
