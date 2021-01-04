

import zipfile
from zipfile import ZipFile 
import os 

def get_all_file_paths(directory): 

	
	file_paths = [] 

	 
	for root, directories, files in os.walk(directory): 
		for filename in files: 
			 
			filepath = os.path.join(root, filename) 
			file_paths.append(filepath)

	() 
	
	directory = input("enter the location: ")
	fname = "/p.zip"
	lname=directory+fname

	
	file_paths = get_all_file_paths(directory) 

	 
	print('Following files will be zipped:') 
	for file_name in file_paths: 
		print(file_name) () 
	with ZipFile(lname,'w', compression= zipfile.ZIP_LZMA) as zip: 
		#i = 0
		for file in file_paths:
		#	arcname = "new" + str(i)
			zip.write(file)#, #arcname)
			#i +=1


	print('All files zipped successfully!')		 


if __name__ == "__main__": 
    main() 