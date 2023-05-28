import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):

        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))

        if 'JE SUIS' in message.content.upper():
            a = message.content.upper().split('JE SUIS ')
            try:
                res = a[1].split('.')[0]
            except:
                res = a[1]
            await message.channel.send('Enchanté ' + res.capitalize() + ', moi c\'est Yves, le bot sympa !')


        elif 'JE TE DETESTE' in message.content.upper() or 'JE ME DETESTE' in message.content.upper():
            await message.channel.send("Pourquoi tant de haine ? Moi je crois qu\'il est bon de se demander si le sujet et réelement détestable ou si c\'est vous qui transposez votre mal-être et votre manque affectif dans l\'aggressivité. Remarquez, le simple fait que vous formuliez ça ainsi me pousse à penser que, en effet, vous êtes détestable.")

client = MyClient()
client.run(<token>)
