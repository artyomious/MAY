
# 1 Задача

def sum_lists(list1, list2):
    return [a + b for a, b in zip(list1, list2)]


print(sum_lists([1, 2, 3], [4, 5, 6]))

# 2 Задача
def palindrome(n):

    n += 1
    while str(n) != str(n)[::-1]:
        n += 1
    return n

print(palindrome(11))
print(palindrome(188))
print(palindrome(191))
print(palindrome(2541))



# 5 Задача

def find(array, subsstr):
    return [word for word in words if word.lower().startswith(subs.lower())]

words = ["Apple", "Banana", "Apricot", "Cherry"]
subs = "a"
print(find[["Apple", "Banana", "Apricot", "Cherry"],'a'])


 return [i for i in array if array.lower().startswith.subsstr.lower()[)]
# 6 Задача

def port(n):

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(port(7))
print(port(10))
print(port(100))



from random import randint

def create_list (n:int) -> list:
    return [randint (1,50) for i in range (n)]

def count_nums ( array: list) -> int:
    s = set (array)
    count = 0

    print (array)
    for i in s:
        if array.count(i)>1:
            count +=1
    return count

print(count_nums(create_list(50)))