import random
print("Enter the number of friends joining your dinner (including you:")
number_of_people = input()
if int(number_of_people) == 0 or int(number_of_people) < 0:
    print("No one is joining for the party")
else:
    people_joining_party = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for a in range(int(number_of_people)):
        names_of_people = input()
        people_joining_party.update({ names_of_people: 0})
    print(people_joining_party)