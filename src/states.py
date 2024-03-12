from aiogram.fsm.state import StatesGroup, State


class VendorCodeState(StatesGroup):
    vendor_code = State()
