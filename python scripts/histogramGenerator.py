import os
import subprocess

def main():
	compileFilesFrom("../jotai-benchmarks/benchmarks/anghaLeaves", "../binaries")
	compileFilesFrom("../jotai-benchmarks/benchmarks/anghaMath", "../binaries")
	generateCFGgrindMapsFrom("./binaries", "./maps")
	generateDotFilesFrom("../binaries", "../cfg", "../maps", "../dots")

def compileFilesFrom(folderPathPrograms, folderPathBinaries):
	files = getFilesFrom(folderPathPrograms)
	print("Encontrados " + str(len(files)) + " arquivos")
	createFolderIfNotExist(folderPathBinaries)
	count = 0
	for fileName in files:
		count = count + 1
		if fileName not in filesNotCompilable():
			print("Compiling file " + fileName + " -> " + str(count) + " / " + str(len(files)))
			regularCompilation(fileName, folderPathPrograms, folderPathBinaries)

def filesNotCompilable():
	return ["a.out"]

def createFolderIfNotExist(folderPath):
	isExist = os.path.exists(folderPath)
	if not isExist:
		os.makedirs(folderPath)

def regularCompilation(fileName, folderPathPrograms, folderPathBinaries):
	osResult = os.system("clang -Wno-everything " + folderPathPrograms + "/" + fileName)
	if osResult == 0:
		os.system("cp " + "./a.out " + folderPathBinaries + "/" + fileName[:-2] + "-regular.out")

def getFilesFrom(folderPath):
	return next(os.walk(folderPath), (None, None, []))[2]

def generateCFGgrindMapsFrom(folderPathBinaries, folderPathMaps):
	files = getFilesFrom(folderPathBinaries)
	createFolderIfNotExist(folderPathMaps)
	count = 0
	for fileName in files:
		count = count + 1
		print("Generating map file " + fileName + " -> " + str(count) + " / " + str(len(files)))
		cfggrindAsMap(fileName, folderPathBinaries, folderPathMaps)

def cfggrindAsMap(fileName, folderPathBinaries, folderPathMaps):
	print("cfggrind_asmmap " + folderPathBinaries + "/" + fileName + " > " + folderPathMaps + "/" + fileName[:-4] + ".map")
	os.system("cfggrind_asmmap " + folderPathBinaries + "/" + fileName + " > " + folderPathMaps + "/" + fileName[:-4] + ".map")

def generateDotFilesFrom(folderPathBinaries, folderCfgFiles, folderPathMaps, folderPathDots):
	files = getFilesFrom(folderPathBinaries)
	createFolderIfNotExist(folderCfgFiles)
	createFolderIfNotExist(folderPathDots)
	count = 0
	for fileName in files:
		try:
			count = count + 1
			print("Generating dot file " + fileName + " -> " + str(count) + " / " + str(len(files)))
			generateDotFile(fileName, folderPathBinaries, folderCfgFiles, folderPathMaps, folderPathDots)
		except Exception as e: 
			print(e)

def generateDotFile(fileName, folderPathBinaries, folderPathCfgs, folderPathMaps, folderPathDots):
	fileCfgName = folderPathCfgs + "/" + fileName[:-4] + ".cfg"
	fileMapName = folderPathMaps + "/" + fileName[:-4] + ".map"
	os.system(" valgrind --tool=cfggrind --cfg-outfile=" + fileCfgName + " --instrs-map=" + fileMapName + " --cfg-dump=main " + folderPathBinaries + "/" + fileName + " 0")
	direct_output = subprocess.check_output('ls *.dot', shell=True).decode("utf-8").split("\n")
	for dotfile in direct_output:
		if dotfile != "":
			os.system("cp " + "./" + dotfile + " " + folderPathDots + "/" + fileName[:-4] + ".dot")
			os.system("rm ./" + dotfile)


if __name__ == "__main__":
	main()