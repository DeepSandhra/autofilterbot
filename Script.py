class script(object):
    START_TXT = """๐ท๐ด๐ป๐ป๐พ ๐ {},
๐ผ๐ ๐ฝ๐ฐ๐ผ๐ด ๐ธ๐ <a href=https://t.me/{}>{}</a>, ๐ธ ๐ฒ๐ฐ๐ฝ ๐ฟ๐๐พ๐๐ธ๐ณ๐ด ๐ผ๐พ๐๐ธ๐ด๐ ๐, ๐น๐๐๐ ๐ฐ๐ณ๐ณ ๐ผ๐ด ๐๐พ ๐๐พ๐๐ ๐ถ๐๐พ๐๐ฟ ๐ฐ๐ฝ๐ณ ๐ผ๐ฐ๐บ๐ด ๐ผ๐ด ๐ฐ๐ณ๐ผ๐ธ๐ฝ.. ๐๐ท๐ด๐ฝ ๐๐ด๐ด ๐ผ๐ ๐ฟ๐พ๐๐ด๐๐ ๐ฆพ\n\n๐๐ ๐๐๐๐๐๐๐ ๐๐๐\n<a href=https://t.me/movi2x><b>Kแผแดsแผ</b></a>"""
    HELP_TXT = """๐ท๐ด๐ {}
๐ท๐ด๐๐ด ๐ธ๐ ๐ผ๐ ๐ท๐ด๐ป๐ฟ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐."""
    ABOUT_TXT = """<b>โฎ ๐ผ๐ ๐ฝ๐ฐ๐ผ๐ด: แดแดแดแด๊ฐษชสแดแดสสแดแด </b>
<b>โฎ ๐ฒ๐๐ด๐ฐ๐๐พ๐: <a href=https://t.me/movi2x><b>Kแผแดsแผ</b></a>
<b>โฎ ๐ป๐ธ๐ฑ๐๐ฐ๐๐: ๐ฟ๐๐๐พ๐ถ๐๐ฐ๐ผ</b>
<b>โฎ ๐ป๐ฐ๐ฝ๐ถ๐๐ฐ๐ถ๐ด: ๐ฟ๐๐๐ท๐พ๐ฝ ๐น</b>
<b>โฎ ๐ณ๐ฐ๐๐ฐ ๐ฑ๐ฐ๐๐ด: ๐ผ๐พ๐ฝ๐ถ๐พ-๐ณ๐ฑ</b>
<b>โฎ ๐ฑ๐พ๐ ๐๐ด๐๐๐ด๐: ๐ท๐ด๐๐พ๐บ๐</b>
<b>โฎ ๐ฑ๐๐ธ๐ป๐ณ ๐๐๐ฐ๐๐๐: ๐1.0.43</b>
<b>โฎ ๐ผ๐๐๐๐๐ ๐๐๐๐๐๐๐ ๐ฟ: <a href=https://t.me/mdiskmovieshd_2022>แดแดแด ษชแด๊ฑ แดสแดษดษดแดส ๐ฅ</a></b>
<b>โฎ ๐ผ๐พ๐๐ธ๐ด๐ ๐๐ด๐๐๐ด๐๐ ๐ฑ๐พ๐ ๐ฌ: <a href=https://t.me/MovieRequestGroup_rebot>๐ผ๐พ๐๐ธ๐ด๐ ๐๐ด๐๐๐ด๐๐ ๐ฌ</a></b>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>
<b>NOTE:</b>
This module only works for my admins
<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban_user  - <code>to ban a user.</code>
โข /unban_user  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>
<b>DEVS:</b>
- <a href=https://t.me/mdiskmovieshd_2022>แดแดแด ษชแด๊ฑ แดสแดษดษดแดส ๐ฅ</a></b>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>
    
- Filter is the feature were users can set automated replies for a particular keyword and Kแผแดsแผ  will respond whenever a keyword is found the message
<b>NOTE:</b>
1. Kแผแดsแผ should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.
<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>
-Kแผแดsแผ  Supports both url and alert inline buttons.
<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Kแผแดsแผ supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format
<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/tmmainchannel)</code>
<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """<b>๐ฐ๐๐๐พ ๐ต๐ธ๐ป๐๐ด๐ ๐พ๐ฝ/๐พ๐ต๐ต ๐ผ๐พ๐ณ๐๐ป๐ด..</b>
<b>๐ฐ๐๐๐พ ๐ต๐ธ๐ป๐๐ด๐ ๐ธ๐ ๐๐ท๐ด ๐ต๐ด๐ฐ๐๐๐๐ด ๐๐พ ๐ต๐ธ๐ป๐๐ด๐ ๐ฐ๐ฝ๐ณ ๐๐ฐ๐๐ด  ๐๐ท๐ด ๐ต๐ธ๐ป๐ด๐ ๐ฐ๐๐๐พ๐ผ๐ฐ๐๐ธ๐ฒ๐ฐ๐ป๐ป๐ ๐ต๐๐พ๐ผ ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป ๐๐พ ๐ถ๐๐พ๐๐ฟ. ๐๐พ๐ ๐ฒ๐ฐ๐ฝ ๐๐๐ด ๐๐ท๐ด ๐ต๐พ๐ป๐ป๐พ๐๐ธ๐ฝ๐ถ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐ ๐๐พ ๐พ๐ฝ ๐ฐ๐ฝ๐ณ ๐พ๐ต๐ต ๐๐ท๐ด ๐ฐ๐๐๐พ๐ต๐ธ๐ป๐๐ด๐ ๐ธ๐ฝ ๐๐พ๐๐ ๐ถ๐๐พ๐๐ฟ.../</b>
<b>๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐ :-
<b>โบโบ /autofilter on - ๐ด๐ฝ๐ฐ๐ฑ๐ป๐ด ๐ฐ๐๐๐พ ๐ต๐ธ๐ป๐๐ด๐ ๐ธ๐ฝ ๐๐ท๐ด ๐ถ๐๐พ๐๐ฟ๐.</b>
<b>โบโบ /autofilter off - ๐ณ๐ธ๐๐ฐ๐ฑ๐ป๐ด๐ณ ๐ฐ๐๐๐พ ๐ต๐ธ๐ป๐๐ด๐ ๐ธ๐ฝ ๐๐ท๐ด ๐ถ๐๐พ๐๐ฟ๐.</b>
<b>โบโบ /set_template - ๐๐ด๐ ๐ฒ๐๐๐๐พ๐ผ ๐ธ๐ผ๐ณ๐ฑ ๐๐ด๐ผ๐ฟ๐ป๐ฐ๐๐ด ๐ต๐พ๐ ๐ฐ๐๐๐พ ๐ต๐ธ๐ป๐๐ด๐.</b>
<b>โบโบ /get_template - ๐ถ๐ด๐ ๐ฒ๐๐๐๐ด๐ฝ๐ ๐ธ๐ผ๐ณ๐ฑ ๐๐ด๐ผ๐ฟ๐ป๐ฐ๐๐ด ๐พ๐ต ๐ฐ๐๐๐พ ๐ต๐ธ๐ป๐๐ด๐.</b>
<b>๐ฒ๐๐ด๐ณ๐ธ๐๐ :- <a href=https://t.me/tmmainchannel>๐๐๐๐๐๐ ๐๐๐๐๐</a></b>"""
    CONNECTION_TXT = """Help: <b>Connections</b>
- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.
<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM
<b>Commands and Usage:</b>
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>
<b>NOTE:</b>
these are the extra features of Kแผแดsแผ
<b>Commands and Usage:</b>
โข /id - <code>get id of a specifed user.</code>
โข /info  - <code>get information about a user.</code>
โข /imdb  - <code>get the film information from IMDb source.</code>
โข /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>
<b>NOTE:</b>
This module only works for my admins
<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban  - <code>to ban a user.</code>
โข /unban  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """โ ๐๐พ๐๐ฐ๐ป ๐ต๐ธ๐ป๐ด๐: <code>{}</code>
<b>โ ๐๐พ๐๐ฐ๐ป ๐ต๐ธ๐ป๐ด๐: <code>{}</code></b>
<b>โ ๐๐พ๐๐ฐ๐ป ๐๐๐ด๐๐: <code>{}</code></b>
<b>โ ๐๐พ๐๐ฐ๐ป ๐ฒ๐ท๐ฐ๐๐: <code>{}</code></b>
<b>โ ๐๐๐ด๐ณ ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code></b>
<b>โ ๐ต๐๐ด๐ด ๐๐๐พ๐๐ฐ๐ถ๐ด: <code>{}</code></b>"""
    DONATE_TXT = """<b>๐๐จ๐ง๐๐ญ๐ข๐จ๐ง & ๐๐๐ข๐ ๐๐ซ๐จ๐ฆ๐จ๐ญ๐ข๐จ๐ง</b> 
โบโบ <b>๐๐จ๐ง๐๐ญ๐ข๐จ๐ง</b>
โชผ <b>๐๐จ๐ฎ ๐๐๐ง ๐๐จ๐ง๐๐ญ๐ ๐๐ง๐ฒ ๐๐ฆ๐จ๐ฎ๐ง๐ญ ๐๐จ๐ฎ ๐๐๐ฏ๐ ๐ณ. 
<b>โโโโโโโโโแ Payment Methods แโโโโโโโโโ
โฎ ๐๐ผ๐ผ๐ด๐น๐ฒ๐ฃ๐ฎ๐
โฎ ๐ฃ๐ฎ๐๐๐บ
โฎ ๐ฃ๐ต๐ผ๐ป๐ฒ๐ฃ๐ฒ
โฎ ๐ฃ๐ฎ๐๐ฃ๐ฎ๐น
_๐๐จ๐ง๐ญ๐๐๐ญ ๐๐ ๐๐จ๐ซ ๐๐ง๐จ๐ฐ ๐๐๐จ๐ฎ๐ญ ๐๐ก๐ ๐๐๐ฒ๐ฆ๐๐ง๐ญ ๐๐ง๐๐จ_
โโโโโโโโโโโโแ <a href=https://t.me/movi2x><b>Kแผแดsแผ</b></a> แโโโโโโโโโโโโ
โบโบ <b>๐๐๐ข๐ ๐๐ซ๐จ๐ฆ๐จ๐ญ๐ข๐จ๐ง</b>
โชผ <b>๐๐จ๐ง๐ญ๐๐๐ญ ๐๐ ๐๐ข๐ญ๐ก ๐๐จ๐ฎ ๐๐จ๐ง๐ญ๐๐ง๐ญ ๐๐ก๐ข๐๐ก ๐๐จ๐ฎ ๐๐๐ง๐ญ ๐๐จ ๐๐ซ๐จ๐ฆ๐จ๐ญ๐ . 
<b>โโโโโโโโโแ Payment Methods แโโโโโโโโโ
โฎ ๐๐ผ๐ผ๐ด๐น๐ฒ๐ฃ๐ฎ๐
โฎ ๐ฃ๐ฎ๐๐๐บ
โฎ ๐ฃ๐ต๐ผ๐ป๐ฒ๐ฃ๐ฒ
โฎ ๐ฃ๐ฎ๐๐ฃ๐ฎ๐น
_๐๐จ๐ง๐ญ๐๐๐ญ ๐๐ ๐๐ข๐ญ๐ก ๐๐จ๐ฎ๐ซ ๐๐จ๐ง๐ญ๐๐ง๐ญ ๐๐ง๐ ๐๐ง๐จ๐ฐ ๐๐๐จ๐ฎ๐ญ ๐๐ก๐ ๐๐๐ฒ๐ฆ๐๐ง๐ญ ๐๐ง๐๐จ_
โโโโโโโโโโโโแ <a href=https://t.me/movi2x><b>Kแผแดsแผ</b></a> แโโโโโโโโโโโโ"""
    LOG_TEXT_G = """#๐๐๐ฐ๐๐ซ๐จ๐ฎ๐ฉ
    
<b>โ ๐๐ซ๐จ๐ฎ๐ฉ โชผ {}(<code>{}</code>)</b>
<b>โ ๐๐จ๐ญ๐๐ฅ ๐๐๐ฆ๐๐๐ซ๐ฌ โชผ <code>{}</code></b>
<b>โ ๐๐๐๐๐ ๐๐ฒ โชผ {}</b>
"""
    LOG_TEXT_P = """#๐๐๐ฐ๐๐ฌ๐๐ซ
    
<b>โ ๐๐ - <code>{}</code></b>
<b>โ ๐๐๐ฆ๐ - {}</b>

@mdiskmovieshd_2022
"""
