# smile = "\U0001f600"

for number in range(10):
    count = 0
    emoticons = ""
    while count <= number:
        emoticons += "\U0001f600"
        count += 1
    print(emoticons)

for number in range(10):
    emoticons = ""
    for count in range(number + 1):
        emoticons += "\U0001f600"
    print(emoticons)

for number in range(1, 11):
    print("\U0001f600" * number)

count = 1
while count < 11:
    print("\U0001f600" * count)
    count += 1