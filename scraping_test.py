from urllib.request import urlopen

url = "https://pvpoke.com/battle/1500/abomasnow/abra/11/1-3-2/0-1-4/"

page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decod('utf-8')

print(html)