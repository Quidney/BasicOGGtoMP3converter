from pydub import AudioSegment
import os

directory = "C:\\Users\\User\\Desktop\\Source"         # Change this to the directory where your ogg files are located
output_directory = "C:\\Users\\User\\Desktop\\Output"  # Change this to the directory where you want the mp3 files to be saved

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for file in os.listdir(directory):
    if file.endswith(".ogg"):
        ogg_path = os.path.join(directory, file)
        mp3_path = os.path.join(output_directory, os.path.splitext(file)[0] + ".mp3")
        AudioSegment.from_file(ogg_path).export(mp3_path, format="mp3")
