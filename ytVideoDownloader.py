import pytube
link = 'https://youtu.be/dQw4w9WgXcQ'
video = pytube.YouTube(link)
stream = video.streams.first()
stream.download('/storage/emulated/0/Python_for_shorts/Video')