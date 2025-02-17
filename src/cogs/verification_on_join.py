import discord
from discord.ext import commands
from asyncio import sleep
from ._settings import log_channel, mod_channel, unverified_role


class logging_verification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    ###### On new join, do this
    async def on_member_join(self, member: discord.Member):
        # Add verification role
        await member.add_roles(member.guild.get_role(unverified_role["needs_approval"]))

        # Log unverified join
        logs_channel = await self.bot.fetch_channel(
            log_channel["verification_log"]
        )  # ADMIN user log
        await logs_channel.send(f"<@{member.id}> joined, but has not verified.")

        # Send Welcome
        guild = member.guild
        welcome_message = f"""
Hi there, {member.mention}
I'm Zorak, the moderatior of {guild.name}.

We are very happy that you have decided to join us.
Before you are allowed to chat, you need to verify that you aren't a bot.
Dont worry, it's easy. Just go to {self.bot.get_channel(mod_channel['verification_channel']).mention} and click the green button.

After you do, all of {guild.name} is availibe to you. Have a great time :-)
"""
        # Send Welcome Message
        await member.send(welcome_message)
        time_unverified_kick = 3600  # 1 hour
        await sleep(time_unverified_kick)

        # Start verification timer
        if "Needs Approval" in [role.name for role in member.roles]:
            # Kick timer, in seconds.
            time_unverified_kick = 3600  # 1 hour
            await sleep(time_unverified_kick)

            if "Needs Approval" in [role.name for role in member.roles]:
                # Log the kick
                await logs_channel.send(
                    f"{member.mention} did not verify, auto-removed. ({(time_unverified_kick/3600)} hour/s)"
                )
                await member.kick(reason="Did not verify.")


def setup(bot):
    bot.add_cog(logging_verification(bot))
