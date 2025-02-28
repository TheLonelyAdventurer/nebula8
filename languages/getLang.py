#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

from config import Config
from core.database.repository.group_language import GroupLanguageRepository
from languages import (EN,IT)

def get(update, context):
    chat = update.effective_message.chat_id
    row = GroupLanguageRepository().getById([chat])
    if row is None:
        return None
    else:
        return row['languages']

def languages(update, context):
    LANGUAGE = get(update,context)

    if LANGUAGE == "" or LANGUAGE is None:
        LANGUAGE = Config.DEFAULT_LANGUAGE

    if LANGUAGE == "IT":
        setLang = IT.Italian
    elif LANGUAGE == "EN":
        setLang = EN.English

    languages.lang_default = setLang["LANG_DEFAULT"]
    languages.start = setLang["START_COMMAND"]
    languages.helps = setLang["HELP_COMMAND"]
    languages.group_info = setLang["GROUP_INFO"]
    languages.bot_welcome = setLang["BOT_WELCOME"]
    languages.ban_message = setLang["BAN_MESSAGE"]
    languages.rules = setLang["RULES"]
    languages.user_ban = setLang["BAN_USER"]
    languages.bot_ban = setLang["BAN_BOT"]
    languages.ban_error = setLang["BAN_ERROR"]
    languages.ban_user_error = setLang["BAN_USER_ERROR"]
    languages.say_error = setLang["SAY_MESSAGE"]
    languages.delete_error_msg = setLang["DELETE_MESSAGE"]
    languages.close_menu_msg = setLang["CLOSE_SETTINGS"]
    languages.main_menu_msg = setLang["MAIN_TEXT_SETTINGS"]
    languages.welcome_set = setLang["WELCOME_SETTINGS"]
    languages.set_welcome_main = setLang["SET_MAIN_WELCOME"]
    languages.set_welcome_help = setLang["WELCOME_MAIN_HELP_SET"]
    languages.weather_message = setLang["WEATHER_MSG"]
    languages.report_msg = setLang["REPORT_ADMIN_MSG"]
    languages.rules_msg = setLang["RULES_MSG"]
    languages.rules_error_msg = setLang["RULES_ERROR_MSG"]
    languages.perm_error = setLang["PERM_MSG_ERROR"]
    languages.perm_ok = setLang["PERM_MSG_OK"]
    languages.close_menu_general = setLang["CLOSE_MENU"]
    languages.global_report_msg = setLang["GLOBAL_REPORT_MSG"]
    languages.error_response_user_msg = setLang["ERROR_RESPONSE_USER_MSG"]
    return LANGUAGE