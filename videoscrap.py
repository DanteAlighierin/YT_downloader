from pytube import YouTube
link=input("enter you url = ")
yt=YouTube(link)
#t=yt.streams.filter(audio_codec='mp4a.40.2').all()
#for i in t:
 #   print(t)
video=yt.streams.get_by_itag(18)
video.download(r'C:\Users\ADMIN\OneDrive\Desktop')
print('done')