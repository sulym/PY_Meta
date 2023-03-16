message =  'Ivan,Mark,Sergey'
def extract_names(message: str) -> list:
    # write your code here

    message = list(message.split(","))
    message_list =[]
    for i in message:
        message_list += [i.strip()]
    return message_list

print(extract_names(message))

######Using the function to clean up extra spaces in a line######десятки