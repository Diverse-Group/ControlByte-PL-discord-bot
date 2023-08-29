from interactions import SlashContext, Extension, slash_command


class PingCommand(Extension):
    @slash_command("ping", description="Odpowiada Pong!")
    async def ping_command(self, ctx: SlashContext):
        await ctx.send("Pong!")


def setup(bot):
    PingCommand(bot)
