# -*- coding: utf-8 -*-

import ckan.plugins as plugins
import ckan.plugins.toolkit as tk


def get_biggest_groups(n):
    """Returns the n biggest groups, to display on start page."""
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    data_dict = {
        'all_fields': True,
    }
    groups = tk.get_action('group_list')(context, data_dict)
    if len(groups) > n:
        return sorted(groups, key=lambda group: group['packages'])[-1:-(n+1):-1]
    else:
        return sorted(groups, key=lambda group: group['packages'])[::-1]


def get_newest_groups():
    """Returns the n most recently updated groups, to display on start page."""
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    data_dict = {
        'all_fields': True,
    }
    groups = tk.get_action('group_list')(context, data_dict)
    if len(groups) > n:
        return sorted(groups, key=lambda group: group['packages'])[-1:-(n+1):-1]
    else:
        return sorted(groups, key=lambda group: group['packages'])[::-1]


def get_newest_datasets():
    pass


def get_most_used_datasets():
    pass


class SocialSciThemePlugin(plugins.SingletonPlugin, tk.DefaultDatasetForm):

    plugins.implements(plugins.IConfigurer, inherit=False)
    plugins.implements(plugins.ITemplateHelpers, inherit=False)

    def update_config(self, config):
        tk.add_template_directory(config, 'templates')
        tk.add_public_directory(config, 'public')

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
            'get_biggest_groups': get_biggest_groups
        }
