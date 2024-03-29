import numpy as np


class DataSource:

    samples = [
        {
            'dimension': (2, 2),
            'data': [
                ((0, 1), 2),
                ((1, 0), 2),
            ]
        },
        {
            'dimension': (4, 4),
            'data': [
                ((0, 3), 4),
                ((1, 1), 8),
                ((2, 2), 4),
            ]
        },
        {
            'dimension': (5, 5),
            'data': [
                ((0, 0), 2),
                ((1, 2), 2),
                ((1, 4), 4),
                ((2, 2), 3),
                ((2, 3), 2),
                ((3, 1), 4),
                ((3, 3), 2),
                ((4, 0), 4),
                ((4, 3), 2),
            ]
        },
        {
            'dimension': (5, 5),
            'data': [
                ((0, 2), 2),
                ((1, 0), 5),
                ((1, 1), 2),
                ((2, 1), 3),
                ((2, 2), 2),
                ((3, 3), 3),
                ((3, 4), 4),
                ((4, 2), 2),
                ((4, 4), 2),
            ]
        },
        {
            'dimension': (7, 7),
            'data': [
                ((0, 6), 6),
                ((1, 0), 2),
                ((1, 3), 3),
                ((2, 1), 3),
                ((2, 5), 6),
                ((3, 5), 3),
                ((4, 0), 3),
                ((4, 1), 6),
                ((4, 5), 3),
                ((5, 1), 5),
                ((5, 5), 2),
                ((6, 0), 2),
                ((6, 4), 3),
                ((6, 5), 2),
            ]
        },
        {
            'dimension': (7, 7),
            'data': [
                ((0, 2), 3),
                ((0, 4), 2),
                ((1, 2), 5),
                ((2, 1), 3),
                ((3, 1), 2),
                ((3, 3), 4),
                ((3, 4), 4),
                ((3, 6), 4),
                ((4, 2), 2),
                ((4, 6), 2),
                ((5, 0), 2),
                ((5, 1), 2),
                ((5, 2), 2),
                ((5, 5), 6),
                ((6, 1), 2),
                ((6, 4), 2),
                ((6, 5), 2),
            ]
        },
        {
            'dimension': (10, 10),
            'data': [
                ((0, 3), 4),
                ((0, 6), 2),
                ((1, 0), 3),
                ((1, 3), 2),
                ((1, 6), 6),
                ((1, 8), 4),
                ((2, 1), 4),
                ((2, 8), 4),
                ((2, 9), 8),
                ((3, 2), 4),
                ((3, 4), 15),
                ((4, 0), 2),
                ((4, 7), 2),
                ((6, 0), 4),
                ((6, 2), 12),
                ((7, 8), 3),
                ((8, 1), 2),
                ((8, 4), 5),
                ((8, 7), 4),
                ((8, 8), 2),
                ((9, 2), 2),
                ((9, 6), 6),
            ]
        },
        {
            'dimension': (10, 10),
            'data': [
                ((0, 2), 4),
                ((0, 6), 2),
                ((0, 7), 6),
                ((1, 5), 5),
                ((2, 2), 2),
                ((2, 4), 3),
                ((2, 6), 3),
                ((3, 7), 2),
                ((3, 8), 4),
                ((4, 0), 9),
                ((5, 3), 12),
                ((5, 8), 9),
                ((6, 1), 4),
                ((6, 9), 3),
                ((7, 3), 12),
                ((8, 1), 2),
                ((8, 6), 4),
                ((8, 8), 4),
                ((9, 3), 7),
                ((9, 8), 3),
            ]
        },
    ]

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, item):
        return self.samples[item]

    def shape(self, item):
        return self.samples[item]['dimension']

    def data(self, item):
        return self.samples[item]['data']

    def board(self, item):
        d = np.zeros(self.samples[item]['dimension'], dtype=int)
        for coord, value in self.samples[item]['data']:
            d[coord] = value
        return d


if __name__ == "__main__":
    source = DataSource()

    for i in range(len(source)):
        print(source.shape(i), source.data(i), sep='\n')
        print('-' * 20)