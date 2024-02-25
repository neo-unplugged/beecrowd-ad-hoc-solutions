# take 2 inputs from user until EOF
while True:
    try:
        x, y = map(int, input().split(" "))
        print(x ^ y)
    except EOFError:
        break
