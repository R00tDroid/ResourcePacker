import glob

def AssetPacker():
    def __init__(self):
        self.output = ""
        self.filters = []
        self.files = []
        self.hash = 0

    def setOutput(self, output):
        self.output = output

    def add(self, filter):
        self.filters += [filter]

    def scan(self):
        for filter in self.filters:
            files = glob.glob(filter, recursive=True)
        #TODO Find files
        #TODO Calculate hash

    def getFiles(self):
        return self.files
    
    def needsUpdate(self):
        return True
         #TODO Check hash against cache
    
    def generate(self):
        if not needsUpdate():
            return
        #TODO Generate output
        #TODO Generate cache
