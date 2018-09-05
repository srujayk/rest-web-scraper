elements = [
    {
        'id': 'search',
        'inputs': [
            {
                'name': 'search_query',
                'clean': cleaners.search_cleaner,
            }
        ],
        'url': 'http://www.fatsecret.com/calories-nutrition/search?q={}',
        'outputs': [
            {
                'name': 'first_result_url',
                'xpath': '//a[@class="prominent"]/@href',
                'li': 0
            }
        ]
    },
    {
        'id': 'nutrition',
        'inputs': [
            {
                'name': 'first_result_url',
                'clean': None,
            }
        ],
        'url': '{first_result_url}',
        'outputs': [
            {
                'name': 'calories',
                'xpath': '//div[@class="factValue"]/text()',
                'li': 0
            },
            {
                'name': 'fat',
                'xpath': '//div[@class="factValue"]/text()',
                'li': 1
            },
            {
                'name': 'carbs',
                'xpath': '//div[@class="factValue"]/text()',
                'li': 0
            },
            {
                'name': 'protein',
                'xpath': '//div[@class="factValue"]/text()',
                'li': 0
            }
        ]
    }
]
