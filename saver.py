import json
from abc import ABC, abstractmethod



#Абстрактный класс для сохранения данных
class Saver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy_object):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


#Класс для сохранения данных в JSON
class JSONSaver(Saver):
    def add_vacancy(self, vacancy_object):

        vacancy_dict = dict(title=vacancy_object.title,
                            url=vacancy_object.url,
                            salary_from=vacancy_object.salary_from,
                            salary_to=vacancy_object.salary_to,
                            requirements=vacancy_object.requirements)

        with open("vacancies.json", "r", encoding="utf-8") as file:
            existing_data = json.load(file)

        existing_data.append(vacancy_dict)

        with open("vacancies.json", "w", encoding="utf-8") as file:
            json.dump(existing_data, file, ensure_ascii=False, indent=4)



    def delete_vacancy(self):
        with open("vacancies.json", "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)