import discord
from discord.ext import commands

import os
import webserver
import random

intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='-', intents=intents)

token = os.environ.get('BOTTOKEN')

@bot.event
async def on_ready():
    print(f'logged in successfully as sohreh hehe :)')
    await bot.change_presence(activity=discord.Game(name="doing my homework 🏳️‍🌈"))
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "sohreh" in message.content.lower():
        await message.channel.send("Yes?")
    if "sunday" in message.content.lower():
        sdm = {
          "1": "Well that's gay.",
          "2": "Fried chicken with gravy and carrots.",
          "3": "One day, after dinner, while my younger sister and I were lounging about in Mr. Gopher Wood's yard, we spotted a fledgling Charmony Dove all on its own."
        }
        rng = random.randint(1, 3)
        await message.channel.send(sdm[str(rng)]) 
    if "pulcinella" in message.content.lower():
       await message.channel.send("STUPID GARDEN GNOME")

    if "zandik" in message.content.lower():
        zdm = {
         "1": "Gay man with an ability to strangle people very nicely and quite fast.",
         "2": "He's young — handsome, too. But he's too rigid.",
         "3": 'He seems interested in those weird machines called "Ruin Guards."'
        }
        rng = random.randint(1, 3)
        await message.channel.send(zdm[str(rng)])

    if "sohreh" in message.content.lower() and "marry me" in message.content.lower():
        shmm = {
            "1": "No, leave me alone and let me write my thesis in peace.",
            "2": "You aren't my sorta type.",
            "3": "One day, I will but not for now.",
            "4": "Of course I will."
        }
        rng = random.randint(1, 4)
        await message.channel.send(shmm[str(rng)])

    if "sowio" in message.content.lower():
        sodm = {
            "1": "That person is scary.",
            "2": "They ate my thesis.",
            "3": "I blame them for my thesis being gone all of a sudden at 3 am."
        }
        rng = random.randint(1, 3)
        await message.channel.send(sodm[str(rng)])

    if "scaramouche" in message.content.lower():
        await message.channel.send("Who in the holy Celestia are you talking about.")
    
    if "uwu" in message.content.lower():
        await message.channel.send("Moshi Moshi? Konnichiwa! 📞✨ Ohio gozaimasu! Only in Ohio, skibidi rizz! 💀 Ohio, Ohio! Sumi mazen? Can you hear me in Ohio? Arigato gozaimasu, Ohio! 🌸")

    if "pantalone" in message.content.lower():
        pm = {
            "1": "It smells like a banker here.",
            "2": "He replaced me, I was supposed to be Zandik's friend.",
            "3": "He needs to stop smoking so much, his lungs are slowly giving up on him."
        }
        rng = random.randint(1, 3)
        await message.channel.send(pm[str(rng)])

    if "i hate you" in message.content.lower() and "sohreh" in message.content.lower():
        await message.channel.send("https://tenor.com/ixcB859NGkm.gif")
    
    if "i love you" in message.content.lower() and "sohreh" in message.content.lower():
        await message.channel.send("Okay, buddy.")

    if "dead" in message.content.lower() and "sohreh" in message.content.lower():
        await message.channel.send("Sure, I am very dead I guess.")

    if "dottore" in message.content.lower():
        dmm = {
            "1": "That's Zandik's new name now, huh.",
            "2": "His experiments seem too unethical for me.",
            "3": "He got expelled from the akademiya for a reason."
        }
        rng = random.randint(1, 3)
        await message.channel.send(dmm[str(rng)])
    
    # to do: add more
    
webserver.keep_alive()
bot.run(token)
