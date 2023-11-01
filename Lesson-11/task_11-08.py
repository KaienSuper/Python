url = input("Enter a URL: ").split("=")[1:2]
url = " ".join(url)
url = url.split("&")[:1]
url = "".join(url)
print(url)
