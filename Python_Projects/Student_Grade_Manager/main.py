class StudentGradeManager():
    def __init__(self, name: str, subject: str, score: int):

        self.__student_list: list = []
        self.__subject_list: list = ['Math', 'Science']
        self.__name: str = name.capitalize()
        self.__subject: str = subject.capitalize()
        self.validate_subject()
        self.__score: int = score
        self.validate_score()
        self.__grade: str = self.score_grader()

        #adding to student records
        self.student_record()

    @property
    def score_getter(self):
        return self.__score

    @score_getter.setter
    def score_setter(self):
        while True:
            try:
                self.__score = int(input('Enter new score'))
                if self.__score not in range(0, 101) or not self.score:
                    raise ValueError('Score not in range(0-100)')
                return
            except ValueError as e:
                print(e)

    def validate_score(self):
        if self.__score in range(0, 101):
            return
        self.score_setter()

    @property
    def subject_getter(self):
        return self.__subject

    @subject_getter.setter
    def subject_setter(self):
        print('Select a subject from this list')
        for i, subject in enumerate(self.__subject_list, start=1):
            print(f'{i}: {subject}')

        num = int(input('Enter subject number'))
        self.__subject = self.__subject_list[num-1]

    def validate_subject(self):
        try:
            if self.__subject in self.__subject_list:
                return
            self.subject_setter()
        except Exception as e:
            print(f'Error validating subject: {e}')

    def score_grader(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 80:
            return 'B'
        elif self.__score >= 70:
            return 'C'
        elif self.__score >= 60:
            return 'D'
        else:
            return 'F'

    def student_record(self):
        self.__student_list.append(
            {
                'name': self.__name,
                'subject': self.__subject,
                'score': self.__score,
                'grade': self.__grade
            }
        )

    def view_all_record(self):
        try:
            if not self.__student_list:
                print("No records found.")
                return
            for student in self.__student_list:
                print(f"Name: {student['name']} | Subject: {student['subject']} "
                      f"| Score: {student['score']} | Grade: {student['grade']}\n")
        except Exception as e:
            print(f"Error viewing records: {e}")

    def student_report(self, name: str):
        name = name.capitalize()

        records = [
            student for student in self.__student_list if student['name'] == name
        ]

        if not records:
            print(f'No records found for {name}')
            return
        
        total_score: int = sum(student['score'] for student in records)
        subject_count: int = len(records)

        for record in records:
                print(f"Name: {record['name']} | Subject: {record['subject']} "
                    f"| Score: {record['score']} | Grade: {record['grade']}\n")
            
        print(f'{name}\'s Average Score: {total_score/subject_count:.2f}')

    
