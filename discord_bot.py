# python library to communicate with discord bot using discord.Client
import discord
from discord.ext import commands

# decouple helps to fetch environment variables
from decouple import config

# getting command classes to be used with on_message method
from commands.google import GoogleCommand
from commands.recent import RecentCommand

command_factory = {
    'google': GoogleCommand,
    'recent': RecentCommand
}


class MyClient(discord.Client):
    async def on_ready(self):
        # confirming that bot is online
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        content = message.content

        # simply replying hey to hi
        if content == 'hi':
            await message.channel.send('hey')
        elif content[0] == config('PREFIX'):
            action, *args = content[1:].split(" ")
            command = command_factory.get(action, None)
            if not command:
                await message.channel.send('Type a valid command !google or !recent')
            elif not args:
                await message.channel.send('Oops! you forgot to mention what to search')

            data = command.execute(message, args)

            for element in data:
                e = discord.Embed(heading=element['content'])
                await message.channel.send(element['heading'], embed=e)


# connecting and making the bot online using MyClient class inheriting from discord.Client
client = MyClient()
client.run(config('DISCORD_TOKEN'))

