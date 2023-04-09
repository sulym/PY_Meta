"""
Напиши функцію message_people, яка приймає список імен people, 
створює і повертає функцію print_message.

Внутрішня функція приймає строку message і в залежності від того, 
чому дорівнює message ('hello'/'meeting'/'bye') виводить результати, 
які показані в прикладі, вона не повинна нічого повертати.
"""

def message_people(people: list) -> callable:
    # write your code here
    def print_message(massage: str) -> None:
        name = ""
        for one_peple in people:
            name += one_peple + ", "
        if massage == "hello":
            print(f"Hello, {name}nice to see you!")
        elif massage == "meeting":
            print(f"{name}we have a meeting in an hour, don't be late!")
        else:
            print(f"Bye {name}see you tomorrow!")
    return print_message

mes_people = message_people(["alex", "bob", "nik"])
mes_people("meeting")


#### M ####

def message_people(people: list) -> callable:
    people_str = ", ".join(people)

    def print_message(message: str) -> None:
        if message == "hello":
            print(f"Hello, {people_str}, nice to see you!")
        elif message == "meeting":
            print(
                f"{people_str}, we have a meeting in an hour, don't be late!"
            )
        elif message == "bye":
            print(f"Bye {people_str}, see you tomorrow!")

    return print_message