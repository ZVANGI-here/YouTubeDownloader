#libraries

# do this before ! (($ python -m pip install pytube))

from pytube import YouTube 

#url

url=input("Enter the YouTube Video Link ! : ")

#wait

print("")
print("")
print("")
print("Please wait .... ")

#script_by

yt=YouTube(url)
print("ZVANGI's script")

#download

print(yt.title)
yt.streams.first().download()

#Done

print("")
print("Download Done !")

#end
