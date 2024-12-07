# Judge statistics on the last Programming Fundamentals exam were not working correctly, so you have the task of taking all the submissions and analyzing them properly. You should collect all the submissions and print the final results and statistics about each language in which the participants submitted their solutions.
# You will be receiving lines in the following format: "{username}-{language}-{points}" until you receive "exam finished". You should store each username and their submissions and points. If a student has two or more submissions for the same language, save only his maximum points.
# You can receive a command to ban a user for cheating in the following format: "{username}-banned". In that case, you should remove the user from the contest but preserve his submissions in the total count of submissions for each language.
# After receiving the "exam finished", print each of the participants in the following format:
# "Results:
# {username1} | {points}
# {username2} | {points}
# …
# {usernameN} | {points}"
# After that, print each language used in the exam in the following format:
# "Submissions:
# {language1} - {submissions_count}
# {language2} - {submissions_count}
# …
# {language3} - {submissions_count}"
# Input / Constraints
# Until you receive "exam finished" you will be receiving participant submissions in the following format: "{username}-{language}-{points}"
# You can receive a ban command -> "{username}-banned"
# The points of the participant will always be a valid integer in the range [0-100];
# Output
# •	Print the exam results for each participant
# •	After that, print each language in the format shown above
# •	Allowed working time / memory: 100ms / 16MB


student_points = {}
language_submissions = {}
banned_users = set()

while True:
    entry = input()
    if entry == "exam finished":
        break

    data = entry.split("-")
    if len(data) == 3:
        username, language, points = data
        points = int(points)


        if username not in student_points:
            student_points[username] = {}
        if language not in student_points[username]:
            student_points[username][language] = points
        else:
            student_points[username][language] = max(student_points[username][language], points)


        if language not in language_submissions:
            language_submissions[language] = 0
        language_submissions[language] += 1

    else:
        username = data[0]
        banned_users.add(username)


print("Results:")
for username, languages in student_points.items():
    if username not in banned_users:
        max_points = max(languages.values())
        print(f"{username} | {max_points}")

print("Submissions:")
for language, count in language_submissions.items():
    print(f"{language} - {count}")
