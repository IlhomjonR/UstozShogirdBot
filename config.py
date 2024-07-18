from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

from environs import Env

env = Env()

env.read_env()

API_TOKEN = env('API_TOKEN')
API_TOKEN = env('ADMINS')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, parse_mode='html')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)