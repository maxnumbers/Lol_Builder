import urllib.request
import json
import os
from glob import glob
import re
import sys
import csv

version_url = "https://ddragon.leagueoflegends.com/api/versions.json"
api_key = "RGAPI-93bc7b31-403b-4d0b-903b-3685ddc05d3e"

# fetch patch number from json url, most recent patch is item 0
fetch_versions = urllib.request.urlopen(version_url)
version_list = json.loads(fetch_versions.read())
version_number = version_list[0]

# fetch runes and rune info, uses version number
runes_url = "https:// ddragon.leagueoflegends.com/cdn/", version_number, "/data/en_US/runesReforged.json"
rune_icons_url = "https://ddragon.leagueoflegends.com/cdn/img/" 
#example: https://ddragon.leagueoflegends.com/cdn/img/perk-images/Styles/Domination/Electrocute/Electrocute.png)
#http://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/perks.json

# fetch character stats, uses version number
char_stats_url = "http://ddragon.leagueoflegends.com/cdn/", version_number, "/data/en_US/champion.json"
fetch_char_stats = urllib.request.urlopen(char_stats_url)
char_stats = json.loads(fetch_char_stats.read())

# fetch items, uses version number
items_url = "http://ddragon.leagueoflegends.com/cdn/", version_number,"/data/en_US/item.json"

#define item_number first 
# items_icon_url = ("http://ddragon.leagueoflegends.com/cdn/", version_number, "/img/item/", item_number, ".png"

print(len(char_stats["data"]))
#for champion,c in char_stats["data"]:
 #   char_skills_url = "http://ddragon.leagueoflegends.com/cdn/", version_number, "/data/en_US/champion/", champion,".json"
  #  champ_splash_url = "http://ddragon.leagueoflegends.com/cdn/img/champion/splash/", champion, "_0.jpg"

