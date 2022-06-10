from typing import Union, Dict

import aiohttp

from app import app
from app.tools import extract_text, write_backup_dump


async def _http_post_data(url: str, data: Dict) -> int:
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{url}", data=data) as r:
            return r.status


async def send_message_to_admin(message: Union[str, Dict]):
    if app.config["TG_REPORTS"]:
        admin: int = app.config["TG_ADMIN"]
        apikey: str = app.config["TG_API_KEY"]
        url = f"https://api.telegram.org/bot{apikey}/sendMessage"
        data = {
            "chat_id": admin,
            "text": extract_text(message),
        }

        code = await _http_post_data(url, data)
        if code != 200:
            write_backup_dump(message)
    else:
        write_backup_dump(message)
