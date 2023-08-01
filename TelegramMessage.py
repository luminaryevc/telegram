#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 16:02:38 2023

@author: shahadsami
"""

import telegram

# استيراد معرف بوتك
bot_token = 'YOUR_BOT_TOKEN'

# إنشاء كائن بوت
bot = telegram.Bot(token=bot_token)

# إرسال الرسالة
chat_id = 'CHAT_ID'
message = 'YOUR_MESSAGE'
bot.send_message(chat_id=chat_id, text=message)