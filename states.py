from aiogram.dispatcher.filters.state import State, StatesGroup


class RegSherikStates(StatesGroup):
    name = State()
    age = State()
    tech = State()
    number = State()
    place = State()
    price = State()
    job = State()
    time = State()
    goal = State()


class RegIshjoyiStates(StatesGroup):
    name = State()
    age = State()
    tech = State()
    number = State()
    place = State()
    price = State()
    job = State()
    time = State()
    goal = State()


class RegHodimStates(StatesGroup):
    office = State()
    tech = State()
    number = State()
    place = State()
    name2 = State()
    time = State()
    time2 = State()
    price = State()
    extra = State()


class RegUstozStates(StatesGroup):
    name = State()
    age = State()
    tech = State()
    number = State()
    place = State()
    price = State()
    job = State()
    time = State()
    goal = State()


class RegShogirdStates(StatesGroup):
    name = State()
    age = State()
    tech = State()
    number = State()
    place = State()
    price = State()
    job = State()
    time = State()
    goal = State()


class AdminStates(StatesGroup):
    yes_or_no = State()