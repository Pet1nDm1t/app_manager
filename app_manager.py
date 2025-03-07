class App:    
    def __init__(self, name, url, description):
        self.name = name
        self.description = description
        self.url = url


def addApp():
    print('Введите название приложения:')
    name = input()
    print('Введите описание приложения:')
    description = input()
    print('Введите url приложения:')
    url = input()
    app = App(name, url, description)
    return app






addApp()