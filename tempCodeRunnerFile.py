import matplotlib.pyplot as plt
import numpy as np  

students =np.array(["Amit", "Rahul", "Priya", "Sneha", "Arjun","Riya", "Karan", "Anjali", "Rohit", "Neha"])

MATH = np.array([78, 65, 89, 92, 70, 84, 73, 95, 68, 88])
PYTHON = np.array([85, 72, 91, 88, 76, 90, 79, 96, 71, 86])
DBMS = np.array([74, 68, 85, 90, 72, 87, 75, 93, 69, 84])
OS = np.array([80, 70, 88, 91, 75, 89, 77, 94, 72, 85])

#V1
x = np.arange(len(students))
width = 0.2
plt.bar(x - 1.5 * width, MATH, width, label='MATH')
plt.bar(x - 0.5 * width, PYTHON, width, label='PYTHON')
plt.bar(x + 0.5 * width, DBMS, width, label='DBMS')
plt.bar(x + 1.5 * width, OS, width, label='OS')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.grid()
plt.title('Student Performance Analysis')
plt.xticks(x, students, rotation=50)
plt.legend()
plt.show()


#V2
plt.subplot(2, 5, 1)
subjects = np.array(["MATH", "PYTHON", "DBMS", "OS"])
amit_marks = np.array([MATH[0], PYTHON[0], DBMS[0], OS[0]])
x_subjects = np.arange(len(subjects))
plt.plot(x_subjects, amit_marks, marker='o', label='Amit')
plt.xticks(x_subjects, subjects, rotation=50)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Amit's Performance")
plt.grid()
plt.legend()

plt.subplot(2, 5, 2)
subjects = np.array(["MATH", "PYTHON", "DBMS", "OS"])
rahul_marks = np.array([MATH[1], PYTHON[1], DBMS[1], OS[1]])
x_subjects = np.arange(len(subjects))
plt.plot(x_subjects, rahul_marks, marker='o', label='Rahul')
plt.xticks(x_subjects, subjects, rotation=50)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Rahul's Performance")
plt.grid()
plt.legend()

plt.subplot(2, 5, 3)
subjects = np.array(["MATH", "PYTHON", "DBMS", "OS"])
priya_marks = np.array([MATH[2], PYTHON[2], DBMS[2], OS[2]])
x_subjects = np.arange(len(subjects))
plt.plot(x_subjects, priya_marks, marker='o', label='Priya')
plt.xticks(x_subjects, subjects, rotation=50)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Priya's Performance")
plt.grid()
plt.legend()

plt.subplot(2, 5, 4)
subjects = np.array(["MATH", "PYTHON", "DBMS", "OS"])
sneha_marks = np.array([MATH[3], PYTHON[3], DBMS[3], OS[3]])
x_subjects = np.arange(len(subjects))
plt.plot(x_subjects, sneha_marks, marker='o', label='Sneha')
plt.xticks(x_subjects, subjects, rotation=50)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Sneha's Performance")
plt.grid()
plt.legend()


plt.subplot(2, 5, 5)
subjects = np.array(["MATH", "PYTHON", "DBMS", "OS"])
arjun_marks = np.array([MATH[4], PYTHON[4], DBMS[4], OS[4]])
x_subjects = np.arange(len(subjects))
plt.plot(x_subjects, arjun_marks, marker='o', label='Arjun')
plt.xticks(x_subjects, subjects, rotation=50)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Arjun's Performance")
plt.grid()
plt.legend()

plt.subplot(2, 5, 6)
subjects = np.array(["MATH", "PYTHON", "DBMS", "OS"])
Riya_marks = np.array([MATH[5], PYTHON[5], DBMS[5], OS[5]])
x_subjects = np.arange(len(subjects))
plt.plot(x_subjects, Riya_marks, marker='o', label='Riya')
plt.xticks(x_subjects, subjects, rotation=50)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Riya's Performance")
plt.grid()
plt.legend()

plt.subplot(2, 5, 7)
subjects = np.array(["MATH", "PYTHON", "DBMS", "OS"])
karan_marks = np.array([MATH[6], PYTHON[6], DBMS[6], OS[6]])
x_subjects = np.arange(len(subjects))
plt.plot(x_subjects, karan_marks, marker='o', label='Karan')
plt.xticks(x_subjects, subjects, rotation=50)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Karan's Performance")
plt.grid()
plt.legend()

plt.subplot(2, 5, 8)
subjects = np.array(["MATH", "PYTHON", "DBMS", "OS"])
Anjali_marks = np.array([MATH[7], PYTHON[7], DBMS[7], OS[7]])
x_subjects = np.arange(len(subjects))
plt.plot(x_subjects, Anjali_marks, marker='o', label='Anjali')
plt.xticks(x_subjects, subjects, rotation=50)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Anjali's Performance")
plt.grid()
plt.legend()

plt.subplot(2, 5, 9)
subjects = np.array(["MATH", "PYTHON", "DBMS", "OS"])
rohit_marks = np.array([MATH[8], PYTHON[8], DBMS[8], OS[8]])
x_subjects = np.arange(len(subjects))
plt.plot(x_subjects, rohit_marks, marker='o', label='Rohit')
plt.xticks(x_subjects, subjects, rotation=50)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Rohit's Performance")
plt.grid()
plt.legend()

plt.subplot(2, 5, 10)
subjects = np.array(["MATH", "PYTHON", "DBMS", "OS"])
neha_marks = np.array([MATH[9], PYTHON[9], DBMS[9], OS[9]])
x_subjects = np.arange(len(subjects))
plt.plot(x_subjects, neha_marks, marker='o', label='Neha')
plt.xticks(x_subjects, subjects, rotation=50)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Neha's Performance")
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()

#V2 Remake with less line of code using loop
subjects = np.array(["MATH", "PYTHON", "DBMS", "OS"])
x_subjects = np.arange(len(subjects))
plt.figure(figsize=(15, 7))
for i in range(len(students)):

    plt.subplot(2, 5, i + 1)
    student_marks = np.array([
        MATH[i],
        PYTHON[i],
        DBMS[i],
        OS[i]
    ])

    plt.plot(x_subjects, student_marks, marker='o', label=students[i])
    plt.xticks(x_subjects, subjects, rotation=20)
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.title(students[i] + "'s Performance",color='Red')
    plt.grid()
    plt.legend()
plt.tight_layout()
plt.show()

#V3
average_marks = []
for i in range(len(students)):
    avg = (MATH[i] + PYTHON[i] + DBMS[i] + OS[i]) / 4
    average_marks.append(avg)
    print(students[i], ":", avg)
max_avg = max(average_marks)
min_avg = min(average_marks)

max_index = average_marks.index(max_avg)
min_index = average_marks.index(min_avg)

print("Highest:", students[max_index], "-", max_avg)
print("Lowest:", students[min_index], "-", min_avg)

plt.bar(students, average_marks, color='green')
for i in range(len(students)):
    plt.text(i, average_marks[i] + 1,
             str(average_marks[i]),
             ha='center')
plt.xlabel('Students')
plt.ylabel('Average Marks')
plt.title('Average Marks of Students', color='red')
plt.xticks(rotation=45, color='purple')
plt.grid()
plt.tight_layout()
plt.show()

#Subject-wise average
subject_averages = [
    np.mean(MATH),
    np.mean(PYTHON),
    np.mean(DBMS),
    np.mean(OS)
]
for i in range(len(subjects)):
    print(subjects[i], ":", subject_averages[i])
max_subject_avg = max(subject_averages)
min_subject_avg = min(subject_averages)
max_subject_index = subject_averages.index(max_subject_avg)
min_subject_index = subject_averages.index(min_subject_avg)
print()
print("Best Subject:", subjects[max_subject_index], "-", max_subject_avg)
print("Lowest Subject:", subjects[min_subject_index], "-", min_subject_avg)

plt.bar(subjects, subject_averages, color='orange')
for i in range(len(subjects)):
    plt.text(i, subject_averages[i] + 1,
             str(round(subject_averages[i], 2)),
             ha='center')
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.title("Subject-wise Average Marks", color='red')
plt.grid()
plt.tight_layout()
plt.show()