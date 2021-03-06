# -*- coding: utf-8 -*-

import ckan.plugins as plugins
import ckan.plugins.toolkit as tk


def get_biggest_groups(n):
    """Returns the n biggest groups, to display on start page."""
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    data_dict = {
        'all_fields': True,
        'sort': 'packages'
    }
    groups = tk.get_action('group_list')(context, data_dict)
    if len(groups) > n:
        return groups[-1:-(n+1):-1]
    else:
        return groups[::-1]


def get_newest_groups(n):
    """Returns the n most recently updated groups, to display on start page."""
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    data_dict = {
        'all_fields': True,
    }
    groups = tk.get_action('group_list')(context, data_dict)

    # The group_list action does not return an updated/created date for the groups.
    # This is probably super slow but let's try it.
    for group in groups:
        data_dict = {
            'id': group['id']
        }
        group['last_revision'] = tk.get_action('group_revision_list')(context, data_dict)[0]['timestamp']

    if len(groups) > n:
        return sorted(groups, key=lambda group: group['last_revision'])[-1:-(n+1):-1]
    else:
        return sorted(groups, key=lambda group: group['last_revision'])[::-1]


def get_popular_datasets(n):
    """Returns the n most viewed datasets, to display on start page."""
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    data_dict = {
        'sort': 'views_total desc',
        'q': 'type:dataset'
    }
    datasets = tk.get_action('package_search')(context, data_dict)['results']
    if len(datasets) > n:
        return datasets[-1:-(n+1):-1]
    else:
        return datasets[::-1]


def get_newest_datasets(n):
    """Returns the n most recently created datasets, to display on start page."""
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    data_dict = {
        'sort': 'metadata_created desc',
        'q': 'type:dataset'
    }
    datasets = tk.get_action('package_search')(context, data_dict)['results']
    if len(datasets) > n:
        return datasets[-1:-(n+1):-1]
    else:
        return datasets[::-1]


class SocialSciThemePlugin(plugins.SingletonPlugin, tk.DefaultDatasetForm):

    plugins.implements(plugins.IConfigurer, inherit=False)
    plugins.implements(plugins.ITemplateHelpers, inherit=False)

    def update_config(self, config):
        tk.add_template_directory(config, 'templates')
        tk.add_public_directory(config, 'public')
        tk.add_resource('fanstatic', 'socialscitheme')

    def get_helpers(self):
        return {}

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []

    def get_helpers(self):
        return {
            'get_biggest_groups': get_biggest_groups,
            'get_newest_groups': get_newest_groups,
            'get_popular_datasets': get_popular_datasets,
            'get_newest_datasets': get_newest_datasets
        }
