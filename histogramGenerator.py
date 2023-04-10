import os

def main():
	compileFilesFrom("./jotai-benchmarks/benchmarks/anghaLeaves", "./binaries")
	generateCFGgrindMapsFrom("./binaries", "./maps")
	generateDotFilesFrom("./binaries", "./cfg")

def compileFilesFrom(folderPathPrograms, folderPathBinaries):
	files = getFilesFrom(folderPathPrograms)
	print("Encontrados " + str(len(files)) + " arquivos")
	createFolderIfNotExist(folderPathBinaries)
	count = 0
	for fileName in files:
		count = count + 1
		if fileName not in filesNotCompilable():
			print("Compilando arquivo " + fileName + " -> " + str(count) + " / " + str(len(files)))
			regularCompilation(fileName, folderPathPrograms, folderPathBinaries)

def filesNotCompilable():
	return ["a.out"]

def createFolderIfNotExist(folderPath):
	isExist = os.path.exists(folderPath)
	if not isExist:
		os.makedirs(folderPath)

def regularCompilation(fileName, folderPathPrograms, folderPathBinaries):
	osResult = os.system("clang -Wno-everything " + folderPathPrograms + "/" + fileName)
	print("Result: " + str(osResult) + " | " + fileName + " to " + fileName[:-2] + "-regular.out")
	if osResult == 0:
		os.system("cp " + "./a.out " + folderPathBinaries + "/" + fileName[:-2] + "-regular.out")

def getFilesFrom(folderPath):
	return next(os.walk(folderPath), (None, None, []))[2]

def generateCFGgrindMapsFrom(folderPathBinaries, folderPathMaps):
	files = getFilesFrom(folderPathBinaries)
	createFolderIfNotExist(folderPathMaps)
	for fileName in files:
		cfggrindAsMap(fileName, folderPathBinaries, folderPathMaps)

def cfggrindAsMap(fileName, folderPathBinaries, folderPathMaps):
	os.system("cfggrind_asmmap " + folderPathBinaries + "/" + fileName + " > " + folderPathMaps + "/" + fileName[:-4] + ".map")

def generateDotFilesFrom(folderPathBinaries, folderCfgFiles):
	files = getFilesFrom(folderPathBinaries)
	createFolderIfNotExist(folderCfgFiles)
	for fileName in files:
		try:
			generateDotFile(fileName, folderPathBinaries, folderCfgFiles)
		except Exception as e: 
			print(e)

def generateDotFile(fileName, folderPathBinaries, folderPathCfgs):
	os.system(" valgrind --tool=cfggrind --cfg-outfile=test.cfg --instrs-map=test.map --cfg-dump=bubble " + folderPathBinaries + "/" + fileName + " 0")
	direct_output = subprocess.check_output('ls *.dot', shell=True)
	for dotfile in direct_output:
		os.system("cp " + "./" + dotfile + " " + folderPathCfgs + "/" + fileName[:-4] + "-regular.out")
		os.system("rm ./" + dotfile)


if __name__ == "__main__":
	main()