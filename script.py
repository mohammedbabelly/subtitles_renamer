import os
from shutil import copyfile
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

  
eps_dir = filedialog.askdirectory(title = "Select season folder")
# eps_dir = input(f"Hey {os.getenv('USER')}, enter the season folder path, ex. /Volume/drivename/GOT/S1/\n")
if not eps_dir.endswith("/"):
    eps_dir += "/"

eps_files = os.listdir(eps_dir)
eps_files = [f for f in eps_files if f.endswith(('.mkv','.rtf'))] #Filtering only the video files
eps_files.sort()
print(*eps_files, sep="\n")


sub_dir = filedialog.askdirectory(title = "Select subtitles folder")
# sub_dir = input(f"Hey {os.getenv('USER')}, enter the season's subtitle folder path, ex. /Volume/drivename/GOT/S1/subtitles/\n")
if not sub_dir.endswith("/"):
    sub_dir += "/"

sub_files = os.listdir(sub_dir)
sub_files = [f for f in sub_files if f.endswith(('.srt','.rtf'))] #Filtering only the video files
sub_files.sort()
print(*sub_files, sep="\n")


#Perform the renaming
if len(eps_files) == len(sub_files):
    for i in range(len(eps_files)):
        sub_file = os.path.splitext(sub_files[i])[0]
        sub_ex = os.path.splitext(sub_files[i])[1]
        eps_file = os.path.splitext(eps_files[i])[0]

        #Copy subtitile
        sub_path = sub_dir + sub_files[i]
        copyfile(sub_path, eps_dir + sub_files[i])


        os.rename(f"{eps_dir}{sub_files[i]}", f"{eps_dir}{eps_file + sub_ex}") 
    print("Done, enjoy your watch 🍿")
else:
    print("Seems like the eposides files and the subtitles files count is not correct.")