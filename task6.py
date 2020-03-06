a_list = ["one", "two", "three"]
b_list = a_list
a_list.append("bob")

a_list[0] = "ONE"
b_list[1] = "TWO"
print(a_list)
print(b_list)

b_list[-1] = "!!!!"

c_list = [1,2,3, a_list, [a_list, b_list], set([1,2,3])]
c_list[4][0][0]

print(set("abcdab"))
