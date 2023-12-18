import asyncio
from time import sleep


from aiogram import Router
from aiogram.types import Message
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters.command import Command

from newsapi import NewsApiClient

dp = Dispatcher()
bot = Bot(
    "6914183611:AAGueSkjiNJWekr5-cdtLd7rZBwJXofp2nY",
    parse_mode=ParseMode.HTML
)
router = Router(name="News Router")
newsapi = NewsApiClient(api_key="be4c897776e9438d8decf7c9277ef726")


@router.message(Command('news'))
async def news(message: Message) -> None:
    habarlar = newsapi.get_sources(
        category="technology",
        # language="en",
        # country="us"
    )
    for habar in habarlar['sources']:
        text = f"ID: {habar['id']}\n"\
            f"Name: {habar['name']}\n"\
            f"Description: {habar['description']}\n"\
            f"Source: {habar['url']}"
        await message.reply(text=text)
        sleep(3)


async def main() -> None:
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
