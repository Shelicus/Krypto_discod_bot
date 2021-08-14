import discord


kurs_channel_btc_id = 'ID-Channel'
kurs_channel_ether_id = 'ID-Channel'
kurs_channel_doge_id = 'ID-Channel'
kurs_channel_litecoin_id = 'ID-Channel'
allgemeine_info_channel_id = 'ID-Channel'





class MyClient(discord.Client):
    try:

        # Einloggen vom Bot
        async def on_ready(self):

            kurs_channel_btc = client.get_channel(kurs_channel_btc_id)
            kurs_channel_ether = client.get_channel(kurs_channel_ether_id)
            kurs_channel_doge = client.get_channel(kurs_channel_doge_id)
            kurs_channel_lite = client.get_channel(kurs_channel_litecoin_id)

            await kurs_channel_lite.purge()
            await kurs_channel_doge.purge()
            await kurs_channel_ether.purge()


            for x in range(24):
                await kurs_channel_btc.send(x+1)
                await kurs_channel_ether.send(x+1)
                await kurs_channel_doge.send(x+1)
                await kurs_channel_lite.send(x+1)


    except:
        pass
client = MyClient()
client.run("API-KEY-Discord-Bot")

