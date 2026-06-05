# print((lambda x: x * 2)(5))

links = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.stackoverflow.com"
]

for link in links:
    # print(link.lstrip("https://www.").rstrip(".com"))
    print(link.removeprefix("https://www.").removesuffix(".com"))

    
    