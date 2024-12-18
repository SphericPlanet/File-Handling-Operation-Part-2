import os
print('Checking if my_file exists or not...')
if os.path.exists("quest.txt"):
    os.remove("quest.txt")
else:
    print("The File Doesn't exist.")