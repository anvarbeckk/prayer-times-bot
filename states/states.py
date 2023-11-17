from aiogram.dispatcher.filters.state import State, StatesGroup


class UserState(StatesGroup):
    get_city = State()
    remind_p_time = State()

