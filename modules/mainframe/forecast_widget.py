import customtkinter as ctk
from .horizontal_scroll import h_scroll
from .weather_image_widget import WeatherImage
from ..read_json import read_json

data_weather = read_json(name_file="config_forecast.json")

class HourlyForecast(ctk.CTkFrame):
    def __init__(self, child_master: object, count: int = 0,  **kwargs):
        ctk.CTkFrame.__init__(
            self,
            master = child_master,
            fg_color= '#5da7b1',
            **kwargs
        )
        #
        self.COUNT = count
        #
        self.grid(row= 0, column = self.COUNT, padx= 20)
        #
        if self.COUNT == 0:
            self.TIME = ctk.CTkLabel(
                master= self,
                text= "Зараз",
                font= ("Arial", 32, "bold")
            )
        else:
            self.TIME = ctk.CTkLabel(
                master= self,
                text= data_weather['list'][self.COUNT]['dt_txt'][11:16],
                font= ("Arial", 32, "bold")
            )
        self.TIME.pack(anchor= 'center')
        #
        self.IMAGE = WeatherImage(
            child_master= self,
            name_json_weather= "config_forecast.json",
            size= (70, 70),
            count= self.COUNT
        )
        self.IMAGE.pack(anchor= 'center', pady= 20)
        #
        self.TEMP = ctk.CTkLabel(
            master= self,
            font= ("Arial", 32, "bold"),
            text= f"{int(data_weather['list'][self.COUNT]['main']['temp'])}°"
        )
        self.TEMP.pack(anchor= 'center', pady= 15)
        #
for el in range(data_weather['cnt']):
    hourly_forecast = HourlyForecast(child_master= h_scroll, count= el)