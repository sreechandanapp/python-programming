numbers=[2,4,-1,-5]
print(numbers)
new_list = []
for i in numbers:
    if i > 0:
        new_list.append(i)
print("Postive numbers:",new_list)

n=int(input("Enter the number of elements:"))
num_list=[]
for i in range(n):
    a=int(input("Enter the numbers:"))
    num_list.append(a)
    print("Entered list:",num_list)
sqr_lst = [x ** 2 for x in num_list]
print("Squared list:",sqr_lst)

word=input("Enter a word:")
vowels=[x for x in word.lower() if x in['a','e,''i','o','u']]
print("the vowels in the word are:",vowels)

w=input("Enter a word:")
ord=[ord(x)for x in w]
print("The ordinal value is:",ord)