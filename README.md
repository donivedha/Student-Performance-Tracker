
# Student Performance Tracker

This project is a simple application to track student performance in terms of marks, attendance, and eligibility to sit for exams. The program collects the following data for 5 subjects:
- Marks (out of 100)
- Attendance (in percentage)

It calculates the student's **CGPA** as the average of marks and checks if the student is allowed to sit for exams based on attendance.

## Features
- Input marks and attendance for 5 subjects.
- Calculate CGPA as the average of marks.
- Check if the student is allowed to sit for exams based on attendance (75% attendance required for each subject).
- Saves the student's data in a SQLite database.

## How to Use
1. Clone the repository or download the source code files.
2. Open the `student_performance_tracker_app.py` file in any Python IDE or text editor.
3. Run the program.
4. Enter the student's name, marks for 5 subjects, and attendance for each subject (in percentage).
5. The program will calculate the CGPA and display if the student is allowed to sit for exams based on their attendance.
6. The data is automatically saved to a local SQLite database (`students.db`).

## Example Input
```
Enter Student Name: John Doe
Enter marks for 5 subjects (out of 100):
Subject 1 Marks: 85
Subject 2 Marks: 90
Subject 3 Marks: 78
Subject 4 Marks: 88
Subject 5 Marks: 92

Enter attendance for 5 subjects (in percentage):
Subject 1 Attendance: 80
Subject 2 Attendance: 75
Subject 3 Attendance: 70
Subject 4 Attendance: 85
Subject 5 Attendance: 90
```

## Example Output
```
Student: John Doe
CGPA: 86.6
Allowed for Exam: No
```

## Requirements
- **Python 3.x** (Tkinter and SQLite are included by default in Python installations).

## Contributing
Feel free to fork this project and submit pull requests with improvements or bug fixes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
