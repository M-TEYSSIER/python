#!/usr/bin/env python3.7

from asyncio import coroutines
import discord
from discord.ext import commands
from dotenv import load_dotenv

import os
import re

class MyClient(discord.Client):
    default_intents = discord.Intents.default()
    default_intents.members=True
    client = discord.Client(intents=default_intents)
    dict_ban=[]
    cmd=['!list', '!add', '!remove']

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-------------------')

    @client.event
    async def on_member_join(member):
        pass

    @client.event
    async def on_message(self, message):
        msg = message.content

        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        # !list show ban words dictionnary
        if msg.startswith("!list"):
            dico = str(self.dict_ban).replace("[", "").replace("]", "").replace("'", "")
            print(dico)
            await message.channel.send("Ban words: \n"+dico)

        # !ban Append ban word on dictonnaty
        if msg.startswith("!add"):
            word = msg.replace("!add ","")
            self.dict_ban.append(word)

        if re.search("!remove", str.lower(msg)):
            word = msg.replace("!remove ","")
            self.dict_ban.remove(word)

        # Delete message with ban word
        if not any(word in message.content for word in self.cmd):
            if any(word in message.content.lower() for word in self.dict_ban):
                await message.delete()
                await message.channel.send(f"WARNING: {message.author}, using bad language")


load_dotenv(dotenv_path="config")

client = MyClient()
client.run(os.getenv("TOKEN"))
