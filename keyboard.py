import types
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup , InlineKeyboardButton

def random_sele():
	tecla_reg = ['🐉Escama de dragon','🌑Luz lunar','🥔Papa','🦅Nido alto','🐺Manada de lobos','🦌Cuerno de ciervo','🦈Dientes de Tiburón']
	tcl = random.sample(tecla_reg , 4)
	return tcl

def registro_Kb():
    reg_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    reg_kb.add(*[KeyboardButton(name) for name in random_sele()])
    return reg_kb

def admin_Kb():
    admin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    admin_kb.add(*[KeyboardButton(name) for name in ['⚔️Atacar','🗺Misiones','🛡Defender','🏅Yo','🏰Castillo','👥Clanes','Admin']])
    return admin_kb

def principal_Kb():
    prin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    prin_kb.add(*[KeyboardButton(name) for name in ['⚔️Atacar','🗺Misiones','🛡Defender','🏅Yo','🏰Castillo','👥Clanes']])
    return prin_kb

def castle_Kb():
    prin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    prin_kb.add(*[KeyboardButton(name) for name in ['⚒Taller','🍺Taberna','🛎Subasta','🏠Tienda','⚖️Intercambio', '⬅️Atras']])
    return prin_kb

def guild_Kb():
    prin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    prin_kb.add(*[KeyboardButton(name) for name in ['📦Stock','📋Lista','ℹ️Otros','🏕Misiones','🤝Alianza', '⬅️Atras']])
    return prin_kb

def atacar_dra_Kb():
    admin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    admin_kb.add(*[KeyboardButton(name) for name in ['🌑','🥔','🦅','🐺','🦌','🦈']])
    return admin_kb 

def atacar_lobo_Kb():
    admin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    admin_kb.add(*[KeyboardButton(name) for name in ['🐉','🌑','🥔','🦅','🦌','🦈']])
    return admin_kb 

def atacar_luna_Kb():
    admin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    admin_kb.add(*[KeyboardButton(name) for name in ['🐉','🥔','🦅','🐺','🦌','🦈']])
    return admin_kb

def atacar_papa_Kb():
    admin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    admin_kb.add(*[KeyboardButton(name) for name in ['🐉','🌑','🦅','🐺','🦌','🦈']])
    return admin_kb

def atacar_aguilas_Kb():
    admin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    admin_kb.add(*[KeyboardButton(name) for name in ['🐉','🌑','🥔','🐺','🦌','🦈']])
    return admin_kb   

def atacar_ciervos_Kb():
    admin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    admin_kb.add(*[KeyboardButton(name) for name in ['🐉','🌑','🥔','🦅','🐺','🦈']])
    return admin_kb

def atacar_tiburon_Kb():
    admin_kb = ReplyKeyboardMarkup(resize_keyboard=True)
    admin_kb.add(*[KeyboardButton(name) for name in ['🐉','🌑','🥔','🦅','🐺','🦌']])
    return admin_kb  

def misionee_kb():
    kb = InlineKeyboardMarkup(row_width=3)
    button1 = InlineKeyboardButton(text="🌲Bosque",   callback_data="bosque")
    button2 = InlineKeyboardButton(text="🍄Pantano", callback_data="pantano")
    button3 = InlineKeyboardButton(text="🏔Valle",   callback_data="valle")
    button4 = InlineKeyboardButton(text="🗡Foray",   callback_data="foray")
    button5 = InlineKeyboardButton(text="📯Arena",   callback_data="arena")
    kb.add(button1, button2,button3,button4,button5)
    return kb