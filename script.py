from pathlib import Path


p = Path.home() /"Downloads"

dirs = {".png":"Images",
        ".jpeg":"Images",
        ".jpg":"Images",
        ".gif":"Images",
        ".png":"Images",
        ".mp4":"Videos",
        ".zip":"Archives",
        ".txt":"Documents",
        ".pdf":"Documents",
        ".json":"Documents",
        ".mp3": "Musiques" ,
        ".wav":"Musiques"
}
tri_dir = Path.home() / "Downloads"
files = [f for f in tri_dir.iterdir() if f.is_file()]
for f in files :

    output_dir = tri_dir /dirs.get(f.suffix,"Autres")
    output_dir.mkdir(exist_ok= True)
    f.rename(output_dir /f.name)