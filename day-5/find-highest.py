student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

#highest=max(student_scores)
#print(highest)

find_highest=0
for high in student_scores:
    if high > find_highest:
        find_highest=high

print(find_highest)


