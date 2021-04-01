# my_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
#
#
# def modify_week(weeks):
#     weeks.append(weeks.pop(0))
#     return weeks
#
#
# print(modify_week(my_week))
#

# my_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# tasks = ["Java", "sleep", "Python", "Data Science", "catch Cruise", "Flex Flex"]
#
#
# def make_daily_plan(days_of_week, tasks_):
#     my_daily_plan = {}
#     for x, y in zip(days_of_week, tasks_):
#         my_daily_plan[x] = y
#     return my_daily_plan
#
#
# print(make_daily_plan(my_week, tasks))

# squares = ["Ones", "Two", "Three", "Four", "Fives"]
# values = [1, 2, 3, 4, 5]


# def square_value(squares_, tasks_):
#     squared_value = {}
#     for a, b in zip(squares_, tasks_):
#         squared_value[a] = b * b
#     return squared_value
#
#
# print(square_value(squares, values))


# Example: {1: ["Dotun", "Mofe", "Nonso"], 2:["Titus", "Abdullahi", "Dami"]}
ds_group_collection = {}

for i in range(4):
    # (name, group) = (input("Input your Name and group separated with a comma(,): ").split(","))
    # name = name
    # group = int(group)
    x = input("Input your names:")
    z = [x.split(",")]
    y = input("Input your group:")
    ds_group_collection[y] = z

print(ds_group_collection)
