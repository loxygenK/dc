from discord import Client
from lib.util.colored_print import log, fatal
import threading

class DiscordClient(Client):

    def __init__(self, config):
        super(Client, self).__init__()
        self.token = config.discord_token
        self.on_ready_callback = []
        self.on_message_callback = []

    def __start(self):
        log("Started discord client. Logging in...")
        self.run(self.token)

    def start(self):
        threading.Thread(target=self.__start).start()

    def add_ready_callback(self, f, *args, **kwargs):
        self.on_ready_callback.append([f, args, kwargs])

    def add_message_callback(self, f, *args, **kwargs):
        self.on_message_callback.append([f, args, kwargs])

    async def on_ready(self, event):
        for func, args, kwargs in self.on_ready_callback:
            returned_value = func(self, *args, **kwargs)
            if returned_value is not None and not returned_value:
                fatal("One of callback functions reported error when handling.")

    async def on_mesage(self, event):
        for func, args, kwargs in self.on_ready_callback:
            returned_value = func(self, event, *args, **kwargs)
            if returned_value is not None and not returned_value:
                fatal("One of callback functions reported error when handling.")

