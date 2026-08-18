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