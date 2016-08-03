# youtube-dl-batch
simple script to automate video downloading with youtube-dl by rg3


# Usage 
```sh
$ wget -O - https://raw.githubusercontent.com/k0ssi/youtube-dl-batch/devel/setup.sh | bash
$ cd youtube-dl-batch/
$ nano links.txt
and add every channel you want
$ python youtube-dl-batch.py 
```
youtube-dl-batch automatically installing vsftp which allows you to download files by ftp. Default login is: dl/dl123


# Help
```
usage: youtube-dl-batch.py [-h] [-da DA] [-v]

youtube-dl-batch 
Batch downloading youtube channels by using youtube-dl by rg3

optional arguments:
  -h, --help     show this help message and exit
  -da DA         Download only the videos uploaded after specified date (example: 19700101 for January 1, 1970)
  -v, --verbose  Will display verbose log
```
