with open('data.txt', 'w') as file:
    file.write("My name is Gauransh")

with open('data.txt', 'r') as file:
    data = file.readlines()
    print("I am the student of Codingal")
    for line in data:
        words = line.split()
        for word in words:
            print(word)
