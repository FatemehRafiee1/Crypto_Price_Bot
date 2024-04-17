import logging
import yaml
from aiogram import Bot, Dispatcher, types

import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.markdown import hbold

from utils import get_change, get_color
from coinex import keyword_responses

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

bot = None
wait_for_coin = False
dp = Dispatcher()

builder = InlineKeyboardBuilder()
for k in keyword_responses.keys():
    builder.add(InlineKeyboardButton(text = k[1:], callback_data=k))
builder.adjust(3, 4)
builder = builder.as_markup()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Welcome, {hbold(message.from_user.full_name)}.", reply_markup=builder)

@dp.message(Command('menu'))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Which coin do you choose {hbold(message.from_user.first_name)}?", reply_markup=builder)

@dp.message()
async def command_handler(message: Message) -> None:
    global wait_for_coin

    if wait_for_coin:
        try:
            now, hc, dc, wc = get_change(config, message.text)
            await message.answer(
                f"🔹 {hbold((message.text).upper())}: {now[-1]['close']} \n\n 📌Changes in: \n\n"
                f"{get_color(hc)} Last hour  =>  {hc} % \n\n"
                f"{get_color(dc)} Last day  =>  {dc} % \n\n"
                f"{get_color(wc)} Last week  =>  {wc} %"
            )

        except TypeError:
            await message.answer("Didn't find such symbol.")

        wait_for_coin = False
        
    else:
        await message.answer("Sorry, wrong command.\nTo access possible options, type /menu.")

@dp.callback_query() 
async def callback_handler(callback_query: types.CallbackQuery):
    global wait_for_coin
    keyword = callback_query.data
    text_response = keyword_responses.get(keyword)

    if keyword == '/other':
        wait_for_coin = True
        await callback_query.message.answer('Waiting for you to type.\nIt should be in the right format. (e.g: BTCUSDT)')
    else:
        now, hc, dc, wc = get_change(config, text_response)
        await callback_query.message.answer(
            f"🔹 {hbold(keyword[1:])}: {now[-1]['close']} $\n\n 📌Changes in: \n\n"
            f"{get_color(hc)} Last hour  =>  {hc} % \n\n"
            f"{get_color(dc)} Last day  =>  {dc} % \n\n"
            f"{get_color(wc)} Last week  =>  {wc} %"
        )

async def main() -> None:
    telegram_bot_token = config["telegram_bot_token"]
    global bot
    bot = Bot(token=telegram_bot_token, default=DefaultBotProperties(parse_mode="HTML"))
    
    await dp.start_polling(bot)

if __name__ == "__main__":       
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
