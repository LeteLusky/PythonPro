import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

CLASIFICACION = {
    "plastico": "contenedor amarillo",
    "botella": "contenedor amarillo",
    "lata": "contenedor amarillo",
    "papel": "contenedor azul",
    "carton": "contenedor azul",
    "vidrio": "contenedor verde",
    "cristal": "contenedor verde",
    "pila": "punto limpio",
    "bateria": "punto limpio",
    "movil": "punto limpio",
    "ropa": "contenedor especialmente de ropa",
    "organico": "contenedor marron",
    "comida": "contenedor marron",
}

@bot.event
async def on_ready():
    print(f"bot listo como {bot.user}")

@bot.command()
async def r(ctx, *, objeto: str):
    objeto = objeto.lower()
    for palabra, contenedor in CLASIFICACION.items():
        if palabra in objeto:
            await ctx.send(f"**{objeto}** va al **{contenedor}** ♻️")
            return
    await ctx.send(f"**{objeto}** no se encuentra en mi base de datos, prueba con otro objeto o añade uno nuevo con **!add**")

@bot.command()
async def lista(ctx):
    mensaje = "**disponible en mi base de datos:**\n\n"
    for palabra, contenedor in CLASIFICACION.items():
        mensaje += f"• **{palabra}** → {contenedor}\n"
    await ctx.send(mensaje)

@bot.command()
async def add(ctx, objeto: str, contenedor: str):
    objeto = objeto.lower()
    contenedor = contenedor.lower()
    if objeto in CLASIFICACION:
        await ctx.send(f"**{objeto}** ya está en la base de datos, usa otro nombre")
    else:
        CLASIFICACION[objeto] = contenedor
        await ctx.send(f"he añadido **{objeto}** al **{contenedor}** ✅")

@bot.command()
async def ayuda(ctx):
    embed = discord.Embed(
        title="♻️ todos mis comandos ♻️",
        description="aquí van todos mis comandos",
        color=0x00ff66
    )
    embed.add_field(name="!r [objeto]", value="dice donde va", inline=False)
    embed.add_field(name="!lista", value="lista todos los objetos", inline=False)
    embed.add_field(name="!add", value="añade un objeto nuevo", inline=False)

    await ctx.send(embed=embed)


bot.run("de este el tuyo.")
