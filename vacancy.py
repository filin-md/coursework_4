#Класс для представления вакансии
class Vacancy:
    def __init__(self, title, url, salary_from, salary_to, requirements):

        self.title = title
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.requirements = requirements


    def __gt__(self, other):
        return self.salary_from > other.salary_from


    def __str__(self):
        return f'''
                "title": {self.title},
                "url": {self.url},
                "salary_from": {self.salary_from},
                "salary_to": {self.salary_to},
                "requierements": {self.requirements}
                '''

    def __repr__(self):
        return f'{self.title}'
