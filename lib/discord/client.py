import asyncio

from discord import Client
from lib.util.colored_print import log, fatal, success


class DiscordClient(Client):

    def __init__(self, config, **options):
        super().__init__(**options)
        self.token = config.discord_token
        self.on_ready_callback = []
        self.on_message_callback = []

    def access(self):
        asyncio.ensure_future(self.start(self.token))
        asyncio.get_event_loop().run_until_complete(self.wait_until_ready())

    def add_ready_callback(self, f, *args, **kwargs):
        self.on_ready_callback.append([f, args, kwargs])

    def add_message_callback(self, f, *args, **kwargs):
        self.on_message_callback.append([f, args, kwargs])

    async def on_ready(self):
        for func, args, kwargs in self.on_ready_callback:
            returned_value = func(self, *args, **kwargs)
            if returned_value is not None and not returned_value:
                fatal("One of callback functions reported error when handling.")

    async def on_message(self, event):
        for func, args, kwargs in self.on_ready_callback:
            returned_value = func(self, event, *args, **kwargs)
            if returned_value is not None and not returned_value:
                fatal("One of callback functions reported error when handling.")

