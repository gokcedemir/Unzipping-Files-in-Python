# Import the os module, for the os.walk function
import os
import zipfile
from zipfile import ZipFile
for root, dirs, files in os.walk("/home/gokce/Desktop/deneme/malwares"):
	for myfile in files:
		if myfile.endswith(".zip"):
			print(os.path.join(root, myfile))
			try:
				myzip =  zipfile.ZipFile(os.path.join(root, myfile), 'r')
                                # b'infected' --> convert password to binary  
				myzip.extractall('/home/gokce/Desktop/deneme/newMalware', myzip.namelist(), b'infected' )
			except:
				pass         
