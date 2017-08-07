from tabulate import tabulate


def print_modules(modules):
    print(tabulate(
        [[
            module['id'],
            module['name'],
            module['media'],
            module['description'],
        ] for module in modules],
        headers=['Id', 'Name', 'Media', 'Description'],
        tablefmt='psql',
    ))


def print_module(module):
    print(tabulate(
        [
            ('id', module['id']),
            ('name', module['name']),
            ('media', module['media']),
            ('description', module['description']),
            ('options', module['options']),
        ],
        headers=['Field', 'Value'],
        tablefmt='psql',
    ))
