#! /usr/bin/python
from urlparse import urlparse
from subprocess import call
import argparse
from argparse import RawTextHelpFormatter
import sys
"""
internal configuration start
"""

lines = [line.rstrip('\n') for line in open('links.txt')]
suffix = "/videos";

links = []
dateafter_parm = ""


def verbose_msg(msg):
	if args.verbose: print("VERBOSE: "+msg)

"""
internal configuration end
"""




parser = argparse.ArgumentParser(description='youtube-dl-batch \nBatch downloading youtube channels by using youtube-dl by rg3',
								 epilog="",formatter_class=RawTextHelpFormatter)
parser.add_argument('-da', type=str,help='Download only the videos uploaded after specified date (example: 19700101 for January 1, 1970)')
parser.add_argument('-v','--verbose',help='Will display verbose log',action="store_true")
args = parser.parse_args()



"""
Checking links extracted from links.txt for /videos suffix to ensure getting all videos from channel
"""
for x in lines:
 if not x.endswith(suffix):
 	x = x+suffix
 	links.append(x)
 else:
 	links.append(x)


if args.da:
	print("::Download only the videos uploaded after "+args.da)
	dateafter_parm = "--dateafter "+args.da
	verbose_msg("adding "+dateafter_parm+" to command ")



"""

"""
for link in links:
	print("downloading: "+link)
	youtubedl_cmd = "youtube-dl -x --audio-format mp3 --audio-quality 3 --ignore-errors --add-metadata --metadata-from-title '%(artist)s - %(title)s' -o '/opt/%(uploader)s/%(title)s.%(ext)s' "+dateafter_parm+" "+link
	verbose_msg("running command "+youtubedl_cmd)
	call(["screen", "-dmS","test","bash","-c",youtubedl_cmd])

	print("Please use htop or check screen for running sessions")
