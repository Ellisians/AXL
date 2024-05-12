import sys
from os import system as System
import os
import base64 as B64
from time import sleep as Sleep
from threading import Thread as ThreadPool
from pystyle import Write, Colors

try:
    from requests import Session
    Session = Session()
except:
    System('pip install requests')
Write.Print('''
██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗     █████╗    ██╗  ██╗   ██╗
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ██╔══██╗   ╚██╗██╔╝   ██║
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║       ███████║    ╚███╔╝    ██║
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       ██╔══██║    ██╔██╗    ██║
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║       ██║  ██║██╗██╔╝ ██╗██╗███████╗
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝       ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝╚══════╝
                                                           Made By: nieakos\n''',
            color=Colors.white_to_blue, interval=0.0)
Token = Write.Input('Token To Sniff:', color=Colors.white_to_blue, interval=0.01)
System('cls')
if Token.startswith('M'):
    Decodestring = Token[:26]
if Token.startswith('O'):
    Decodestring = Token[:24]
if Token.startswith('N'):
    Decodestring = Token[:24]
End = '=='


def BotChecker():
    BotCheck = Session.get('https://discordapp.com/api/v9/users/@me', headers={'Authorization': Token})
    if BotCheck.status_code in (201, 200, 204, 203):
        return 'UserAccount'
    else:
        return 'BotAccount'


class AXL:

    def __init__(self):
        self.Session = Session
        self.ThreadPool = ThreadPool
        self.System = System
        self.Write = Write
        self.Colors = Colors
        self.OS = os
        self.Sys = sys

    def UserInfo(self):
        Login = self.Session.get('https://discordapp.com/api/v9/users/@me', headers={
            'Authorization': Token,
            'Content-Type': 'application/json'})
        if Login.status_code == 401:
            self.Write.Print('Token Invalid. Proceeding With Token Sniff...', color=self.Colors.white_to_blue,
                             interval=0.0)
            b64_decode = B64.b64decode(Decodestring + End).decode('utf-8')
            LookUp = self.Session.post('https://lookupguru.herokuapp.com/lookup', json={'input': b64_decode})
            if LookUp.status_code in (201, 200, 204, 203, 202):
                TokenType = LookUp.json()['data']['is_bot']
                TokenUsername = LookUp.json()['data']['username']
                TokenID = LookUp.json()['data']['id']
                TokenAvatarUrl = LookUp.json()['data']['avatar']['url']
                TokenDiscrim = LookUp.json()['data']['discriminator']
                self.Write.Print(
                    f'\nSniffed Token. Results: \nIs Bot: {TokenType}, \nToken ID: {TokenID}, \nToken Username: {TokenUsername}#{TokenDiscrim}, \nToken Avatar: {TokenAvatarUrl}\n',
                    color=self.Colors.white_to_blue, interval=0.0)
            if LookUp.status_code in (401, 400, 403, 402, 405):
                self.Write.Print(
                    f'\nHm... AXL Couldn\'t Sniff out this Token\'s Information, Please try another token.\n',
                    color=self.Colors.white_to_blue, interval=0.0)
            if 'retry_after' in LookUp.text:
                Timer = LookUp.json()['retry_after']
                self.Write.Print(f'\nAXL has been Timed-Out by the API Please try again in: {Timer}\n',
                                 color=self.Colors.white_to_blue, interval=0.0)
                Sleep(Timer)
        if Login.status_code == 200:
            jsonpack = Login.json()
            self.Write.Print(
                ' ' + jsonpack['username'] + '#' + jsonpack['discriminator'] + ' -' + ' ' + jsonpack['id'] + '\n',
                color=self.Colors.white_to_blue, interval=0.0)
            self.Write.Print(f'Copying Account Info on:' + ' ' + jsonpack['username'] + '#' + jsonpack[
                'discriminator'] + ' -' + ' ' + jsonpack['id'] + '...', color=self.Colors.white_to_blue, interval=0.0)
            Guilds = self.Session.get('https://discordapp.com/api/v9/users/@me/guilds', headers={
                'Authorization': Token,
                'Content-Type': 'application/json'})
            Friends = self.Session.get('https://discordapp.com/api/v9/users/@me/relationships', headers={
                'Authorization': Token,
                'Content-Type': 'application/json'})
            Settings = self.Session.get('https://discordapp.com/api/v9/users/@me/settings', headers={
                'Authorization': Token,
                'Content-Type': 'application/json'})
            Settings2 = self.Session.get('https://discordapp.com/api/v9/users/@me', headers={
                'Authorization': Token,
                'Content-Type': 'application/json'})
            if Settings.status_code in (201, 204, 203, 200):
                PHONENUM = Settings2.json()['phone']
                EMAILAD = Settings2.json()['email']
                MFA = Settings2.json()['mfa_enabled']
                THEME = Settings.json()['theme']
                LANGUAGE = Settings.json()['locale']
                DEVMODE = Settings.json()['developer_mode']
                self.Write.Print(
                    f'\nPhone Number: {PHONENUM} \nEmail Address: {EMAILAD} \n2FA Verification: {MFA} \nTheme: {THEME} \nLanguage: {LANGUAGE} \nDeveloper Mode: {DEVMODE}\n',
                    color=self.Colors.white_to_blue, interval=0.0)
            if Settings.status_code in (401, 400, 403, 402, 405):
                self.Write.Print(
                    f'\nHmm... AXL Couldn\'t Sniff out this Token\'s Information, Please try another token.\n',
                    color=self.Colors.white_to_blue, interval=0.0)
            if Friends.status_code in (201, 200, 204, 203):
                datapack = Friends.json()
                for data in datapack:
                    friendid = data['id']
                    friendname = data['user']['username']
                    frienddiscrim = data['user']['discriminator']
                    self.Write.Print('\nSniffed Friend:' + ' ' + friendname + '#' + frienddiscrim + ' -' + friendid,
                                     color=self.Colors.white_to_blue, interval=0.0)
                self.Write.Print('\nFinished Scraping Friends List.\n', color=self.Colors.white_to_blue, interval=0.0)
                Sleep(0.5)
            if Friends.status_code in (401, 400, 403, 402, 405):
                self.Write.Print(
                    f'\nHmm... AXL Couldn\'t Sniff out this Token\'s Information, Please try another token.\n',
                    color=self.Colors.white_to_blue, interval=0.0)
            if 'retry_after' in Friends.text:
                Timer = Friends.json()['retry_after']
                self.Write.Print(f'\nAXL has been Timed-Out by the API Please try again in: {Timer}\n',
                                 color=self.Colors.white_to_blue, interval=0.0)
                Sleep(Timer)
            if Guilds.status_code in (201, 200, 204, 203):
                datapack = Guilds.json()
                for data in datapack:
                    guildid = data['id']
                    guildname = data['name']
                    self.Write.Print('\nSniffed Guild:' + guildname + ' -' + guildid, color=self.Colors.white_to_blue,
                                     interval=0.0)
                self.Write.Print('\nFinished Scraping Guild List.\n', color=self.Colors.white_to_blue, interval=0.0)
                Sleep(0.5)
            if Guilds.status_code in (401, 400, 403, 402, 405):
                self.Write.Print(
                    f'\nHmm... AXL Couldn\'t Sniff out this Token\'s Information, Please try another token.\n',
                    color=self.Colors.white_to_blue, interval=0.0)
            if 'retry_after' in Guilds.text:
                Timer = Guilds.json()['retry_after']
                self.Write.Print(f'\nAXL has been Timed-Out by the API Please try again in: {Timer}\n',
                                 color=self.Colors.white_to_blue, interval=0.0)
                Sleep(Timer)
        if 'retry_after' in Login.text:
            Timer = Login.json()['retry_after']
            self.Write.Print(f'\nAXL has been Timed-Out by the API Please try again in: {Timer}\n',
                             color=self.Colors.white_to_blue, interval=0.0)
            Sleep(Timer)
        self.System('pause')
        self.OS.startfile(self.Sys.argv[0])
        self.Sys.exit()

    def BotInfo(self):
        Login = self.Session.get('https://discordapp.com/api/v9/users/@me', headers={
            'Authorization': f'Bot {Token}',
            'Content-Type': 'application/json'})
        if Login.status_code == 401:
            self.Write.Print('\nToken Invalid. Proceeding With Token Sniff...' + '\n', color=self.Colors.white_to_blue,
                             interval=0.0)
            b64_decode = B64.b64decode(Decodestring + End).decode('utf-8')
            LookUp = self.Session.post('https://lookupguru.herokuapp.com/lookup', json={'input': b64_decode})
            if LookUp.status_code in (201, 200, 204, 203, 202):
                TokenType = LookUp.json()['data']['is_bot']
                TokenUsername = LookUp.json()['data']['username']
                TokenID = LookUp.json()['data']['id']
                TokenAvatarUrl = LookUp.json()['data']['avatar']['url']
                TokenDiscrim = LookUp.json()['data']['discriminator']
                self.Write.Print(
                    f'\nSniffed Token. Results: \nIs Bot: {TokenType}, \nToken ID: {TokenID}, \nToken Username: {TokenUsername}#{TokenDiscrim}, \nToken Avatar: {TokenAvatarUrl}' + '\n',
                    color=self.Colors.white_to_blue, interval=0.0)
            if LookUp.status_code in (401, 400, 403, 402, 405):
                self.Write.Print(
                    f'\nHmm... AXL Couldn\'t Sniff out this Token\'s Information, Please try another token.\n',
                    color=self.Colors.white_to_blue, interval=0.0)
            if 'retry_after' in LookUp.text:
                Timer = LookUp.json()['retry_after']
                self.Write.Print(f'\nAXL has been Timed-Out by the API Please try again in: {Timer}\n',
                                 color=self.Colors.white_to_blue, interval=0.0)
                Sleep(Timer)
        if Login.status_code == 200:
            jsonpack = Login.json()
            self.Write.Print(jsonpack['username'] + '#' + jsonpack['discriminator'] + ' -' + ' ' + jsonpack['id'],
                             color=self.Colors.white_to_blue, interval=0.0)
            self.Write.Print(f'\nCopying Account Info on:' + ' ' + jsonpack['username'] + '#' + jsonpack[
                'discriminator'] + ' -' + ' ' + jsonpack['id'] + '...', color=self.Colors.white_to_blue, interval=0.0)
            Guilds = self.Session.get('https://discordapp.com/api/v9/users/@me/guilds', headers={
                'Authorization': f'Bot {Token}',
                'Content-Type': 'application/json'})
            self.Write.Print(
                f'\nInvite Link To Bot: \nhttps://discord.com/api/oauth2/authorize?client_id={jsonpack["id"]}&permissions=8&scope=bot',
                color=self.Colors.white_to_blue, interval=0.0)
            if Guilds.status_code in (201, 200, 204, 203):
                datapack = Guilds.json()
                for data in datapack:
                    guildid = data['id']
                    guildname = data['name']
                    self.Write.Print('\nSniffed Guild:' + guildname + ' -' + guildid, color=self.Colors.white_to_blue,
                                     interval=0.0)
                self.Write.Print('\nFinished Scraping Guild List.\n', color=self.Colors.white_to_blue, interval=0.0)
                Sleep(5)
            if Guilds.status_code in (401, 400, 403, 402, 405):
                self.Write.Print(
                    f'\nHmm... AXL Couldn\'t Sniff out this Token\'s Information, Please try another token.\n',
                    color=self.Colors.white_to_blue, interval=0.0)
            if 'retry_after' in Guilds.text:
                Timer = Guilds.json()['retry_after']
                self.Write.Print(f'\nAXL has been Timed-Out by the API Please try again in: {Timer}\n',
                                 color=self.Colors.white_to_blue, interval=0.0)
                Sleep(Timer)
        if 'retry_after' in Login.text:
            Timer = Login.json()['retry_after']
            self.Write.Print(f'\nAXL has been Timed-Out by the API Please try again in: {Timer}\n',
                             color=self.Colors.white_to_blue, interval=0.0)
            Sleep(Timer)
        self.System('pause')
        self.OS.startfile(self.Sys.argv[0])
        self.Sys.exit()


if __name__ == '__main__':
    if BotChecker() == 'UserAccount':
        AXL().UserInfo()
    if BotChecker() == 'BotAccount':
        AXL().BotInfo()
