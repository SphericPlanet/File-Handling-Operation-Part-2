import os
meta = open("meta.txt", "w")
meta.write("Hi! I am Dan and I am 12 yr old.")
meta.close()

os.remove('meta.txt')
