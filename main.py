from display import App
from intro_function import sign_up, sign_in
from weather_function import get_weather

# Implement back end into the front end
def main():
    app = App()
    app.intro_page.sign_up_button.configure(command=lambda: sign_up(app))
    app.intro_page.sign_in_button.configure(command=lambda: sign_in(app))
    app.weather_page.get_info_button.configure(command=lambda: get_weather(app))
    app.mainloop()

if __name__ == "__main__":
    main()
    