import customtkinter
from ..read_json import read_json
from .frame_manager import scrollable_frame
from ..request_api import requests_api
import time
import datetime

# dict_label = read_json(name_file="config_weather.json")

# CITY_NAME= dict_label['name']
# CURRENT_TEMP = f"{int(dict_label['main']['temp'])}°"
# MAX_TEMP = f"макс.: {int(dict_label['main']['temp_max'])}°"
# MIN_TEMP = f"мін.: {int(dict_label['main']['temp_min'])}°"
# WEATHER_DESCRIPTION = dict_label['weather'][0]['description'].capitalize()
#
class CityFrame(customtkinter.CTkFrame):
    def __init__(self, child_master: object, count: int= 0, **kwargs):
        customtkinter.CTkFrame.__init__(
            self, 
            master= child_master, 
            width= 250, 
            height= 100, 
            fg_color= "#4599A4",
            border_width= 2,
            border_color= "#FFFFFF",
            corner_radius= 20,
            **kwargs
        )
        self.pack(anchor= "center", expand= True, pady= 20) 
        
        self.COUNT = count
        
        self.LIST_CITY = read_json(name_file= "config_api.json")['city_name']
        self.position_map()
        
        self.dict_label = read_json(name_file= f"config_weather_{self.LIST_CITY[self.COUNT]}.json")
        self.time_city()
        self.CITY_NAME= self.dict_label['name']
        self.CURRENT_TEMP = f"{int(self.dict_label['main']['temp'])}°"
        self.MAX_TEMP = f"макс.: {int(self.dict_label['main']['temp_max'])}°"
        self.MIN_TEMP = f"мін.: {int(self.dict_label['main']['temp_min'])}°"
        self.WEATHER_DESCRIPTION = self.dict_label['weather'][0]['description'].capitalize()
        # 
        self.CURRENT_POSITION = customtkinter.CTkLabel(
            master= self,
            text = self.position_map(),
            font= ('Roboto Slab', 16, 'bold'),
            text_color= '#FFFFFF',
        )
        self.CURRENT_POSITION.place(x = 14, y = 8)
        #
        self.CURRENT_TEMP = customtkinter.CTkLabel(
            master= self,
            text = self.CURRENT_TEMP,
            font=("Roboto Slab", 50, 'bold'),
            text_color= "#FFFFFF",
        )
        self.CURRENT_TEMP.place(x = 160, y = 6)
        #
        self.CITY_NAME = customtkinter.CTkLabel(
            master = self,
            text = self.CITY_NAME,
            font = ("Roboto Slab", 12, "bold"),
            text_color = "#FFFFFF" 
        )
        self.CITY_NAME.place(x = 14, y = 33)
        #
        self.MAX_TEMP = customtkinter.CTkLabel(
            master = self,
            text = self.MAX_TEMP,
            font = ("Roboto Slab", 12, "bold"),
            text_color = "#f7f4f3" 
        )
        self.MAX_TEMP.place(x = 110, y = 65)
        #
        self.MIN_TEMP = customtkinter.CTkLabel(
            master = self,
            text = self.MIN_TEMP,
            font = ("Roboto Slab", 12, "bold"),
            text_color = "#f7f4f3" 
        )
        self.MIN_TEMP.place(x = 175, y = 65)
        #
        self.WEATHER_DESCRIPTION = customtkinter.CTkLabel(
            master = self,
            text = self.WEATHER_DESCRIPTION,
            font = ("Roboto Slab", 12, "bold"),
            text_color = "#f7f4f3" 
        )
        self.WEATHER_DESCRIPTION.place(x = 14, y = 65)
    def position_map(self):
        requests_api(count= self.COUNT)
        if self.COUNT == 0:
            return 'Поточна позиція'
        else:
            return f'{self.LIST_CITY[self.COUNT]}'
    def time_city(self):
        time_city = time.gmtime(self.dict_label['dt'])
        # time_city = datetime.datetime.fromtimestamp(self.dict_label['dt'])
        print(time_city)
        
        


for i in range(8):
    city_frame = CityFrame(child_master= scrollable_frame, count= i)