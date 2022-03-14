# import re
# from pytube import Playlist

# YOUTUBE_STREAM_AUDIO = '140' # modify the value to download a different stream
# DOWNLOAD_DIR = 'C:\\Users\\window 10\\Downloads\\geeky show django'

# playlist = Playlist('https://www.youtube.com/playlist?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6')

# # this fixes the empty playlist.videos list
# playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

# print(len(playlist.video_urls))

# for url in playlist.video_urls:
#     print(url)

# # physically downloading the audio track
# for video in playlist.videos:
#     audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
#     audioStream.download(output_path=DOWNLOAD_DIR)

# from pytube import Playlist
# playlist = Playlist('https://www.youtube.com/playlist?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6')
# # print('Number of videos in playlist: %s' % len(playlist.video_urls))
# for video_url in playlist.video_urls:
#     print(video_url)
# Playlist.download_all()

import re
from pytube import Playlist
# playlist = Playlist('https://www.youtube.com/playlist?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6')  
# DOWNLOAD_DIR = 'C:\\Users\\window 10\\Downloads\\geeky show django'
# playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")    
# print(len(playlist.video_urls))    
# for url in playlist.video_urls:
#     print(url)    
# for video in playlist.videos:
#     print('downloading : {} with url : {}'.format(video.title, video.watch_url))
#     video.streams.\
#         filter(type='video', progressive=True, file_extension='mp4').\
#         order_by('resolution').\
#         desc().\
#         first().\
#         download(DOWNLOAD_DIR)

playlist = Playlist('https://www.youtube.com/playlist?list=PLbGui_ZYuhigchy8DTw4pX4duTTpvqlh6')  
cur_dir='C:\\Users\\window 10\\Downloads\\geeky show django'
for video in playlist.videos:
    print('downloading : {} with url : {}'.format(video.title, video.watch_url))
    video.streams.\
        filter(type='video', progressive=True, file_extension='mp4').\
        order_by('resolution').\
        desc().\
        first().\
        download(cur_dir)