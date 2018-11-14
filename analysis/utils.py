from .models import Survey

import numpy as np
import pandas as pd


def read_from_excel(path: str):
    df = pd.read_excel(path)
    return df


def insert_surveys(path: str):
    index = ['index', 'name', 'age', 'sex', 'former_occupation', 'desired_occupation1',
             'address', 'desired_salary']
    df = read_from_excel(path)

    for row in df.itertuples():
        kwargs = {}
        for i, value in enumerate(row):
            if pd.isnull(value) or i == 0:
                continue

            elif i == 7:
                kwargs[index[i]] = int(value)
            else:
                kwargs[index[i]] = value

        Survey.objects.create(**kwargs)
