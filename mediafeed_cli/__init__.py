__version__ = '0.1.dev0'


def main():
    from . import cli, prints
    from .api import Server

    args = cli.parser.parse_args()
    api = Server(args.host)

    if args.group_command == 'module':
        if args.command == 'list':
            modules = api.list_modules(url=args.url, options=args.options)
            prints.print_modules(modules)
        elif args.command == 'show':
            module = api.get_module(id=args.id)
            prints.print_module(module)
        else:
            cli.parser_module.print_usage()
    else:
        cli.parser.print_usage()
