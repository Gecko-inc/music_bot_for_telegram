import asyncio
import pytgcalls
import pyrogram

API_HASH = None
API_ID = None
CHAT_ID = '@ptnlab_chat'
INPUT_FILENAME = 'input.raw'
OUTPUT_FILENAME = 'output.raw'
CLIENT_TYPE = pytgcalls.GroupCallFactory.MTPROTO_CLIENT_TYPE.PYROGRAM


async def main(client):
    await client.start()
    while not client.is_connected:
        await asyncio.sleep(1)
    group_call = pytgcalls.GroupCallFactory(client, CLIENT_TYPE) \
        .get_file_group_call(INPUT_FILENAME, OUTPUT_FILENAME)
    await group_call.start(CHAT_ID)

    await pyrogram.idle()


if __name__ == '__main__':
    pyro_client = pyrogram.Client(
        "test",
        api_hash=API_HASH,
        api_id=API_ID,
    )
    main_client = pyro_client

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(main_client))
