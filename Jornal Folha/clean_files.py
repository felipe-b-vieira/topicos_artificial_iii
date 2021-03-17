import os, re
import codecs

def clean_files(foldername):
    for root, dirs, files in os.walk(foldername+'/'):
        for file in files:
            filename, extension = os.path.splitext(file)
            print("Cleaning file: "+filename)
            exitfile = codecs.open('cleaned_'+foldername+'/'+filename,"w", encoding='utf-8')
            writingText = False
            for line in codecs.open(foldername+'/'+filename+extension, 'rb', errors='ignore').readlines():
                line = line.decode('latin-1').encode('utf-8')
                line = line.decode('utf-8')
                if line=="</TEXT>\n":
                    writingText = False
                    exitfile.write("\n")
                if writingText:
                    exitfile.write(line)
                if line == "<TEXT>\n":
                    writingText = True
            exitfile.close()
            
clean_files("textos")