import pytube
link=input('cxkjvk')
yt=pytube.YouTube(link)
yt.streams.first().download()
print('jsfjgs',link)