PERCENT_PRODUCT = [
    "товар", "телевизор", "пылесос", "велосипед", 'компьютер'
    "стол", "стул", "чай", "аквариум", "компьютер", "мотоцикл",
    "телефон", "блендер",
]

PERCENT_TASKS = dict(
    A=[
        dict(
            question="""вычислите {perc}% от числа {num}"""
        ),
    ],
    B=[
        dict(
            question="""найдите число, {perc}% которого равняется {num}"""
        ),
        dict(
            question="""число {num} составляет {perc}% от некого числа, найдите его"""
        ),
        dict(
            question="""{num} это {perc}% от неизвестного числа, чему равно все число ?"""
        )
    ],
    C=[
        dict(
            question="""сколько число {num_1} составляет процентов от числа {num_2}"""
        )
    ],
    D=[
        dict(
            question="""{name} стоит {cost_old}$. После повышения цены {name} стоит
            {cost_new}$. На сколько процентов увеличилась цена ?""",
            meta="price up"
        ),
        dict(
            question="""цена {name}а {cost_old}$. После подорожания {name}а его
            стоимость составляет {cost_new}$. На сколько процентов увеличилась цена ?""",
            meta="price up"
        ),
        dict(
            question="""{name} стоит {cost_old}$. После скидки новая цена {name}а
            составляет {cost_new}$. На сколько процентов снизилась цена {name}а ?""",
            meta="price down"
        ),
        dict(
            question="""{name} стоил {cost_old}$ до скидки и {cost_new}$ после скидки.
            На сколько процентов снизилась цена {name}а ?""",
            meta="price down"
        ),
        # dict(
        #     question="""цена {name}а была снижена на {}% а затем еще на {}%.
        #     После скидок {name} стоит {}$. Сколько стоил {name} до скидки ?""",
        #     meta="price down"
        # )
    ]



    # perc_9="""цена {name}а после снижения цены на {}% составляет {}%.
    # Сколько стоили {name}а до скидки ?"""
)

PERCENT = dict(
    PERCENT_PRODUCT=PERCENT_PRODUCT,
    PERCENT_TASKS=PERCENT_TASKS
)
