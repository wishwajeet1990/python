import subprocess
URL = input("Enter URL Of video : - ")
my_video = f"yt-dlp --no-check-certificate -f bestvideo+bestaudio --merge-output-format mp4 \"{URL}\""
subprocess.run(my_video,shell=True)


#               https://youtu.be/qrMnoY8qBJM?si=dV8Glb2qGdgfAGY8