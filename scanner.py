import asyncio

host = input('Host')


async def handle_client():
    return


async def scaner(host, port):
    try:
        reader, writer = await asyncio.open_connection(host, port)
        return port
    except:
        pass

async def main():
    futurs = []
    for i in range(1, 65535):
        futurs.append(scaner(host, i))
    done, pending = await asyncio.wait(futurs)
    for i in done:
        res = i.result()
        if res != None:
            print('Порт ' + str(res) + ' открыт')

asyncio.run(main())
