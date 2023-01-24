# 1) Aşağıdaki String'in 5. harfini my_letter isimli bir değişkene atayınız.

my_string = "James Hetfield"

# Cevap 1)
my_letter = my_string[4]
print(my_letter)


# Aşağıdaki String'in 5. ve 8. karakteri arasındaki tüm harflerini yazdırınız (5 ve 8 dahil)

my_new_string = "QuentinTarantino"

# Cevap 2)
print(my_new_string[4:8])


# Aşağıdaki String'i kod ile tersten yazın

my_last_string = "Afyonkarahisarlılaştıramadıklarımızdanmısınız"

# Cevap 3)
print(my_last_string[::-1])


##Integer & Float

# 1) Aşağıdaki işlemin sonucu hangi veri tipinde olacaktır?

print(3 + 10.2 + 50)

# Cevap 1)
print("Result: Float")


# 2) Aşağıdaki işlemin sonucu kaçtır?

print(5 + 8 * 12)

# Cevap 2)
print("Result: ", 101)


##List & Dictionary & Set

# 1) Bu listeyi 3 farklı yoldan oluşturunuz: [1,2,"a"]


# Cevap 1.a)
mylist1 = [1, 2, "a"]
print(mylist1)

# Cevap 1.b)
mylist2 = []
mylist2.append(1)
mylist2.append(2)
mylist2.append("a")
print(mylist2)

# Cevap 1.c)
mylist3 = list()
mylist3.append(1)
mylist3.append(2)
mylist3.append("a")
print(mylist3)


# 2) Aşağıdaki "a"'yı tek satırda alınız:

my_list = [1, 4, [2, 3, "a"]]

# Cevap 2)
print(my_list[2][2])


# 3) Aşağıdaki "b"'yi tek satırda alınız:

my_dictionary = {"k1": 2, "kk": [4, {"kkkk": "b"}]}

# Cevap 3)
print(my_dictionary["kk"][1]["kkkk"])


# 4) Aşağıdaki liste set'e çevirilince hangi değerler içinde kalacaktır?

my_list_to_be_set = [11, 12, 22, 33, 11, 22, 45, 32, 21, 22, 33, 45]

# Cevap 4)
mynewset = set(my_list_to_be_set)
print(mynewset)


# Boolean

# 1) Aşağıdaki ifadenin sonucu ne olacaktır?

x = 40 * 5 + 3

y = 208 - 2 * 4

# Cevap 1)
print(x > y)


# 2) Aşağıdaki ifadenin sonucu ne olacaktır?

a = 40 * (4 - 2)

b = 80 - 2 * -5

# Cevap 2)
print(a > b)
