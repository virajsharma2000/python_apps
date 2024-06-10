from moviepy.editor import *
import easygui

def generate_memory_photos_presentation(photos,output_file_name):
 clips = []

 for photo in photos:
  clips.append(ImageClip(photo).set_duration(2))

 video = concatenate(clips, method = 'compose')

 total_duration = len(clips) * 2

 audio = AudioFileClip('memories_song.mp3')

 video = video.set_audio(audio).subclip(0, total_duration)

 video.write_videofile(
            output_file_name, 
            fps=24,             
            codec='libx264',
            bitrate="800k",     # Adjust bitrate for faster processing
            audio_codec='aac',  # Use a standard audio codec
            preset='ultrafast'  # Use a faster preset for encoding
        )
 


photos = []

while True:
 photo_file = easygui.fileopenbox()

 if photo_file == None:
  break

 else:
  photos.append(photo_file)

output_file = input('Enter output file: ')

generate_memory_photos_presentation(photos,output_file)
