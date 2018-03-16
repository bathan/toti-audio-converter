import os
SCRIPT_PATH = os.path.realpath(__file__)
DIR_PATH = os.path.dirname(BASE_SCRIPT_PATH)
SOURCE_DIR = DIR_PATH + '/input'
DESTINATION_DIR = DIR_PATH + '/output'
for filename in os.listdir(SOURCE_DIR):
    if (filename.endswith(".wma")): #or .avi, .mpeg, whatever.
		inputFile = SOURCE_DIR + "/" + filename
		fileWithoutExtension = os.path.splitext(os.path.basename(inputFile))[0]
		outputFile = DESTINATION_DIR + "/" + fileWithoutExtension + ".mp3"
		command = "ffmpeg -i {0} -vn -ar 44100 -ac 2 -b:a 192k -f mp3 {1}".format(inputFile,outputFile)
		os.system(command);
    else:
        continue
