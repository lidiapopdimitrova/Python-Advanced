from os.path import exists
from os import remove

command = input()
while True:
    if command == "End":
        break
    command_parts = command.split("-")
    to_do, file_name = command_parts[0], command_parts[1]
    if to_do == "Create":
        with open(f'./{file_name}', "w") as file:
            pass
    elif to_do == "Add":
        content = command_parts[2]
        with open(f'./{file_name}', 'a') as file:
            file.write(content + '\n')
    elif to_do == "Replace":
        if not exists(f'./{file_name}'):
            print('An error occurred.')

        old_string, new_string = command_parts[2], command_parts[3]
        with open(f'./{file_name}', 'r+') as file:
            file_content = file.read().replace(old_string, new_string)
            file.seek(0)
            file.truncate()
            file.write(file_content)
    else:
        if not exists(f'./{file_name}'):
            print("An error occurred.")

        remove(f'./{file_name}')

    command = input()

