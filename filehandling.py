# with open("hello.txt", 'a') as file:
#     file.write("starting the practise of  handlings files ........")

with open("hello.txt", 'r') as file:
    content = file.read()
    print(content)