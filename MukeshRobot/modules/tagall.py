import asyncio

from telethon import events
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator
import random
from MukeshRobot import telethn as client

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]
          
TAGMES = [ " **𝐎𝐲𝐲 𝐭𝐞𝐫𝐞 𝐛𝐚𝐥𝐞 𝐤𝐨 𝐣𝐚𝐤𝐚𝐫 𝐛𝐚𝐭𝐚𝐭𝐚 𝐡𝐮 𝐭𝐮 𝐲𝐡𝐚 𝐬𝐞𝐭𝐭𝐢𝐧𝐠 𝐤𝐚𝐫 𝐫𝐡𝐢 𝐡𝐚𝐢🥱** ",
           " **𝐀𝐩𝐤𝐢 𝐞𝐤 𝐩𝐢𝐜 𝐦𝐢𝐥𝐞𝐠𝐢 𝐤𝐲𝐚 𝐢𝐦𝐚𝐠𝐢𝐧𝐞 𝐤𝐚𝐫 𝐤𝐞 𝐦*𝐭𝐡 𝐤𝐚𝐫𝐧𝐚 𝐡𝐢** ",
           " **𝐕𝐜 𝐂𝐡𝐚𝐥𝐨 𝐑𝐨𝐦𝐚𝐧𝐭𝐢𝐜 𝐁𝐚𝐭𝐞𝐧 𝐊𝐚𝐫𝐭𝐞 𝐇𝐚𝐢𝐧 𝐊𝐮𝐜𝐡 𝐊𝐮𝐜𝐡😃** ",
           " **𝐓𝐡𝐚𝐧𝐝𝐢 𝐦𝐞 𝐭𝐮𝐦𝐡𝐚𝐫𝐚 𝐤𝐡𝐚𝐝𝐚 𝐡𝐨𝐭𝐚 𝐡𝐚𝐢 𝐤𝐲𝐚 😁🥲** ",
           " **𝐔𝐟𝐟 𝐊𝐲𝐚 𝐦𝐚𝐚𝐥 𝐡𝐚𝐢 𝐲𝐚𝐚𝐫 😁😂🥺** ",
           " **𝐏𝐭𝐚 𝐇𝐚𝐢 𝐁𝐨𝐡𝐨𝐭 𝐌𝐢𝐬𝐬 𝐊𝐚𝐫 𝐑𝐡a 𝐓𝐡a 𝐀𝐚𝐩𝐤𝐨 𝐛𝐚𝐭𝐡𝐫𝐨𝐨𝐦 𝐦𝐞 🤭** ",
           " **𝐎𝐲𝐞 𝐃𝐌 𝐊𝐚𝐫𝐨 𝐀𝐩𝐤𝐚 𝐦𝐨𝐨𝐝 𝐛𝐧𝐚 𝐝𝐞𝐭𝐢 𝐡𝐮 😅😅** ",
           " **𝐌𝐞𝐫𝐢 𝐁𝐡𝐢 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫𝐛𝐚 𝐃𝐨𝐠𝐞.𝐇𝐢𝐥𝐥𝐚 𝐇𝐢𝐥𝐥𝐚 𝐤𝐞 𝐭𝐡𝐚𝐤 𝐠𝐲𝐚 𝐡𝐮 ??🙂** ",
           " **𝐎𝐲𝐲 𝐭𝐞𝐫𝐞 𝐛𝐚𝐥𝐞 𝐤𝐨 𝐣𝐚𝐤𝐚𝐫 𝐛𝐚𝐭𝐚𝐭𝐚 𝐡𝐮 𝐭𝐮 𝐲𝐡𝐚 𝐬𝐞𝐭𝐭𝐢𝐧𝐠 𝐤𝐚𝐫 𝐫𝐡𝐢 𝐡𝐚𝐢🥲** ",
           " **𝐤𝐚 𝐡𝐨 𝐤𝐚𝐫𝐞𝐣𝐚 1 𝐜𝐡𝐮𝐦𝐦𝐚 𝐧𝐚 𝐝𝐞𝐛𝐮 😅😋** ",
           " **𝐎𝐲𝐲 𝐌𝐞𝐫𝐞 𝐊𝐨 𝐀𝐩𝐧𝐞 𝐛𝐞𝐝𝐫𝐨𝐨𝐦 𝐦𝐞 𝐤𝐢𝐝𝐧𝐞𝐩 𝐤𝐚𝐫 𝐥o😅😅 ** ",
           " **𝐀𝐚𝐩𝐤𝐢 𝐏𝐚𝐫𝐭𝐧𝐞𝐫 𝐀𝐚𝐩𝐤𝐨 𝐃𝐡𝐮𝐧𝐝 𝐑𝐡𝐞 𝐇𝐚𝐢𝐧 𝐉𝐥𝐝𝐢 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐲𝐢𝐚𝐞😅😅** ",
           " **𝐇𝐚𝐦 𝐃𝐨𝐬𝐭 𝐁𝐚𝐧 𝐒𝐚𝐤𝐭𝐞 𝐇𝐚𝐢...?🥰 𝐌𝐚𝐬𝐭𝐞𝐫𝐛𝐚𝐭𝐢𝐧𝐠 𝐤𝐚𝐫𝐧𝐞 𝐦𝐞 𝐡𝐞𝐥𝐩 𝐡𝐨 𝐣𝐚𝐲𝐞𝐠𝐢 𝐦𝐞𝐫𝐢 😁🤔** ",
           " **𝐒𝐨𝐧𝐞 𝐂𝐡𝐚𝐥 𝐆𝐲𝐞 𝐊𝐲𝐚 𝐉𝐀𝐍𝐄𝐌𝐀𝐍 🙄🙄** ",
           " **𝐇𝐚𝐦 𝐃𝐨𝐬𝐭 𝐁𝐚𝐧 𝐒𝐚𝐤𝐭𝐞 𝐇𝐚𝐢...?🥰 𝐌𝐚𝐬𝐭𝐞𝐫𝐛𝐚𝐭𝐢𝐧𝐠 𝐤𝐚𝐫𝐧𝐞 𝐦𝐞 𝐡𝐞𝐥𝐩 𝐡𝐨 𝐣𝐚𝐲𝐞𝐠𝐢 𝐦𝐞𝐫𝐢 😁 😁😕** ",
           " **𝐲𝐨𝐮𝐫 𝐟𝐚𝐯𝐨𝐮𝐫𝐢𝐭𝐞 𝐚𝐜𝐭𝐫𝐞𝐬𝐬 (𝐒𝐔𝐍𝐍𝐘 𝐋𝐄𝐎𝐍𝐄, 𝐨𝐫 𝐌𝐈𝐘𝐀 𝐊𝐇𝐀𝐋𝐈𝐅𝐀)🙃** ",
           " **𝐎𝐲𝐲 𝐏𝐫𝐢𝐲𝐚 𝐁𝐡𝐚𝐛𝐡𝐢 𝐤𝐚 𝐤𝐲𝐚 𝐡𝐚𝐢 😁😁😛** ",
           " **𝐇𝐞𝐥𝐥𝐨 𝐁𝐚𝐛𝐲 𝐊𝐤𝐫𝐡..?🤔** ",
           " **𝐎𝐲𝐲 𝐬𝐮𝐧𝐨 𝐀𝐩 𝐑𝐨𝐣 𝐡𝐢𝐥𝐚𝐭𝐞 𝐡𝐨 𝐤𝐲𝐚 𝐩𝐚𝐭𝐥𝐞 𝐡𝐨 𝐠𝐲𝐞 𝐡𝐨 😅** ",
           " **𝐂𝐡𝐥𝐨 𝐇𝐚𝐦 𝐝𝐨𝐧𝐨 𝐫𝐚𝐭 𝐛𝐚𝐥𝐚.𝐠𝐚𝐧𝐞 𝐤𝐡𝐚𝐭𝐞 𝐡𝐚𝐢 😁.🤗** ",
           " **𝐂𝐡𝐚𝐥𝐨 𝐡𝐚𝐦 𝐝𝐨𝐧𝐨 𝐫𝐨𝐦𝐚𝐧𝐭𝐢𝐜 𝐛𝐚𝐭𝐞 𝐤𝐚𝐫𝐭𝐞 𝐡𝐚𝐢 😇** ",
           " **𝐨𝐨𝐲 𝐦𝐞𝐫𝐢 𝐡𝐞𝐥𝐩 𝐤𝐚𝐫𝐨𝐠𝐞 𝐦𝐚𝐬𝐭𝐞𝐫𝐛𝐚𝐭𝐞 𝐤𝐚𝐫𝐧𝐞 𝐦𝐞 😁🤭** ",
           " **𝐎𝐲𝐲 𝐭𝐮 𝐢𝐭𝐧𝐢 𝐡𝐨𝐭 𝐤𝐲𝐮 𝐡𝐚𝐢 𝐝𝐞𝐤𝐡𝐭𝐞 𝐡𝐢 𝐦𝐚𝐧 𝐤𝐚𝐫𝐭𝐚 𝐡𝐚𝐢 𝐡𝐢𝐥𝐚 𝐥𝐮 😁😀🥺🥺** ",
           " **𝐎𝐲𝐞 𝐏𝐚𝐠𝐚𝐥 𝐚𝐩𝐤𝐢 𝐚𝐠𝐞 𝐤𝐲𝐚 𝐡𝐚𝐢 𝐡𝐨𝐭 𝐥𝐠𝐭𝐞 𝐡𝐨 𝐚𝐩😶** ",
           " **𝐀𝐚𝐣 𝐇𝐨𝐥𝐢𝐝𝐚𝐲 𝐇𝐚𝐢 𝐊𝐲𝐚 𝐒𝐜𝐡𝐨𝐨𝐥 𝐌𝐞..??🤔** ",
           " **𝐤𝐚 𝐡𝐨 𝐤𝐚𝐫𝐞𝐣𝐚 1 𝐜𝐡𝐮𝐦𝐦𝐚 𝐧𝐚 𝐝𝐞𝐛𝐮 😅😜** ",
           " **𝐌𝐞𝐫𝐢 𝐁𝐡𝐢 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫𝐛𝐚 𝐃𝐨𝐠𝐞.𝐇𝐢𝐥𝐥𝐚 𝐇𝐢𝐥𝐥𝐚 𝐤𝐞 𝐭𝐡𝐚𝐤 𝐠𝐲𝐚 𝐡𝐮 🙂🙂** ",
           " **𝐚𝐩𝐤𝐢 𝐚𝐠𝐞 𝐤𝐲𝐚 𝐡𝐚𝐢 𝐡𝐨𝐭 𝐡𝐨 𝐚𝐩 𝐝𝐞𝐤𝐡𝐭𝐞 𝐡𝐢 𝐦𝐚𝐧 𝐤𝐚𝐫𝐭𝐚 𝐡𝐢𝐥𝐚𝐭𝐞 𝐫𝐡𝐮😁😪** ",
           " **𝐍𝐢𝐜𝐞 𝐓𝐨 𝐌𝐞𝐞𝐭 𝐔𝐡 𝐉𝐀𝐍𝐄𝐌𝐀𝐍☺** ",
           " **𝐇𝐞𝐥𝐥𝐨 𝐀𝐩𝐤𝐚 𝐛𝐫𝐞𝐚𝐤 𝐮𝐩 𝐤𝐚𝐫𝐛𝐚 𝐝𝐞𝐭𝐚 𝐡𝐮 𝐚𝐩 𝐦𝐞𝐫𝐞 𝐬𝐞 𝐬𝐞𝐭𝐭𝐢𝐧𝐠 𝐤𝐚𝐫𝐥𝐨 😀😁🙊** ",
           " **𝐎𝐲𝐲 𝐭𝐞𝐫𝐞 𝐛𝐚𝐥𝐞 𝐤𝐨 𝐣𝐚𝐤𝐚𝐫 𝐛𝐚𝐭𝐚𝐭𝐚 𝐡𝐮 𝐭𝐮 𝐲𝐡𝐚 𝐬𝐞𝐭𝐭𝐢𝐧𝐠 𝐤𝐚𝐫 𝐫𝐡𝐢 𝐡𝐚𝐢😺** ",
           " **𝐎𝐲𝐲 𝐬𝐮𝐧𝐨 𝐀𝐩 𝐑𝐨𝐣 𝐡𝐢𝐥𝐚𝐭𝐞 𝐡𝐨 𝐤𝐲𝐚 𝐩𝐚𝐭𝐥𝐞 𝐡𝐨 𝐠𝐲𝐞 𝐡𝐨🥲** ",
           " **𝐎𝐲𝐲 𝐭𝐞𝐫𝐞 𝐛𝐚𝐥𝐞 𝐤𝐨 𝐣𝐚𝐤𝐚𝐫 𝐛𝐚𝐭𝐚𝐭𝐚 𝐡𝐮 𝐭𝐮 𝐲𝐡𝐚 𝐬𝐞𝐭𝐭𝐢𝐧𝐠 𝐤𝐚𝐫 𝐫𝐡𝐢 𝐡𝐚𝐢😅** ",
           " **𝐀𝐩𝐤𝐢 𝐞𝐤 𝐩𝐢𝐜 𝐦𝐢𝐥𝐞𝐠𝐢 𝐤𝐲𝐚 𝐢𝐦𝐚𝐠𝐢𝐧𝐞 𝐤𝐚𝐫 𝐤𝐞 𝐦*𝐭𝐡 𝐤𝐚𝐫𝐧𝐚 𝐡𝐢😅** ",
           " **𝐓𝐡𝐚𝐧𝐝𝐢 𝐦𝐞 𝐭𝐮𝐦𝐡𝐚𝐫𝐚 𝐤𝐡𝐚𝐝𝐚 𝐡𝐨𝐭𝐚 𝐡𝐚𝐢 𝐤𝐲𝐚 😁😆😆😆** ",
           " **𝐎𝐫 𝐁𝐚𝐭𝐚𝐨 𝐁𝐡𝐚𝐛𝐡𝐢 𝐊𝐚𝐢𝐬𝐢 𝐇𝐚𝐢😉** ",
           " **𝐀𝐚𝐣 𝐓𝐮𝐦 𝐟𝐢𝐧𝐠𝐞𝐫 𝐬𝐞 𝐡𝐢 𝐤𝐚𝐚𝐦 𝐜𝐡𝐚𝐥𝐚𝐨. 𝐆𝐡𝐚𝐫 𝐦𝐞 𝐛𝐚𝐢𝐠𝐚𝐧 𝐨𝐫 𝐦𝐮𝐤𝐢 𝐤𝐡𝐚𝐭𝐚𝐦 𝐡𝐨 𝐠𝐲𝐞 𝐡𝐚𝐢 🙈🙈🙈** ",
           " **𝐎𝐲𝐲 𝐏𝐫𝐢𝐲𝐚 𝐁𝐡𝐚𝐛𝐡𝐢 𝐤𝐚 𝐤𝐲𝐚 𝐡𝐚𝐢 𝐡𝐚𝐢 😁😁👀** ",
           " **𝐘𝐚𝐡𝐚 𝐀𝐚 𝐉𝐚𝐨:- [ @TEAM_CDX ] 𝐌𝐚𝐬𝐭𝐢 𝐊𝐚𝐫𝐞𝐧𝐠𝐞 🤭🤭** ",
           " **𝐲𝐨𝐮𝐫 𝐟𝐚𝐯𝐨𝐮𝐫𝐢𝐭𝐞 𝐚𝐜𝐭𝐫𝐞𝐬𝐬 (𝐒𝐔𝐍𝐍𝐘 𝐋𝐄𝐎𝐍𝐄, 𝐨𝐫 𝐌𝐈𝐘𝐀 𝐊𝐇𝐀𝐋𝐈𝐅𝐀)😹** ",
           " **𝐨 𝐡𝐞𝐥𝐥𝐨 𝐚𝐩𝐤𝐢 𝐚𝐠𝐞 𝐤𝐲𝐚 𝐡𝐚𝐢 𝐡𝐨𝐭 𝐥𝐠𝐭𝐞 𝐡𝐨 𝐚𝐩😻** ",
           " **𝐓𝐮𝐦 𝐫𝐨𝐣 𝐡𝐢𝐥𝐚𝐭𝐞 𝐡𝐨 𝐤𝐲𝐚 , 𝐁𝐡𝐮𝐭 𝐩𝐚𝐭𝐤𝐞 𝐡𝐢 𝐠𝐲𝐞 𝐡𝐨 💕😴🙃** ",
           " **𝐌𝐞𝐫𝐢 𝐁𝐡𝐢 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫𝐛𝐚 𝐃𝐨𝐠𝐞.𝐇𝐢𝐥𝐥𝐚 𝐇𝐢𝐥𝐥𝐚 𝐤𝐞 𝐭𝐡𝐚𝐤 𝐠𝐲𝐚 𝐡𝐮 .??😕** ",
           " **𝐲𝐨𝐮𝐫 𝐟𝐚𝐯𝐨𝐮𝐫𝐢𝐭𝐞 𝐚𝐜𝐭𝐫𝐞𝐬𝐬 (𝐒𝐔𝐍𝐍𝐘 𝐋𝐄𝐎𝐍𝐄, 𝐨𝐫 𝐌𝐈𝐘𝐀 𝐊𝐇𝐀𝐋𝐈𝐅𝐀)🙃** ",
           " **𝐁𝐡𝐚𝐛𝐡𝐢 𝐣𝐢 𝐤𝐨 𝐤𝐡𝐮𝐬𝐡 𝐫𝐤𝐡𝐚 𝐤𝐚𝐫𝐨 𝐭𝐡𝐚𝐧𝐝𝐢 𝐦𝐞 𝐰𝐚𝐫𝐧𝐚 𝐤𝐢𝐬𝐢 𝐨𝐫 𝐤𝐞 𝐬𝐚𝐭𝐡 𝐛𝐡𝐚𝐠 𝐣𝐚𝐲𝐞𝐠𝐢 😅😀😀?🙃** ",
           " **𝐉𝐡𝐚𝐭𝐞 𝐧𝐚 𝐜𝐡*𝐜*𝐈 𝐨𝐫 𝐛𝐚𝐭𝐞 𝐮𝐜𝐡𝐢 𝐮𝐜𝐡𝐢 😴😴😅** ",
           " **𝐌𝐞𝐫𝐢 𝐁𝐡𝐢 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫𝐛𝐚 𝐃𝐨𝐠𝐞.𝐇𝐢𝐥𝐥𝐚 𝐇𝐢𝐥𝐥𝐚 𝐤𝐞 𝐭𝐡𝐚𝐤 𝐠𝐲𝐚 𝐡𝐮 .??🙂🧐** ",
           " **𝐌𝐞𝐫𝐚 𝐄𝐤 𝐊𝐚𝐚𝐦 𝐊𝐚𝐫 𝐃𝐨𝐠𝐞.𝐏𝐥𝐳 𝐦𝐮𝐭𝐡 𝐦𝐚𝐫 𝐝𝐨😁😁.?** ",
           " **𝐁𝐡𝐚𝐛𝐡𝐢 𝐣𝐢 𝐤𝐨 𝐤𝐡𝐮𝐬𝐡 𝐫𝐤𝐡𝐚 𝐤𝐚𝐫𝐨 𝐭𝐡𝐚𝐧𝐝𝐢 𝐦𝐞 𝐰𝐚𝐫𝐧𝐚 𝐤𝐢𝐬𝐢 𝐨𝐫 𝐤𝐞 𝐬𝐚𝐭𝐡 𝐛𝐡𝐚𝐠 𝐣𝐚𝐲𝐞𝐠𝐢 😅😀😀😠** ",
           " **𝐚𝐩𝐤𝐢 𝐚𝐠𝐞 𝐤𝐲𝐚 𝐡𝐚𝐢 𝐡𝐨𝐭 𝐡𝐨 𝐚𝐩 𝐝𝐞𝐤𝐡𝐭𝐞 𝐡𝐢 𝐦𝐚𝐧 𝐤𝐚𝐫𝐭𝐚 𝐡𝐢𝐥𝐚𝐭𝐞 𝐫𝐡𝐮😁❤** ",
           " **𝐎𝐲𝐲 𝐬𝐮𝐧𝐨 𝐀𝐩 𝐑𝐨𝐣 𝐡𝐢𝐥𝐚𝐭𝐞 𝐡𝐨 𝐤𝐲𝐚 𝐩𝐚𝐭𝐥𝐞 𝐡𝐨 𝐠𝐲𝐞 𝐡𝐨👱** ",
           " **𝐁𝐨𝐡𝐨𝐭 𝐘𝐚𝐚𝐝 𝐀𝐚 𝐑𝐡𝐢 𝐇𝐚𝐢 𝐁𝐡𝐚𝐛𝐡𝐢 𝐣𝐢 𝐤𝐚𝐢𝐬𝐢 𝐡𝐚𝐢🤧❣️** ",
           " **𝐎𝐲𝐲 𝐬𝐮𝐧𝐨 𝐀𝐩 𝐑𝐨𝐣 𝐡𝐢𝐥𝐚𝐭𝐞 𝐡𝐨 𝐤𝐲𝐚 𝐩𝐚𝐭𝐥𝐞 𝐡𝐨 𝐠𝐲𝐞 𝐡𝐨😏😏** ",
           " **𝐀𝐩𝐤𝐢 𝐞𝐤 𝐩𝐢𝐜 𝐦𝐢𝐥𝐞𝐠𝐢 𝐤𝐲𝐚 𝐢𝐦𝐚𝐠𝐢𝐧𝐞 𝐤𝐚𝐫 𝐤𝐞 𝐦*𝐭𝐡 𝐤𝐚𝐫𝐧𝐚 𝐡𝐢🤐** ",
           " **𝐁𝐡𝐚𝐛𝐡𝐢 𝐣𝐢 𝐤𝐨 𝐤𝐡𝐮𝐬𝐡 𝐫𝐤𝐡𝐚 𝐤𝐚𝐫𝐨 𝐭𝐡𝐚𝐧𝐝𝐢 𝐦𝐞 𝐰𝐚𝐫𝐧𝐚 𝐤𝐢𝐬𝐢 𝐨𝐫 𝐤𝐞 𝐬𝐚𝐭𝐡 𝐛𝐡𝐚𝐠 𝐣𝐚𝐲𝐞𝐠𝐢 😅😀😀😒** ",
           " **𝐁𝐡𝐚𝐛𝐡𝐢 𝐣𝐢 𝐤𝐨 𝐤𝐡𝐮𝐬𝐡 𝐫𝐤𝐡𝐚 𝐤𝐚𝐫𝐨 𝐭𝐡𝐚𝐧𝐝𝐢 𝐦𝐞 𝐰𝐚𝐫𝐧𝐚 𝐤𝐢𝐬𝐢 𝐨𝐫 𝐤𝐞 𝐬𝐚𝐭𝐡 𝐛𝐡𝐚𝐠 𝐣𝐚𝐲𝐞𝐠𝐢 😅😮😮** "
           " **𝐉𝐡𝐚𝐭𝐞 𝐧𝐚 𝐜𝐡*𝐜*𝐈 𝐨𝐫 𝐛𝐚𝐭𝐞 𝐮𝐜𝐡𝐢 𝐮𝐜𝐡𝐢 😴😴😅👀** ",
           " **𝐘𝐚𝐡𝐚 𝐀𝐚 𝐉𝐚𝐨:- [ @TEAM_CDX ] 𝐌𝐚𝐬𝐭𝐢 𝐊𝐚𝐫𝐞𝐧𝐠𝐞 🤭🙈** ",
           " **𝐀𝐩𝐤𝐢 𝐞𝐤 𝐩𝐢𝐜 𝐦𝐢𝐥𝐞𝐠𝐢 𝐤𝐲𝐚 𝐢𝐦𝐚𝐠𝐢𝐧𝐞 𝐤𝐚𝐫 𝐤𝐞 𝐦*𝐭𝐡 M𝐚𝐫𝐧𝐚 𝐡ai 😅😅** ",
           " **𝐁𝐡𝐚𝐛𝐡𝐢 𝐣𝐢 𝐤𝐨 𝐤𝐡𝐮𝐬𝐡 𝐫𝐤𝐡𝐚 𝐤𝐚𝐫𝐨 𝐭𝐡𝐚𝐧𝐝𝐢 𝐦𝐞 𝐰𝐚𝐫𝐧𝐚 𝐤𝐢𝐬𝐢 𝐨𝐫 𝐤𝐞 𝐬𝐚𝐭𝐡 𝐛𝐡𝐚𝐠 𝐣𝐚𝐲𝐞𝐠𝐢 😅🥺🥺** ",
           " **𝐎𝐲𝐲 𝐬𝐮𝐧𝐨 𝐀𝐩 𝐑𝐨𝐣 𝐡𝐢𝐥𝐚𝐭𝐞 𝐡𝐨 𝐤𝐲𝐚 𝐩𝐚𝐭𝐥𝐞 𝐡𝐨 𝐠𝐲𝐞 𝐡𝐨👀** ",
           " **𝐁𝐡𝐚𝐛𝐡𝐢 𝐣𝐢 𝐤𝐨 𝐤𝐡𝐮𝐬𝐡 𝐫𝐤𝐡𝐚 𝐤𝐚𝐫𝐨 𝐭𝐡𝐚𝐧𝐝𝐢 𝐦𝐞 𝐰𝐚𝐫𝐧𝐚 𝐤𝐢𝐬𝐢 𝐨𝐫 𝐤𝐞 𝐬𝐚𝐭𝐡 𝐛𝐡𝐚𝐠 𝐣𝐚𝐲𝐞𝐠𝐢 😅😀😀🙂** ",
           " **𝐍𝐚 𝐉𝐚𝐦𝐢𝐧 𝐏𝐞 𝐍𝐚 𝐀𝐬𝐡𝐦𝐚𝐧 𝐩𝐞 𝐓𝐞𝐫𝐢 𝐆**𝐝 𝐦𝐚𝐫𝐮𝐧𝐠𝐚 𝐚𝐩𝐧𝐞 𝐁𝐡𝐚𝐢 𝐤𝐞 𝐦𝐚𝐤𝐚𝐧 𝐩𝐞?🤔** ",
           " **𝐤𝐚 𝐡𝐨 𝐤𝐚𝐫𝐞𝐣𝐚 1 𝐜𝐡𝐮𝐦𝐦𝐚 𝐧𝐚 𝐝𝐞𝐛𝐮 😅..🥺** ",
           " **𝐓𝐮𝐦 𝐫𝐨𝐣 𝐡𝐢𝐥𝐚𝐭𝐞 𝐡𝐨 𝐤𝐲𝐚 , 𝐁𝐡𝐮𝐭 𝐩𝐚𝐭𝐤𝐞 𝐡𝐢 𝐠𝐲𝐞 𝐡𝐨 💕😴🥺🥺** ",
           " **𝐊𝐚𝐥 𝐌𝐚𝐣𝐚 𝐀𝐲𝐚 𝐓𝐡𝐚 𝐍𝐚 Bathroom me 🤭😅** ",
           " **𝐍𝐚 𝐉𝐚𝐦𝐢𝐧 𝐏𝐞 𝐍𝐚 𝐀𝐬𝐡𝐦𝐚𝐧 𝐩𝐞 𝐓𝐞𝐫𝐢 𝐆**𝐝 𝐦𝐚𝐫𝐮𝐧𝐠𝐚 𝐚𝐩𝐧𝐞 𝐁𝐡𝐚𝐢 𝐤𝐞 𝐦𝐚𝐤𝐚𝐧 𝐩𝐞😁😁**",
           " **𝐎𝐲𝐲 𝐭𝐞𝐫𝐞 𝐛𝐚𝐥𝐞 𝐤𝐨 𝐣𝐚𝐤𝐚𝐫 𝐛𝐚𝐭𝐚𝐭𝐚 𝐡𝐮 𝐭𝐮 𝐲𝐡𝐚 𝐬𝐞𝐭𝐭𝐢𝐧𝐠 𝐤𝐚𝐫 𝐫𝐡𝐢 𝐡𝐚𝐢👀** ",
           " **𝐌𝐞𝐫𝐢 𝐁𝐡𝐢 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫𝐛𝐚 𝐃𝐨𝐠𝐞.𝐇𝐢𝐥𝐥𝐚 𝐇𝐢𝐥𝐥𝐚 𝐤𝐞 𝐭𝐡𝐚𝐤 𝐠𝐲𝐚 𝐡𝐮😼** ",
           " **𝐎𝐲𝐲 𝐭𝐞𝐫𝐞 𝐛𝐚𝐥𝐞 𝐤𝐨 𝐣𝐚𝐤𝐚𝐫 𝐛𝐚𝐭𝐚𝐭𝐚 𝐡𝐮 𝐭𝐮 𝐲𝐡𝐚 𝐬𝐞𝐭𝐭𝐢𝐧𝐠 𝐤𝐚𝐫 𝐫𝐡𝐢 𝐡𝐚𝐢😸** ",
           " **𝐓𝐡𝐚𝐧𝐝𝐢 𝐦𝐞 𝐭𝐮𝐦𝐡𝐚𝐫𝐚 𝐤𝐡𝐚𝐝𝐚 𝐡𝐨𝐭𝐚 𝐡𝐚𝐢 𝐤𝐲𝐚 😁🙈** ",
           " **𝐀𝐚𝐩𝐤𝐢 𝐏𝐚𝐫𝐭𝐧𝐞𝐫 𝐀𝐚𝐩𝐤𝐨 𝐃𝐡𝐮𝐧𝐝 𝐑𝐡𝐞 𝐇𝐚𝐢𝐧 𝐉𝐥𝐝𝐢 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐲𝐢𝐚𝐞😅😅✌️🤞** ",
           " **𝐲𝐨𝐮𝐫 𝐟𝐚𝐯𝐨𝐮𝐫𝐢𝐭𝐞 𝐚𝐜𝐭𝐫𝐞𝐬𝐬 (𝐒𝐔𝐍𝐍𝐘 𝐋𝐄𝐎𝐍𝐄, 𝐨𝐫 𝐌𝐈𝐘𝐀 𝐊𝐇𝐀𝐋𝐈𝐅𝐀) 🥰** ",
           " **𝐇𝐚𝐦 𝐃𝐨𝐬𝐭 𝐁𝐚𝐧 𝐒𝐚𝐤𝐭𝐞 𝐇𝐚𝐢...?🥰 𝐌𝐚𝐬𝐭𝐞𝐫𝐛𝐚𝐭𝐢𝐧𝐠 𝐤𝐚𝐫𝐧𝐞 𝐦𝐞 𝐡𝐞𝐥𝐩 𝐡𝐨 𝐣𝐚𝐲𝐞𝐠𝐢 𝐦𝐞𝐫𝐢 😁 😁.🥺🥺** ",
           " **𝐁𝐡𝐚𝐛𝐡𝐢 𝐣𝐢 𝐤𝐨 𝐤𝐡𝐮𝐬𝐡 𝐫𝐤𝐡𝐚 𝐤𝐚𝐫𝐨 𝐭𝐡𝐚𝐧𝐝𝐢 𝐦𝐞 𝐰𝐚𝐫𝐧𝐚 𝐤𝐢𝐬𝐢 𝐨𝐫 𝐤𝐞 𝐬𝐚𝐭𝐡 𝐛𝐡𝐚𝐠 𝐣𝐚𝐲𝐞𝐠𝐢 😅😀😀🥲** ",
           " **𝐒𝐢𝐧𝐠𝐥𝐞 𝐇𝐨 𝐘𝐚 𝐌𝐢𝐧𝐠𝐥𝐞 😉** ",
           " **𝐎𝐲𝐲 𝐢𝐭𝐧𝐚 𝐡𝐨𝐭 𝐤𝐲𝐮 𝐡𝐨 𝐭𝐮𝐦 𝐝𝐞𝐤𝐡 𝐤𝐞 𝐤𝐡𝐚𝐝𝐚 𝐡𝐨 𝐣𝐚𝐭𝐚 𝐡𝐚𝐢 😂 𝐑𝐨𝐧𝐠𝐭𝐞😁😁😁😋🥳** ",
           " **𝐔𝐟𝐟 𝐊𝐲𝐚 𝐦𝐚𝐚𝐥 𝐡𝐚𝐢 𝐲𝐚𝐚𝐫 DEKH KE KHADA HO GYA 😁😂🧐** ",
           " **𝐚𝐩𝐤𝐢 𝐚𝐠𝐞 𝐤𝐲𝐚 𝐡𝐚𝐢 𝐡𝐨𝐭 𝐡𝐨 𝐚𝐩 𝐝𝐞𝐤𝐡𝐭𝐞 𝐡𝐢 𝐦𝐚𝐧 𝐤𝐚𝐫𝐭𝐚 𝐡𝐢𝐥𝐚𝐭𝐞 𝐫𝐡𝐮😁🥺** ",
           " **𝐘𝐚𝐡𝐚 𝐀𝐚 𝐉𝐚𝐨:- [ @TEAM_CDX ] 𝐌𝐚𝐬𝐭𝐢 𝐊𝐚𝐫𝐞𝐧𝐠𝐞 🤭🤭** ",
           " **𝐎𝐲𝐲 𝐢𝐭𝐧𝐚 𝐡𝐨𝐭 𝐤𝐲𝐮 𝐡𝐨 𝐭𝐮𝐦 𝐝𝐞𝐤𝐡 𝐤𝐞 𝐤𝐡𝐚𝐝𝐚 𝐡𝐨 𝐣𝐚𝐭𝐚 𝐡𝐚𝐢 😂 𝐑𝐨𝐧𝐠𝐭𝐞😁😁😁 😊** ",
           " **𝐀𝐩𝐤𝐢 𝐞𝐤 𝐩𝐢𝐜 𝐦𝐢𝐥𝐞𝐠𝐢 𝐤𝐲𝐚 𝐢𝐦𝐚𝐠𝐢𝐧𝐞 𝐤𝐚𝐫 𝐤𝐞 𝐦*𝐭𝐡 m𝐚𝐫𝐧𝐚 𝐡𝐢🥺🥺** ",
           " **𝐉𝐨𝐢𝐧 𝐊𝐚𝐫 𝐋𝐨:- [ @TEAM_CDX ] 🤗** ",
           " **𝐀𝐚𝐩𝐤𝐢 𝐏𝐚𝐫𝐭𝐧𝐞𝐫 𝐀𝐚𝐩𝐤𝐨 𝐃𝐡𝐮𝐧𝐝 𝐑𝐡𝐞 𝐇𝐚𝐢𝐧 𝐉𝐥𝐝𝐢 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐲𝐢𝐚𝐞😅😅😗** ",
           " **𝐚𝐩𝐤𝐢 𝐚𝐠𝐞 𝐤𝐲𝐚 𝐡𝐚𝐢 𝐡𝐨𝐭 𝐡𝐨 𝐚𝐩 𝐝𝐞𝐤𝐡𝐭𝐞 𝐡𝐢 𝐦𝐚𝐧 𝐤𝐚𝐫𝐭𝐚 𝐡𝐢𝐥𝐚𝐭𝐞 𝐫𝐡𝐮😁🥺** ",
           " **𝐀𝐚𝐣 𝐓𝐮𝐦 𝐟𝐢𝐧𝐠𝐞𝐫 𝐬𝐞 𝐡𝐢 𝐤𝐚𝐚𝐦 𝐜𝐡𝐚𝐥𝐚𝐨. 𝐆𝐡𝐚𝐫 𝐦𝐞 𝐛𝐚𝐢𝐠𝐚𝐧 𝐨𝐫 𝐦𝐮𝐤𝐢 𝐤𝐡𝐚𝐭𝐚𝐦 𝐡𝐨 𝐠𝐲𝐞 𝐡𝐚𝐢 😁🥰** ",
           " **𝐍𝐚 𝐉𝐚𝐦𝐢𝐧 𝐏𝐞 𝐍𝐚 𝐀𝐬𝐡𝐦𝐚𝐧 𝐩𝐞 𝐓𝐞𝐫𝐢 𝐆**𝐝 𝐦𝐚𝐫𝐮𝐧𝐠𝐚 𝐚𝐩𝐧𝐞 𝐁𝐡𝐚𝐢 𝐤𝐞 𝐦𝐚𝐤𝐚𝐧 𝐩𝐞😜** ",
           " **𝐎𝐲𝐲 𝐢𝐭𝐧𝐚 𝐡𝐨𝐭 𝐤𝐲𝐮 𝐡𝐨 𝐭𝐮𝐦 𝐝𝐞𝐤𝐡 𝐤𝐞 𝐤𝐡𝐚𝐝𝐚 𝐡𝐨 𝐣𝐚𝐭𝐚 𝐡𝐚𝐢 😂 𝐑𝐨𝐧𝐠𝐭𝐞😁😁😁🥰** ",
           ]

         

@client.on(events.NewMessage(pattern="^/tagall ?(.*)"))
@client.on(events.NewMessage(pattern="^@all ?(.*)"))
@client.on(events.NewMessage(pattern="^#all ?(.*)"))
@client.on(events.NewMessage(pattern="^#tag ?(.*)"))
@client.on(events.NewMessage(pattern="^/utag ?(.*)"))
@client.on(events.NewMessage(pattern="^@utag ?(.*)"))
@client.on(events.NewMessage(pattern="^#utag ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "__This command can be use in groups and channels!__"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧 𝐂𝐚𝐧 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐓𝐨 𝐀𝐥𝐥 𝐁𝐚𝐛𝐲...")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("/tagall hello 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐎𝐤 𝐅𝐨𝐫 𝐓𝐚𝐠𝐠𝐢𝐧𝐠..")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "/tagall hii 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐎𝐫 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞..."
            )
    else:
        return await event.respond(
            "/tagall hii 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 𝐎𝐫 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞..."

        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[ {usr.first_name} ](tg://user?id={usr.id}) "
 
        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
      

            elif mode == "text_on_reply":
                await msg.reply(f"[ {random.choice(EMOJI)} ](tg://user?id={usr.id})")
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@client.on(events.NewMessage(pattern="^/cancel$"))
@client.on(events.NewMessage(pattern="^/stop$"))
async def cancel_spam(event):
    if not event.chat_id in spam_chats:
        return await event.respond("𝐇𝐞𝐫𝐞 𝐍𝐨 𝐀𝐧𝐲 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐈𝐬 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐁𝐲 𝐌𝐞..")
    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐈𝐬 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐀𝐝𝐦𝐢𝐧𝐬.. 𝐘𝐨𝐮 𝐂𝐚𝐧'𝐭 𝐔𝐬𝐞 𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝..")

    else:
        try:
            spam_chats.remove(event.chat_id)
        except:
            pass
        return await event.respond("♦𝗥𝗢𝗞 𝗗𝗜𝗬𝗔 𝗠𝗔𝗗𝗛𝗔𝗥𝗖𝗛𝗢𝗗♦")


__mod_name__ = "✯Tᴀɢ✯"
__help__ = """
──「  ᴏɴʟʏ ғᴏʀ ᴀᴅᴍɪɴs 」──

❍ /ᴛᴀɢᴀʟʟ , #tag , .tagmember , @ᴀʟʟ , #all '(ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴏʀ ᴀᴅᴅ ᴀɴᴏᴛʜᴇʀ ᴍᴇssᴀɢᴇ) ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴀʟʟ ᴍᴇᴍʙᴇʀs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ, ᴡɪᴛʜᴏᴜᴛ ᴇxᴄᴇᴘᴛɪᴏɴ.'
❍ /cancel ғᴏʀ ᴄᴀɴᴄᴇʟ ᴛʜᴇ ɢᴏɪɴɢ ᴛᴀɢɢɪɴɢ
☆............𝙱𝚈 » [𝐊𝐀𝐌𝐄𝐄𝐍𝐀](https://t.me/BRANDED_KAMEENAA)............☆
"""
