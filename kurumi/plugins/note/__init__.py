from nonebot import on_command, CommandSession


__plugin_name__ = 'note'
__plugin_usage__ = r"""note: 
    华华的笔记
usage:
    hnote 查看
    takenote 记笔记
"""

me = 3066749824

@on_command('hnote', only_to_me = False)
async def check_note(session: CommandSession):
    if session.event['user_id'] != me:
        return
    try:
        f = open('D:\\Study\\CQAbot\\nonebot\\kurumi\\plugins\\note\\note.txt', 
        'r', encoding = 'utf-8')
        await session.send(f.read())
    finally:
        f.close()


@on_command('takenote', only_to_me = False)
async def add_note(session: CommandSession):
    if session.event['user_id'] != me:
        return
    note = session.get('note', prompt = '华华想记什么？')
    if note == 'nothing':
        await session.send('那你叫我干嘛？')
        return
    try:
        f = open('D:\\Study\\CQAbot\\nonebot\\kurumi\\plugins\\note\\note.txt', 
        'a', encoding = 'utf-8')
        f.write(note)
        f.write('\n')
        await session.send('记下了')
    finally:
        f.close()

@add_note.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if stripped_arg:
        session.state['note'] = stripped_arg
    return
