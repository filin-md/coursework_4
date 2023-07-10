import json
from pprint import pprint

import requests

from abc import ABC, abstractmethod


#Абстрактный класс для работы с API
class PlatformApi(ABC):
    @abstractmethod
    def get_vacancies(self, keyword):
        pass


#Класс для работы с API SuperJob
class SuperJobAPI(PlatformApi):
    def __init__(self):
        self.vacancies_list = []

    def get_vacancies(self, keyword):
        headers = {
                      "X-Api-App-Id": "v3.r.137669675.66af09a8c7959642ffb7fe36dab7b9876095fd8e.0309adb76158cfc4b83762728168b29390c8a5ca"
        }

        for page in range(1):
            params = {
                "keyword": keyword,
                "page": page,
                "count": "100",
            }
            resp = requests.get("https://api.superjob.ru/2.0/vacancies/",
                                params=params,
                                headers=headers).json()
            for vacancy in resp['objects']:
                self.vacancies_list.append(vacancy)



#Класс для работы с API HeadHunter
class HeadHunterAPI(PlatformApi):
    def __init__(self):
        self.vacancies_list = []

    def get_vacancies(self, keyword):
        for page in range(1):
            url = "https://api.hh.ru/vacancies"
            params = {
                "per_page": 100,
                "page": page,
                "text": keyword,
                "archived": False,
            }

            result = requests.get(url, params=params).json()
            for vacancy in result["items"]:
                self.vacancies_list.append(vacancy)

