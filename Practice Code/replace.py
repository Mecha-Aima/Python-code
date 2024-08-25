name = input("Enter your name : ")
date = input("Enter the date : ")

template = '''
Dear <|NAME|>,
    You are selected!
    <|DATE|>'''

print(template.replace("<|NAME|>",name).replace("<|DATE|>",date)) 