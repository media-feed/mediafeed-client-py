from argparse import ArgumentParser


def read_int(value, default=None):
    if value.lower() in {'none', 'null'}:
        return None
    return int(value)


parser = ArgumentParser()
parser.add_argument('--host', metavar='URL', default='http://127.0.0.1:8080/')
subparsers = parser.add_subparsers(dest='group_command')


# Module

parser_module = subparsers.add_parser('module')
parser_module_subparsers = parser_module.add_subparsers(dest='command')


parser_module_list = parser_module_subparsers.add_parser('list')
parser_module_list.add_argument('-u', '--url')
parser_module_list.add_argument('-o', '--options')


parser_module_show = parser_module_subparsers.add_parser('show')
parser_module_show.add_argument('id')


# Group

parser_group = subparsers.add_parser('group')
parser_group_subparsers = parser_group.add_subparsers(dest='command')


parser_group_list = parser_group_subparsers.add_parser('list')
parser_group_list.add_argument('-i', '--root-id', type=int)
parser_group_list.add_argument('-r', '--recursive', action='store_true', default=True)
parser_group_list.add_argument('-n', '--no-recursive', action='store_false', dest='recursive')


parser_group_show = parser_group_subparsers.add_parser('show')
parser_group_show.add_argument('id', type=int)
parser_group_show.add_argument('-r', '--recursive', action='store_true', default=True)
parser_group_show.add_argument('-n', '--no-recursive', action='store_false', dest='recursive')


parser_group_add = parser_group_subparsers.add_parser('add')
parser_group_add.add_argument('name')
parser_group_add.add_argument('-p', '--parent-id', type=read_int)


parser_group_edit = parser_group_subparsers.add_parser('edit')
parser_group_edit.add_argument('id', type=int)
parser_group_edit.add_argument('-p', '--parent-id', type=read_int, default=0)
parser_group_edit.add_argument('-n', '--name')


parser_group_remove = parser_group_subparsers.add_parser('remove')
parser_group_remove.add_argument('id', type=int)
