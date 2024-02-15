class Student:
    def __init__(self, first_name, last_name, score):
        # Initialize a Student with first name, last name, and score
        self.first_name = first_name
        self.last_name = last_name
        self.score = score

class MaxHeap:
    def __init__(self):
        # Initialize an empty heap
        self.students = []

    def insert(self, student):
        # Add a student to the end of the array
        self.students.append(student)
        # Restore the heap property (max heap) after insertion
        self._heapify_up()

    def remove_max(self):
        if not self.students:
            return None
        if len(self.students) == 1:
            return self.students.pop()
        # Save the student with the highest score (at the root)
        max_student = self.students[0]
        # Replace the root with the last element and restore the heap property
        self.students[0] = self.students.pop()
        self._heapify_down()
        return max_student

    def display(self):
        for student in self.students:
            # Display information for each student
            print(f"{student.first_name} {student.last_name}: {student.score}")

    def _heapify_up(self):
        index = len(self.students) - 1
        while index > 0:
            parent_index = (index - 1) // 2
            # Swap with the parent if the student has a higher score
            if self.students[index].score > self.students[parent_index].score:
                self.students[index], self.students[parent_index] = (
                    self.students[parent_index],
                    self.students[index],
                )
                index = parent_index
            else:
                break

    def _heapify_down(self):
        index = 0
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest = index

            # Determine the index of the left child if it has a higher score
            if (
                left_child_index < len(self.students)
                and self.students[left_child_index].score > self.students[largest].score
            ):
                largest = left_child_index

            # Determine the index of the right child if it has a higher score
            if (
                right_child_index < len(self.students)
                and self.students[right_child_index].score > self.students[largest].score
            ):
                largest = right_child_index

            # Swap with the child (left or right) if necessary and continue downward
            if largest != index:
                self.students[index], self.students[largest] = (
                    self.students[largest],
                    self.students[index],
                )
                index = largest
            else:
                break


class StudentTalentPool:
    def __init__(self):
        self.max_heap = MaxHeap()

    def run(self):
        while True:
            print("\nMenu Options:")
            print("1. Add Student")
            print("2. Remove Highest Scoring Student")
            print("3. Display Students")
            print("4. Exit")
            
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                # Add a new student to the talent pool
                first_name = input("Enter student's first name: ")
                last_name = input("Enter student's last name: ")
                score = float(input("Enter student's score: "))
                new_student = Student(first_name, last_name, score)
                self.max_heap.insert(new_student)
                print("Student added successfully.")
            elif choice == "2":
                # Remove the student with the highest score
                removed_student = self.max_heap.remove_max()
                if removed_student:
                    print(
                        f"Removed highest scoring student: {removed_student.first_name} {removed_student.last_name}"
                    )
                else:
                    print("Talent pool is empty.")
            elif choice == "3":
                # Display all students in the talent pool
                print("\nCurrent Talent Pool:")
                self.max_heap.display()
            elif choice == "4":
                # Exit the program
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    # Create an instance of the program and run it
    talent_pool_program = StudentTalentPool()
    talent_pool_program.run()
