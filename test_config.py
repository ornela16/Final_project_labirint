import configparser

def test_conf():
    config = configparser.ConfigParser()
    config.sections()

    config.read('test_config.ini') #Название файла с конфигурациями

    print(config.sections()) #Печатаем секции конфигурационного файла

    # Вычитаем секцию sectionA — получим значение prop:

def test_conf():
    config = configparser.ConfigParser()
    config.sections()

    config.read('test_config.ini')  # Название файла с конфигурациями
    config.sections()
    sA = config["sectionA"]["prop"]  # Получаем значение переменной prop из секции

# Значения переменной можно привести к другому типу данных с помощью метода getint:


def test_conf():
    config = configparser.ConfigParser()
    config.sections()

    config.read('test_config.ini')
    config.sections()

    prop = config["sectionA"].get("prop") #Строка
    prop_int = config["sectionA"].getint("prop_init") #Число

    print(prop_int / 1)