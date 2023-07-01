def copy_file(command: str) -> None:
    command = command.split()
    command_info = [0]
    file = command[1]
    file_copy = command[2]
    
    if file != file_copy and command_info == "cp":
        with open(file_in, "r") as file_in, open(file_out, "w") as file_out:
            file_out.write(file_in.read())
    
print(copy_file(command="cp file.txt fi23le.txt"))