#---------------------------------------------------------------------------------------------------
# Bibliotheken die Importiert wurden
#---------------------------------------------------------------------------------------------------
import asyncio
from discord.ext import commands
import discord
import requests
from datetime import datetime
from verarbeitung import *

#---------------------------------------------------------------------------------------------------
# Channel-IDs
#---------------------------------------------------------------------------------------------------
kurs_channel_btc_id = channel_id
kurs_channel_ether_id = channel_id
kurs_channel_doge_id = channel_id
kurs_channel_litecoin_id = channel_id

#---------------------------------------------------------------------------------------------------
# API-KEY
#---------------------------------------------------------------------------------------------------
API_KEY = API-Key
allgemeine_info_channel_id = channel_id

ausfuehrung = 0

#---------------------------------------------------------------------------------------------------
# Funktion zur Abfrage bei der API von Bitcoin.de
#---------------------------------------------------------------------------------------------------
def kurse(API_KEY, trading_pair):
    try:
        kurs = []
        url = f'https://api.bitcoin.de/v4/{trading_pair}/basic/rate.json?apikey={API_KEY}'
        data = requests.get(url).json()
        kurs.append(data['rate']['rate_weighted'])
        kurs.append(data['rate']['rate_weighted_3h'])
        kurs.append(data['rate']['rate_weighted_12h'])
        return kurs
    except:
        return ['Fail']

#---------------------------------------------------------------------------------------------------
# Funktion zur Zeit Abfrage
#---------------------------------------------------------------------------------------------------
def zeit_full():
    datetime_now = datetime.now()
    time_now = datetime_now.strftime('%H:%M:%S')
    return time_now



intents = discord.Intents.default()

client = commands.Bot(
    command_prefix="$",
    help_command=None,
    intents=intents
)


@client.event
async def on_connect():
    # Einloggen vom Bot
    print("[Ich habe mich eingeloggt]...")
    await client.wait_until_ready()
    client.loop.create_task(change_status())
    client.loop.create_task(kurs_verarbeitung())

#---------------------------------------------------------------------------------------------------
# Funktion zur Verarbeitung der Kurse
#---------------------------------------------------------------------------------------------------
async def kurs_verarbeitung():
    global ausfuehrung
    if (ausfuehrung == 0):
        ausfuehrung = 1

        kurs_channel_btc = client.get_channel(kurs_channel_btc_id)
        kurs_channel_ether = client.get_channel(kurs_channel_ether_id)
        kurs_channel_doge = client.get_channel(kurs_channel_doge_id)
        kurs_channel_litecoin = client.get_channel(kurs_channel_litecoin_id)

        kurs_liste_btc = []
        for x in range(24):
            kurs_liste_btc.append('#')
        kurs_liste_ether = []
        for x in range(24):
            kurs_liste_ether.append('#')
        kurs_liste_doge = []
        for x in range(24):
            kurs_liste_doge.append('#')
        kurs_liste_lite = []
        for x in range(24):
            kurs_liste_lite.append('#')
        zeit_speicher = []
        for x in range(24):
            zeit_speicher.append('#')

        dauerhaftes_ausfuehren = True
        fehler = 0
        again = True




        while dauerhaftes_ausfuehren == True:
            try:
                try:
                    datetime_now = datetime.now()
                    time_now = int(datetime_now.strftime('%M'))

                except Exception as fehler_zeitabfrage:
                    await fehler.send("Fehler bei der Zeitabfrage von Minuten: ")
                    await fehler.send(fehler_zeitabfrage)
                    time_now = -1


                try:
                    # Kurs Ausgabe alle Stunde
                    if time_now % 60 == 0 and again == True:

                        neu_anordung(kurs_liste_btc)
                        neu_anordung(kurs_liste_ether)
                        neu_anordung(kurs_liste_doge)
                        neu_anordung(kurs_liste_lite)
                        neu_anordung(zeit_speicher)

                        for x in range(23, 0, -1):
                            name = 'message_btc_' + str(x)
                            variable_btc = await kurs_channel_btc.fetch_message(message(name))
                            message_btc = f'Kurs: {kurs_liste_btc[-x]} \n {zeit_speicher[-x]}'
                            await variable_btc.edit(content=message_btc)

                        for x in range(23, 0, -1):
                            name = 'message_ether_' + str(x)
                            variable_ether = await kurs_channel_ether.fetch_message(message(name))
                            message_ether = f'Kurs: {kurs_liste_ether[-x]} \n {zeit_speicher[-x]}'
                            await variable_ether.edit(content=message_ether)

                            name = 'message_doge_' + str(x)
                            variable_doge = await kurs_channel_doge.fetch_message(message(name))
                            message_doge = f'Kurs: {kurs_liste_doge[-x]} \n {zeit_speicher[-x]}'
                            await variable_doge.edit(content=message_doge)

                            name = 'message_lite_' + str(x)
                            variable_lite = await kurs_channel_litecoin.fetch_message(message(name))
                            message_lite = f'Kurs: {kurs_liste_lite[-x]} \n {zeit_speicher[-x]}'
                            await variable_lite.edit(content=message_lite)


                        aktueller_kurs_btc = kurse(API_KEY, 'btceur')
                        if aktueller_kurs_btc[0] != 'Fail':
                            counter = 0
                            async for c in kurs_channel_btc.history():
                                counter = counter + 1
                            if counter >= 24:
                                await kurs_channel_btc.purge(limit=1)
                            zeit_speicher[0] = zeit_full()
                            kurs_liste_btc[0] = aktueller_kurs_btc[0]
                            await kurs_channel_btc.send(f''' Gesamt: {aktueller_kurs_btc[0]} /Gewichtete Kurs von 3h: {aktueller_kurs_btc[1]} /Gewichtete Kurs von 12h: {aktueller_kurs_btc[2]} /Zeit: {zeit_full()}''')


                        aktueller_kurs_eth=kurse(API_KEY, 'etheur')
                        if aktueller_kurs_eth[0] != 'Fail':
                            counter = 0
                            async for c in kurs_channel_ether.history():
                                counter = counter + 1
                            if counter >= 24:
                                await kurs_channel_ether.purge(limit=1)
                            zeit_speicher[0] = zeit_full()
                            kurs_liste_ether[0] = aktueller_kurs_eth[0]
                            await kurs_channel_ether.send(f''' Gesamt: {aktueller_kurs_eth[0]} /Gewichtete Kurs von 3h: {aktueller_kurs_eth[1]} /Gewichtete Kurs von 12h: {aktueller_kurs_eth[2]} /Zeit: {zeit_full()}''')


                        aktueller_kurs_doge = kurse(API_KEY, 'dogeeur')
                        kurs_liste_doge[0] = aktueller_kurs_doge
                        if aktueller_kurs_doge[0] != 'Fail':
                            counter = 0
                            async for c in kurs_channel_doge.history():
                                counter = counter + 1
                            if counter >= 24:
                                await kurs_channel_doge.purge(limit=1)
                            kurs_liste_doge[0] = aktueller_kurs_doge[0]
                            await kurs_channel_doge.send(f''' Gesamt: {aktueller_kurs_doge[0]} /Gewichtete Kurs von 3h: {aktueller_kurs_doge[1]} /Gewichtete Kurs von 12h: {aktueller_kurs_doge[2]} /Zeit: {zeit_full()}''')


                        aktueller_kurs_ltc = kurse(API_KEY, 'ltceur')
                        kurs_liste_lite[0] = aktueller_kurs_ltc
                        if aktueller_kurs_ltc[0] != 'Fail':
                            counter = 0
                            async for c in kurs_channel_litecoin.history():
                                counter = counter + 1
                            if counter >= 24:
                                await kurs_channel_litecoin.purge(limit=1)
                            kurs_liste_lite[0] = aktueller_kurs_ltc[0]
                            await kurs_channel_litecoin.send(f''' Gesamt: {aktueller_kurs_ltc[0]} /Gewichtete Kurs von 3h: {aktueller_kurs_ltc[1]} /Gewichtete Kurs von 12h: {aktueller_kurs_ltc[2]} /Zeit: {zeit_full()}''')

                        again = False
                    elif time_now % 60 != 0 and again == False:
                        again = True


                except Exception as fehler_kurs_ausgabe:
                    fehler = client.get_channel(allgemeine_info_channel_id)
                    print("Probleme mit bei der Kursausgabe: ")
                    print(fehler_kurs_ausgabe)
                    await fehler.send("Probleme mit bei der Kursausgabe: ")
                    await fehler.send(fehler_kurs_ausgabe)


                await asyncio.sleep(40)


            except Exception as Kurs_schleife:
                fehler=client.get_channel(allgemeine_info_channel_id)
                print("Fehler Abfrage des Kurses: ")
                print(Kurs_schleife)
                await fehler.send("Fehler Abfrage des Kurses: ")
                await fehler.send(Kurs_schleife)

#---------------------------------------------------------------------------------------------------
# ??nderung des Status
#---------------------------------------------------------------------------------------------------
async def change_status():
    while True:
        try:
            await client.change_presence(activity=discord.Activity(
                type=discord.ActivityType.playing,
                name="Gebe Kryptokurse aus!",
                status=discord.Status.online))
            await asyncio.sleep(10)
            await client.change_presence(activity=discord.Activity(
                type=discord.ActivityType.listening,
                name="Abfrage von neuen Kryptokursen",
                status=discord.Status.invisible))
            await asyncio.sleep(10)
        except:
            pass

#---------------------------------------------------------------------------------------------------
# BOT-Token
#---------------------------------------------------------------------------------------------------
client.run(BOT-Token)
