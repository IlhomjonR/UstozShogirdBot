
# https://t.me/UstozShogirdBot
from aiogram import Bot, Dispatcher, executor, types
from inline_btns import *

from states import *

from aiogram.dispatcher import FSMContext
from states import *

from config import dp, bot, ADMINS



async def command_menu(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'start'),
        ]
    )


@dp.message_handler(commands=['start'], state='*')
async def start_command(message: types.Message, state: FSMContext):
    await state.finish()
    btn = await start_command_btn()
    await message.answer(text=f"""
<b>Assalom alaykum {message.from_user.first_name}
UstozShogird kanalining rasmiy botiga xush kelibsiz</b>

/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!""", reply_markup=btn)


@dp.message_handler(commands=['help'])
async def start_command(message: types.Message):
    await message.answer(text=f"""
UzGeeks faollari tomonidan tuzilgan Ustoz-Shogird kanali. 

Bu yerda Programmalash bo`yicha
  #Ustoz,  
  #Shogird,
  #oquvKursi,
  #Sherik,  
  #Xodim va 
  #IshJoyi 
 topishingiz mumkin. 

E'lon berish: @UstozShogirdBot

Admin @UstozShogirdAdminBot""")


@dp.message_handler(content_types=['text'], state=AdminStates.yes_or_no)
async def yes_or_no_state(message: types.Message, state: FSMContext):
    text = message.text
    if text == "HA":
        for admin in ADMINS:
            btn = await admin_btn()
            data = await state.get_data()
            await state.finish()
            await bot.send_message(admin, data.get('context'), reply_markup=btn)
    elif text == "YO'Q":
        await state.finish()
        await start_command(message)


@dp.callback_query_handler(text="yes")
async def admin_yes_callback(call: types.CallbackQuery):
    context = call.message.text
    await call.answer()
    await bot.send_message(-1001542180736, context)


@dp.message_handler(text="Sherik kerak")
async def start_command(message: types.Message):
    await message.answer(text=f"""
Sherik topish uchun ariza berish

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.""")
    await message.answer("Ism, familiyangizni kiriting?")
    await RegSherikStates.name.set()


@dp.message_handler(state=RegSherikStates.name)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("""
🕑 Yosh: 

Yoshingizni kiriting?
Masalan, 19""")
    await RegSherikStates.age.set()


@dp.message_handler(state=RegSherikStates.age)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("""
📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#""")
    await RegSherikStates.tech.set()


@dp.message_handler(state=RegSherikStates.tech)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(tech=message.text)
    await message.answer("""
📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67""")
    await RegSherikStates.number.set()


@dp.message_handler(state=RegSherikStates.number)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(number=message.text)
    await message.answer("""
🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.""")
    await RegSherikStates.place.set()


@dp.message_handler(state=RegSherikStates.place)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(place=message.text)
    await message.answer("""
💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?""")
    await RegSherikStates.price.set()


@dp.message_handler(state=RegSherikStates.price)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer("""
👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba""")
    await RegSherikStates.job.set()


@dp.message_handler(state=RegSherikStates.job)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(job=message.text)
    await message.answer("""
🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00""")
    await RegSherikStates.time.set()


@dp.message_handler(state=RegSherikStates.time)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(time=message.text)
    await message.answer("""
🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering.""")
    await RegSherikStates.goal.set()


@dp.message_handler(state=RegSherikStates.goal)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    goal = message.text
    btn = await yesno_btn()
    data = await state.get_data()
    context = (
 f"""Sherik kerak:

🏅 Sherik: {data.get('name')}
🕑 Yosh: {data.get('age')}
📚 Texnologiya: {data.get('tech')}
🇺🇿 Telegram: @{message.from_user.username}
📞 Aloqa: {data.get('number')} 
🌐 Hudud: {data.get('place')}
💰 Narxi: {data.get('price')} 
👨🏻‍💻 Kasbi: {data.get('job')}
🕰 Murojaat qilish vaqti: {data.get('time')} 
🔎 Maqsad: {goal}

#sherik""")
    await message.answer(context, reply_markup=btn)
    await state.update_data(context=context)
    await AdminStates.yes_or_no.set()


@dp.message_handler(text="Ish joyi kerak")
async def start_command(message: types.Message):
    await message.answer(text=f"""
Ish joyi topish uchun ariza berish

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.""")
    await message.answer("Ism, familiyangizni kiriting?")
    await RegIshjoyiStates.name.set()


@dp.message_handler(state=RegIshjoyiStates.name)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("""
🕑 Yosh: 

Yoshingizni kiriting?
Masalan, 19""")
    await RegIshjoyiStates.age.set()


@dp.message_handler(state=RegIshjoyiStates.age)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("""
📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#""")
    await RegIshjoyiStates.tech.set()


@dp.message_handler(state=RegIshjoyiStates.tech)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(tech=message.text)
    await message.answer("""
📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67""")
    await RegIshjoyiStates.number.set()


@dp.message_handler(state=RegIshjoyiStates.number)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(number=message.text)
    await message.answer("""
🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.""")
    await RegIshjoyiStates.place.set()


@dp.message_handler(state=RegIshjoyiStates.place)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(place=message.text)
    await message.answer("""
💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?""")
    await RegIshjoyiStates.price.set()


@dp.message_handler(state=RegIshjoyiStates.price)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer("""
👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba""")
    await RegIshjoyiStates.job.set()


@dp.message_handler(state=RegIshjoyiStates.job)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(job=message.text)
    await message.answer("""
🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00""")
    await RegIshjoyiStates.time.set()


@dp.message_handler(state=RegIshjoyiStates.time)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(time=message.text)
    await message.answer("""
🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering.""")
    await RegIshjoyiStates.goal.set()


@dp.message_handler(state=RegIshjoyiStates.goal)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    goal = message.text
    btn = await yesno_btn()
    data = await state.get_data()
    context = (
 f"""Ish joyi kerak:

👨‍💼 Xodim: {data.get('name')}
🕑 Yosh: {data.get('age')}
📚 Texnologiya: {data.get('tech')}
🇺🇿 Telegram: @{message.from_user.username}
📞 Aloqa: {data.get('number')} 
🌐 Hudud: {data.get('place')}
💰 Narxi: {data.get('price')} 
👨🏻‍💻 Kasbi: {data.get('job')}
🕰 Murojaat qilish vaqti: {data.get('time')} 
🔎 Maqsad: {goal}

#ishJoyi""")
    await message.answer(context, reply_markup=btn)
    await state.update_data(context=context)
    await AdminStates.yes_or_no.set()


@dp.message_handler(text="Hodim kerak")
async def start_command(message: types.Message):
    await message.answer(text=f"""
Hodim topish uchun ariza berish

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.""")
    await message.answer("🎓 Idora nomi?")
    await RegHodimStates.office.set()


@dp.message_handler(state=RegHodimStates.office)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(office=message.text)
    await message.answer("""
📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#""")
    await RegHodimStates.tech.set()


@dp.message_handler(state=RegHodimStates.tech)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(tech=message.text)
    await message.answer("""
📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67""")
    await RegHodimStates.number.set()


@dp.message_handler(state=RegHodimStates.number)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(number=message.text)
    await message.answer("""
🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.""")
    await RegHodimStates.place.set()


@dp.message_handler(state=RegHodimStates.place)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(place=message.text)
    await message.answer("""
✍️Mas'ul ism sharifi?""")
    await RegHodimStates.name2.set()
    
    
@dp.message_handler(state=RegHodimStates.name2)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(name2=message.text)
    await message.answer("""
🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00""")
    await RegHodimStates.time.set()


@dp.message_handler(state=RegHodimStates.time)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(time=message.text)
    await message.answer("""
🕰 Ish vaqtini kiriting?""")
    await RegHodimStates.time2.set()
    
    
@dp.message_handler(state=RegHodimStates.time2)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(time2=message.text)
    await message.answer("""
💰 Maoshni kiriting?""")
    await RegHodimStates.price.set()


@dp.message_handler(state=RegHodimStates.price)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer("""
‼️ Qo`shimcha ma`lumotlar?""")
    await RegHodimStates.extra.set()

@dp.message_handler(state=RegHodimStates.extra)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    extra = message.text
    btn = await yesno_btn()
    data = await state.get_data()
    context = (
 f"""Xodim kerak:

🏢 Idora: {data.get("office")}
📚 Texnologiya: {data.get('tech')} 
🇺🇿 Telegram: @{message.from_user.username}
📞 Aloqa: {data.get('number')} 
🌐 Hudud: {data.get('place')}  
✍️ Mas'ul: {data.get('name2')} 
🕰 Murojaat vaqti: {data.get('time')} 
🕰 Ish vaqti: {data.get('time2')}  
💰 Maosh: {data.get('price')} 
‼️ Qo`shimcha: {extra}

#xodim""")
    await message.answer(context, reply_markup=btn)
    await state.update_data(context=context)
    await AdminStates.yes_or_no.set()


@dp.message_handler(text="Ustoz kerak")
async def start_command(message: types.Message):
    await message.answer(text=f"""
Ustoz topish uchun ariza berish

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.""")
    await message.answer("Ism, familiyangizni kiriting?")
    await RegUstozStates.name.set()


@dp.message_handler(state=RegUstozStates.name)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("""
🕑 Yosh: 

Yoshingizni kiriting?
Masalan, 19""")
    await RegUstozStates.age.set()


@dp.message_handler(state=RegUstozStates.age)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("""
📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#""")
    await RegUstozStates.tech.set()


@dp.message_handler(state=RegUstozStates.tech)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(tech=message.text)
    await message.answer("""
📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67""")
    await RegUstozStates.number.set()


@dp.message_handler(state=RegUstozStates.number)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(number=message.text)
    await message.answer("""
🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.""")
    await RegUstozStates.place.set()


@dp.message_handler(state=RegUstozStates.place)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(place=message.text)
    await message.answer("""
💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?""")
    await RegUstozStates.price.set()


@dp.message_handler(state=RegUstozStates.price)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer("""
👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba""")
    await RegUstozStates.job.set()


@dp.message_handler(state=RegUstozStates.job)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(job=message.text)
    await message.answer("""
🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00""")
    await RegUstozStates.time.set()


@dp.message_handler(state=RegUstozStates.time)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(time=message.text)
    await message.answer("""
🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering.""")
    await RegUstozStates.goal.set()


@dp.message_handler(state=RegUstozStates.goal)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    goal = message.text
    btn = await yesno_btn()
    data = await state.get_data()
    context = (
 f"""Ustoz kerak:

🎓 Shogird: {data.get('name')}
🕑 Yosh: {data.get('age')}
📚 Texnologiya: {data.get('tech')}
🇺🇿 Telegram: @{message.from_user.username}
📞 Aloqa: {data.get('number')} 
🌐 Hudud: {data.get('place')}
💰 Narxi: {data.get('price')} 
👨🏻‍💻 Kasbi: {data.get('job')}
🕰 Murojaat qilish vaqti: {data.get('time')} 
🔎 Maqsad: {goal}

#shogird""")
    await message.answer(context, reply_markup=btn)
    await state.update_data(context=context)
    await AdminStates.yes_or_no.set()
    

@dp.message_handler(text="Shogird kerak")
async def start_command(message: types.Message):
    await message.answer(text=f"""
Shogird topish uchun ariza berish

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.""")
    await message.answer("Ism, familiyangizni kiriting?")
    await RegShogirdStates.name.set()


@dp.message_handler(state=RegShogirdStates.name)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("""
🕑 Yosh: 

Yoshingizni kiriting?
Masalan, 19""")
    await RegShogirdStates.age.set()


@dp.message_handler(state=RegShogirdStates.age)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("""
📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#""")
    await RegShogirdStates.tech.set()


@dp.message_handler(state=RegShogirdStates.tech)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(tech=message.text)
    await message.answer("""
📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67""")
    await RegShogirdStates.number.set()


@dp.message_handler(state=RegShogirdStates.number)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(number=message.text)
    await message.answer("""
🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting.""")
    await RegShogirdStates.place.set()


@dp.message_handler(state=RegShogirdStates.place)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(place=message.text)
    await message.answer("""
💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?""")
    await RegShogirdStates.price.set()


@dp.message_handler(state=RegShogirdStates.price)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer("""
👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba""")
    await RegShogirdStates.job.set()


@dp.message_handler(state=RegShogirdStates.job)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(job=message.text)
    await message.answer("""
🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00""")
    await RegShogirdStates.time.set()


@dp.message_handler(state=RegShogirdStates.time)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    await state.update_data(time=message.text)
    await message.answer("""
🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering.""")
    await RegShogirdStates.goal.set()


@dp.message_handler(state=RegShogirdStates.goal)
async def register_next_step_handler(message: types.Message, state: FSMContext):
    goal = message.text
    btn = await yesno_btn()
    data = await state.get_data()
    context = (
 f"""Sherik kerak:

🎓 Ustoz: {data.get('name')}
🕑 Yosh: {data.get('age')}
📚 Texnologiya: {data.get('tech')}
🇺🇿 Telegram: @{message.from_user.username}
📞 Aloqa: {data.get('number')} 
🌐 Hudud: {data.get('place')}
💰 Narxi: {data.get('price')} 
👨🏻‍💻 Kasbi: {data.get('job')}
🕰 Murojaat qilish vaqti: {data.get('time')} 
🔎 Maqsad: {goal}

#shogird""")
    await message.answer(context, reply_markup=btn)
    await state.update_data(context=context)
    await AdminStates.yes_or_no.set()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=command_menu)
