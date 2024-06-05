class Applicant:
    def __init__(self, age, skill_level):
        self.age = age
        self.skill_level = skill_level

    def __repr__(self):
        return f'Applicant(Age: {self.age}, Skill: {self.skill_level})'

class PriorityQueue:
    def __init__(self):
        self.applicants = []

    def add_applicant(self, applicant):
        self.applicants.append(applicant)
        self.applicants.sort(key=lambda x: (-ord(x.skill_level), x.age))

    def promote_applicant(self, applicant, new_skill_level):
        for a in self.applicants:
            if a == applicant:
                a.skill_level = new_skill_level
                break
        self.applicants.sort(key=lambda x: (-ord(x.skill_level), x.age))

    def pop_best_applicant(self):
        if not self.applicants:
            raise KeyError('No applicants available')
        return self.applicants.pop(0)
    
    def checkskill(self, grade):
        if (ord(grade) < 70 and ord(grade) > 65) or (ord(grade) < 102 and ord(grade) > 97):
            if ord(grade) < 102 and ord(grade) > 97:
                return chr(ord(grade)-32)
            return grade
        return False


if __name__ == "__main__":
    pq = PriorityQueue()

    pq.add_applicant(Applicant(25, 'C'))
    pq.add_applicant(Applicant(22, 'B'))
    pq.add_applicant(Applicant(30, 'F'))
    pq.add_applicant(Applicant(22, 'E'))
    pq.add_applicant(Applicant(22, 'E'))
    pq.add_applicant(Applicant(22, 'C'))

    while True:
        print("\nCommands:\n1.add applicant\n2.promote applicant\n3.pop best applicant\n4.exit\n")
        command = int(input("Enter Command: "))
        if command == 4:
            break
        elif command == 1:
            age = int(input("enter age: "))
            skill = input("Enter skill grade: ")
            if pq.checkskill(skill):
                pq.add_applicant(Applicant(age,pq.checkskill(skill)))
            else:
                print("Invalid Grade\n")
            print(pq.applicants)
        elif command == 2:
            print(pq.applicants)
            app = int(input("Which applicant: "))
            grade = input("To Which Grade: ")
            if pq.checkskill(grade):
                pq.promote_applicant(pq.applicants[app-1],pq.checkskill(grade))
            else:
                print("Invalid Grade\n")
            print(pq.applicants)
        elif command == 3:
            best_applicant = pq.pop_best_applicant()
            print(f'Best applicant: Age {best_applicant.age}, Skill Level {best_applicant.skill_level}')
            print(pq.applicants)
        else:
            print("Invalid command!!!\n")
