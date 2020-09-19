embed = discord.Embed(
    title="",
    color=discord.Colour(0x3b12ef),
    url="",
    description="",
    timestamp=datetime.datetime.utcfromtimestamp(1580842764)
)
embed.set_image(url="")
embed.set_thumbnail(url="")
embed.set_author(
    name="",
    url="",
    icon_url=""
)
embed.set_footer(
    text="",
    icon_url=""
)

embed.add_field(
    name="",
    value=""
)
embed.add_field(
    name="",
    value=""
)
embed.add_field(
    name="",
    value=""
)
embed.add_field(
    name="",
    value="",
    inline=True
)
embed.add_field(
    name="",
    value="",
    inline=True
)

await ctx.send(
    content="",
    embed=embed
)

If you want to send a local file as the embed image:
embed = discord.Embed()
embed.set_image(
    url=""
)
image = discord.File("")
await ctx.send(
    embed=embed
    file=image
)
