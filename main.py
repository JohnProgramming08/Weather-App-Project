from display import App
from intro_function import sign_up

# Testing Purposes
def main():
    app = App()
    app.intro_page.sign_up_button.configure(command=lambda: sign_up(app))
    app.mainloop()

if __name__ == "__main__":
    main()
    