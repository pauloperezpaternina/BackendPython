def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Paulo", "lastname": "Perez"}

    super_list = [
        {"firstname": "Paulo", "lastname": "Perez"},
        {"firstname": "Javier", "lastname": "Paternina"},
        {"firstname": "Ana", "lastname": "Doe"},
        {"firstname": "Ingris", "lastname": "Vega"},
        {"firstname": "Paula", "lastname": "Perez"},
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for dict in super_list:
        print(dict)
        for key, value in dict.items():
            print(key, ":", value)

if __name__ == '__main__':
    run()