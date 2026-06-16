#Nakee Hayes
#CIS261
# WK10 VIBE Coding

import os
import sys


FILENAME = "student_grades.txt"


class Student:
	def __init__(self, name: str, student_id: str, test1: float, test2: float, test3: float):
		self.name = name
		self.id = student_id
		self.test1 = float(test1)
		self.test2 = float(test2)
		self.test3 = float(test3)
		self.average = 0.0
		self.grade = ""
		self.calculate()

	def calculate(self):
		self.average = round((self.test1 + self.test2 + self.test3) / 3.0, 2)
		avg = self.average
		if avg >= 90:
			self.grade = "A"
		elif avg >= 80:
			self.grade = "B"
		elif avg >= 70:
			self.grade = "C"
		elif avg >= 60:
			self.grade = "D"
		else:
			self.grade = "F"

	def to_record(self) -> str:
		return f"{self.name}|{self.id}|{self.test1:.2f}|{self.test2:.2f}|{self.test3:.2f}|{self.average:.2f}|{self.grade}\n"

	@staticmethod
	def from_record(line: str):
		parts = line.strip().split("|")
		if len(parts) < 7:
			raise ValueError("Malformed record")
		name, sid, t1, t2, t3, avg, grade = parts[:7]
		# Create student from scores (recalculate to ensure consistency)
		s = Student(name, sid, float(t1), float(t2), float(t3))
		return s


def load_records(filename: str) -> list:
	students = []
	if not os.path.exists(filename):
		return students
	try:
		with open(filename, "r", encoding="utf-8") as f:
			for lineno, line in enumerate(f, start=1):
				line = line.strip()
				if not line:
					continue
				try:
					s = Student.from_record(line)
					students.append(s)
				except Exception:
					print(f"Warning: skipping malformed line {lineno} in {filename}")
	except Exception as e:
		print(f"Error loading file {filename}: {e}")
	return students


def save_records(filename: str, students: list) -> None:
	try:
		with open(filename, "w", encoding="utf-8") as f:
			for s in students:
				f.write(s.to_record())
		print(f"Saved {len(students)} record(s) to {filename}")
	except Exception as e:
		print(f"Error saving to {filename}: {e}")


def add_student_interactive(students: list) -> None:
	print("=" * 50)
	print("Enter student information (press ESC at any prompt to cancel):")
	try:
		name = input("Name: ").strip()
		if name.lower() == "esc":
			print("Cancelled adding student.")
			print("=" * 50)
			return
		sid = input("ID: ").strip()
		if sid.lower() == "esc":
			print("Cancelled adding student.")
			print("=" * 50)
			return
		def get_score(prompt):
			while True:
				val = input(prompt).strip()
				if val.lower() == "esc":
					raise KeyboardInterrupt
				try:
					v = float(val)
					if v < 0 or v > 100:
						print("Enter a score between 0 and 100.")
						continue
					return v
				except ValueError:
					print("Invalid number, try again.")

		t1 = get_score("Test 1 score: ")
		t2 = get_score("Test 2 score: ")
		t3 = get_score("Test 3 score: ")
		s = Student(name, sid, t1, t2, t3)
		students.append(s)
		print(f"Added {name} (ID: {s.id}) with average {s.average:.2f} and grade {s.grade}")
		print("=" * 50)
	except KeyboardInterrupt:
		print("Adding student cancelled.")
		print("=" * 50)


def display_students(students: list) -> None:
	if not students:
		print("No student records to display.")
		return
	header = f"{'Name':20} | {'ID':10} | {'Test1':6} | {'Test2':6} | {'Test3':6} | {'Avg':6} | {'Grade':5}"
	print(header)
	print("-" * len(header))
	for s in students:
		print(f"{s.name:20} | {s.id:10} | {s.test1:6.2f} | {s.test2:6.2f} | {s.test3:6.2f} | {s.average:6.2f} | {s.grade:5}")


def class_statistics(students: list) -> None:
	if not students:
		print("No records for statistics.")
		return
	highest_student = max(students, key=lambda s: s.average)
	lowest_student = min(students, key=lambda s: s.average)
	class_avg = round(sum(s.average for s in students) / len(students), 2)
	print(f"Highest average: {highest_student.average:.2f} ({highest_student.name})")
	print(f"Lowest average:  {lowest_student.average:.2f} ({lowest_student.name})")
	print(f"Class average:   {class_avg:.2f}")


def search_student(students: list) -> None:
	name = input("Enter name to search (case-insensitive): ").strip()
	if name.lower() == "esc":
		print("Search cancelled.")
		return
	matches = [s for s in students if name.lower() in s.name.lower()]
	if not matches:
		print("No students found matching that name.")
		return
	display_students(matches)


def get_single_key():
	"""Read a single keypress from user. Returns the key name or character."""
	try:
		# Windows
		import msvcrt

		ch = msvcrt.getch()
		if ch == b"\x1b":
			return 'ESC'
		try:
			return ch.decode()
		except Exception:
			return ''
	except ImportError:
		# Unix
		import sys
		import termios
		import tty

		fd = sys.stdin.fileno()
		old = termios.tcgetattr(fd)
		try:
			tty.setraw(fd)
			ch = sys.stdin.read(1)
			if ch == '\x1b':
				return 'ESC'
			return ch
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old)


def main():
	print("=" * 50)
	print("Student Grade Calculator")
	print("Using data structure: Student class (Option B)")
	print("=" * 50)
	students = load_records(FILENAME)
	if students:
		print(f"Loaded {len(students)} student(s) from {FILENAME}")

	while True:
		print("\nMenu: (press ESC at any time to exit)")
		print("1. Add new student")
		print("2. Display all students")
		print("3. Search student by name")
		print("4. Class statistics")
		print("5. Save records now")
		print("6. Exit")
		choice = input("Choose an option (1-6) or press ESC: ").strip()
		if choice.lower() == 'esc':
			print("Exiting — saving records...")
			save_records(FILENAME, students)
			break
		if choice == '1':
			add_student_interactive(students)
		elif choice == '2':
			display_students(students)
		elif choice == '3':
			search_student(students)
		elif choice == '4':
			class_statistics(students)
		elif choice == '5':
			print("Saving records...")
			save_records(FILENAME, students)
		elif choice == '6':
			print("Exiting — saving records...")
			save_records(FILENAME, students)
			break
		else:
			print("Invalid choice — please select 1-6 or press ESC.")


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("\nInterrupted — saving records...")
		try:
			save_records(FILENAME, [])
		except Exception:
			pass
