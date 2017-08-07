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
    elif args.group_command == 'source':
        if args.command == 'metadata':
            source_metadata = api.get_source_metadata(args.module_id, args.url, options=args.options)
            prints.print_source_metadata(source_metadata)
        elif args.command == 'list':
            sources = api.list_sources(group_id=args.group_id, recursive=args.recursive, auto_download_media=args.auto_download_media, persist_thumbnails=args.persist_thumbnails, error=args.error)
            prints.print_sources(sources)
        elif args.command == 'show':
            source = api.get_source(args.module_id, args.id)
            prints.print_source(source)
        elif args.command == 'add':
            source = api.add_source(args.module_id, args.url, id=args.id, group_id=args.group_id, options=args.options, name=args.name, thumbnail_url=args.thumbnail_url, web_url=args.web_url, auto_download_media=args.auto_download_media, persist_thumbnails=args.persist_thumbnails)
            prints.print_source(source)
        elif args.command == 'edit':
            source = api.edit_source(args.module_id, args.id, group_id=args.group_id, url=args.url, options=args.options, name=args.name, thumbnail_url=args.thumbnail_url, web_url=args.web_url, auto_download_media=args.auto_download_media, persist_thumbnails=args.persist_thumbnails)
            prints.print_source(source)
        elif args.command == 'remove':
            api.remove_source(args.module_id, args.id)
        elif args.command == 'update':
            api.update_source(args.module_id, args.id, viewed=args.viewed)
        else:
            cli.parser_source.print_usage()
    else:
        cli.parser.print_usage()
