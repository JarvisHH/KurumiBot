# manual

import nonebot
from nonebot import on_command, CommandSession

me = 3066749824

@on_command('manual', only_to_me = False)
async def _(session: CommandSession):
    # 获取设置了名称的插件列表
    plugins = list(filter(lambda p: p.name, nonebot.get_loaded_plugins()))

    arg = session.current_arg_text.strip().lower()
    if not arg:
        # 如果没有发送参数，就发送功能列表
        await session.send(
            'Features Available: \n' + '\n'.join(p.name for p in plugins)
        )
        return

    # 如果发送参数就发送相应命令的使用帮助
    for p in plugins:
        if p.name.lower() == arg:
            await session.send(p.usage)