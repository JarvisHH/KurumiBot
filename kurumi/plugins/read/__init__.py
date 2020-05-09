from nonebot import on_command, CommandSession
import time

__plugin_name__ = 'read'
__plugin_usage__ = r"""read: 
    看看华华读了什么
usage:
    hread: 查询
    hdone: 添加
    hclear: 清空"""

me = 3066749824

@on_command('hread', only_to_me = False)
async def ask_read(session: CommandSession):
    try:
        f = open('D:\\Study\\CQAbot\\nonebot\\kurumi\\plugins\\read\\hread.txt', 
        'r', encoding = 'utf-8', errors = 'ignore')
        await session.send(f.read())
        if session.event['user_id'] == me:
            time.sleep(1.2)
            await session.send('写这么少还有脸叫我')
            time.sleep(0.6)
            await session.send('你怎么回事')
    finally:
        f.close()

@on_command('hdone', only_to_me = False)
async def add_done(session: CommandSession):
    if session.event['user_id'] != me:
        await session.send('滚')
        return
    done = session.get('done', prompt = '华华又读了什么呢？')
    if done == 'nothing':
        await session.send('读都没读为啥叫我！！！')
        return
    try:
        f = open('D:\\Study\\CQAbot\\nonebot\\kurumi\\plugins\\read\\hread.txt', 
        'a', encoding = 'utf-8')
        f.write(done)
        f.write('\n')
        await session.send('记下了')
    finally:
        f.close()

@add_done.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if stripped_arg:
        session.state['done'] = stripped_arg
    return

@on_command('hclear', only_to_me = False)
async def all_clear(session: CommandSession):
    if session.event['user_id'] != me:
        return
    f = open('D:\\Study\\CQAbot\\nonebot\\kurumi\\plugins\\read\\hread.txt', 
        'w', encoding = 'utf-8')
    f.write('')
    await session.send('done')