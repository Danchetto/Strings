input_dict = open("./dictionary.txt")

new_dict = open("./dict.txt", 'w')


data = []
for line in input_dict:

    data.append(line.split()[0])

data.sort(key=lambda x: len(str(x)))

for word in data:
    new_dict.write(word + '\n')

input_dict.close()
new_dict.close()