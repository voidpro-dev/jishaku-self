dir = "."

code = open(f"{dir}/jishaku/types.py","r",encoding="utf_8").read()
code = code.replace("BotT = typing.Union[commands.Bot, commands.AutoShardedBot]", "BotT = typing.Union[commands.Bot, None]")
code = code.replace("discord.version_info >= (2, 0, 0)", "False")
open(f"{dir}/jishaku/types.py","w",encoding="utf_8").write(code)

code = open(f"{dir}/jishaku/modules.py","r",encoding="utf_8").read()
code = code.replace("discord.version_info >= (2, 0, 0)", "False")
open(f"{dir}/jishaku/modules.py","w",encoding="utf_8").write(code)

code = open(f"{dir}/jishaku/paginators.py","r",encoding="utf_8").read()
code = code.replace("discord.version_info >= (2, 0, 0)", "False")
open(f"{dir}/jishaku/paginators.py","w",encoding="utf_8").write(code)

code = open(f"{dir}/jishaku/shim/paginator_170.py","r",encoding="utf_8").read()
code = code.replace("bot: typing.Union[commands.Bot, commands.AutoShardedBot],", "bot: typing.Union[commands.Bot, None],")
open(f"{dir}/jishaku/shim/paginator_170.py","w",encoding="utf_8").write(code)

code = open(f"{dir}/jishaku/features/root_command.py","r",encoding="utf_8").read()
code = code.replace("if isinstance(self.bot, discord.AutoShardedClient):", "if False:")
code = code.replace("elif self.bot.shard_count:", "elif False:")
code = code.replace("f\"{intent.replace('_', ' ')} intent is {remarks.get(getattr(self.bot.intents, intent, None))}\"", "f\"{intent.replace('_', ' ')} intent is {remarks.get(True)}\"")
open(f"{dir}/jishaku/features/root_command.py","w",encoding="utf_8").write(code)

code = open(f"{dir}/jishaku/flags.py","r",encoding="utf_8").read()
code = code.replace("return not ctx.author.is_on_mobile() if isinstance(ctx.author, discord.Member) and ctx.bot.intents.presences else True", "return not ctx.author.is_on_mobile() if isinstance(ctx.author, discord.Member) else True")
open(f"{dir}/jishaku/flags.py","w",encoding="utf_8").write(code)

code = open(f"{dir}/jishaku/exception_handling.py","r",encoding="utf_8").read()
code = code.replace("""paginator = commands.Paginator(prefix='```py')
    for line in traceback_content.split('\\n'):""", """paginator = commands.Paginator(prefix='```py')
    start = False
    for line in traceback_content.split('\\n'):""")
code = code.replace("""for line in traceback_content.split('\\n'):
        paginator.add_line(line)""", """for line in traceback_content.split('\\n'):
        if "Traceback (most recent call last):" in line and not start:
            paginator.add_line(line)
            start = True
        elif 'in _repl_coroutine' in line:
            paginator.add_line(line.replace("_repl_coroutine", "jishaku"))
            start = False
        elif not start:
            paginator.add_line(line)""")
open(f"{dir}/jishaku/exception_handling.py","w",encoding="utf_8").write(code)
