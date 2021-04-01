#It's not work
from pytube import YouTube
url = 'https://www.youtube.com/watch?v=uo_Jk8Zy8Lc'
my_video = YouTube(url)
print(my_video.title)

my_video = my_video.streams.get_highest_resolution()
my_video.download()