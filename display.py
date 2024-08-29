import customtkinter as ctk

class Page(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.normal_font = ctk.CTkFont(family="Arial", size=17)
        self.title_font = ctk.CTkFont(family="Arial", size=20, weight="bold", underline=True)
        self.button_font = ctk.CTkFont(family="Arial", size=20, weight="bold")

    # Create all frames needed for the page
    def create_frames(self):
        pass

    # Create all widgets needed for the page
    def create_widgets(self):
        pass

    # Create an empty row
    def empty_row(self, row):
        ctk.CTkLabel(self, text="").grid(row=row, column=0, padx=20, pady=20)


class IntroPage(Page):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_frames()
        self.create_widgets()

    def create_frames(self):
        self.sign_in_frame = ctk.CTkFrame(self, height=200)
        self.sign_in_frame.grid(row=1, column=0, padx=20, pady=20)
        self.sign_up_frame = ctk.CTkFrame(self, height=200)
        self.sign_up_frame.grid(row=1, column=1, padx=20, pady=20)
    
    def create_widgets(self):
        self.intro_title = ctk.CTkLabel(self, text="Welcome, if you are new then please sign up", font=self.title_font)
        self.intro_title.grid(row=0, column=0, padx=20, pady=20, columnspan=2)

        # Sign in frame
        self.sign_in_button = ctk.CTkButton(self.sign_in_frame, text="Sign In", font=self.button_font)
        self.sign_in_button.grid(row=3, column=0, padx=20, pady=20)
        self.empty_row(0)
        self.username_entry1 = ctk.CTkEntry(self.sign_in_frame, placeholder_text="Username")
        self.username_entry1.grid(row=1, column=0, padx=20, pady=20)
        self.password_entry1 = ctk.CTkEntry(self.sign_in_frame, placeholder_text="Password", show="*")
        self.password_entry1.grid(row=2, column=0, padx=20, pady=20)

        # Sign up frame
        self.sign_up_button = ctk.CTkButton(self.sign_up_frame, text="Sign Up", font=self.button_font)
        self.sign_up_button.grid(row=4, column=0, padx=20, pady=10)
        self.empty_row(0)
        self.username_entry2 = ctk.CTkEntry(self.sign_up_frame, placeholder_text="Username")
        self.username_entry2.grid(row=1, column=0, padx=20, pady=10)
        self.password_entry2 = ctk.CTkEntry(self.sign_up_frame, placeholder_text="Password", show="*")
        self.password_entry2.grid(row=2, column=0, padx=20, pady=10)
        self.confirm_password_entry = ctk.CTkEntry(self.sign_up_frame, placeholder_text="Confirm Password", show="*")
        self.confirm_password_entry.grid(row=3, column=0, padx=20, pady=10)


class WeatherPage(Page):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_frames()
        self.create_widgets()

    def create_frames(self):
        self.info_frame = ctk.CTkFrame(self, height=200)
        self.info_frame.grid(row=0, column=0, padx=20, pady=20, rowspan=2)
        self.city_frame = ctk.CTkFrame(self, height=200)
        self.city_frame.grid(row=0, column=1, padx=20, pady=20)
        self.recommendations_frame = ctk.CTkFrame(self, height=200)
        self.recommendations_frame.grid(row=1, column=1, padx=20, pady=20)

    def create_widgets(self):
        # Info frame
        self.info_title = ctk.CTkLabel(self.info_frame, text="Weather Info", font=self.title_font)
        self.info_title.grid(row=0, column=0, padx=20, pady=10, columnspan=2)
        self.empty_row(1)
        self.temp_label = ctk.CTkLabel(self.info_frame, text="Temperature: ", font=self.normal_font)
        self.temp_label.grid(row=2, column=0, padx=20, sticky="W")
        self.feels_like_label = ctk.CTkLabel(self.info_frame, text="Feels Like: ", font=self.normal_font)
        self.feels_like_label.grid(row=3, column=0, padx=20, sticky="W")
        self.humidity_label = ctk.CTkLabel(self.info_frame, text="Humidity: ", font=self.normal_font)
        self.humidity_label.grid(row=4, column=0, padx=20, sticky="W")
        self.wind_speed_label = ctk.CTkLabel(self.info_frame, text="Wind Speed: ", font=self.normal_font)
        self.wind_speed_label.grid(row=5, column=0, padx=20, sticky="W")
        self.current_weather = ctk.CTkLabel(self.info_frame, text="Current Weather: ", font=self.normal_font)
        self.current_weather.grid(row=6, column=0, padx=20, sticky="W")
        self.sunset_time = ctk.CTkLabel(self.info_frame, text="Sunset Time: ", font=self.normal_font)
        self.sunset_time.grid(row=7, column=0, padx=20, sticky="W")
        self.sunrise_time = ctk.CTkLabel(self.info_frame, text="Sunrise Time: ", font=self.normal_font)
        self.sunrise_time.grid(row=8, column=0, padx=20, sticky="W")

        # City frame
        self.city_entry = ctk.CTkEntry(self.city_frame, placeholder_text="City")
        self.city_entry.grid(row=0, column=0, padx=20, pady=10)
        self.get_info_button = ctk.CTkButton(self.city_frame, text="Get Weather Info", font=self.button_font)
        self.get_info_button.grid(row=1, column=0, padx=20, pady=10)

        # Recommendations frame
        self.recommendations_title = ctk.CTkLabel(self.recommendations_frame, text="Recommendations", font=self.title_font)
        self.recommendations_title.grid(row=0, column=0, padx=20, pady=10)
        self.hat_recommendation = ctk.CTkLabel(self.recommendations_frame, text="Hat: ", font=self.normal_font)
        self.hat_recommendation.grid(row=1, column=0, padx=20, sticky="W")
        self.umbrella_recommendation = ctk.CTkLabel(self.recommendations_frame, text="Umbrella: ", font=self.normal_font)
        self.umbrella_recommendation.grid(row=2, column=0, padx=20, sticky="W")
        self.coat_recommendation = ctk.CTkLabel(self.recommendations_frame, text="Coat: ", font=self.normal_font)
        self.coat_recommendation.grid(row=3, column=0, padx=20, sticky="W")
        self.sunscreen_recommendation = ctk.CTkLabel(self.recommendations_frame, text="Sunscreen: ", font=self.normal_font)
        self.sunscreen_recommendation.grid(row=4, column=0, padx=20, sticky="W")


class App(ctk.CTk):
    def __init__(self):
        # Set the window up
        super().__init__()
        self.title("Weather App")

        # Create the pages
        self.intro_page = IntroPage(self)
        self.intro_page.pack()
        self.weather_page = WeatherPage(self)

    def change_page(self):
        self.intro_page.pack_forget()
        self.weather_page.pack()

    # Display an error message to the user
    def show_error(self, message):
        self.error_window = ctk.CTkToplevel(fg_color="red")
        self.error_window.title("Error")
        self.error_window._fg_color
        self.error_message = ctk.CTkLabel(self.error_window, text=message)
        self.error_message.pack()
        self.error_window.mainloop()

        

