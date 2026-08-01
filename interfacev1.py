from tkinter import *

import os , subprocess

app = Tk()

#--------------Variables-------------------
link_folder = StringVar()
link_video = StringVar()
#audio = StringVar()
#--------------Fonctions-------------------

def downloader(link_folder, link_video):
 verif =  subprocess.run("yt-dlp --version", shell=True, capture_output=True, text=True)
 if verif.stdout=="":
    print("yt-dlp n est pas installe . tkt attends je vais l installer pour toi")
    subprocess.run("sudo apt install yt-dlp", shell=True)
 os.chdir(link_folder)
 subprocess.run(["yt-dlp", link_video, "-o", f"{link_folder}/%(title)s.%(ext)s"])

#----------------Labels--------------------
app.title("Video Downloader")
app.geometry("600x300")
app.resizable(True, True)
app.config(bg="#1e1e1e")
logo=PhotoImage(file="logo.png")
app.iconphoto(True, logo)
msg_welcome= Label(app, text="👻 Bienvenue !", bg="#1e1e1e", fg="#064b9b", font=("verdana", 17, "italic bold"))
msg_link_folder = Label(app, text="🔗 lien du dossier :", bg="#1e1e1e", fg="white", font=("verdana", 12))
emplacement_link_folder = Entry(app, textvariable=link_folder, width=30, bg="#f1ebeb", fg="#1e1e1e", font=("verdana", 12))
valide_link_folder = Button(app, text="ok!", bg="#064b9b", fg="white", font=("verdana", 12, "bold"),command=lambda:downloader(link_folder.get(), link_video.get()))
msg_link_video = Label(app, text="🔗 lien de la vidéo :", bg="#1e1e1e", fg="white", font=("verdana", 12))
emplacement_link_video = Entry(app, textvariable=link_video, width=30, bg="#f1ebeb", fg="#1e1e1e", font=("verdana", 12))

#--------------Interface-------------------
msg_welcome.pack(pady=20)
msg_link_folder.place(x=20, y=60)
emplacement_link_folder.place(x=180, y=60)
msg_link_video.place(x=20, y=100)
emplacement_link_video.place(x=180, y=100)
valide_link_folder.pack(pady=60)

if __name__ == "__main__":
    app.mainloop()