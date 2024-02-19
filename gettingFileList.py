import os
# %%
# moving to directory with all photos
os.chdir("D:/DCIM")

# Getting list of all folders
folderList = os.listdir()

# %%
# this is used for testing is a path is a file or directory
# os.path.isdir(path)¶
for ii in folderList:
    os.path.join()