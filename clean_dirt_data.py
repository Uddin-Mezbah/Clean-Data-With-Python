data = "https://pynative.com/python-basic-exercise-for-beginners/ >>"
new_data = data.lower()
output_data = ''

for char in new_data:
    # print(char)
    if (char == 'a') or (char == 'e') or (char == 'i') or (char == 'o') or (char == 'u') :
        # print(f"{char} found")
        
        output_data += char + ' '  #output_data =output_data + char
        


print(output_data)