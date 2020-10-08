from pytube import YouTube
link=input("enter you url = ")
yt=YouTube(link)
video=yt.streams.get_by_itag(37)#fullhd resolution
video.download('') # platform-independent directory
print('done')
