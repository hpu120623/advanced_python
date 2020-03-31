# python为了将语义变的更加明确，就引入了async和await关键词用于原生定义的协程

async def downloader(url):
    return 'python'

async def down_url(url):
    # dosomething1
    html = await downloader(url) # await对应yield from
    return html

if __name__ == '__main__':
    coro = down_url('https://www.baidu.com')
    coro.send(None)