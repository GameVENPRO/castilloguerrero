#coding:utf-8
import telebot
import datetime
import time
import logging
import config

logging.basicConfig(format=u'%(filename)s[LINEA:%(lineno)-3s]# %(levelname)-5s [%(asctime)s] %(message)s'
                    ,level = logging.INFO, filename='ww.log')

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

salfetka = '''
‼ modo de silencio! ‼️
Caminante! Prepárate para el ataque (⚔ataque) a ' Valiente Guerrero, Elegir un enemigo!'

Si de repente te gusta cambiarte antes de una pelea, ¡puedes ayudarte a ir y cambiarte!

‼ modo de silencio! ‼️
 '''

bot = telebot.TeleBot(config.token)

while 1:
    now = str(datetime.datetime.now().time().replace(microsecond=0))
    if now in ['03:54:59', '07:39:00', '11:54:59', '15:54:59', '19:54:59', '23:54:59']:
        logging.info('Ejecutar un golpe en el temporizador в:' + now)

        bot.send_message(-1001064490030, 'PRONTO LA BATALLA @lolinyan @f0xpwnz @pongg8 @Sicdez @danilsolo')
        bot.send_message(-1001064490030, 'PRONTO LA BATALLA @Lybot0 @mperrrsh @nii_batca @Puzya @Wood_elf')
        bot.send_message(-1001064490030, 'PRONTO LA BATALLA @klim9379992 @mirotvArec @FoolishDreamer @nitroacid @TrentorEx')
        bot.send_message(-1001064490030, 'PRONTO LA BATALLA @Fenicu @SYMRAK @komakomakoma @eegor7 @SenyaArt')
        bot.send_message(-1001064490030, 'PRONTO LA BATALLAА @Irrissa @bigup_universe @Sympho @baka_bunny @Dinker9')
        bot.send_message(-1001064490030, 'PRONTO LA BATALLA @DiKill @l2aggron @anoouse')

        msg = bot.send_message(-1001064490030, salfetka)
        bot.pin_chat_message(msg.chat.id, msg.message_id)

        logging.debug(niceprint(str(msg)))

    if now in ['03:58:30', '07:58:30', '11:58:30', '15:58:30', '19:58:30', '23:58:30']:
        logging.info('Ejecutar un golpe en el temporizador в:' + now)

        bot.send_message(-1001064490030, 'BATALLA @lolinyan @f0xpwnz @pongg8 @Sicdez @danilsolo')
        bot.send_message(-1001064490030, 'BATALLA @Lybot0 @mperrrsh @nii_batca @Puzya @Wood_elf')
        bot.send_message(-1001064490030, 'BATALLA @klim9379992 @mirotvArec @FoolishDreamer @nitroacid @TrentorEx')
        bot.send_message(-1001064490030, 'BATALLA @Fenicu @SYMRAK @komakomakoma @eegor7 @SenyaArt')
        bot.send_message(-1001064490030, 'BATALLA @Irrissa @bigup_universe @Sympho @baka_bunny @Dinker9')
        bot.send_message(-1001064490030, 'BATALLA @DiKill @l2aggron @anoouse')

    if now in ['03:31:59', '07:31:59', '11:31:59', '15:31:59', '19:31:59', '23:31:59']:
        logging.info('Ejecutar un golpe en el temporizador в:' + now)

        bot.send_message(-1001064490030, 'Empuja más @lolinyan @f0xpwnz @pongg8 @Sicdez @danilsolo')
        bot.send_message(-1001064490030, 'Empuja más @Lybot0 @mperrrsh @nii_batca @Puzya @Wood_elf')
        bot.send_message(-1001064490030, 'Empuja más @klim9379992 @mirotvArec @FoolishDreamer @nitroacid @TrentorEx')
        bot.send_message(-1001064490030, 'Empuja más @Fenicu @SYMRAK @komakomakoma @eegor7 @SenyaArt')
        bot.send_message(-1001064490030, 'Empuja más @Irrissa @bigup_universe @Sympho @baka_bunny @Dinker9')
        bot.send_message(-1001064490030, 'Empuja más @DiKill @l2aggron @anoouse')


    time.sleep(1)
