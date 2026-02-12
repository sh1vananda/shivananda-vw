# fizzbuzz using while loop

def fizzbuzz(start, end):
    while start <= end:
        if start %  3 == 0 and start %  5 == 0:
            print("FizzBuzz")
            start += 1
        elif start %  3 == 0:
            print("Fizz")
            start += 1
        elif start %  5 == 0:
            print("Buzz")
            start += 1
        else:
            print(start)
            start += 1

start, end = input("enter start and end: ").split()
fizzbuzz(int(start), int(end))
