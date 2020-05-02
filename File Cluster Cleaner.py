##  Importing Modules  ##
import os

##  Function for Creating Folders  ##
def createFolders(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

##  Function for file movement to specified folders  ##
def move(folderName, files):
    for file in files:
        if os.path.exists(f"{folderName}/{file}"):
            rem = os.getcwd()
            path2 = os.path.join(rem, folderName, 'AlreadyExist')
            if not os.path.exists(path2):
                os.makedirs(path2)
            os.replace(file, f"{path2}/{file}")
        else:
            os.replace(file, f"{folderName}/{file}")

##  Listing all Files & Removing Cleaner Code File from list  ##
files = os.listdir()
files.remove("Cleaner.py")
print(files)

##  Create Folders  ##
createFolders('Images')
createFolders('Docs')
createFolders('Music')
createFolders('Others')
createFolders('Videos')

##  Initializing Extensions  ##
imgExts = [".jpeg", ".jfif", ".png", ".tiff", ".gif", ".tif", ".bmp", ".jpg", ".eps", ".cr2", ".raw", ".nef", ".orf", ".sr2"]

docExts = [".odt", ".pdf", ".xls", ".xlsx", ".doc", ".docx", ".ods", ".ppt", ".txt", ".pptx", "rtf"]

videoExts = [".mp4",".flv", ".webm", ".mkv", ".vob", ".ogv", ".drc", ".mng", ".avi", ".mts", ".m2ts", ".ts", ".mov", ".qt", ".wmv", ".yuv", ".rm", ".rmvb", ".asf", ".amv", ".m4v", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".m2v", ".svi", ".3gp", ".3g2", ".mxf", ".roq", ".nsv", ".f4v", ".f4p", ".f4a", ".f4b"]

musicExts = [".mp3", ".aa", ".aac", ".aax", ".act", ".aiff", ".alac", ".amr", ".ape", ".au", ".awb", ".dct", ".dss", ".dvf", ".flac", ".gsm", ".iklax", ".ivs", ".m4a", ".m4b", ".m4p", ".mmf", ".mpc", ".msv", ".nmf", ".nsf", ".ogg", ".oga", ".mogg", ".opus", ".ra", ".rm", ".rf64", ".sln", ".tta", ".voc", ".wav", ".wma", ".wv", ".8svx", ".cda"]

##  Categorising Files According Extension   ##
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
music = [file for file in files if os.path.splitext(file)[1].lower() in musicExts]
video = [file for file in files if os.path.splitext(file)[1].lower() in videoExts]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

##  Other Extension Handling  ##
others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in musicExts) and (ext not in docExts) and (ext not in imgExts) and (ext not in videoExts) and os.path.isfile(file):
        others.append(file)

##  Final File Moving to Specified Folders  ##
move("Music", music)
move("Videos", video)
move("Docs", docs)
move("Images", images)
move("Others", others)
