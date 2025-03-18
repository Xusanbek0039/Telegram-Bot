import asyncio
import wikipedia
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

wikipedia.set_lang("uz")
TOKEN = "6699105976:AAFPvHPn0AF-OvYy1dP-rrBpdWKpFMxmEJw"

dp = Dispatcher()


@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("IT Creative. Xush kelibsiz!")


@dp.message()
async def sendWiki(message: Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except wikipedia.exceptions.PageError:
        await message.answer("Bu mavzuga oid maqola topilmadi.")
    except wikipedia.exceptions.DisambiguationError:
        await message.answer("Bu mavzu juda umumiy, iltimos, aniqroq so‘rov yuboring.")


async def main() -> None:
    async with Bot(token=TOKEN) as bot:
        await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
