from wrapper import MyWebApp

webApp = MyWebApp('Feedback-System')
app = webApp.app


def main():
    webApp.run()
    print('webApp is running')


if __name__ == '__main__':
    main()
