from discord.ext.commands import has_permissions
from interactions import Extension, Button, ActionRow, ButtonStyle, ComponentContext, listen, component_callback
from interactions.ext.prefixed_commands import prefixed_command, PrefixedContext

import Funtions.config as cfg


class JoinLad(Extension):

    @prefixed_command(name="join_lad")
    async def verify(self, ctx: PrefixedContext):
        if ctx.author.guild_permissions.ADMINISTRATOR:
            if ctx.channel_id == int(cfg.get("JOIN_LAD_CHANNEL_ID")):
                # Wczytaj regulamin z pliku
                with open("Assets/join_course_message.txt", "r") as file:
                    rules = file.read()

                # Wysłanie regulaminu wraz z przyciskiem
                button = Button(custom_id="join_lad", style=ButtonStyle.PRIMARY, label="Dołącz ✅")
                await ctx.send(rules.replace("%course%", "LAD/FBD"), components=[ActionRow(button)])

    # @listen("on_component")
    @component_callback("join_lad")
    async def on_verify_button(self, ctx: ComponentContext):
        if ctx.custom_id == "join_lad":
            role_id = cfg.get("LAD_ROLE_ID")
            role = ctx.guild.get_role(role_id)
            await ctx.author.add_role(role)
            await ctx.send("✅ Dołączyłeś do kursu LAD/FBD!", ephemeral=True)
            await ctx.author.send("✅ Dołączyłeś do kursu LAD/FBD!")
