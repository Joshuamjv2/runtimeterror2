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
