import glob, os

class AssetFilter:
    def __init__(self, directory, filter, root):
        self.directory = directory
        self.filter = filter
        self.root = root

class AssetLocation:
    def __init__(self, file, location):
        self.file = file
        self.location = location

class AssetPacker:
    def __init__(self):
        self.output = ""
        self.filters = []
        self.files = []
        self.hash = 0

    def setOutput(self, output):
        self.output = output

    def add(self, directory, filter="*.*", root = "/"):
        self.filters += [AssetFilter(directory, filter, root)]

    def scan(self):
        self.files = []

        for filter in self.filters:
            for file in glob.glob(filter.directory + "/**/*.*", recursive=True):
                relativeLocation = os.path.relpath(file, filter.directory)
                self.files += [AssetLocation(file, filter.root + relativeLocation)]
        #TODO Calculate hash

    def getFiles(self):
        return self.files
    
    def needsUpdate(self):
        return True
         #TODO Check hash against cache
    
    def generate(self):
        if not self.needsUpdate():
            return
        #TODO Generate cache

        f = open(self.output + ".hpp", "w")
        f.write("#pragma once\n\n")
        f.write("typedef unsigned long AssetIdentifier;\n\n")
        f.write("extern AssetIdentifier getAssetCount();\n")
        f.write("extern const char* getAssetLocation(AssetIdentifier asset);\n")
        f.write("extern void* getAssetBuffer(AssetIdentifier asset);\n")
        f.write("extern unsigned long getAssetBufferSize(AssetIdentifier asset);\n")
        f.close()

        f = open(self.output + ".cpp", "w")
        f.write("#include \"" + os.path.basename(self.output) + ".hpp\"\n\n")
        f.write("struct Asset { const char* location; unsigned char* buffer; unsigned long bufferSize; };\n")
        f.close()
        
