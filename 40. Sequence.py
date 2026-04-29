cities = ['Hyd','Vizag','Chennai']
print(cities)
print(len(cities))
print(cities*2)

list1 = ["ab","cd"]
list2 = ["gf","hi"]
print(list1+list2)
print(list1.index('ab'))

cse = ["Girls", "Boys","Students"]
CSE = []
CSE = cse.copy()
print(CSE)
print("Students" in cse)

list3 = [1,2,3,4,5,6,7,8,9,10]
print(min(list3))
print(max(list3))

given_list = [x for x in range(5)]
print(given_list)
new_list = [ var + 3 for var in given_list]
print(new_list)

given_list = {x for x in range(5)}
print(given_list)
new_list = { var + 3 for var in given_list}
print(new_list)