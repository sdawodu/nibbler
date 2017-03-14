import logging

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

BACKEND = 'Text'  # Errbot will start in text mode (console only mode) and will answer commands from there.

BOT_DATA_DIR = r'/home/seun/AAM/development/errbot/data'
BOT_EXTRA_PLUGIN_DIR = '/home/seun/AAM/development/errbot/plugins'

BOT_LOG_FILE = r'/home/seun/AAM/development/errbot/errbot.log'
BOT_LOG_LEVEL = logging.DEBUG

BOT_IDENTITY = {
    'username' : '166618_4370357@chat.hipchat.com',
    'password' : 'Screenwriterbotpassword',
    # Group admins can create/view tokens on the settings page after logging
    # in on HipChat's website
    'token'    : 'QRgp3JsrMjk4hh8nRtmE3f4d9Z2541LzV7e9xW5u',
    # If you're using HipChat server (self-hosted HipChat) then you should set
    # the endpoint below. If you don't use HipChat server but use the hosted version
    # of HipChat then you may leave this commented out.
    # 'endpoint' : 'https://api.hipchat.com',
    # If your self-hosted Hipchat server is using SSL, and your certificate
    # is self-signed, set verify to False or hypchat will fail
    # 'verify': False,
}
CHATROOM_FN = 'screenwriterbot'

BOT_ADMINS = ('@seun', '@zsoobhan')

BOT_ALT_PREFIXES = ('@niblr',)