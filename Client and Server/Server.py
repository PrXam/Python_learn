import asyncio


dict_data = {}


def put(writer, req):
    try:
        list_req = req.split()
        if len(list_req) != 3:
            raise Exception
        if str(list_req[0]) not in dict_data:
            dict_data[str(list_req[0])] = []
            dict_data[str(list_req[0])].append((float(list_req[1]), int(list_req[2])))
        match = 0
        for tup in dict_data[str(list_req[0])]:
            if type(tup) == tuple and int(tup[1]) == int(list_req[2]):
                index = dict_data[str(list_req[0])].index(tup)
                dict_data[str(list_req[0])][index] = (float(list_req[1]), int(list_req[2]))
                match = 1
                break
        if match == 0:
            dict_data[str(list_req[0])].append((float(list_req[1]), int(list_req[2])))
        writer.write(b'ok\n\n')
    except Exception as err:
        print(err)
        writer.write(b'error\nwrong command\n\n')


def get(writer, req):
    try:
        if str(req) == '*':
            response = 'ok\n'
            for key, value in dict_data.items():
                for elem in value:
                    response = response + (' '.join([str(key), str(elem[0]), str(elem[1])]) + '\n')
            response = response + '\n'
            writer.write(response.encode())
        elif len(req.split()) == 1 and dict_data.get(str(req)) is None:
            writer.write(b'ok\n\n')
        elif len(req.split()) == 1 and dict_data.get(str(req)):
            response = 'ok\n'
            for elem in dict_data[str(req)]:
                response = response + (' '.join([str(req), str(elem[0]), str(elem[1])]) + '\n')
            response = response + '\n'
            writer.write(response.encode())
        else:
            writer.write(b'error\nwrong command\n\n')
    except Exception as err:
        print(err)
        writer.write(b'error\nwrong command\n\n')


async def handler(reader, writer):
    while True:
        data = await reader.read(1024)
        if data:
            data = data.decode()
            try:
                comm, req = data.split(' ', 1)
                req = req[:-1]
            except ValueError:
                comm = 0
            if comm == 'put':
                put(writer, req)
            elif comm == 'get':
                get(writer, req)
            else:
                writer.write(b'error\nwrong command\n\n')
        else:
            writer.close()
            break


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(handler, host, port, loop=loop)
    server = loop.run_until_complete(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == '__main__':
    run_server('127.0.0.1', 8888)