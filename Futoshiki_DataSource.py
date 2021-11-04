
class SampleSource:
    raw_data = [
"""
1 0

0 0
""",

"""
1<0
^ v
0>0
""",

"""
0>0
v ^
0<0
""",

"""
0 0<3<0

0 0 0 0
^
0>0 0 0
^
0 0 0<0
""",

"""
0>3 5 1 0

0 2 0 5 0
        ^
0 0 0 0 0

0 5 0 3 0

0 4 3 2<0
""",

"""
0>0 5 0 0

0 2 0 0 0
        ^
0 0 0 0 0

0 0 0 3 0

0 0 0 2<0
""",

"""
0 0<0 0<0
    ^
0 0>0 0 0

0 0 0 0 0

0<0 0 0 0
v ^
0 0 0<0<0
""",

"""
0 3 0>0 0 5 0
        v   ^
0 0 0 0 0 0 0
  ^
4 5 0>0 0 2 7
      v
0 0 0 0 0 0 0
    v       v
2 6 0 0 0 1 3
            ^
0 0 0 0 0 0 0

0 2 0 0<0 3<0
""",

"""
0 0 0 0 0 0 0
^ ^     ^
0 0 0 0 4<0 0
          ^
0 0 0 0 5 0 0
            ^
0 0 0 0 0 0 0

1 0 0 3>0 0<0
    v
6>0 0 0 0>0>0
        ^
0<3>0 0 0 0 7
""",

"""
0 1 0 0 0<0 7<0
^   v v        
0 0 0 0 0<0 0>0
  v            
0>4 0>7 0<0 3 0
        v      
0 0 0 0 0 0 0<0
v             v
0<6 0 2 0 4 0 0
      ^        
0 0 0 0 0 0>0 0
    ^ ^ ^      
0 0 0<0 0 0 0 0

0 0 0 0 0 0 0 3
""",

"""
0 8>0 0<0 0 1 0<5
        ^        
0 1 0<0 0 0 0 0 0
      v          
0 0 0<0 0 0 0 0 0
^     ^ ^   ^    
0 0 0 0 0 0 6<0 0
  v   v          
0 0 0 0 0>0 9 0 0
^             ^  
7 4 8>0 0 0 0>0>0
    v v     v    
0 0<0 0 0 0 0 0 0
              ^  
0 0<0<0 3 0 0 7 1

0 0 4 0 0 0 0>0 7
""",

"""
0 0<0 0>0 0 0 0>0
        v v      
0 7 8 0>3 5 0<0<0
  ^              
0 0 6 0 0>0 0 0 0
v         ^     v
7 0 0 3 0 0 0>0 0
  v             v
0 3 0 0 0 9 0 0<0
      v          
0>0 0>0>0 2 0<0 0
  v     v       v
0 0 0<0 0 0<0 0 0
v   v            
0 0 0 0 0 0 0 0 0
  v           ^  
0<0 7<0<0 0>0 0 0
"""
    ]

    def __iter__(self):
        return iter(self.raw_data)

    def __len__(self):
        return len(self.raw_data)

    def __getitem__(self, item):
        return self.raw_data[item]

    def size(self, i):
        return (len(self.data(i)) + 1) // 2

    def data(self, i):
        return self.raw_data[i].split('\n')[1:-1]

    def grid(self, i):
        return [[int(c) for c in line[::2]] for line in self.data(i)[::2]]

    def constraints(self, i):
        res = []
        for i, line in enumerate(self.data(i)):
            if i % 2:
                for j, c in enumerate(line[::2]):
                    x, y = i // 2, j
                    if c == '^':
                        res.append(((x, y), (x + 1, y)))
                    elif c == 'v':
                        res.append(((x + 1, y), (x, y)))
            else:
                for j, c in enumerate(line[1::2]):
                    x, y = i // 2, j
                    if c == '<':
                        res.append(((x, y), (x, y + 1)))
                    elif c == '>':
                        res.append(((x, y + 1), (x, y)))
        return res


def gene_spaces(grid, constraints):
    size = len(grid)
    spaces = [[{val} if val else set(range(1, size + 1)) for val in row] for row in grid]

    def flatten_size(item):
        return len(item) if isinstance(item, set) else sum((flatten_size(s) for s in item))

    curr_size = flatten_size(spaces)
    while True:
        # unique value constraint for rows and columns
        for x in range(size):
            for y in range(size):
                sp = spaces[x][y]
                if len(sp) == 1:
                    for i in range(size):
                        if i != x:
                            spaces[i][y] -= sp
                        if i != y:
                            spaces[x][i] -= sp

        # constraints defined by assignment
        for low, high in constraints:
            l0, l1, h0, h1 = *low, *high

            min_value = min(spaces[l0][l1])
            spaces[h0][h1] = {v for v in spaces[h0][h1] if v > min_value}

            max_value = max(spaces[h0][h1])
            spaces[l0][l1] = {v for v in spaces[l0][l1] if v < max_value}

        new_size = flatten_size(spaces)
        if new_size >= curr_size:
            break
        curr_size = new_size

    return spaces


if __name__ == "__main__":
    data = SampleSource()
    i = 3
    print(*gene_spaces(data.grid(i), data.constraints(i)), sep="\n")
