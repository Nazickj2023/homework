import customtkinter as ctk
from .main_frame import main_window
from ..read_json import read_json
from ..write_json import create_json
import json
import requests

class HorizontalScroll(ctk.CTkScrollableFrame):
    def __init__(self, child_master: object, **kwargs):
        ctk.CTkScrollableFrame.__init__(
            self, 
            master= child_master, 
            width= 820,
            height= 240,
            border_color= "#FFFFFF",
            orientation= "horizontal",
            border_width= 5,
            corner_radius= 20,
            fg_color= '#5DA7B1',
            bg_color= '#5DA7B1',
            label_text= f'Захід сонця о {None}.',
            **kwargs
        )
        self.place(x= 325, y= 430)
    
    def request_forecast_api(self):
        #
        data_api = read_json(name_file= 'config_api.json')
        API_KEY = data_api['api_key']
        CITY_NAME = data_api['city_name']
        CNT = data_api['cnt']
        #
        try:
            # "https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}&units=metric&lang=uk&cnt=3".format(CITY_NAME, API_KEY)
            response = requests.get(url = data_api['config_forecast'].format(CITY_NAME, API_KEY, CNT))
            #
            if response.status_code == 200:
                # data_dict = json.loads(response.content)
                data_dict = response.json()
                create_json(name_file= 'config_forecast.json', name_dict= data_dict)
                print(json.dumps(data_dict, indent= 4))
        except requests.exceptions.RequestException as exception:
            print(f'Error getting weather: {exception}')
            
        


h_scroll= HorizontalScroll(child_master= main_window)
h_scroll.request_forecast_api()