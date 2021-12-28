import discord

# Colors
neg_color = 0xff3333
pos_color = 0x00A86B
neutral_color = 0x8368ff
error_color = 0xDE3163

# General information
staff_impersonation_embed = discord.Embed(title="Staff impersonation is a punishable offense!", color=neg_color)
guildless_embed = discord.Embed(title="Guildless!", description="This player is not in a guild!", color=neg_color)
unknown_ign_embed = discord.Embed(title="Please enter a valid Minecraft username!", color=neg_color)
unknown_ign_msg = "Unknown IGN!"

# Errors
not_owner_embed = discord.Embed(title=f"Your soul lacks the strength to utilize this command!",
                                description="You are not the owner of this bot!",
                                color=error_color)

missing_role_embed = discord.Embed(title=f"Your soul lacks the strength to utilize this command!",
                                description="You do not have the required roles to access this restricted command!",
                                color=error_color)

missing_permissions_embed = discord.Embed(title=f"Your soul lacks the strength to utilize this command!",
                                    description="You do not have the required permissions to access this restricted command!",
                                    color=error_color)

member_not_found_embed = discord.Embed(title=f"Member not found",
                                    description="This member doesn't seem to exist.\nCheck you have their ID or tag's capitalization and spelling correct!",
                                    color=error_color)

err_404_embed = discord.Embed(title="404 - Not Found",
                            description="The bot encountered an error 404 while performing this action!",
                            color=error_color)

bot_missing_perms_embed = discord.Embed(title="Missing permissions!",
                                        description="Due to the role hierarchy, the bot does not have the permission to do that!",
                                        color=error_color)
