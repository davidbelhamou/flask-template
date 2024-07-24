from wrapper import MyWebApp
webapp = MyWebApp('myapp')
app = webapp.app

def main():
    webapp.run()
    print("app is running)

if __name__ == '__main__':
    main()
    
