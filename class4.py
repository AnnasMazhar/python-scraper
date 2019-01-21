# # dictionaries
#
# d = {"name": "Annas", "age": 22, "profession": "Engineer", "hobbies":["Gaming", "Coding", "reading"],\
#     "Jobs": {"Internship": "Byco", "1stjob": "Mentat"}}
# print(d)
# print("Hobbies: ", d["hobbies"][2])
# print(d["Jobs"]["1stjob"])
# d.update({"Salary": 20000})
# d.update({"Graduation":2018})
# d.update({"University": "Sir syed"})
# print(d)
#
# for key, value in d.items():
#     print(key, value)
# if "Jobs" in d:
#     del d["Jobs"]
#
# print(d)

# student = {"name":"Saad", "Major": "Computer Science", "Year": 2018, "Grade": "A"}
# for key in sorted(student):
#     print("%s: %s" % (key, student[key]))
#
# color_dict = {'red':'#FF0000',
#           'green':'#008000',
#           'black':'#000000',
#           'white':'#FFFFFF'}
#
# for key in sorted(color_dict):
#     print("%s: %s" % (key, color_dict[key]))

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4 = {}
# for d in (dic1, dic2, dic3): dic4.update(d)
# print(dic4)
#
# dic4[0] = 0
# print(dic4)

cars = {}
cars["Honda"] = 2015
cars["Toyaota"]  = 2017
cars["Nissan"] = 2018
cars["Audi"] = 2018
print(cars)

print(len(cars))
