import logging, asyncio

from os import environ
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

logging.basicConfig(level=logging.ERROR)
       
SESSION = environ.get("SESSION", "BQFsDkoAkRav7KiFgMAESlQ4ULlTe_4P7L2F67EFT2-p2eL4sZWYflJ5BiDDrGkWM3q9VFipe3GIZf9FiSasvfS2tgdk8yk6Iozd2ZCjQ2J8b4IC21RNP6YLkJyKr2XoDD3luocIFpmr6MfqHHB7E6jBz2ZDrE3yp_j_4CTFMM2VTp4Ouy8dzpxdIY6mtuHWXF7OmOLp94qyaCpls03FiBRCfvS7AWIEjPEX-JQcVa7Ek1t3XYJ4PKICXiJ7ta3BueZzH3tBL7nudHxV2WHW6_rMNGbPQDPtFMy6RIdOnumov_7H-ZMnFtJvc66-Jv6R2QsNQCHB_BnEFyw6pxoxrwKvP1bbXAAAAAGHr3v5AA")        
User = Client(name="AcceptUser", session_string=SESSION)


@User.on_message(filters.command(["run", "approve"], [".", "/"]))                     
async def approve(client, message):
    Id = message.chat.id
    await message.delete(True)
 
    try:
       while True: # create loop is better techniq to accept within seconds 💀
           try:
               await client.approve_all_chat_join_requests(Id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await client.approve_all_chat_join_requests(Id) 
           except Exception as e:
               logging.error(str(e))
    except FloodWait as s:
        asyncio.sleep(s.value)
        while True:
           try:
               await client.approve_all_chat_join_requests(Id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await client.approve_all_chat_join_requests(Id) 
           except Exception as e:
               logging.error(str(e))

    msg = await client.send_message(Id, "**Task Completed** ✓ **Approved Pending All Join Request**")
    await msg.delete()


logging.info("Bot Started....")
User.run()







