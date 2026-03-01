import os
import sys
import django
import asyncio
from asgiref.sync import sync_to_async
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

load_dotenv()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "basis_lead_system.settings")
django.setup()

from leads.models import Lead

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


class LeadForm(StatesGroup):
    name = State()
    phone = State()
    service = State()
    budget = State()
    message = State()


@dp.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    await message.answer("Как вас зовут?")
    await state.set_state(LeadForm.name)


@dp.message(LeadForm.name)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите номер телефона:")
    await state.set_state(LeadForm.phone)


@dp.message(LeadForm.phone)
async def get_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Тип услуги? (training / constructor / furniture)")
    await state.set_state(LeadForm.service)


@dp.message(LeadForm.service)
async def get_service(message: types.Message, state: FSMContext):
    await state.update_data(service=message.text.lower())
    await message.answer("Введите бюджет (только цифры):")
    await state.set_state(LeadForm.budget)


@dp.message(LeadForm.budget)
async def get_budget(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Введите только цифры.")
        return

    await state.update_data(budget=int(message.text))
    await message.answer("Опишите задачу:")
    await state.set_state(LeadForm.message)


@dp.message(LeadForm.message)
async def get_message(message: types.Message, state: FSMContext):
    data = await state.get_data()

    @sync_to_async
    def create_lead(data, message_text):
        score = 0

        if data["budget"] > 300000:
            score += 3

        if data["service"] == "constructor":
            score += 2

        if "срочно" in message_text.lower():
            score += 2

        is_hot = score >= 5

        lead = Lead.objects.create(
            name=data["name"],
            phone=data["phone"],
            service_type=data["service"],
            budget=data["budget"],
            message=message_text,
            score=score,
            is_hot=is_hot,
        )

        return lead
    lead = await create_lead(data, message.text)

    if lead.is_hot:
        await message.answer("🔥 Ваша заявка приоритетная! Мы скоро свяжемся.")

        await bot.send_message(
            ADMIN_ID,
            f"🔥 Новый горячий лид!\n\n"
            f"Имя: {lead.name}\n"
            f"Телефон: {lead.phone}\n"
            f"Бюджет: {lead.budget}"
        )

    else:
        await message.answer("Спасибо! Мы свяжемся с вами.")

    await state.clear()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())