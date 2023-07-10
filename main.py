from api_processor import HeadHunterAPI, SuperJobAPI
from saver import JSONSaver
from vacancy import Vacancy

# Создание экземпляра класса сохранения в JSON файл
json_saver = JSONSaver()
# Очистка существующего файла, или создание пустого
json_saver.delete_vacancy()

def hh_vacancies(keyword):
    '''Функция для вывода вакансий с сайта HeadHunter по ключевому запросу keyword'''
    hh_api = HeadHunterAPI()
    hh_api.get_vacancies(keyword)
    list_of_hh_vacancies = []
    for vacancy in hh_api.vacancies_list:
        title = vacancy['name']
        url = vacancy['alternate_url']
        salary_from = vacancy['salary']['from'] if vacancy['salary'] else None
        salary_to = vacancy['salary']['to'] if vacancy['salary'] else None
        requirements = vacancy['snippet']['requirement']
        list_of_hh_vacancies.append(Vacancy(title, url, salary_from, salary_to, requirements))

    for vacancy in list_of_hh_vacancies:
        print(vacancy)
        json_saver.add_vacancy(vacancy)


def sj_vacancies(keyword):
    '''Функция для вывода вакансий с сайта SuperJob по ключевому запросу keyword'''
    superjob_api = SuperJobAPI()
    superjob_api.get_vacancies(keyword)
    list_of_sj_vacancies = []
    for vacancy in superjob_api.vacancies_list:
        title = vacancy['profession']
        url = vacancy['link']
        salary_from = vacancy['payment_from']
        salary_to = vacancy['payment_to']
        requirements = vacancy['candidat']
        list_of_sj_vacancies.append(Vacancy(title, url, salary_from, salary_to, requirements))

    for vacancy in list_of_sj_vacancies:
        print(vacancy)
        json_saver.add_vacancy(vacancy)



# Функция для взаимодействия с пользователем
def user_interaction():
    keyword = input("Введите ключевое слово для поиска вакансий: ")

    while True:
        platform = int(input("Введите с какой платформы хотите получить вакансии - "
                             "\n1. HeadHunter; "
                             "\n2. SuperJob; "
                             "\n3. C обеих платформ\n"))
        if platform == 1:
            hh_vacancies(keyword)
            break
        elif platform == 2:
            sj_vacancies(keyword)
            break
        elif platform == 3:
            hh_vacancies(keyword)
            sj_vacancies(keyword)
            break
        else:
            print("Неверный ответ. Введите 1, 2 или 3")

#
if __name__ == "__main__":
    user_interaction()
