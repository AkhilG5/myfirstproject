# for i in range(1,101):
#     print(i)


# i = 0
# while i<100:
#     print(i)
#     i+=1


# nums = [1, 2, 3, 4, 5]

# # squared = list(map(lambda x: x**2, nums))
# # print(squared)


# squared = []
# for i in nums:
#     squared.append(i**2)
# print(squared)


# prices = {"apple": 100, "banana": 50, "orange": 80}

# discounted = dict(map(lambda item: (item[0], item[1] * 0.9), prices.items()))
# print(discounted)

# disc = {}
# for key,val in prices.items():
#     disc[key]=val*0.9
# print(disc)


# li = [1,2,3,4,5]
# li = list(map(lambda x : x**3,li))
# print(li) 

# dic = {"akhil":1000,"aditya":500,"aditi":100}
# dic = dict(map(lambda x : (x[0], x[1]*0.5),dic.items()))
# print(dic)


# a = "akhil"
# a=list(map(lambda x : x+"1",a))
# a="".join(a)
# print(a)



# dict1 = {1:"ak",2:"bk",3:"ac"}
# # for key , val in dict1.items():
# #     dict1[key]=val+"2"
# # print(dict1)
# dict1 = dict(map(lambda x: (x[0],x[1]+"2"),dict1.items()))
# print(dict1)


l1 = [10,20,30,40,50]
l1 = list(map(lambda x : str(x)+"_adi",l1))
print(l1)