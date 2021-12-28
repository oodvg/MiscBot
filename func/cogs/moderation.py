import discord
from discord.ext import commands

from func.classes.Union import Union
from func.classes.Integer import Integer

class Moderation(commands.Cog, name="Moderation"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        """Mute the mentioned user indefinitely!"""
        await ctx.send(embed=await Union(user=member).mute(ctx.author, ctx.guild.roles, reason))


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: discord.Member, *, reason=None):
        """Unmute the mentioned user!"""
        await ctx.send(embed=await Union(user=member).unmute(ctx.guild.roles))


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kick the mentioned user!"""
        await ctx.send(embed=await Union(user=member).kick(ctx.author, reason))


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Ban the mentioned user!"""
        await ctx.send(embed=await Union(user=member).ban(ctx.guild, ctx.author, reason))

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def softban(self, ctx, member: discord.Member, *, reason=None):
        """Softban the mentioned user!"""
        await ctx.send(embed=await Union(user=member).softban(ctx.guild, ctx.author, reason))


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user: discord.User, *, reason=None):
        """Unban the mentioned user!"""
        await ctx.send(embed=await Union(user=user).unban(ctx.guild, ctx.author, reason))


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int, *, reason: str=None):
        """Clears the given number of messages!"""
        await Integer(integer=amount).purge(ctx, reason)

def setup(bot):
    bot.add_cog(Moderation(bot))
