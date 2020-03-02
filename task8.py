a_str = "1,2,3,4,5,6,7,8,9,10"
b_list = [1,2,3,4,5,6,7,8,9,10]
c_set = set([1,2,3,4,5,6,7,8,9,10])
d_tuple = (1,2,3,4,5,6,7,8,9,10)

print("Str: len %d size %d"%(len(a_str), a_str.__sizeof__()))

print("List: len %d size %d"%(len(b_list), b_list.__sizeof__()))

print("Set: len %d size %d"%(len(c_set ), c_set.__sizeof__()))

print("Tuple: len %d size %d"%(len(d_tuple), d_tuple.__sizeof__()))