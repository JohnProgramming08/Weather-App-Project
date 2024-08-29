from display import App
from intro_function import sign_up, sign_in

# Testing Purposes
def main():
    app = App()
    app.intro_page.sign_up_button.configure(command=lambda: sign_up(app))
    app.intro_page.sign_in_button.configure(command=lambda: sign_in(app))
    app.mainloop()

if __name__ == "__main__":
    main()
    