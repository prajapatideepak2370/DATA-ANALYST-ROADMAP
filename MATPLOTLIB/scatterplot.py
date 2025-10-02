import matplotlib.pyplot as plt

studies_hr = [1,2,3,4,5]
exam_scored = [56,75,79,86,99]

plt.scatter(studies_hr,exam_scored, color='red', marker='o')
plt.title("Relationship Between Study hours and Exam scores")
plt.xlabel('Study Hours')
plt.ylabel('Exam Scores')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend(['Exam Scores'], loc='upper left')
plt.show()
plt.close()