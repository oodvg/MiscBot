from __main__ import bot

import discord
from discord.ext import commands, bridge
from discord.commands import option

from src.func.General import General
from src.func.Union import Union
from src.utils.consts import partner_channel_id, information_embed, neutral_color


class Staff(commands.Cog, name="staff"):
    """
    Commands for Miscellaneous staff members.
    """

    def __init__(self, bot):
        self.bot = bot

    @bridge.bridge_command()
    @commands.has_role("Staff")
    async def inactive(self, ctx):
        """View all inactive users in the guild!"""
        await ctx.defer()
        for embed in await General.inactive(ctx):
            await ctx.respond(embed=embed)

    @bridge.bridge_command(aliases=["fs"])
    @commands.has_role("Staff")
    @option(
        name="member",
        description="The Discord member who you would like to forcesync",
        required=True,
        input_type=discord.Member
    )
    @option(
        name="name",
        description="Their Minecraft username",
        required=True,
        input_type=str
    )
    async def forcesync(self, ctx, member: discord.Member, name: str):
        """Update a user's discord nick, tag and roles for them!"""
        res = await Union(user=member).sync(ctx, name, None, True)
        if isinstance(res, discord.Embed):
            await ctx.respond(embed=res)
        elif isinstance(res, str):
            await ctx.respond(res)

    @bridge.bridge_command()
    @commands.has_role("Admin")
    @option(
        name="organization_name",
        description="The name of the organization you are partnering with",
        required=True,
        input_type=str
    )
    async def partner(self, ctx, *, organization_name: str):
        """Create an embed with information about a partner!"""
        await bot.get_channel(partner_channel_id).send(embed=await General.partner(ctx, organization_name))
        await ctx.respond(embed=discord.Embed(title=f"Miscellaneous has officially partnered with {organization_name}",
                                              color=neutral_color).set_footer(
            text="The partner embed has been sent to the partners channel!"))

    @bridge.bridge_command()
    @commands.has_role("Admin")
    async def information(self, ctx):
        await ctx.respond(embed=information_embed)

    @bridge.bridge_command()
    @commands.has_role("Staff")
    @option(
        name="send_ping",
        description="Enter 'False' if you don't want to ping New Members upon completion of rolecheck",
        required=False,
        input_type=bool
    )
    async def rolecheck(self, ctx, send_ping: bool = True):
        """Sync the names and roles of everyone in the discord!"""
        await General.rolecheck(ctx, send_ping)

    @bridge.bridge_command(aliases=[])
    @commands.has_role("Moderator")
    async def residency(self, ctx, member: discord.Member = None, reason: int = None):
        """Used to update a member's residency in the guild!"""
        await General.resident_membership(ctx, member, reason)

    @bridge.bridge_command(aliases=['rl', 'reslist', 'residencylist'])
    @commands.has_role("Staff")
    async def residentlist(self, ctx):
        await ctx.respond(embed=(await General.resident_list(ctx)))


def setup(bot):
    bot.add_cog(Staff(bot))
