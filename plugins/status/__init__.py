from datetime import datetime, timedelta
from nonebot import get_bot, on_command, CommandSession


def timedelta2str(td):
    mm, ss = divmod(td.seconds, 60)
    hh, mm = divmod(mm, 60)
    s = "%d:%02d:%02d" % (hh, mm, ss)
    if td.days:
        def plural(n):
            return n, abs(n) != 1 and "s" or ""

        s = ("%d day%s, " % plural(td.days)) + s
    return s


bot = get_bot()
start_time = datetime.now()


@on_command('status', only_to_me=False)
async def _(session: CommandSession):
    now = datetime.now()
    uptime: timedelta = now - start_time
    msg = f'uptime: {timedelta2str(uptime)}'
    await session.send(msg)
