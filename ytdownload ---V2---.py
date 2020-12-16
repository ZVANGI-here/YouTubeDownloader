#libraries 
#|------------|---------|

from pytube import YouTube

#variabels
#|------------|---------|

url = input('Enter The Video Link here : ')
yt = YouTube(url)
videos = yt.streams.all()


#quality_download   
#|------------|---------|

i = 1
for stream in videos:
    print (str(i) + " - " + str(stream))
    i += 1

stream_quality = int(input('Enter The quality number you want : '))

#place_download & downloading

video = videos[stream_quality - 1]
print ('The Download place is in [[C:\Users\ZVANGI\Downloads]]')
video.download("C:\Users\ZVANGI\Downloads")

print ('here we go sir . . . Your download has been completed')
print ('script by --ZVANGI--     OwO')

#Done !!
