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


# Source

parser_source = subparsers.add_parser('source')
parser_source_subparsers = parser_source.add_subparsers(dest='command')


parser_source_metadata = parser_source_subparsers.add_parser('metadata')
parser_source_metadata.add_argument('module_id')
parser_source_metadata.add_argument('url')
parser_source_metadata.add_argument('-o', '--options')


parser_source_list = parser_source_subparsers.add_parser('list')
parser_source_list.add_argument('-g', '--group-id', type=read_int, default=0)
parser_source_list.add_argument('-r', '--recursive', action='store_true', default=False)
parser_source_list.add_argument('--no-recursive', action='store_false', dest='recursive')
parser_source_list.add_argument('-m', '--auto-download-media', action='store_true', default=None)
parser_source_list.add_argument('--no-auto-download-media', action='store_false', dest='auto_download_media')
parser_source_list.add_argument('-t', '--persist-thumbnails', action='store_true', default=None)
parser_source_list.add_argument('--no-persist-thumbnails', action='store_false', dest='persist_thumbnails')
parser_source_list.add_argument('-e', '--error', action='store_true', default=None)
parser_source_list.add_argument('--no-error', action='store_false', dest='error')


parser_source_show = parser_source_subparsers.add_parser('show')
parser_source_show.add_argument('module_id')
parser_source_show.add_argument('id')


parser_source_add = parser_source_subparsers.add_parser('add')
parser_source_add.add_argument('module_id')
parser_source_add.add_argument('url')
parser_source_add.add_argument('--id')
parser_source_add.add_argument('--group-id', type=int)
parser_source_add.add_argument('--options')
parser_source_add.add_argument('--name')
parser_source_add.add_argument('--thumbnail-url')
parser_source_add.add_argument('--web-url')
parser_source_add.add_argument('-m', '--auto-download-media', action='store_true', default=None)
parser_source_add.add_argument('--no-auto-download-media', action='store_false', dest='auto_download_media')
parser_source_add.add_argument('-t', '--persist-thumbnails', action='store_true', default=None)
parser_source_add.add_argument('--no-persist-thumbnails', action='store_false', dest='persist_thumbnails')


parser_source_edit = parser_source_subparsers.add_parser('edit')
parser_source_edit.add_argument('module_id')
parser_source_edit.add_argument('id')
parser_source_edit.add_argument('--group-id', type=read_int, default=0)
parser_source_edit.add_argument('--url')
parser_source_edit.add_argument('--options')
parser_source_edit.add_argument('--name')
parser_source_edit.add_argument('--thumbnail-url')
parser_source_edit.add_argument('--web-url')
parser_source_edit.add_argument('-m', '--auto-download-media', action='store_true', default=None)
parser_source_edit.add_argument('--no-auto-download-media', action='store_false', dest='auto_download_media')
parser_source_edit.add_argument('-t', '--persist-thumbnails', action='store_true', default=None)
parser_source_edit.add_argument('--no-persist-thumbnails', action='store_false', dest='persist_thumbnails')


parser_source_remove = parser_source_subparsers.add_parser('remove')
parser_source_remove.add_argument('module_id')
parser_source_remove.add_argument('id')


parser_source_update = parser_source_subparsers.add_parser('update')
parser_source_update.add_argument('module_id')
parser_source_update.add_argument('id')
parser_source_update.add_argument('--viewed', action='store_true', default=False)
parser_source_update.add_argument('--no-viewed', action='store_false', dest='viewed')


# Item

parser_item = subparsers.add_parser('item')
parser_item_subparsers = parser_item.add_subparsers(dest='command')


parser_item_list = parser_item_subparsers.add_parser('list')
parser_item_list.add_argument('-g', '--groups-id', type=int, action='append', default=[])
parser_item_list.add_argument('-r', '--recursive', action='store_true', default=False)
parser_item_list.add_argument('--no-recursive', action='store_false', dest='recursive')
parser_item_list.add_argument('-s', '--sources_id', action='append', default=[])
parser_item_list.add_argument('-v', '--viewed', action='store_true', default=None)
parser_item_list.add_argument('-n', '--no-viewed', action='store_false', dest='viewed')
parser_item_list.add_argument('-m', '--media', action='store_true', default=None)
parser_item_list.add_argument('--no-media', action='store_false', dest='media')


parser_item_show = parser_item_subparsers.add_parser('show')
parser_item_show.add_argument('module_id')
parser_item_show.add_argument('id')


parser_item_edit = parser_item_subparsers.add_parser('edit')
parser_item_edit.add_argument('module_id')
parser_item_edit.add_argument('id')
parser_item_edit.add_argument('-v', '--viewed', action='store_true', default=None)
parser_item_edit.add_argument('-n', '--no-viewed', action='store_false', dest='viewed')


parser_item_download = parser_item_subparsers.add_parser('download')
parser_item_download.add_argument('module_id')
parser_item_download.add_argument('id')
parser_item_download.add_argument('-o', '--options')


parser_item_remove_media = parser_item_subparsers.add_parser('remove-media')
parser_item_remove_media.add_argument('module_id')
parser_item_remove_media.add_argument('id')
parser_item_remove_media.add_argument('-f', '--filename')
