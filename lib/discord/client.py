import asyncio
from functools import reduce
from typing import Type, List

import discord
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

    def search_channel(self, query, filter_by: List[Type] = []) -> discord.TextChannel:
        channel_table = list([[x, x.channels] for x in self.guilds])
        all_channels = reduce(lambda x, y: x + y[1], channel_table, [])
        filtered_channels = list(filter(lambda x: type(x) in filter_by, all_channels))
        channel_names = {x.name: x for x in filtered_channels}

        # 1. perfect matching of only channel name
        if query in channel_names:
            return channel_names[query]

        # 2. partial matching of only channel name
        hit_channels = list(filter(lambda kv: kv[0].find(query) != -1, channel_names.items()))
        if len(hit_channels) > 1:
            fatal("There was multiple channel hits to your channel name!")
            return None
        elif len(hit_channels) == 1:
            return hit_channels[0][1]

        return None


