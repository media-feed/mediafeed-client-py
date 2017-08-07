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
    elif args.group_command == 'group':
        if args.command == 'list':
            groups = api.list_groups(root_id=args.root_id, recursive=args.recursive)
            prints.print_groups(groups)
        elif args.command == 'show':
            group = api.get_group(args.id)
            prints.print_group(group)
        elif args.command == 'add':
            group = api.add_group(args.name, parent_id=args.parent_id)
            prints.print_group(group)
        elif args.command == 'edit':
            group = api.edit_group(args.id, parent_id=args.parent_id, name=args.name)
            prints.print_group(group)
        elif args.command == 'remove':
            api.remove_group(args.id)
        else:
            cli.parser_group.print_usage()
    else:
        cli.parser.print_usage()
