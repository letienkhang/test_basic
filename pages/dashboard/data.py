# data.py
import os


def get_data():
    image_folder = 'image'

    data_list = [
        {
            'name': 'Search',
            'element': 'input',
            'xpath': 'https://github.com/example1',
            'tags': ['Search', 'Product'],
            'type': 'example_type_1',
            'image': os.path.join(image_folder, 'widget_search.png'),
            'typescreen': 'example_screen_type_1',
            'related': ['Adaptive Exercise Generator', 'AdLlama']
        },
        {
            'name': 'First product',
            'element': 'sayidka',
            'xpath': 'https://github.com/example2',
            'tags': ['Product'],
            'type': 'example_type_2',
            'image': os.path.join(image_folder, 'widget_first_result_search_now.png'),
            'typescreen': 'example_screen_type_2',
            'related': ['Search', 'Agent Neo']
        },
        {
            'name': 'Search',
            'element': 'input',
            'xpath': 'https://github.com/example1',
            'tags': ['Search', 'Product'],
            'type': 'example_type_1',
            'image': os.path.join(image_folder, 'widget_search.png'),
            'typescreen': 'example_screen_type_1',
            'related': ['Adaptive Exercise Generator', 'AdLlama']
        },
        {
            'name': 'First product',
            'element': 'sayidka',
            'xpath': 'https://github.com/example2',
            'tags': ['Product'],
            'type': 'example_type_2',
            'image': os.path.join(image_folder, 'widget_first_result_search_now.png'),
            'typescreen': 'example_screen_type_2',
            'related': ['Search', 'Agent Neo']
        },
        {
            'name': 'Search',
            'element': 'input',
            'xpath': 'https://github.com/example1',
            'tags': ['Search', 'Product'],
            'type': 'example_type_1',
            'image': os.path.join(image_folder, 'widget_search.png'),
            'typescreen': 'example_screen_type_1',
            'related': ['Adaptive Exercise Generator', 'AdLlama']
        },
        {
            'name': 'First product',
            'element': 'sayidka',
            'xpath': 'https://github.com/example2',
            'tags': ['Product'],
            'type': 'example_type_2',
            'image': os.path.join(image_folder, 'widget_first_result_search_now.png'),
            'typescreen': 'example_screen_type_2',
            'related': ['Search', 'Agent Neo']
        },
    ]

    return data_list
