import sys

writer = open("final_train.txt", "w")

file_name = sys.argv[1]
for line in open(file_name, "r").readlines():
    for word in line.split():
        writer.write(word + "\n")
writer.close()

