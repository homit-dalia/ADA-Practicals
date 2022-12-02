a=[22,35,40,11,15,33,14,17,19,100,144,122]

def searchElement(keyElement):
    length = len(a)
    print(keyElement, a, length)
    for i in range(0,length):
        if a[i] == keyElement:
            return i+1
    return -1

# keyElement = input("Enter key element ")
# keyElement = int(keyElement)
keyElement = 15
result = searchElement(keyElement)
print('Key element is found/notfound at ', result)
