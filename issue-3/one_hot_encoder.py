from typing import List, Tuple
from unittest import TestCase


class TestEncoder(TestCase):
    def test_pasta(self):
        input_arr = ['Carbonara', 'Boloniese', 'Fettuccine']
        output = [
            ('Carbonara', [0, 0, 1]),
            ('Boloniese', [0, 1, 0]),
            ('Fettuccine', [1, 0, 0]),
        ]
        self.assertEqual(fit_transform(input_arr), output)

    def test_copies(self):
        input_arr = ['Hello world']*10
        output = [('Hello world', [1])]*10
        self.assertEqual(fit_transform(input_arr), output)

    def test_exception(self):
        input_arr = 1
        with self.assertRaises(TypeError):
            fit_transform(input_arr)

    def test_null(self):
        input_arr = []
        self.assertNotEqual(fit_transform(input_arr), [('', [1])])


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows
