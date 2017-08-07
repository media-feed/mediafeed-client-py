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


def print_source_metadata(source_metadata):
    print(tabulate(
        [
            ('id', source_metadata['id']),
            ('url', source_metadata['url']),
            ('options', source_metadata.get('options')),
            ('name', source_metadata['name']),
            ('thumbnail_url', source_metadata.get('thumbnail_url')),
            ('web_url', source_metadata.get('web_url')),
        ],
        headers=['Field', 'Value'],
        tablefmt='psql',
    ))


def print_sources(sources):
    print(tabulate(
        [[
            source['module_id'],
            source['id'],
            source['group_path_name'],
            source['name'],
            source['web_url'],
            source['last_success_update'],
            source['error'],
        ] for source in sources],
        headers=['Module Id', 'Id', 'Group', 'Name', 'Web URL', 'Update', 'Error'],
        tablefmt='psql',
    ))


def print_source(source):
    print(tabulate(
        [
            ('module_id', source['module_id']),
            ('id', source['id']),
            ('group_id', source['group_id']),
            ('group_path_name', source['group_path_name']),
            ('url', source['url']),
            ('options', source['options']),
            ('name', source['name']),
            ('thumbnail_url', source['thumbnail_url']),
            ('web_url', source['web_url']),
            ('auto_download_media', source['auto_download_media']),
            ('persist_thumbnails', source['persist_thumbnails']),
            ('last_success_update', source['last_success_update']),
            ('last_success_update_timestamp', source['last_success_update_timestamp']),
            ('error', source['error']),
            ('items', len(source['items_id'])),
        ],
        headers=['Field', 'Value'],
        tablefmt='psql',
    ))


def print_items(items):
    print(tabulate(
        [[
            item['module_id'],
            item['id'],
            ', '.join(item['sources_id']),
            item['name'],
            item['datetime'],
            item['viewed'],
            len(item['medias']),
        ] for item in items],
        headers=['Module Id', 'Id', 'Source', 'Name', 'Date', 'Viewed', 'Media'],
        tablefmt='psql',
    ))


def print_item(item):
    print(tabulate(
        [
            ('module_id', item['module_id']),
            ('id', item['id']),
            ('sources_id', ', '.join(item['sources_id'])),
            ('url', item['url']),
            ('datetime', item['datetime']),
            ('timestamp', item['timestamp']),
            ('name', item['name']),
            ('thumbnail_url', item['thumbnail_url']),
            ('media_url', item['media_url']),
            ('viewed', item['viewed']),
        ],
        headers=['Field', 'Value'],
        tablefmt='psql',
    ))
    if item['medias']:
        print('Medias:')
        for media in item['medias']:
            print('  %s' % media)
    if item['text']:
        if item['medias']:
            print()
            print('--------------------------------------------------------------------------------')
        print()
        print(item['text'])
