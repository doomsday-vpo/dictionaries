# The force users struggle to remember which side is the different force users from because they switch them too often. So you are tasked to create a web application to manage their profiles. You should store information for every unique force user registered in the application.
# You will receive several input lines in one of the following formats:
# "{force_side} | {force_user}"
# "{force_user} -> {force_side}"
# The "force_user" and "force_side" are strings, containing any character.
# If you receive "force_side | force_user":
# •	If there is no such force user and no such force side -> create a new force side and add the force user to the corresponding side.
# •	Only if there is no such force user in any force side -> add the force user to the corresponding side.
# •	If there is such force user already -> skip the command and continue to the next operation.
# If you receive a "force_user -> force_side":
# •	If there is such force user already -> change their side.
# •	If there is no such force user in any force side -> add the force user to the corresponding force side.
# •	If there is no such force user and no such force side -> create new force side and add the force user to the corresponding side.
# •	Then you should print on the console: "{force_user} joins the {force_side} side!".
# You should end your program when you receive the command "Lumpawaroo". At that point, you should print each force side. For each side, print the force users.
# In case there are no forced users on a side, you shouldn't print the side information.
# Input / Constraints
# •	The input comes in the form of commands in one of the formats specified above.
# •	The input ends when you receive the command "Lumpawaroo".
# Output
# •	As output for each force side, you must print all the force users.
# •	The output format is:
# "Side: {force_side}, Members: {force_users_count}
# ! {force_user1}
# ! {force_user2}
# …
# ! {force_userN}"
# •	In case there are NO force users on a side, don't print this side.


force_sides = {}


def add_user(side, user):

    for force_side in force_sides.values():
        if user in force_side:
            return False


    if side not in force_sides:
        force_sides[side] = []
    force_sides[side].append(user)
    return True


def switch_side(user, new_side):

    for side in force_sides.values():
        if user in side:
            side.remove(user)


    if new_side not in force_sides:
        force_sides[new_side] = []
    force_sides[new_side].append(user)
    print(f"{user} joins the {new_side} side!")


while True:
    command = input()
    if command == "Lumpawaroo":
        break

    if "|" in command:
        side, user = command.split(" | ")
        add_user(side, user)
    elif "->" in command:
        user, side = command.split(" -> ")
        switch_side(user, side)

for side, users in force_sides.items():
    if users:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
