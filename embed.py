embed = discord.Embed(
    title = "this *supports* a **subset** of ~~R Markdown~~",
    color = discord.Color(0x3b12ef),
    url = "https://discordapp.com",
    description = "this supports [named links](https://discordapp.com) on top of the subset of markdown.\nYou can use newlines too!",
    timestamp = datetime.datetime.utcfromtimestamp(1600126440)
)
embed.set_image(utl = "")
embed.set_thumbnail(url = "")
embed.set_author(
    name = "Matthew McLaren",
    url = "",
    icon_url = ""
)
embed.set_footer(
    text = "footer text",
    icon_url = ""
)

embed.add_field(
    name = "footer title",
    value = "some of these properties have different limits."
)
ember.add_field(
    name = "another footer title",
    value = "try exceeding some of them! (coz idk them)"
)
embed.add_field(
    name = ":thinking: this supports emotes! (and custom ones too)",
    values = "if you exceed them, the error will tell you which value exceeds it."
)
embed.add_field(
    name = "Inline",
    value = "these last two fields",
    inline = True
)
embed.add_field(
    name = "Fields",
    value = "are inlne fields",
    inline = True
)

await ctx.send(
    content = "This is a normal message to be sent alongside the embed",
    embed = embed
)

if you want to send a local file as the embed image:
embed = discord.Embed()
embed.set_image(
    url = "attachment://hello.png"
)
image = discord.File("hello.png")
await ctx.send(
    embed = embed
    file = image
)
