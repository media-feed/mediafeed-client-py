import os
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


def print_groups(groups):
    def make_tree(groups):
        lines = []
        for group in groups:
            lines.append('- %s (id = %s)' % (group['name'], group['id']))
            for source in group['sources_id']:
                lines.append('  * %s' % source)
            lines += ['  ' + line for line in make_tree(group['children'])]
        return lines
    print(os.linesep.join(make_tree(groups)))


def print_group(group):
    print(tabulate(
        [
            ('id', group['id']),
            ('name', group['name']),
            ('parent_id', group['parent_id']),
            ('parent_path_name', group['parent_path_name']),
            ('path_name', group['path_name']),
            ('children_id', ', '.join((str(x) for x in group['children_id']))),
            ('sources_id', ', '.join((str(x) for x in group['sources_id']))),
        ],
        headers=['Field', 'Value'],
        tablefmt='psql',
    ))
