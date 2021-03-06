# To create new file 
# to create new directory
# Remane file 
# Delete file
# delete multiple file with similar names
# delete folder
ls
# First Column − Represents the file type and the permission given on the file. Below is the description of all type of files.

# Second Column − Represents the number of memory blocks taken by the file or directory.

# Third Column − Represents the owner of the file. This is the Unix user who created this file.

# Fourth Column − Represents the group of the owner. Every Unix user will have an associated group.

# Fifth Column − Represents the file size in bytes.

# Sixth Column − Represents the date and the time when this file was created or modified for the last time.

# Seventh Column − Represents the file or the directory name.
#file manupulation 
pwd
mkdir linuxtuto
ls
mkdir -p linuxtuto # to make it as parent directory 
mkdir -vp linuxtuto # to have visibility in details of action taken for mkdir

#to remove
rmdir linuxtuto
rmdir -pv linuxtuto # to have visibility in details of action taken for mkdir
rm -r foldername
rm filename


# To create file 
touch newfile # touch is use to create, modify
touch newfile1 file2 file3 #will create all the list of files 

# to copy file 
cp -r newfile linuxlearn/ # will copy everythign to dir linuxlern folder  -r is for recursion everything in folder

# move mv [options] <source> <destination>



# tomeasure and troubleshoot resources
iostat


# vi text edit more 
ZZ (cap) -- Save and exit
:q!  -- discrad all the changes, since last save and exit
:wq -- save and exit

# to view file 
cat <filename>
less <filename>
head <filename>
tail <filename>

# Wildcards


