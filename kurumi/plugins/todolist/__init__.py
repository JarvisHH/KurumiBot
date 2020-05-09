from nonebot import on_command, CommandSession

__plugin_name__ = 'todolist'
__plugin_usage__ = r"""todolist:
    华华のTodolist:
usage:
    todolist: 查看Todolist
    addtodo: 添加事件
    deltodo: 删除事件"""

me = 3066749824


@on_command('todolist', only_to_me = False)
async def ask_todolist(session: CommandSession):
    if session.event['user_id'] != me:
        await session.send('这是只有主人才能调用的命令哦')
        return
    try:
        f = open('D:\\Study\\CQAbot\\nonebot\\kurumi\\plugins\\todolist\\todolist', 
        'r', encoding = 'utf-8')
        li = eval(f.read())
    finally:
        f.close()
    
    if len(li) == 0:
        await session.send('华华想要做的事情都做完了呢')
        return
    i = 0
    message = "华华のtodolist如下:\n"
    for x in li:
        message += '[{}] {}\n'.format(i, x)
        i = i + 1
    await session.send(message)



@on_command('addtodo', only_to_me = False)
async def add_todo(session: CommandSession):
    if session.event['user_id'] != me:
        return
    todo = session.get('todo', prompt = '华华想做什么？')
    if todo == 'nothing':
        await session.send('那你叫我干嘛？')
        return
    
    try:
        f = open('D:\\Study\\CQAbot\\nonebot\\kurumi\\plugins\\todolist\\todolist', 
        'r', encoding = 'utf-8')
        li = eval(f.read())
        li.append(todo)
        f = open('D:\\Study\\CQAbot\\nonebot\\kurumi\\plugins\\todolist\\todolist', 
        'w', encoding = 'utf-8')
        f.write(str(li))
        await session.send('记下了')
    finally:
        f.close()

@add_todo.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if stripped_arg:
        session.state['todo'] = stripped_arg
    return


@on_command('deltodo', only_to_me = False)
async def del_todo(session: CommandSession):
    if session.event['user_id'] != me:
        return
    f = open('D:\\Study\\CQAbot\\nonebot\\kurumi\\plugins\\todolist\\todolist', 
    'r', encoding = 'utf-8')
    li = eval(f.read())
    if len(li) == 0:
        await session.send('华华想要做的事情都做完了呢')
        return
    done = session.get('done', prompt = '华华要删什么？')
    if done == 'nothing':
        await session.send('那你叫我干嘛？')
        return
    
    i = eval(done)
    if i >= len(li):
        return
    else:
        li.pop(i)
        await session.send('好了')
    f = open('D:\\Study\\CQAbot\\nonebot\\kurumi\\plugins\\todolist\\todolist', 
    'w', encoding = 'utf-8')
    f.write(str(li))
    f.close()

    


@del_todo.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if stripped_arg:
        session.state['done'] = stripped_arg
    return
