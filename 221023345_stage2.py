print("Enter the number of friends joining (including you):")
number_of_people = input()
if int(number_of_people) == 0 or int(number_of_people) < 0:
    print("No one is joining for the party")
else:
    people_joining_party = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for a in range(int(number_of_people)):
        names_of_people = input()
        people_joining_party.update({ names_of_people: 0})
    print("Enter the total bill value:")
    bilamount = input()
    names_of_friends = list(people_joining_party.keys())
    bill_amount_for_every_one = float(float(bilamount) / int(number_of_people))
    for b in names_of_friends:
        people_joining_party.update({b: round(bill_amount_for_every_one, 2)})
    print(people_joining_party)