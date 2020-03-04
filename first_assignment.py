#input Form for the user
applicant_name = input('Name: ')
gender = input('Gender: ')

opening_remarks = print(f'''
\n
Hello {applicant_name}, thanks for cosidering to apply for a Law Degree at Makerere University.
Plese provide the required information as requested below;''')

subject = input('For subjects, please insert a space between each subject.\nAll three major Subjects: ').split()
marks = input('Respective Marks for main subjects in uppercase: ').split()
subsidiary = input('Subsidiary subject: ')
sub_mark = input('Sub-Aggregates: ')
gp_marks = input('GP marks: ')

#grading for marks
grading = {'A':6, 'B':5, 'C':4, 'D':3, 'E':2, 'O':1, 'F':0}
output = ''

for ch in marks:
    output+=str(grading.get(ch))

a = output[0]
b = output[1]
c = output[2]

a = int(a)
b = int(b)
c = int(c)

#total points
Total_points = a + b + c

#dealing with weights
for_weights = [a, b, c]
for_weights.sort(reverse=True)
top_two_for_weights = (for_weights[0]+for_weights[1])*3
last_for_weights = (for_weights[2])*2

total_weights_main = top_two_for_weights + last_for_weights