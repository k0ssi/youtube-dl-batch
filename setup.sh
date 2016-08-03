# installing requirements
sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl
sudo apt-get install screen libav-tools git vsftpd -y 
sudo useradd -m -d /opt dl
echo dl:dl123 | chpasswd
