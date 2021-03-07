import telebot
import sqlite3
import logging
import time
import datetime
import conf
import flask
from keyboard import (admin_Kb, principal_Kb , registro_Kb,
    castle_Kb, guild_Kb, atacar_dra_Kb, atacar_lobo_Kb, atacar_luna_Kb, atacar_papa_Kb, atacar_aguilas_Kb, atacar_ciervos_Kb, atacar_tiburon_Kb)

# ###############################################################
# API_TOKEN = config.token
# WEBHOOK_HOST = '85.143.174.217'
# WEBHOOK_PORT = 8443  # 443, 80, 88 or 8443 (port need to be 'open')
# WEBHOOK_LISTEN = '0.0.0.0'  # In some VPS you may need to put here the IP addr
# WEBHOOK_SSL_CERT = './webhook_cert.pem'  # Path to the ssl certificate
# WEBHOOK_SSL_PRIV = './webhook_pkey.pem'  # Path to the ssl private key

# WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
# WEBHOOK_URL_PATH = "/%s/" % API_TOKEN
# # logger = telebot.logger
# # telebot.logger.setLevel(logger.info)
# bot = telebot.TeleBot(API_TOKEN)
# app = flask.Flask(__name__)


# # Empty webserver index, return nothing, just http 200
# @app.route('/', methods=['GET', 'HEAD'])
# def index():
#     return ''


# # Process webhook calls
# @app.route(WEBHOOK_URL_PATH, methods=['POST'])
# def webhook():
#     if flask.request.headers.get('content-type') == 'application/json':
#         json_string = flask.request.get_data().decode('utf-8')
#         update = telebot.types.Update.de_json(json_string)
#         bot.process_new_updates([update])
#         return ''
#     else:
#         flask.abort(403)
# ###############################################################


adminskeyboarhide = telebot.types.ReplyKeyboardRemove()

admins = ['JuanShotLC','Devil']

salfetka = '''
‼ modo de silencio! ‼️
Caminante! Prepárate para el ataque (⚔ataque) a ' Valiente Guerrero, Elegir un enemigo!' ‼️
 '''
logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)-3s]# %(levelname)-5s [%(asctime)s] %(message)s'
                    , level = logging.INFO)

bot = telebot.TeleBot(conf.token)


def niceprint(string):
    tabindex = 0
    out = ''
    for i in string:
        if i == ',':
            out += i
            out += '\n'
            out += '\t' * tabindex
            continue
        if i == '{':
            tabindex += 1
        if i == '}':
            tabindex -= 1
            out += '\n'
        out += i
    return out

@bot.message_handler(commands=['start'])
def send_welcome(message):
    userid = message.from_user.id
    username = message.from_user.username
             
    logging.info('USER: ' + str(username) + ' CMD: /start')

    conn = sqlite3.connect('castillowars.db')
    c = conn.cursor()

    userlist = []
    for row in c.execute('SELECT username FROM heroes'):
        userlist.append(row[0])

    if username in userlist:
        if username in admins:
            bot.send_message(message.chat.id, 'Ya Estas Registrado Admin', reply_markup=admin_Kb())
        else:
            bot.send_message(message.chat.id, 'Ya Estas Registrado', reply_markup=principal_Kb())
        conn.commit()
        conn.close()
    else:

        bot.send_sticker(message.chat.id, 'CAACAgEAAxkBAAEB7BdgOA8VimAAATplEjtXp0IRxejpASoAAiwBAAJ9BsBFdTpwxjEI5z0eBA')
        bot.send_message(message.chat.id, 'Elige el castillo al que jurarás lealtad 🗡', reply_markup=registro_Kb())
        
@bot.message_handler(func=lambda msg: msg.text == '🐉Escama de dragon')
def registro_user(message):
        logging.info('USER: ' + str(message.from_user.username) + ' CMD: Se unio para el Castillo 🐉Escama de dragon')

        # print(message)
        userid = message.from_user.id
        username = message.from_user.username
          
        flats = '🐉'   
        castle = 'Escama de dragon'      
        conn = sqlite3.connect('castillowars.db')
        c = conn.cursor()
        querry = "INSERT INTO heroes (id, username, heroflag, castlename, heroname) VALUES ('{}', '{}', '{}', '{}', '{}')".format(userid, username, flats, castle, username)
        c.execute(querry)
        conn.commit()
        conn.close()       
        bot.send_message(message.chat.id, '🎉Te unes a los valientes guerreros del Castillo de 🐉Escama de dragon.\n Date prisa y únete al chat de nuestros jugadores: @', reply_markup=principal_Kb())

@bot.message_handler(func=lambda msg: msg.text == '🦈Dientes De Tiburón')
def registro2_user(message):
        logging.info('USER: ' + str(message.from_user.username) + ' CMD: Se unio para el Castillo 🦈Dientes De Tiburón')

        # print(message)
        userid = message.from_user.id
        username = message.from_user.username
       
        flats = '🦈'   
        castle = 'Dientes De Tiburón'      
        conn = sqlite3.connect('castillowars.db')
        c = conn.cursor()
        querry = "INSERT INTO heroes (id, username, heroflag, castlename, heroname) VALUES ('{}', '{}', '{}', '{}', '{}')".format(userid, username, flats, castle, username)
        c.execute(querry)
        conn.commit()
        conn.close()       
        bot.send_message(message.chat.id, '🎉Te unes a los valientes guerreros del Castillo de 🦈Dientes De Tiburón.\n Date prisa y únete al chat de nuestros jugadores: @', reply_markup=principal_Kb())
 
@bot.message_handler(func=lambda msg: msg.text == '🦌Cuerno de ciervo')
def registro2_user(message):
        logging.info('USER: ' + str(message.from_user.username) + ' CMD: Se unio para el Castillo 🦌Cuerno de ciervo')

        # print(message)
        userid = message.from_user.id
        username = message.from_user.username

        flats = '🦌'   
        castle = 'Cuerno de ciervo'      
        conn = sqlite3.connect('castillowars.db')
        c = conn.cursor()
        querry = "INSERT INTO heroes (id, username, heroflag, castlename, heroname) VALUES ('{}', '{}', '{}', '{}', '{}')".format(userid, username, flats, castle, username)
        c.execute(querry)
        conn.commit()
        conn.close()       
        bot.send_message(message.chat.id, '🎉Te unes a los valientes guerreros del Castillo de 🦌Cuerno de ciervo.\n Date prisa y únete al chat de nuestros jugadores: @', reply_markup=principal_Kb())
 
@bot.message_handler(func=lambda msg: msg.text == '🦅Nido alto')
def registro2_user(message):
        logging.info('USER: ' + str(message.from_user.username) + ' CMD: Se unio para el Castillo 🦅Nido alto')

        # print(message)
        userid = message.from_user.id
        username = message.from_user.username
                     
        flats = '🦅'   
        castle = 'Nido alto'      
        conn = sqlite3.connect('castillowars.db')
        c = conn.cursor()
        querry = "INSERT INTO heroes (id, username, heroflag, castlename, heroname) VALUES ('{}', '{}', '{}', '{}', '{}')".format(userid, username, flats, castle, username)
        c.execute(querry)
        conn.commit()
        conn.close()       
        bot.send_message(message.chat.id, '🎉Te unes a los valientes guerreros del Castillo de 🦅Nido alto.\n Date prisa y únete al chat de nuestros jugadores: @', reply_markup=principal_Kb())
     
@bot.message_handler(func=lambda msg: msg.text == '🐺Manada de lobos')
def registro2_user(message):
        logging.info('USER: ' + str(message.from_user.username) + ' CMD: Se unio para el Castillo 🐺Manada de lobos')

        # print(message)
        userid = message.from_user.id
        username = message.from_user.username
        
        flats = '🐺'   
        castle = 'Manada de lobos'      
        conn = sqlite3.connect('castillowars.db')
        c = conn.cursor()
        querry = "INSERT INTO heroes (id, username, heroflag, castlename, heroname) VALUES ('{}', '{}', '{}', '{}', '{}')".format(userid, username, flats, castle, username)
        c.execute(querry)
        conn.commit()
        conn.close()       
        bot.send_message(message.chat.id, '🎉Te unes a los valientes guerreros del Castillo de 🐺Manada de lobos.\n Date prisa y únete al chat de nuestros jugadores: @', reply_markup=principal_Kb())

@bot.message_handler(func=lambda msg: msg.text == '🥔Papa')
def registro6_user(message):
        logging.info('USER: ' + str(message.from_user.username) + ' CMD: Se unio para el Castillo 🥔Papa')

        userid = message.from_user.id
        username = message.from_user.username

        flats = '🥔'   
        castle = 'Papa'      
        conn = sqlite3.connect('castillowars.db')
        c = conn.cursor()
        querry = "INSERT INTO heroes (id, username, heroflag, castlename, heroname) VALUES ('{}', '{}', '{}', '{}', '{}')".format(userid, username, flats, castle, username)
        c.execute(querry)
        conn.commit()
        conn.close()       
        bot.send_message(message.chat.id, '🎉Te unes a los valientes guerreros del Castillo de 🥔Papa.\n Date prisa y únete al chat de nuestros jugadores: @', reply_markup=principal_Kb())
 
@bot.message_handler(func=lambda msg: msg.text == '🌑Luz lunar')
def registro7_user(message):
        logging.info('USER: ' + str(message.from_user.username) + ' CMD: Se unio para el Castillo 🌑Luz lunar')

        userid = message.from_user.id
        username = message.from_user.username

        flats = '🌑'   
        castle = 'Luz lunar'      
        conn = sqlite3.connect('castillowars.db')
        c = conn.cursor()
        querry = "INSERT INTO heroes (id, username, heroflag, castlename, heroname) VALUES ('{}', '{}', '{}', '{}', '{}')".format(userid, username, flats, castle, username)
        c.execute(querry)
        conn.commit()
        conn.close()       
        bot.send_message(message.chat.id, '🎉Te unes a los valientes guerreros del Castillo de 🌑Luz lunar.\n Date prisa y únete al chat de nuestros jugadores: @', reply_markup=principal_Kb())
           
@bot.message_handler(func=lambda msg: msg.text == '🏅Yo')
def me(message):
    logging.info('USER: ' + str(message.from_user.username) + ' CMD: 🏅Yo')
    
    conn = sqlite3.connect('castillowars.db')
    c = conn.cursor()
    querry = "SELECT * from heroes where id = {}".format(message.from_user.id)
    logging.debug(querry)
    for i in c.execute(querry):
        logging.debug(str(i))

        if str(i[13]) == str('0'):
            out = '\n'
        else:
            out =   '🌟Felicidades! Nuevo nivel!🌟'+'\n' + 'Presiona'+' /level_up'+'\n \n'
            

        out +=   'La batalla de los 7 castillos comienza en ' +'\n \n'
        out +=   str(i[2]) + str(i[4]) + ' Maestro del Castillo de' + str(i[3]) + '\n'
        out += '🏅Nivel: ' + str(i[5]) + '\n'
        out += '⚔️Ataque: ' + str(i[7]) + ' 🛡Defensa: ' + str(i[8]) + '\n'
        out += '🔥Exp: ' + '0/'
        out +=  str(i[9]) + '\n'
        out += '❤️Vida:' + '300/'
        out +=  str(i[11]) + '\n'
        out += '🔋Stamina:' + '5/' 
        out +=  str(i[10]) + '\n'
        out += '💧Mana:' + '0/' 
        out +=  str(i[12]) + '\n'
        out += '💰' + str(i[13])

        if str(i[14]) == str('0'):
            out += ''            
        else:    
            out += '👝' + str(i[14]) 

        if str(i[15]) == str('0'):
            out += '\n \n'            
        else:
            out += '💎' + str(i[15]) + '\n'


        out += '🎽Euipamiento' + '⚔+' + 'nada' + '🛡+' + 'nada' + '\n'
        out += '🎒Bag: '
        out +=  str(i[25]) +' /inv' +'\n'

        if str(i[27]) == str('0'):           
            out += '\n'
        else:
            out += 'Mascota: ' +  str(i[27]) +' /pet'+ '\n' + '\n'

        out += 'Estado:' + '\n'
        out +=  str(i[29]) + '\n \n'
        out += 'More: /heroe'

        bot.send_message(message.chat.id, out,  parse_mode='HTML')
    conn.commit()
    conn.close()

@bot.message_handler(func=lambda msg: msg.text == '⚔️Atacar')
def me(message):
    userid = message.from_user.id
    username = message.from_user.username
             
    logging.info('USER: ' + str(message.from_user.username) + ' CMD: ⚔️Atacar')

    conn = sqlite3.connect('castillowars.db')
    c = conn.cursor()
    querry = "SELECT * from heroes where id = {}".format(message.from_user.id)
    logging.debug(querry)
    for i in c.execute(querry):
        logging.debug(str(i))

        if '🐉' == str(i[2]):
            bot.send_message(message.chat.id, 'AJa, ¿lo suficientemente audaz? ¡Elige un enemigo!', reply_markup=atacar_dra_Kb())

        if '🌑' == str(i[2]):
                 bot.send_message(message.chat.id, 'AJa, ¿lo suficientemente audaz? ¡Elige un enemigo!', reply_markup=atacar_luna_Kb())

        if '🥔' == str(i[2]):
                   bot.send_message(message.chat.id, 'AJa, ¿lo suficientemente audaz? ¡Elige un enemigo!', reply_markup=atacar_papa_Kb())

        if '🦅' == str(i[2]):
                        bot.send_message(message.chat.id, 'AJa, ¿lo suficientemente audaz? ¡Elige un enemigo!', reply_markup=atacar_aguilas_Kb())

        if '🐺' == str(i[2]):
                            bot.send_message(message.chat.id, 'AJa, ¿lo suficientemente audaz? ¡Elige un enemigo!', reply_markup=atacar_lobo_Kb())

        if '🦌' == str(i[2]):
                           bot.send_message(message.chat.id, 'AJa, ¿lo suficientemente audaz? ¡Elige un enemigo!', reply_markup=atacar_ciervos_Kb())

        if '🦈' == str(i[2]):
                bot.send_message(message.chat.id, 'AJa, ¿lo suficientemente audaz? ¡Elige un enemigo!', reply_markup=atacar_tiburon_Kb())

    conn.commit()
    conn.close()

@bot.message_handler(func=lambda msg: msg.text == '🐉')
def ata_dra(message):
    logging.info('USER: ' + str(message.from_user.username) + ' CMD: 🐉')

    c = conn.cursor()
    querry = "SELECT * from heroes where id = {}".format(message.from_user.id)
    logging.debug(querry)
    for i in c.execute(querry):
        logging.debug(str(i))
        if '🐉' == str(i[2]):            
                bot.send_message(message.chat.id, 'Te uniste a las formaciones defensivas. La próxima batalla es en 3h 16 minutos.'
                '💬 Pase la espera por el resultado de la batalla charlando con jugadores de otros castillos en @chatwarscommunity 💬', reply_markup=principal_Kb())
        else:
                bot.send_message(message.chat.id, '⚔️Atacando Al Castillo 🐉Escama de dragon', reply_markup=principal_Kb())

    conn.commit()
    conn.close()  

@bot.message_handler(func=lambda msg: msg.text == '🌑')
def ata_lu(message):
    logging.info('USER: ' + str(message.from_user.username) + ' CMD: 🌑')

    c = conn.cursor()
    querry = "SELECT * from heroes where id = {}".format(message.from_user.id)
    logging.debug(querry)
    for i in c.execute(querry):
        logging.debug(str(i))
        if '🌑' == str(i[2]):            
            bot.send_message(message.chat.id, 'Te uniste a las formaciones defensivas. La próxima batalla es en 3h 16 minutos.'
            '💬 Pase la espera por el resultado de la batalla charlando con jugadores de otros castillos en @chatwarscommunity 💬', reply_markup=principal_Kb())
        else:
            bot.send_message(message.chat.id, '⚔️Atacando Al Castillo 🌑Luz lunar', reply_markup=principal_Kb())
                
    conn.commit()
    conn.close()

@bot.message_handler(func=lambda msg: msg.text == '🥔')
def ata_pa(message):
    logging.info('USER: ' + str(message.from_user.username) + ' CMD: 🥔')

    c = conn.cursor()
    querry = "SELECT * from heroes where id = {}".format(message.from_user.id)
    logging.debug(querry)
    for i in c.execute(querry):
        logging.debug(str(i))
        if '🥔' == str(i[2]):            
             bot.send_message(message.chat.id, 'Te uniste a las formaciones defensivas. La próxima batalla es en 3h 16 minutos.'
             '💬 Pase la espera por el resultado de la batalla charlando con jugadores de otros castillos en @chatwarscommunity 💬', reply_markup=principal_Kb())
        else:
             bot.send_message(message.chat.id, '⚔️Atacando Al Castillo 🥔Papa', reply_markup=principal_Kb())  
    conn.commit()
    conn.close()

@bot.message_handler(func=lambda msg: msg.text == '🦅')
def ata_ag(message):
    logging.info('USER: ' + str(message.from_user.username) + ' CMD: 🦅')

    c = conn.cursor()
    querry = "SELECT * from heroes where id = {}".format(message.from_user.id)
    logging.debug(querry)
    for i in c.execute(querry):
        logging.debug(str(i))
        if '🦅' == str(i[2]):            
            bot.send_message(message.chat.id, 'Te uniste a las formaciones defensivas. La próxima batalla es en 3h 16 minutos.'
            '💬 Pase la espera por el resultado de la batalla charlando con jugadores de otros castillos en @chatwarscommunity 💬', reply_markup=principal_Kb())
        else:
            bot.send_message(message.chat.id, '⚔️Atacando Al Castillo 🦅Nido alto', reply_markup=principal_Kb())
    conn.commit()
    conn.close()

@bot.message_handler(func=lambda msg: msg.text == '🐺')
def ata_lo(message):
    logging.info('USER: ' + str(message.from_user.username) + ' CMD: 🐺')

    c = conn.cursor()
    querry = "SELECT * from heroes where id = {}".format(message.from_user.id)
    logging.debug(querry)
    for i in c.execute(querry):
        logging.debug(str(i))
        if '🐺' == str(i[2]):            
            bot.send_message(message.chat.id, 'Te uniste a las formaciones defensivas. La próxima batalla es en 3h 16 minutos.'
            '💬 Pase la espera por el resultado de la batalla charlando con jugadores de otros castillos en @chatwarscommunity 💬', reply_markup=principal_Kb())
        else:
            bot.send_message(message.chat.id, '⚔️Atacando Al Castillo 🐺Manada de lobos', reply_markup=principal_Kb())
    conn.commit()
    conn.close()

@bot.message_handler(func=lambda msg: msg.text == '🦌')
def ata_ci(message):
    logging.info('USER: ' + str(message.from_user.username) + ' CMD: 🦌')
    c = conn.cursor()
    querry = "SELECT * from heroes where id = {}".format(message.from_user.id)
    logging.debug(querry)
    for i in c.execute(querry):
        logging.debug(str(i))
        if '🦌' == str(i[2]):            
              bot.send_message(message.chat.id, 'Te uniste a las formaciones defensivas. La próxima batalla es en 3h 16 minutos.'
              '💬 Pase la espera por el resultado de la batalla charlando con jugadores de otros castillos en @chatwarscommunity 💬', reply_markup=principal_Kb())
        else:
              bot.send_message(message.chat.id, '⚔️Atacando Al Castillo 🦌Cuerno de ciervo', reply_markup=principal_Kb())
    conn.commit()
    conn.close()

@bot.message_handler(func=lambda msg: msg.text == '🦈')
def ata_ti(message):
    logging.info('USER: ' + str(message.from_user.username) + ' CMD: 🦈')

    c = conn.cursor()
    querry = "SELECT * from heroes where id = {}".format(message.from_user.id)
    logging.debug(querry)
    for i in c.execute(querry):
        logging.debug(str(i))
        if '🦈' == str(i[2]):            
            bot.send_message(message.chat.id, 'Te uniste a las formaciones defensivas. La próxima batalla es en 3h 16 minutos.'
            '💬 Pase la espera por el resultado de la batalla charlando con jugadores de otros castillos en @chatwarscommunity 💬', reply_markup=principal_Kb())
        else:
            bot.send_message(message.chat.id, '⚔️Atacando Al Castillo 🦈Dientes de Tiburón', reply_markup=principal_Kb())
    conn.commit()
    conn.close()

@bot.message_handler(commands=['heroe'])
def heroe(message):
    logging.info('USER: ' + str(message.from_user.username) + ' CMD: /heroe')

    conn = sqlite3.connect('castillowars.db')
    c = conn.cursor()
    querry = "SELECT * from heroes where id = {}".format(message.from_user.id)
    logging.debug(querry)
    for i in c.execute(querry):
        logging.debug(str(i))
        
        out =   str(i[2]) + str(i[4]) + '\n'
        out += '🏅Nivel: ' + str(i[5]) + '\n'
        out += '⚔️Ataque: ' + str(i[7]) + ' 🛡Defensa: ' + str(i[8]) + '\n'
        out += '🔥Exp: ' + '0/'
        out +=  str(i[9]) + '\n'
        out += '❤️Vida:' + '300/'
        out +=  str(i[11]) + '\n'
        out += '🔋Stamina:' + '5/' 
        out +=  str(i[10]) + '\n'
        out += '💧Mana:' + '0/' 
        out +=  str(i[12]) + '\n'
        out += '💰' + str(i[13])

        if str(i[14]) == str('0'):
            out += ''            
        else:    
            out += '👝' + str(i[14]) 

        if str(i[15]) == str('0'):
            out += ' '            
        else:
            out += '💎' + str(i[15]) + '\n'      
        out += '📚Pergaminos: ' + '\n'        
        out += '🎉Logros:' + ' /logros' + '\n'        
        out += '🏛Información de clase: ' + str(i[11]) + ' /clase' + '\n' +'\n'
                
        out += '✨Efectos:' + str(i[11]) + '🛡↑/efectos' + '\n' + '\n'
        
        out += '🎽Euipamiento' + '⚔️+' + 'nada' + '🛡+' + 'nada' + '\n'
        if str(i[14]) == str('0'):
            out += ''            
        else:    
            out += 'Casco: ' + str(i[20]) + '🛡+' + '\n'
                
        if str(i[14]) == str('0'):
            out += ''            
        else:          
            out += 'Grantes: ' + str(i[11]) + '🛡+' + '\n' 
        
        if str(i[14]) == str('0'):
            out += ''            
        else:         
            out += 'Armadura: ' + str(i[11]) + '🛡+' + '\n'
        
        if str(i[14]) == str('0'):
            out += ''            
        else:  
            out += 'Botas: ' + str(i[11]) + '🛡+' + '\n'
        
        if str(i[14]) == str('0'):
            out += ''            
        else:  
            out += 'Arma Principal: ⚔️+' + str(i[11]) + '🛡+' + '\n'
        
        if str(i[14]) == str('0'):
            out += ''            
        else:  
            out += 'Arman Segundaria: ⚔️+' + str(i[11]) + '🛡+' + '\n'
        
        if str(i[14]) == str('0'):
            out += ''            
        else:  
            out += 'Capa: ' + str(i[11]) + '🛡+' + '\n'
        
        if str(i[14]) == str('0'):
            out += ''            
        else:  
            out += 'Anillo: ' + str(i[11]) + '🛡+' + '\n'
        
        if str(i[14]) == str('0'):
            out += ''            
        else:  
            out += 'Collar: ' + str(i[11]) + '🛡+' + '\n'
                
        out += '\n'
        out += '🎒Bolso: '
        out +=  str(i[23]) +' /inv' +'\n'
        out += '📦Almacén: '
        out +=  str(i[23]) +' /alm' +'\n'


        bot.send_message(message.chat.id, out,  parse_mode='HTML')
    conn.commit()
    conn.close()

@bot.message_handler(func=lambda msg: msg.text == '🗺Misiones')
def me(message):
    logging.info('USER: ' + str(message.from_user.username) + ' CMD: 🦈')
    bot.send_message(message.chat.id, '🌲Bosque 3min \n Pueden pasar muchas cosas en el bosque.\n'
        '🗡Foray 🔋🔋 \n'
        'La incursión es una actividad peligrosa. Alguien puede notarlo y puede golpearlo. Pero si pasas desapercibido, conseguirás mucho botín. \n'
        '📯Arena \n'
        'Arena no es un lugar para débiles. Aquí luchas contra otros jugadores y si sales victorioso, adquieres una experiencia preciosa.'
        , reply_markup=principal_Kb())

@bot.message_handler(func=lambda msg: msg.text == '👥Clanes')
def me(message):
    logging.info('USER: ' + str(message.from_user.username) + ' CMD: 👥Clanes')
    conn = sqlite3.connect('castillowars.db')
    c = conn.cursor()
    querry = "SELECT * from heroes where id = {}".format(message.from_user.id)
    logging.debug(querry)
    for i in c.execute(querry):
        logging.debug(str(i))

        if str(i[14]) == str('0'):
            
             bot.send_message(message.chat.id, 'out',  parse_mode='HTML')        
        else:
            
            bot.send_message(message.chat.id,'Clan', reply_markup=guild_Kb())

            #You don't have a guild yet. You can found a guild for 3000💰.Use /guildcreate [name] to do so.
        # bot.send_message(message.chat.id, str(i))
    conn.commit()
    conn.close()

@bot.message_handler(commands=['crearclan'], content_types=['text'])
def delallusers(message):
    logging.info('USER: ' + str(message.from_user.username) + ' CMD: ' + message.text )    
    username = message.from_user.username
    userid = message.from_user.id
    
    end = None if message.text.find('@') == -1 else message.text.find('@')
    logging.debug(message.text[11:message.text.find('@')])
    nom_clan = message.text[11:message.text.find('@')]

    conn = sqlite3.connect('castillowars.db')
    c = conn.cursor()

    guildslis = []
    for row in c.execute('SELECT heroname FROM heros_gulids'):
        guildslis.append(row[0])

    if username in guildslis:
            bot.send_message(message.chat.id, '¡Ya estas En un Clan!', reply_markup=principal_Kb())          
    else:
            querry = "SELECT * from heroes where id = {}".format(message.from_user.id)
            logging.debug(querry)
            for i in c.execute(querry):
                logging.debug(str(i))

                if  str(i[13]) >= str('3000'):
                        querry1 = "SELECT * from heroes where id = {}".format(message.from_user.id)
                        logging.debug(querry1)
                        for i in c.execute(querry1):
                            logging.debug(str(i))                                   
                            gold = 3000
                            nombre = str(i[4])
                            nivel = str(i[5])
                            ataque = str(i[7])
                            defensa = str(i[8])
                        
                            querry2 = "INSERT INTO guilds (nom_g,comandante,attack,defense) VALUES ('{}', '{}', '{}', '{}')".format(nom_clan, nombre, ataque, defensa)
                            querry3 = "INSERT INTO heros_gulids (guild,heroname,nivel,ataque,defensa) VALUES ('{}', '{}', '{}', '{}', '{}')".format(nom_clan, nombre, nivel, ataque, defensa)
                            querry4 = "UPDATE heroes SET gold = (gold -'{}')  WHERE id = '{}'".format(gold, userid)
                            c.execute(querry2)
                            c.execute(querry3)
                            c.execute(querry4)
                            logging.info('USER: ' + str(username) + ' a creado un clan llamado: ' + nom_clan )
                            bot.send_message(message.chat.id, 'Haz creado el clan con exito.', reply_markup=principal_Kb())
                else:
                    logging.info('USER: ' + str(username) + ' No tiene suficientemente oro para crear el clan' )
                    bot.send_message(message.chat.id, 'No tines suficientemente oro para crear el clan. ¡Anda a trabajar peresozo!', reply_markup=principal_Kb())
    conn.commit()
    conn.close()
    
@bot.message_handler(commands=['del'])
def delallusers(message):
    logging.info('USER: ' + str(message.from_user.username) + ' CMD: /delheroes')

    if message.from_user.username not in admins:
        return

    conn = sqlite3.connect('castillowars.db')
    c = conn.cursor()
    querry = "DELETE from heroes"
    logging.debug(querry)
    for i in c.execute(querry):
        logging.debug(str(i))
        bot.send_message(message.chat.id, str(i))
    conn.commit()
    conn.close()

@bot.message_handler(commands=['alluser'])
def showallusers(message):
    # logging.debug(niceprint(str(message)))
    logging.info('USER: ' + str(message.from_user.username) + ' CMD: /alluser')

    if message.from_user.username not in admins:
        return
    conn = sqlite3.connect('castillowars.db')
    c = conn.cursor()
    querry = "SELECT * from heroes"
    logging.debug(querry)
    out = ''

    for idx, i in enumerate(c.execute(querry)):
        out += str(i[2]) + '|'
        out += '🏅' + str(i[4]) + ' ⚔' + str(i[5]) + ' 🛡' + str(i[6]) + '|' 
        out += '/show_' + str(i[1]) + '\n\n'

    bot.send_message(message.chat.id, out)
    conn.commit()
    conn.close()

@bot.message_handler(func=lambda message: message.text and '/show' in message.text, content_types=['text'])
def getcurrentuser(message):
    logging.debug(niceprint(str(message)))
    logging.info('USER: ' + str(message.from_user.username) + ' CMD: ' + message.text)

    if message.from_user.username not in admins:
        return

    conn = sqlite3.connect('castillowars.db')
    c = conn.cursor()
    end = None if message.text.find('@') == -1 else message.text.find('@')
    logging.debug(message.text[6:message.text.find('@')])
    querry = "SELECT * from heroes where username = '{}'".format(message.text[6:end])
    logging.debug(querry)    
    for i in c.execute(querry):
        logging.debug(str(i))

        out =  '@' + str(i[1]) + ' | ' + str(i[2]) + ' | ' + str(i[3]) + '\n'
        out =  str(i[2]) + str(i[4]) + '\n'
        out += '🏅Nivel: ' + str(i[5]) + '\n'
        out += '⚔️Ataque:' + str(i[6]) + ' 🛡Defensa:' + str(i[7]) + '\n'
        out += '🔥Exp: ' + str(i[8]) + '/' + '\n'
        out += '❤️Vida: ' + str(i[10]) + '/' + '\n'
        out += '🔋Stamina: ' + str(i[9]) + '/'+ '\n'
        out += '💧Mana: ' + str(i[11]) + '🛡' + '\n'
        out += '💰' + str(i[12])
        if str(i[13]) == str('0'):
            out += ''            
        else:    
            out += '👝' + str(i[13]) 

        if str(i[14]) == str('0'):
            out += '\n'            
        else:
            out += '💎' + str(i[14]) + '\n'
        
        out += '📚Pergaminos: ' + str(i[11]) + '/' + '\n'        
        out += '🎉Logros:' + ' /logros' + '\n'        
        out += '🏛Información de clase: /clase' + '\n' +'\n'
        out += '✨Efectos:' + str(i[11]) + '🛡↑/efectos' + '\n' + '\n'
        out += '🎽Euipamiento' + '⚔️+' + str(i[5]) + '🛡+' + str(i[6]) + '\n'
        if str(i[14]) == str('0'):
            out += 'Casco: ' + str(i[11]) + '🛡+' + '\n'
        else:
            out += '\n'
        if str(i[14]) == str('0'):
            out += 'Grantes: ' + str(i[11]) + '🛡+' + '\n'
        else:
            out += '\n'     
        if str(i[14]) == str('0'):
            out += 'Armadura: ' + str(i[11]) + '🛡+' + '\n'
        else:
            out += '\n'
        if str(i[14]) == str('0'):
            out += 'Botas: ' + str(i[11]) + '🛡+' + '\n'
        else:
            out += '\n'
        if str(i[14]) == str('0'):
            out += 'Arma Principal: ⚔️+' + str(i[11]) + '🛡+' + '\n'
        else:
            out += '\n'
        if str(i[14]) == str('0'):
            out += 'Arman Segundaria: ⚔️+' + str(i[11]) + '🛡+' + '\n'
        else:
            out += '\n'
        if str(i[14]) == str('0'):
            out += 'Capa: ' + str(i[11]) + '🛡+' + '\n'
        else:
            out += '\n'
        if str(i[14]) == str('0'):            
            out += 'Anillo: ' + str(i[11]) + '🛡+' + '\n'
        else:
            out += '\n'
        if str(i[14]) == str('0'):        
            out += 'Collar: ' + str(i[11]) + '🛡+' + '\n'
        else:
            out += '\n'
        if str(i[14]) == str('0'):        
            out += '\n'
        else:
            out += '\n'
        
        out += '🎒Bolso: '
        out +=  str(i[23]) +' /inv' +'\n'
        out += '📦Almacén: '
        out +=  str(i[23]) +' /alm' +'\n'

        logging.debug(out)
        bot.send_message(message.chat.id, out, parse_mode='HTML')
        # bot.send_message(message.chat.id, str(i))
    conn.commit()
    conn.close()

    logging.debug(niceprint(str(message)))
    logging.info('USER: ' + str(message.from_user.username) + ' CMD: ' + message.text)

    if datetime.datetime.fromtimestamp(message.date) < datetime.datetime.now()-datetime.timedelta(minutes=1):
        logging.info('MensajesAntiguos')
        return

    if 'HasConocido' in message.text and message.forward_from:
        out = 'Escribe primero cualquier mensaje Replay en esto y tomar la mafia, si no tienes tiempo, '
        out += 'inténtalo de nuevo\nmonton:\n'
        conn = sqlite3.connect('castillowars.db')
        c = conn.cursor()

        for row in c.execute('SELECT username from mobspersons'):
            out += '@' + str(row[0]) + ' '

        conn.commit()
        conn.close()
        bot.reply_to(message, out)


    if 'Modo de silencio' in message.text.lower() or 'servilleta' in message.text.lower():
        bot.reply_to(message, salfetka)
        bot.pin_chat_message(-1001064490030, message.message_id + 1)


if __name__ == '__main__':
    bot.polling(none_stop=True)

# ###############################################################
# # Remove webhook, it fails sometimes the set if there is a previous webhook
# bot.remove_webhook()
# time.sleep(1)


# # Set webhook
# bot.set_webhook(url=WEBHOOK_URL_BASE+WEBHOOK_URL_PATH,
#                 certificate=open(WEBHOOK_SSL_CERT, 'r'))


# # Start flask server
# app.run(host=WEBHOOK_LISTEN,
#         port=WEBHOOK_PORT,
#         ssl_context=(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV),
#         debug=True)