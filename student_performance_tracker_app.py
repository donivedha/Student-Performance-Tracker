
import tkinter as tk
from tkinter import messagebox
import sqlite3

class Student:
    def __init__(self, name):
        self.name = name
        self.attendance = [0] * 5
        self.marks = [0] * 5
        self.cgpa = 0.0

    def calculate_cgpa(self):
        total_marks = sum(self.marks)
        self.cgpa = total_marks / 5

    def is_allowed_for_exam(self):
        return all(att >= 75 for att in self.attendance)


class StudentPerformanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Performance Tracker")

        # Database setup
        self.conn = sqlite3.connect("students.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT,
                marks TEXT,
                attendance TEXT,
                cgpa REAL,
                allowed_exam TEXT
            )
        ''')
        self.conn.commit()

        # UI components
        self.name_label = tk.Label(root, text="Enter Student Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        self.marks_entries = []
        self.attendance_entries = []

        for i in range(5):
            tk.Label(root, text=f"Subject {i+1} Marks:").grid(row=i+1, column=0)
            marks_entry = tk.Entry(root)
            marks_entry.grid(row=i+1, column=1)
            self.marks_entries.append(marks_entry)

            tk.Label(root, text=f"Subject {i+1} Attendance:").grid(row=i+1, column=2)
            attendance_entry = tk.Entry(root)
            attendance_entry.grid(row=i+1, column=3)
            self.attendance_entries.append(attendance_entry)

        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate_results)
        self.calculate_button.grid(row=6, column=0, columnspan=4)

    def calculate_results(self):
        name = self.name_entry.get()
        if not name:
            messagebox.showerror("Error", "Please enter the student's name.")
            return

        student = Student(name)

        try:
            for i in range(5):
                student.marks[i] = float(self.marks_entries[i].get())
                student.attendance[i] = float(self.attendance_entries[i].get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for marks and attendance.")
            return

        student.calculate_cgpa()
        allowed_for_exam = student.is_allowed_for_exam()

        # Save to database
        self.cursor.execute('''
            INSERT INTO students (name, marks, attendance, cgpa, allowed_exam)
            VALUES (?, ?, ?, ?, ?)
        ''', (student.name, str(student.marks), str(student.attendance), student.cgpa,
              'Yes' if allowed_for_exam else 'No'))
        self.conn.commit()

        # Display results
        result_message = f"Student: {student.name}
"
        result_message += f"CGPA: {student.cgpa}
"
        result_message += f"Allowed for Exam: {'Yes' if allowed_for_exam else 'No'}"
        messagebox.showinfo("Results", result_message)


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentPerformanceApp(root)
    root.mainloop()
