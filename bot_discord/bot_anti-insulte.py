#!/usr/bin/env python3

import discord

from sys import argv
import os
import re
import sqlite3

class MyClient(discord.Client):
    default_intents = discord.Intents.default()
    default_intents.members=True
    client = discord.Client(intents=default_intents)

    cmd=['~help', '~list', '~add', '~remove']

    if not os.path.exists("ban_words.sqlite"):
        condb = sqlite3.connect("ban_words.sqlite", timeout=1000)
        con = condb.cursor()
        con.execute('''
            CREATE TABLE ban_words(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom text NOT NULL UNIQUE);
                ''')
        con.commit()
    else:
        condb = sqlite3.connect("ban_words.sqlite", timeout=1000)
        con = condb.cursor()

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-------------------')
        print("Server with bot:")
        for guild in client.guilds:
            print(guild)
        print('-------------------')

    def add_bw(self, word):
        try:
            self.con.execute(f'INSERT INTO ban_words (nom) VALUES ("{word}")')
            self.condb.commit()
        except:
            self.condb.rollback()

    def del_bw(self, word):
        try:
            self.con.execute(f'DELETE FROM ban_words WHERE nom="{word}"')
            self.condb.commit()
        except:
            self.condb.rollback()

    def listing(self):
        self.con.execute('SELECT nom FROM ban_words ORDER BY nom ASC')
        rows = self.con.fetchall()
        result=[]
        for e in rows:
            result.append(e[0])
        return result

    @client.event
    async def on_member_join(member):
        pass

    @client.event
    #@commands.has_role()
    async def on_message(self, message):
        msg = message.content

        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        # Print help menu
        if msg.startswith("~show_help"):
            await message.channel.send("```\
                FR:\
                \nLe bot FlashModz a pour but de vérifier les messages du chat et de les supprimer si des mots ne sont pas appropriés.\
                \n~show_help: Affiche les menu d'aide.\n~show_list: Affiche les mots non appropriés présent dans la base de données.\
                \n~add_ban_word <mot>: Ajout le mot dans la base de données.\
                \n~remove_ban_word <mot>: Supprime le mot de la base de données.\
                \nEN:\
                \nThe FlashModz bot have purpose to check new messages on chat and delete if they not appropriated.\
                \n~show_help: Print the help menu.\n~show_list: Print the ban words list registered on database.\
                \n~add_ban_word <word>: Add single word on database.\
                \n~remove_ban_word <word>: Delete word from the database.```")

        # !list show ban words dictionnary
        if msg.startswith("~show_list"):
            liste = self.listing()
            await message.channel.send("Banned words list:")
            await message.channel.send(f'```{liste}```')

        # Append ban word on dictonnaty
        if msg.startswith("~add_ban_word"):
            word = msg.replace("~add_ban_word ","")
            self.add_bw(word)

        # Remove word from the dictonnary
        if re.search("~remove_ban_word", str.lower(msg)):
            word = msg.replace("~remove_ban_word ","")
            self.del_bw(word)

        # Delete message with ban word on chat
        if not any(message.content.startswith(word) for word in self.cmd):
            if any(word in list(message.content.lower().split(" ")) for word in  self.listing()):
                await message.delete()
                await message.channel.send(f"WARNING: {message.author.mention}, surveille ton langage !")


client = MyClient()
client.run(argv[1])