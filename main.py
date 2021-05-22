import discord
import signal
import sqlite3
from itertools import chain

client = discord.Client()

connection = sqlite3.connect('introductions.db')

@client.event
async def on_ready():
    print('Log on')

@client.event
async def on_message(message):
    if (message.author == client.user):
        return
    if (message.content.startswith('>get_intro')):
        if (len(message.mentions) == 0):
            cursor = connection.execute("SELECT introduction from INTROS where id='" + str(message.author.id) + "'")
            try:
                first_row = next(cursor)
                for row in chain((first_row,), cursor):
                    await message.channel.send(row[0])
                    pass
            except StopIteration as e: ## DO NOT HAVE INTRO OF SOMEONE ELSE
                await message.channel.send("I don't have your introduction! Use `>set_intro` to set your intro!.")
                pass
        else:
            cursor = connection.execute("SELECT introduction from INTROS where id='" + str(message.mentions[0].id) + "'") ## GETTING INTRO OF SOMEONE ELSE
            try:
                first_row = next(cursor)
                for row in chain((first_row,), cursor):
                    await message.channel.send(row[0])
                    pass
            except StopIteration as e: ## DO NOT HAVE INTRO OF SOMEONE ELSE
                await message.channel.send("I don't have the intro of this user.")
                pass
    if (message.content.startswith('>set_intro')):
        intro = message.content[11:]
        if (intro):
            cursor = connection.execute("SELECT introduction from INTROS where id='" + str(message.author.id) + "'")
            try:
                first_row = next(cursor)
                for row in chain((first_row,), cursor):
                    connection.execute("UPDATE INTROS set INTRODUCTION = '" + intro + "' where ID = '" + str(message.author.id) +"'")
                    pass
            except StopIteration as e:
                # There's nothing here
                connection.execute("INSERT INTO INTROS (ID,INTRODUCTION) VALUES ('" + str(message.author.id) + "', '" + str(intro) + "')")
                pass
            await message.channel.send('Your introduction has been saved!')

client.run('token')

def keyboardInterruptHandler(signal, frame):
    connection.commit()
    connection.close()
    exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)

while True:
    pass
