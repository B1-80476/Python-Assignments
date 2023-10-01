# Q6. Write a function in Python to count and display the total number of words
# in a text file.


f = open("story.txt", "r")

count = 0
for line in f:
    for word in line:
        if word == " " or word == "." or word == "'":
            continue
        else:
         count += 1

print(count)
