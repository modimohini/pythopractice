# bashstuff
> redirecting to a file 
    ls -lR > directory-tree.txt

>> redirects to a file, appending data 
    echo mylabserver.com >> /ect/hosts

# need sudo permission 
yum update -y
yum install -y nc               

 nc -vz google.com 443          # here 433 is the port number 

# To login, open ssh to linux vm 
- $ssh <user_name>@<public_ip>
- sudo -i ---> to become root login

1. Creating users 
    - $useradd <user_name>
2. Creating Group 
    - $groupadd <group_name>
3. Adding user to group
    - $usermod -g <group_name> <user_name>
4. To check/confirm user is added to which group
    - $ id <usesr_name> 
        - example:  id <user_name>
uid=1002(<user_name>) gid=1008(<group_name>) groups=1008(<group_name>) 
5. To add user to ,ultiple group 
    - usermod -aG <group_name> <user_name>
eg: [root@ip-10-10-10-90 ~]# usermod -aG newgrp jolly
[root@ip-10-10-10-90 ~]# id jolly
uid=1002(jolly) gid=1008(poweruser) groups=1008(poweruser),1007(newgrp)

# permissions 700, 400, 765 -- UserGroupOther
drwxr--r--
* rwx
* 000 -- 0
* 001 -- 1
* 010 -- 2
* 011 -- 3
* 100 -- 4
* 101 -- 5
* 110 -- 6
* 111 -- 7   
# Persmission for Directory 
- chmod 1777 dirname

# Working with Users and Permissions
- Managing users in Linux

- New sudo Users 
- SSH, Redirection and Permission in Linux 

# Networking 
- Testing DNS Resolution 
- Monitoring Network Access 
- Network Filesystems 

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
cat <filename> | less #or |more
less <filename>
head -2 <filename> # no of lines -2
tail -3 <filename> # no of lines -3
sort <filename> # sort alphabetically 
nl <filenam> # number the lines in file 
nl -s '.' -w 30 <filename> # . is for number '1. ' and -w is the width from margin as w -30

# Wildcards
* - represents zero or more characters
? - represents a single character
[] - represents a range of characters


# grep
cat <filename> | grep lemon   # we will get 'lemon' from the file  
cat newfile | grep -i a       # we get all list containing letter 'a'  -i match both (upper and lower) case
cat newfile | grep -v a   # shows all the lies that do not match the serch string 
cat newfile | grep -c ben     # display count of matching lines
cat newfile | grep -n         # matching line and its number 
cat newfile | grep -l         # shows name of the file with string 

# sort 
sort newfile                   # -r --> revverse sorting, -n --> sorts numerically, -f --> case insensitive sorting 
sort -r newfile
cat newfile | grep -v a | sort -r 

# to check permissions -l
ls -l <path>

# process managemtn 
top 
top -m
jobs
ps f
ps <pid> # status of single process running 

# kill
kill -15 [pid]  <-  sends sigterm  --> file is sometime backup
kill     [pid]  <-  sends sigterm
kill  -2 [pid]  <-  sends sigint
kill  -1 [pid]  <-  sends sigup
kill  -9 [pid]  <-  sends sigkill  --> it kill at that moment (dirty shutdown, file may get corropted, +ve help to kill bad process)

pkill -f '<PATTERN>'     <- it will match the patter and kill the process/task 


# setting up cron job
crontab -l  # listcurrent cron jobs 
conntab -e  # edit cron job 

min (0 - 59)
| hr (0 - 23)
| | day of month (1 - 31)
| | | month(1 - 12)
| | | | day of the week (0 - 6) __ Sun - Sat, 7 is Sunday on some sys
| | | | |
* * * * * <job name>

* * * * * echo 'hey' >> /temp/demo.txt


# regular expressions tr sed vi grep
cat newfile | grep ^a | grep t$    # ^ (carrot) will filter everthing with string starting with 'a' and '$' will filter anything that ends with 't'

# interval regular expression
{n}     --> matches preceding char appering 'n' times exactly 
{n.m}   --> matches preceding char appering 'n' times but not more than 'm'
{n, }   --> matches preceding char only when it appears 'n' times or more
\+      --> matches 1 or more occurence of previous char
\?      --> matches zero or one occurence of previous char
.       --> replace any character
^       --> start of string
$       --> matches end of string

cat newfile | grep -E p\{2}  # -E is regular expression 
cat newfile | grep "a\+t"    # filter to anything ending with 'at'



# Measure and Troubleshoot Resource Usage (200.1)
measure CUP and disk Usageiostat
startfree
vm status
Isof
ps, pstree, top
netstats
w, uptime 

