import json
import random
from io import BytesIO

import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands

requests.packages.urllib3.disable_warnings()
EIGHTBALL_LIST = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs points to yes.", "Reply hazy, try again.", "Ask again later.", "Better not to tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good", "Very doubtful.", "Be more polite.", "How would i know", "100%", "Think harder", "Sure""In what world will that ever happen", "As i see it no.", "No doubt about it", "Focus", "Unfortunately yes", "Unfortunately no,", "Signs point to no"]

def get_hello():
	return "Don't talk to me, I am being developed!"

@commands.command()
async def hello(ctx):
	await ctx.send(get_hello(), reference=ctx.message)

def get_taunt():
	return BeautifulSoup(requests.get('https://fungenerators.com/random/insult/shakespeare/').content, "html.parser").find('h2').text

@commands.command()
async def taunt(ctx):
	await ctx.send(get_taunt(), reference=ctx.message)

def get_cat_fact():
  return json.loads(requests.get('https://catfact.ninja/fact').text)['fact']

@commands.command()
async def cat_fact(ctx):
	await ctx.send(get_cat_fact(), reference=ctx.message)

def get_dog_fact():
  return json.loads(requests.get('https://dog-api.kinduff.com/api/facts').text)['facts'][0]

@commands.command()
async def dog_fact(ctx):
	await ctx.send(get_dog_fact(), reference=ctx.message)
					
def get_pug_fact():
	return BeautifulSoup(requests.get('https://fungenerators.com/random/facts/dogs/pug').content, "html.parser").find('h2').text[:-15]

@commands.command()
async def pug_fact(ctx):
	await ctx.send(get_pug_fact(), reference=ctx.message)

def get_cat_pic():
	return BytesIO(requests.get("https://cataas.com/cat").content)

@commands.command()
async def cat_pic(ctx):
	await ctx.send(file=discord.File(fp=get_cat_pic(), filename="cat.png"), reference=ctx.message)

def get_joke():
  return json.loads(requests.get('https://geek-jokes.sameerkumar.website/api?format=json').text)['joke']

@commands.command()
async def joke(ctx):
	await ctx.send(get_joke(), reference=ctx.message)
  
def get_quote():
	return (json.loads(requests.get('https://zenquotes.io/api/random').text)[0]['q'] + "\n- " + json.loads(requests.get('https://zenquotes.io/api/random').text)[0]['a'])

@commands.command()
async def quote(ctx):
	await ctx.send(get_quote(), reference=ctx.message)
	
def get_eightball():
    return random.choice(EIGHTBALL_LIST)

@commands.command(aliases=["8ball"])
async def eightball(ctx):
	await ctx.send(f"🎱 - {get_eightball()}", reference=ctx.message)

def get_fake_person():
	person = json.loads(requests.get('https://randomuser.me/api/').text)['results']
	name = f"Name: {person[0]['name']['title']} {person[0]['name']['first']} {person[0]['name']['last']}"
	hometown = f"Hometown: {person[0]['location']['city']}, {person[0]['location']['country']}"
	age = f"Age: {person[0]['dob']['age']} Years old"
	return f"You have requested a fake person:\n\n {name} \n {hometown} \n {age}"

@commands.command()
async def fake_person(ctx):
	await ctx.send(get_fake_person(), reference=ctx.message)

def get_dog_pic(breed):
	embed = discord.Embed(title="Dog Pic!", description='A lovely dog pic just for you.')
	if breed is None:
		link = requests.get("https://dog.ceo/api/breeds/image/random").json()["message"]
	elif breed is not None:
		link =  requests.get(f"https://dog.ceo/api/breed/{breed}/images/random").json()["message"]
	embed.set_image(url=link)
	return embed

@commands.command()
async def dog_pic(ctx, *, breed=None):
    await ctx.send(embed=get_dog_pic(breed))

def get_pokedex(pokemon):
	data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}")
	if data.status_code == 200:
		data = data.json()
		embed = discord.Embed(title=data['name'].title(),color=discord.Color.blue())
		embed.set_thumbnail(url=data['sprites']['front_default'])
		embed.add_field(name="Stats", value=data['name'].title())
		embed.add_field(name="Weight", value=data['weight'])
		embed.add_field(name="Type", value=data['types'][0]['type']['name'].title())
		embed.add_field(name="Abilities", value=data["abilities"][0]['ability']['name']) 
		return embed
	elif data.status_code == 404:
		embed = discord.Embed(title="Uhh oh...",color=discord.Color.blue())
		embed.set_thumbnail(url="https://assets.pokemon.com/assets/cms2/img/misc/gus/buttons/logo-pokemon-79x45.png")
		embed.add_field(name="Error", value=pokemon.title() + " does not exist!")
		return embed
	#TODO add else to handle unhandled status codes

@commands.command()
async def pokedex(ctx, *, pokemon):
    await ctx.send(embed=pokedex(pokemon))