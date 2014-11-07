import requests
import random
import sys
r = requests.get('https://hackbulgaria.com/api/students/', verify=False)
content = r.json()

print ("Hello, you can use one the the following commands:")
print("list_courses - this lists all the courses that are available now.")
print ("match_teams <course_id>, <team_size>, <group_time>")
print ("\n")



def list_courses():
    id = 1
    courses = {}
    for i in content:
        for j in i["courses"]:
            if j['name'] not in courses.values():
                courses[id] = j['name']
                id += 1
    for k, v in courses.items():
        print("[{}] {}".format(k, v))
    return courses


def match_teams(course_id, team_size, group_time):
    name_of_course = list_courses()[course_id]

    students = []
    for i in content:
        for j in i["courses"]:
            if j['name'] == name_of_course and j['group'] == group_time:
                students.append(i["name"])

    random.shuffle(students)
    buf = 0
    while buf != len(students):
        for i in range(0, team_size):
            buf += 1
            if buf == len(students):
                break
            print (students[buf])
        print ("============")

match_teams(5, 3, 2)
