from nonebot import on_command, CommandSession
import config


__plugin_name__ = 'now'
__plugin_usage__ = r"""now:
    华华现在在做什么
usage:
    hnow || 在干嘛: 询问
    hdoing: 更改
    clearnow: 清空"""


@on_command('hnow', aliases = ('在干嘛'), only_to_me = False)
async def ask_now(session: CommandSession):
    try:
        f = open('D:\\Study\\CQAbot\\nonebot\\kurumi\\plugins\\now\\now.txt', 
        'r', encoding = 'utf-8')
        text = f.read()
        if text:
            await session.send(text)
        else:
            await session.send('华华没有告诉我她在干什么...')
    finally:
        f.close()

@on_command('hdoing', only_to_me = False)
async def change_now(session: CommandSession):
    if not session.event['user_id'] in config.SUPERUSERS:
        await session.send('滚')
        return
    doing = session.get('doing', prompt = '华华在干什么呢？')
    try:
        f = open('D:\\Study\\CQAbot\\nonebot\\kurumi\\plugins\\now\\now.txt', 
        'w', encoding = 'utf-8')
        f.write(doing)
        await session.send('哦')
    finally:
        f.close()

@change_now.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if stripped_arg:
        session.state['doing'] = stripped_arg
    return

@on_command('clearnow', only_to_me = False)
async def clear_now(session: CommandSession):
    if not session.event['user_id'] in config.SUPERUSERS:
        return
    try:
        f = open('D:\\Study\\CQAbot\\nonebot\\kurumi\\plugins\\now\\now.txt', 
        'w', encoding = 'utf-8')
        f.write('')
        await session.send('done')
    finally:
        f.close()