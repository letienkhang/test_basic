# data.py
import os


def get_data_web():

    data_list = [
        {
            'name': 'Canonical',
            'path': 'pages/canonical/canonical_page.py',
            'tags': ['Canonical', 'Link'],
        },
        {
            'name': 'Index - Follow',
            'path': '/Users/kanglee/PycharmProjects/pythonProject5/pages/sitemap/sitemap.py',
            'tags': ['Index', 'Follow', 'Link'],
        },
        {
            'name': 'Checkout',
            'path': '/Users/kanglee/PycharmProjects/pythonProject5/pages/checkout_basic/main.py',
            'tags': ['Checkout', 'Product'],
        },
        {
            'name': 'Checkout Product Link',
            'path': '/Users/kanglee/PycharmProjects/pythonProject5/pages/checkou_by_link/test.py',
            'tags': ['Checkout', 'Product'],
        },

    ]

    return data_list
