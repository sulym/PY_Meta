url = "exampleshop.com/fancy-coffee-cup-p-90764-12052019.html"

def get_product_id(url: str) -> str:
    # write your code here
    index_url = url.rfind("p")
    product = ""
    for i in range(index_url+2, len(url)):
        if url[i] == "-":
            break
        product += url[i]
    return product

print(get_product_id(url))

##############################
###### Mentor resolution #####
##############################

def get_product_id(url: str) -> str:
    tokens = url.split("-")
    return tokens[-2]