
from urlparse import urlparse
from subprocess import call

lines = [line.rstrip('\n') for line in open('links.txt')]
suffix = "/videos";

links = []




for x in lines:
 if not x.endswith(suffix):
 	x = x+suffix
 	links.append(x)
 else:
 	links.append(x)


for link in links:
	print("starting:" +link)
	youtubedl_cmd = "youtube-dl -x --audio-format mp3 --audio-quality 3 --ignore-errors --add-metadata --metadata-from-title '%(artist)s - %(title)s' -o '/opt/%(uploader)s/%(title)s.%(ext)s' "+link
	#print (youtubedl_cmd)
	call(["screen", "-dmS","test","bash","-c",youtubedl_cmd])
