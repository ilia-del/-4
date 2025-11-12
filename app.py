# დავალება 4

class Student:
    def __init__(self, name, age, subjects):
        self.name = name
        self.age = age
        self.subjects = subjects

    def add_subject(self, subject):
        self.subjects.append(subject)

    def get_info(self):
        return f"{self.name} is {self.age} and studies: {', '.join(self.subjects)}"


# --- ა) List ---
students = []

# უკვე გვაქვს
alice = Student("Alice", 15, ["Math", "Science"])
students.append(alice)

# 1. დავამატოთ კიდევ 3 სტუდენტი
bob = Student("Bob", 16, ["History", "Math"])
carol = Student("Carol", 15, ["Art", "Science"])
dave = Student("Dave", 17, ["Physics", "Chemistry"])

students.extend([bob, carol, dave])

# 2. სტუდენტების რაოდენობა
print("სტუდენტების რაოდენობა:", len(students))

# 3. წაშალოთ სტუდენტი სახელით (მაგალითად Bob)
students = [s for s in students if s.name != "Bob"]
print("Bob წაიშალა. ახალი სია:", [s.name for s in students])


# --- ბ) Dictionary ---
grades = {}

# 1–2. დავამატოთ თითოეულისთვის ნიშანი
grades["Alice"] = {"grade": 9, "subjects": alice.subjects}
grades["Carol"] = {"grade": 8, "subjects": carol.subjects}
grades["Dave"] = {"grade": 10, "subjects": dave.subjects}

# 3. განვაახლოთ ერთი ნიშანი (მაგალითად Carol)
grades["Carol"]["grade"] = 9

# 4. გადავუაროთ და დავპრინტოთ ფორმატირებულად
for name, info in grades.items():
    print(f"{name} has grade {info['grade']} and studies {', '.join(info['subjects'])}")


# --- გ) Tuples ---
schedule = ("Math", "Lunch", "Science", "Gym")

# 2. მეორე ელემენტი
print("მეორე ელემენტი:", schedule[1])

# 3. შეცვლის მცდელობა (გაჩვენებს შეცდომას)
try:
    schedule[1] = "Break"
except TypeError as e:
    print("შეცდომა:", e)


# --- დ) Sets ---
classes = {"Robotics", "Debate", "Art"}

# 2. დავამატოთ ახალი გაკვეთილი (დუპლიკატით)
classes.add("Music")
classes.add("Art")  # დუპლიკატი, არაფერი შეიცვლება
print("გაკვეთილები:", classes)

# 3. შემოწმება
print("Art არის სეტში?", "Art" in classes)
print("Biology არის სეტში?", "Biology" in classes)

# 4. საერთო გაკვეთილები
morning_classes = {"Math", "Science", "Robotics"}
afternoon_classes = {"Art", "Robotics", "History"}
print("საერთო გაკვეთილები:", morning_classes & afternoon_classes)