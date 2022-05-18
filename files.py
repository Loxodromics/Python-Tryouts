import shutil
import os


# copy a file
src = "file_for_copying.bla"
dst = "copied_file.bla"

shutil.copyfile(src, dst)

# create a directory
# get current directory
path = os.getcwd()
path += "/newDir"
mode = 0o700
print("trying to create: " + path)
try: 
	os.mkdir(path) 
except OSError as error: 
	print(error)

# create symlink
dst_symlink = "symlinked_file.bla"
os.symlink(src, dst_symlink)

print ("done")