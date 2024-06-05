from aiogram import Router, tupes


echo_router = Router


@echo_router.message()
sync def echo_handler(mesage: types.Message):
    await message.reply(message.test)