@dp.message(Command("picture"))
async def picture_handler(message: types.Message):
    file = types.FSInpputFile("images/cat.jpg")
    #await message.answer_photo
    (photo=file, caption = "Kotik")
