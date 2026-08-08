student = {'Sarah':100, 'Hamza':70, 'Ruby': 40, 'Archie': 50, 'julia': 20}
sum = 0
for key, value in student.items():
    sum += value

print (sum/5)
print(max(student.values()))
print(min(student.values()))


