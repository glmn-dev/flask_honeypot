import hashlib
import json
import time
from typing import Union

from flask import Request
from app import app


def write_backup_dump(log: dict) -> None:
    with open("routes.log", "a") as file:
        file.write(json.dumps(log, indent=4, sort_keys=True))
        file.write("\r\n")


def extract_text(text: Union[dict, str]) -> str:
    if isinstance(text, dict):
        return "\n".join("{!r}: {!r},".format(k, v) for k, v in text.items())
    return text


def parse_headers(headers, d: dict) -> dict:
    for header in headers:
        d[header[0]] = header[1]
    return d


def default_actions(req: Request) -> dict:
    d: dict = {}
    d = parse_headers(req.headers, d)
    d['request_type'] = req.method
    d['path'] = req.full_path
    d['ip_address'] = req.remote_addr
    d['port'] = app.config["PORT"]
    if req.method == 'POST':
        d['body'] = req.get_data().decode('utf-8')
    d['hash'] = hashlib.md5(json.dumps(d).encode('utf-8')).hexdigest()
    d['unix_timestamp'] = int(time.time())
    d['readable_timestamp'] = time.ctime()
    return d
