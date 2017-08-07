from argparse import ArgumentParser


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
