def read_from_file(file_name: str) -> list[str]:
    # write your code here
    with open(file_name, "r") as file:
        content = file.read().lower().split()
        new_ls = [i.replace('"', "") for i in content]
        ls = [i for i in new_ls if i[:1] == "w"]
        return sorted(ls)
        


print(read_from_file(file_name="t1.txt"))