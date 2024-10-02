from taskController import add_task, update_task, delete_task, view_all_tasks, view_one_task
from embed import simple_embed, error_embed, advanced_embed, task_embed
from utils import truncate_name
 
def setup_commands(bot):
    
    @bot.command(name='add')
    async def add_task_command(ctx, taskname: str = None, description: str = None, responsible: str = ""):

        if taskname is None or description is None:
            await ctx.send(embed=error_embed('All the fields must be filled!'))
            return

        try:
            add_task(taskname.strip().capitalize(), description.strip().capitalize(), responsible.strip())

            await ctx.send(embed=simple_embed("Task added!"))

        except Exception as error:
            await ctx.send(embed=error_embed(str(error)))
    

    @bot.command(name='update')
    async def update_task_status(ctx, taskname: str = None, status: str = None):
        
        if taskname is None or status is None:
            await ctx.send(embed=error_embed('All the fields must be filled!'))
            return
        
        try:
            update_task(taskname.strip().capitalize(), status.strip().capitalize())

            await ctx.send(embed=simple_embed("Task updated!"))

        except Exception as error:
            await ctx.send(embed=error_embed(str(error)))
    

    @bot.command(name='delete')
    async def delete_task_command(ctx, taskname: str = None):

        if taskname is None:
            await ctx.send(embed=error_embed('All the fields must be filled!'))
            return

        try:
            delete_task(taskname.strip().capitalize())

            await ctx.send(embed=simple_embed("Task deleted!"))

        except Exception as error:
            await ctx.send(embed=error_embed(str(error)))


    @bot.command(name='tasks')
    async def view_tasks(ctx):
        try:
            tasks = view_all_tasks()

            if not tasks:
                await ctx.send(embed=error_embed('No tasks avaliable!'))
                return
            
            task_list = "```md\n"
            task_list += f"{'Task Name':<30} | {'Status':<11} | {'Responsible':<16}\n"
            task_list += "-" * 64 + "\n"

            for name, status, responsible in tasks:
                truncated_name = truncate_name(name, 30)
                task_list += f"{truncated_name:<30} | {status:<11} | {responsible:<16}\n"
        
            task_list += "```"

            # await ctx.send(embed=advanced_embed('Tasklist', task_list))
            await ctx.send(task_list)

        except Exception as error:
            await ctx.send(embed=error_embed(str(error)))


    @bot.command(name='task')
    async def view_task(ctx, taskname: str = None):

        if taskname is None:
            await ctx.send(embed=error_embed('All the fields must be filled!'))
            return
        
        try:
            task = view_one_task(taskname.capitalize())
            await ctx.send(embed=task_embed(task))

        except Exception as error:
            await ctx.send(embed=error_embed(str(error)))