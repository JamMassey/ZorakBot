import random


def n_sided_dice(n:int = 6):
	return 	random.choice(list(range(1,n+1)))

@commands.command()
async def rolldice(ctx):
	await ctx.send(f"**{ctx.message.author.name}** rolled a **{n_sided_dice()}**", reference=ctx.message)