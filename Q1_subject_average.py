import numpy as np

# 4x4 matrix: each row = a student, columns = Math, Science, English, History
student_scores = np.array([
    [78, 85, 72, 90],
    [88, 79, 81, 76],
    [92, 91, 68, 84],
    [65, 87, 75, 80]
])
subjects = ["Math", "Science", "English", "History"]

# Mean of each column (axis=0 goes down the rows)
subject_averages = np.mean(student_scores, axis=0)

print("Average score per subject:")
for subject, avg in zip(subjects, subject_averages):
    print(f"  {subject}: {avg:.2f}")

best = np.argmax(subject_averages)
print(f"Subject with the highest average: {subjects[best]} ({subject_averages[best]:.2f})")
