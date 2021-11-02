#!/usr/bin/env python3
# -*- coding utf-8 -*-

# Created for GTA Flashmodz RP french server (https://discord.gg/F4B7NAQE9S)
# in order to calculate governental's tax for LS's citizens 

#!/usr/bin/env python3.7

from sys import argv
import os
import re
import sqlite3
from math import floor
import re

import discord
from discord.ext.commands import Context

class MyClient(discord.Client):
    default_intents = discord.Intents.default()
    default_intents.members=True
    client = discord.Client(intents=default_intents)

    cmd=['~help']
    

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('-------------------')
        print('⭐ ---////---bot est allumé----////---⭐')
        print('-------------------')
        print("Server with bot:")
        for guild in client.guilds:
            print(guild)
        print('-------------------')

    @client.event
    async def on_member_join(member):
        pass

    @client.event
    async def on_message(self, message):
        metier = dict([("Vigneron", 887773645911502874), ("LSPD", 887773645924081686), ("Mecano", 887773645911502877), \
            ("Taxi", 887773645911502873), ("Concessionaire", 887773645911502876), ("Unicorn", 887773645911502872), \
            ("Tabac", 887773645911502871), ("EMS", 887773645924081685),("Agent-Immo", 887773645924081684)])

        msg = message.content
        roles_id = message.author.roles
        
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        # Print help menu
        if msg.startswith("+help"):
            await message.channel.send("```HELP:\n\
                \
                ```")
        
        if msg.startswith("+impots"):
            ChiffreAffaire = int(msg.replace("+impots ", ""))
            for job_name in metier:
                if re.search(str(job_name), str(roles_id)):
                    job = job_name

            # LSPD
            if job == "LSPD":
                taux = 0.11111
                impots = ChiffreAffaire * taux 
                tax = floor(impots)

            # MECANO
            if job == "Mecano":
                taux = 0.15257
                impots = ChiffreAffaire * taux 
                tax = floor(impots)
            
            # TAXI
            if job == "Taxi" :
                taux = 0.11321
                impots = ChiffreAffaire * taux 
                tax = floor(impots)

            # CONCESS
            if job == "Concessionnaire" :
                taux = 0.11354
                impots = ChiffreAffaire * taux 
                tax = floor(impots)

            # TABAC
            if job == "Tabac":
                taux = 0.11465
                impots = ChiffreAffaire * taux 
                tax = floor(impots)

            # Agent IMMO
            if job == "Agent-Immo" :
                taux = 0.3
                impots = ChiffreAffaire * taux 
                tax = floor(impots)

            # Unicorn
            if job == "Unicorn" :
                taux = 0.11356
                impots = ChiffreAffaire * taux 
                tax = floor(impots)

            # EMS
            if job == "EMS" :
                taux = 0.0
                impots = ChiffreAffaire * taux 
                tax = floor(impots)
            
            # Vigneron
            if job == "Vigneron":
                taux = 0.26548
                impots = ChiffreAffaire * taux
                tax = floor(impots)
            
            await message.channel.send(f"La taxe est de: {tax}$ :money_with_wings: ```Une notification est envoyée au gouvernement.``` Le gouvernement vous remercie et est toujours présent pour améliorer votre quotidien sur l'île. Bonne continuation!")
            channel_imposision = client.get_channel(902971905747869716)
            await channel_imposision.send(f"Le corps de métier {job} a annoncé un CA de {ChiffreAffaire}$, donc une taxe à payer de: {tax}$")            

# pour faire apparaitre les roles: message.author.roles 
# ID channel Imposision: 902971905747869716
# ID Rôle
# ID Police     : 887773645924081686
# ID MECANO     : 887773645911502877
# ID TAXI       : 887773645911502873
# ID CONCESS    : 887773645911502876
# ID TABAC      : 887773645911502871
# ID EMS        : 887773645924081685
# ID Agent IMMO : 887773645924081684
# ID Vigneron   : 887773645911502874
# ID Unicorn    : 887773645911502872
#for job_name in metier:
#    if re.search(str(job_name), str(roles_id)):

"""
Métier à mettre dans une liste que l'on va pouvoir parser et afficher dans metier
"""


client = MyClient()
client.run(argv[1])