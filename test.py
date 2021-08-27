import os

# Getting the current work directory (cwd)
thisdir = os.getcwd()

# r=root, d=directories, f = files
for r, d, f in os.walk(thisdir):
	for file in d:
	t= file.split("_")
	# print( t[len(t)-2])
	if ( int (t[len(t)-2]) > 0 ):
		print(file)
