import os, re

def clean(line):
    if line[:13]=="Archive-name:" \
        or line[:14]=="Last-modified:" \
        or re.match(r"^[- \n=]*$", line):
        return ""
    line = line.strip("|")
    line = line.strip(">")
    line = line.strip("-")
    line = re.sub(r'\[.*\]', '', line)
    line = re.sub(r'^[0-9]*[.)]', '', line)
    line = re.sub(r'^ *', '', line)
    return line

def clean_files(foldername):
    for root, dirs, files in os.walk(foldername+'/'):
        for file in files:
            filename, extension = os.path.splitext(file)
            print("Cleaning file: "+filename)
            exitfile = open('cleaned_'+foldername+'/'+filename,"w")
            readingHeader = True
            for line in open(foldername+'/'+filename, encoding="utf8").readlines():
                if not readingHeader:
                    line = clean(line)
                    exitfile.write(line)
                elif line=="\n":
                    readingHeader = False
            exitfile.close()
            
clean_files("train")
clean_files("test")