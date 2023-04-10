import os

def main():
	files = getFilesFrom("./jotai-benchmarks/benchmarks/anghaLeaves")
	for fileName in files:
		if fileName not in ["a.out"]:
			file = open ("./jotai-benchmarks/benchmarks/anghaLeaves/" + fileName , 'r+')
			content = file.read()
			content = content.replace("int16_t", "myint16_t")
			content = content.replace("int8_t", "myint8_t")
			content = content.replace("int32_t", "myint32_t")
			content = content.replace("int64_t", "myint64_t")
			content = content.replace("sigset_t", "mysigset_t")
			content = content.replace("id_t", "myid_t")
			content = content.replace("u_long", "myu_long")
			content = content.replace("u_char", "myu_char")
			content = content.replace("u_short", "myu_short")
			content = content.replace("u_int", "myu_int")
			content = content.replace("uint", "myuint")
			content = content.replace("daddr_t", "mydaddr_t")
			content = content.replace("dev_t", "mydev_t")
			content = content.replace("off_t", "myoff_t")
			content = content.replace("timer_t", "mytimer_t")
			content = content.replace("caddr_t", "mycaddr_t")
			content = content.replace("ssize_t", "myssize_t")
			content = content.replace("locale_t", "mylocale_t") 
			content = content.replace("pthread_t", "mypthread_t")
			content = content.replace("pthread_mutex_t", "mypthread_mutex_t")
			file.seek(0)
			file.write(content)
			file.truncate()
			file.close()

def getFilesFrom(folderPath):
	return next(os.walk(folderPath), (None, None, []))[2]

if __name__ == "__main__":
	main()