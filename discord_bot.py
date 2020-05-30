# python library to communicate with discord bot using discord.Client
import discord
from discord.ext import commands

# decouple helps to fetch environment variables
from decouple import config

# getting command classes to be used with on_message method
from commands.google import GoogleCommand
from commands.recent import RecentCommand

# command factory as a factory pattern to decide which class to be used at run time
command_factory = {
    'google': GoogleCommand,
    'recent': RecentCommand
}


class MyClient(discord.Client):
    async def on_ready(self):
        # confirming that bot is online
        print('Logged in as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        content = message.content

        # simply replying hey to hi
        if content == 'hi':
            await message.channel.send('hey')

        # handles commands like !google and !recent
        elif content[0] == config('PREFIX'):
            # eliminating prefix and saving command and its arguments
            action, *args = content[1:].split(" ")

            # using factory pattern to choose class for executing message
            command = command_factory.get(action, None)

            # if command does not exist in dictionary
            if not command:
                await message.channel.send('Type a valid command !google or !recent')

            # since both the command require arguments
            elif not args:
                await message.channel.send('Oops! you forgot to mention what to search')

            # data fetched by executing command
            data = command.execute(args)

            # embedding data for better display
            for element in data:
                e = discord.Embed(title=element['data'])
                await message.channel.send(element['description'], embed=e)


# connecting and making the bot online using MyClient class inheriting from discord.Client
client = MyClient()
client.run(config('DISCORD_TOKEN'))

