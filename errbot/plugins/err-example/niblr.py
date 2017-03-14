from errbot import BotPlugin, botcmd
import requests


class Niblr(BotPlugin):
    """
    This is a very basic plugin to try out your new installation and get you started.
    Feel free to tweak me to experiment with Errbot.
    You can find me in your init directory in the subdirectory plugins.
    """

    @botcmd  # flags a command
    def niblr_random(self, msg, args):  # a command callable with !tryme3

        req = requests.get(
            'https://peaceful-eyrie-12759.herokuapp.com/niblr/random',
        )
        return req.json()['results']

    @botcmd
    def niblr_feedme(self, msg, args):
        args_list = args.split()
        cuisine = cost = ''
        if args_list:
            cuisine = args_list[0]
            for arg in args_list:
                if arg.startswith("cost:"):
                    cost = arg.split(':')[1]
                    break
        if cuisine.startswith('cost:'):
            cuisine = ''


        req = requests.get(
            'https://peaceful-eyrie-12759.herokuapp.com/niblr/list',
            params={
                'cuisine': cuisine,
                'cost': cost
            }
        )
        return req.json()['results']