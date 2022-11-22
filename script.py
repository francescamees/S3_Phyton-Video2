
import tkinter as tk
from tkinter import ttk
import os
from tkinter.ttk import Combobox


def runBash(command):
	os.system(command)


def parse_video_stream(file_name):
    str = "ffmpeg -i " + file_name + " 2>&1 | grep Stream"
    print(str)
    runBash(str)

def codec_H256(file_name):
    aux = file_name.split(".")
    str = "ffmpeg -i "+file_name+" -vcodec libx265 -codec:a copy "+aux[0]+"_H256.mp4"
    print(str)
    runBash(str)

def codec_VP8(file_name):
    aux = file_name.split(".")
    str = "ffmpeg -i "+file_name+" -vcodec libvpx -codec:a copy "+aux[0]+"_VP8.webm"
    print(str)
    runBash(str)

def codec_VP9(file_name):
    aux = file_name.split(".")
    str = "ffmpeg -i "+file_name+" -vcodec libvpx-vp9 -codec:a copy "+aux[0]+"_VP9.webm"
    print(str)
    runBash(str)

def codec_AV1(file_name):
    aux = file_name.split(".")
    str = "ffmpeg -i "+file_name+" -vcodec libaom-av1 -codec:a copy "+aux[0]+"_AV1.mkv"
    print(str)
    runBash(str)

def new_video_720p():
    str = "ffmpeg -i BBB_720p_H256.mp4 -i BBB_720p_VP8.webm -filter_complex hstack output.mp4"
    print(str)
    runBash(str)
    str = "ffmpeg -i BBB_720p_VP9.webm -i BBB_720p_AV1.mkv -filter_complex hstack output2.mp4"
    print(str)
    runBash(str)
    str = "ffmpeg -i output.mp4 -i output2.mp4 -filter_complex vstack output3.mp4"
    print(str)
    runBash(str)

def new_video_480p():
    str = "ffmpeg -i BBB_480p_H256.mp4 -i BBB_480p_VP8.webm -filter_complex hstack output_480p.mp4"
    print(str)
    runBash(str)
    str = "ffmpeg -i BBB_480p_VP9.webm -i BBB_480p_AV1.mkv -filter_complex hstack output2_480p.mp4"
    print(str)
    runBash(str)
    str = "ffmpeg -i output_480p.mp4 -i output2_480p.mp4 -filter_complex vstack output3_480p.mp4"
    print(str)
    runBash(str)

def new_video_360x240():
    str = "ffmpeg -i BBB_360x240_H256.mp4 -i BBB_360x240_VP8.webm -filter_complex hstack output_360x240.mp4"
    print(str)
    runBash(str)
    str = "ffmpeg -i BBB_360x240_VP9.webm -i BBB_360x240_AV1.mkv -filter_complex hstack output2_360x240.mp4"
    print(str)
    runBash(str)
    str = "ffmpeg -i output_360x240.mp4 -i output2_360x240.mp4 -filter_complex vstack output3_360x240.mp4"
    print(str)
    runBash(str)

def new_video_160x120():
    str = "ffmpeg -i BBB_160x120_H256.mp4 -i BBB_160x120_VP8.webm -filter_complex hstack output_160x120.mp4"
    print(str)
    runBash(str)
    str = "ffmpeg -i BBB_160x120_VP9.webm -i BBB_160x120_AV1.mkv -filter_complex hstack output2_160x120.mp4"
    print(str)
    runBash(str)
    str = "ffmpeg -i output_160x120.mp4 -i output2_160x120.mp4 -filter_complex vstack output3_160x120.mp4"
    print(str)
    runBash(str)

#codec_H256("BBB_160x120.mp4")
#codec_VP8("BBB_160x120.mp4")
#codec_VP9("BBB_160x120.mp4")
#codec_AV1("BBB_160x120.mp4")
#new_video_160x120()

# We could conclude that VP8 is the worst codec for higher quality videos, for the only rate that quality is better than the other codecs is for 160x120.
# The video tends to look good with either codec (VP9, h.265 and AV1). However, h.265 slightly outperforms VP9, and AV1 to h.265.
# In order to achieve a higher compression rate, VP9 takes longer than h.265 because it needs to perform more processing. All that extra processing means that they will take longer to encode the video but clearly the worst codec in terms of time is AV1.
# Therefore form this exercise and comparing the videos I would say that maybe the best codec is h.265.

def run():

    if combo.get() == "BBB_160x120.mp4":
        file = "BBB_160x120.mp4"
    elif combo.get() == "BBB_360x240.mp4":
        file = "BBB_360x240.mp4"
    elif combo.get() == "BBB_480p.mp4":
        file = "BBB_480p.mp4"
    elif combo.get() == "BBB_720p.mp4":
        file = "BBB_720p.mp4"

    if combo2.get() == "VP8":
        codec_VP8(file)
    elif combo2.get() == "VP9":
        codec_VP9(file)
    elif combo2.get() == "h265":
        codec_H256(file)
    elif combo2.get() == "AV1":
        codec_AV1(file)


ventana = tk.Tk()
ventana.title("Video converter program")
ventana.geometry('450x300')

tk.Label(ventana, text="Video name you want to convert ('BBB_720p.mp4'):").place(x=40, y=20) #, anchor="center"


combo = Combobox(ventana)
combo['values']= ("BBB_160x120.mp4", "BBB_360x240.mp4", "BBB_480p.mp4", "BBB_720p.mp4")
combo.place(x=170, y=70, anchor=tk.CENTER)


tk.Label(ventana, text="Choose the codec to convert:").place(x=50, y=100) #, anchor="center"

combo2 = Combobox(ventana)
combo2['values']=("h256", "VP8", "VP9", "AV1")
combo2.place(x=170, y=150, anchor=tk.CENTER)

boton_convertir = ttk.Button(ventana, text="Convert", command=run())
boton_convertir.pack()
boton_convertir.place(x=300, y=230)
ventana.mainloop()