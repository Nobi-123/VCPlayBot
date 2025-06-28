import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQHBq6EAiBcItVFwgzef4si4fPC7s-VEU6fDJobl03M7jl2pYTt21RpER_7ihx-o2N801xb3gvcnTx0YgQIJxvCESW558tJaW_yZOVo3pBr7iCR0YViMv0k6AHW3Pph5ozcyQWMMVsPZw2VBrgzQ7UPZBIXuTYd394ZC47MYrPQo2ZTFIYl11skk3XyI_UzJQALxtVWfgujGGk-lXajaO-pBa2_3efsygYvnJuMfAEASKWdAh8qQ82_oSV2k-ikyAnTzGmNVfqLehs2n--9kzNIl3-cYDQChWeT1DFwHWMkaoG6JZcAw9dOebSeto7qI90ve02ZGMtM-yK5Qz8BRnyjCZMyawQAAAAGz9WqZAA")
BOT_TOKEN = getenv("7930139593:AAEfK99-9dRhR4F-NJw9EpC61yUs1f-aY9c")
BOT_NAME = getenv("Test")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "New_Channel_Mine")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/9b13ea3ce046a1a5c8098.png")
admins = {}
API_ID = int(getenv("29469601"))
API_HASH = getenv("c5773359dc095f51b3d57f2f7969c5dc")
BOT_USERNAME = getenv("bakixhanma_testbot")
ASSISTANT_NAME = getenv("ItxmEsCaRlEt", "Scarlet")
OWNER_NAME = getenv("ItZmEcUrSeD", "Cursed")
SUPPORT_GROUP = getenv("HANMA_SUPPORT", "AwesomeSupport")
PROJECT_NAME = getenv("PROJECT_NAME", "VCPlayBot2.0")
SOURCE_CODE = getenv("SOURCE_CODE", "")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8023408663").split()))
