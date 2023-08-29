from discord.ext.commands import has_permissions
from interactions import Extension, Button, ActionRow, ButtonStyle, ComponentContext, listen, component_callback
from interactions.ext.prefixed_commands import prefixed_command, PrefixedContext

import Funtions.config as cfg


class VerifyCommand(Extension):

    @prefixed_command(name="verifycben")
    async def verify(self, ctx: PrefixedContext):
        if ctx.author.guild_permissions.ADMINISTRATOR:
            if ctx.channel_id == int(cfg.get("VERIFY_CHANNEL_ID")):
                # Wczytaj regulamin z pliku
                with open("Assets/rules.txt", "r") as file:
                    rules = file.read()

                # Wysłanie regulaminu wraz z przyciskiem
                button = Button(custom_id="verify_me", style=ButtonStyle.PRIMARY, label="Zwerifikuj się ✅")
                await ctx.send(rules, components=[ActionRow(button)])

    #@listen("on_component")
    @component_callback("verify_me")
    async def on_verify_button(self, ctx: ComponentContext):
        if ctx.custom_id == "verify_me":
            role_id = cfg.get("VERIFY_ROLE_ID")
            role = ctx.guild.get_role(role_id)
            await ctx.author.add_role(role)
            await ctx.send("✅ Zostałeś zakwalifikowany na serwerze ControlByte!", ephemeral=True)
            await ctx.author.send("✅ Zostałeś zakwalifikowany na serwerze ControlByte!")

