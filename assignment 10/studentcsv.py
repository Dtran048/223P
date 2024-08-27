import csv

in_path = 'stu.csv'
out_path = 'output.txt'

with open(in_path, 'r', newline = '') as inputfile, open(out_path, 'w', newline = '') as writerFile:
    read_file = csv.reader(inputfile)
    write_file = csv.writer(writerFile, delimiter=',', quoting= csv.QUOTE_MINIMAL)
    row_counter = -1
    stu_list = []
    for row in read_file:
        stu_list.append(row)
        row_counter +=1
    print(f'There are {row_counter} students. ' )
    for i in range(9,13):
        row_counter = 0
        age = 0
        for row in stu_list:
            if row[3] == f'{i}th':
                age += int(row[1])
                row_counter +=1
        if row_counter != 0:
            age = age/row_counter
        print(f'the average age in {i}th grade is {age} years old.')

with open('10th_graders.csv', mode = 'w') as student_file:
    student_writer = csv.writer(student_file, delimiter = ',', quoting = csv.QUOTE_MINIMAL)
    for row in stu_list:
        if row[3] == f'10th':
            student_writer.writerow([row[0], row[5]])
