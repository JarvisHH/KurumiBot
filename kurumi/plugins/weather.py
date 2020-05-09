from nonebot import on_command, CommandSession
import random

# 教程里的weather和几个简单的关键字回复

@on_command('weather', aliases = ('weather', '天气'))
async def weather(session: CommandSession):
    city = session.get('city', prompt = '你想查询哪个城市的天气呢？')
    weather_report = await get_weather_of_city(city)
    await session.send(weather_report)

@weather.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['city'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的城市名称不能为空呢，请重新输入')
    session.state[session.current_key] = stripped_arg

async def get_weather_of_city(city: str) -> str:
    return f'我tm一个bot能知道天气就见鬼了'

@on_command('hive', only_to_me = False)
async def hive(session: CommandSession):
    await session.send('华华不是废物啦，摸摸')

@on_command('zoule', aliases = ('走了'), only_to_me = False)
async def zoule(session: CommandSession):
    await session.send('“走了”不就是去读读的借口 [CQ:face,id=77]')

@on_command('hgame', only_to_me = False)
async def hgame(session: CommandSession):
    await session.send("华华今天还没有game哟")

@on_command('coin', aliases = ('抛硬币'), only_to_me = False)
async def coin(session: CommandSession):
    if random.randint(0, 1) == 0:
        await session.send('正面')
    else:
        await session.send('反面')