# coding=utf8
"""sopel-amatsukaze.byte

Collect bytes and grow your HDD size.
"""
from __future__ import unicode_literals, absolute_import, division, print_function

from sopel import plugin


@plugin.command('byte')
def bytes_game(bot, trigger):
    bot.say('Hello, world!')
