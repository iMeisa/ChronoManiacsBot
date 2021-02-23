from twitchio.ext import commands
import json
from random import randint

with open('bot_info.json', 'r') as f:
    credentials = json.load(f)

client = commands.Bot(
    irc_token=credentials['irc_token'],
    client_id=credentials['client_id'],
    nick='chronomaniacs',
    prefix='!',
    initial_channels=credentials['channels']
)


@client.event
async def event_ready():
    print('I AM ALIVE')
    ws = client.ws
    await ws.send_privmsg(credentials['channels'][0], 'I AM ALIVE')


@client.event
async def event_message(message):
    if message.content.lower().startswith('hi'):
        await message.channel.send(f'Hi @{message.author.display_name}')

    await client.handle_commands(message)


@client.command(name='test')
async def test(ctx):
    await ctx.send('Yep I work')


@client.command(name='dice', aliases=['roll'])
async def dice(ctx, sides=6):
    result = randint(1, sides)
    await ctx.send(f'Roll: {result}')


if __name__ == '__main__':
    client.run()
