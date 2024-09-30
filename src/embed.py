import discord

def simple_embed(message: str):
    simple = discord.Embed(
        description=f'**{message}**',
        color=discord.Color.light_embed()
    )
    return simple


def error_embed(message: str):
    error = discord.Embed(
        title='**__ERROR!__**',
        description=f'{message}',
        color=discord.Color.red()
    )
    return error


def advanced_embed(title: str, message: str):
    advanced = discord.Embed(
        title=f'**__{title}__**',
        description=f'{message}',
        color=discord.Color.light_embed()
    )
    return advanced


def task_embed(task):
    coolTask = discord.Embed(
        title=f"**__{task['name']}__**",
        description=f"{task['description']}",
        color=discord.Color.light_embed()
    )

    coolTask.add_field(name="Responsible", value=task['responsible'], inline=True)
    coolTask.add_field(name="Status", value=task['status'], inline=True)
    coolTask.add_field(name="Created at", value=task['created_at'].strftime("%d/%m/%Y %H:%M:%S"), inline=True)

    return coolTask