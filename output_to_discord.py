"""send message to discord channel"""
import requests
import json
import os
import discord

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTEwOTExNzI2MTU4NDgwMTgyMg.Gym7cX.F7YAsuhu6xgGvLSMfCEuNR0yPLPNw5h3EL0KxA'
    client = discord.Client(intents=discord.Intents.all())

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to Discord!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel.name)
        print(f'{username}: {user_message} ({channel})')

        if user_message.startswith('?'):
            user_message = user_message[1:]
            await send_message(message, user_message, True)
        else:
            await send_message(message, user_message, False)
    client.run(TOKEN)
