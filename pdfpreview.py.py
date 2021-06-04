#!/usr/bin/env python3
import discord
from discord.ext import commands, tasks
import pdf2image
import requests

bot = commands.Bot(command_prefix='.')
token = 'placeholder'

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command(pass_context=True)
async def pdf(ctx,link):
    pdf = requests.get(link)
    schot = pdf2image.convert_from_bytes(pdf.content)[0]
    schot.save("temp.png", filename="temp.png")
    await ctx.send(file=discord.File(r'temp.png'))

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(token)
