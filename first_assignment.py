#input Form for the user
applicant_name = input('Name: ')
gender = input('Gender: ').upper()
if gender != 'M' and gender != 'MALE' and gender != 'F' and gender != 'FEMALE':
    print("""
    Please check gender. Insert as 'M' or 'MALE' for Male,
    'F' or 'FEMALE' for Female.
     """)
    gender = input('Gender: ')

opening_remarks = print(f'''
\n
Hello {applicant_name}, thanks for cosidering to apply for a Law Degree at Makerere University.
Plese provide the required information as requested below;''')

subject = input('For subjects, please insert a space between each subject.\nAll three major Subjects: ').split()
marks = input('Respective Marks for main subjects in uppercase: ').split()
subsidiary = input('Subsidiary subject: ')
sub_mark = input('Sub-Aggregates: ')
gp = input('GP marks: ')

gp  = int(gp)
sub_mark = int(sub_mark)

gp_point = 0
sub_point = 0
gender_point = 0

#for gender point
if gender == 'F' or gender == 'FEMALE':
    gender_point = 1.5
else:
    pass

#for subsidiary
if sub_mark > 0 and sub_mark <= 6:
    sub_point = 1
elif sub_mark > 6:
    pass

#for GP
if gp > 50 and gp <= 100:
    gp_point = 1
elif gp < 50:
    pass

#grading for marks
grading = {'A':6, 'B':5, 'C':4, 'D':3, 'E':2, 'O':1, 'F':0}
output = ''

for ch in marks:
    output+=str(grading.get(ch))

#get individual values from output for calculations
a = output[0]
b = output[1]
c = output[2]

a = int(a)
b = int(b)
c = int(c)

Total_points = a + b + c + gp_point + sub_point + gender_point
Total_points = float(Total_points)

#dealing with weights fron the list
for_weights = [a, b, c]
for_weights.sort(reverse=True)
top_two_for_weights = (for_weights[0]+for_weights[1])*3
last_for_weights = (for_weights[2])*2 + gp_point + gender_point + sub_point

total_weights_main = top_two_for_weights + last_for_weights
total_weights_main = float(total_weights_main)

#results according to form
print('\n')
print('\n')
print(f'''{applicant_name}
Results:
''')
print(str(subject[0]) + ': '+ str(marks[0]))
print(str(subject[1]) + ': '+ str(marks[1]))
print(str(subject[2]) + ': '+ str(marks[2]))
print(subsidiary +': '+ str(sub_mark))
print('GP: ' + str(gp))
print('\nTotal points: ' + str(Total_points))
print('Weights: ' + str(total_weights_main))

if total_weights_main > 35:
    print(f'''
    Congs {applicant_name}. You qualify for the Bsc.LAW pre-entry exam.
    You will be notified on when the exam takes place.
    Thanks
    MGT
    ''')
else:
    print(f'''
    Sorry {applicant_name}. Your results don't match the expected results to enable you to do this course.
    Our Team will contact you about some other courses we would recommend for you. 
    Thanks
    MGT
    ''')
