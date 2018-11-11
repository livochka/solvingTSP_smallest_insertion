class Table:
    """
    Represents 2D table with distances between each any two cities
    """

    def __init__(self, data):
        self.data = self.generate(data)

    def generate(self, data):
        """
        Generating 2D table with distances
        data: list [x, y] coordinates of cities
        return: 2D list
        """
        table = []
        for city in range(len(data)):
            city_table = []
            for city2 in range(len(data)):
                if city2 != city:
                    city_table.append(self.distance(data[city], data[city2]))
                else:
                    city_table.append(0)
            table.append(city_table)
        return table

    def length(self):
        """
        return: the length of table
        """
        return len(self.data[0])

    def height(self):
        """
        return: the height of table
        """
        return len(self.data)

    @staticmethod
    def distance(c1, c2):
        """
        list, list -> float
        c1: [x, y] of city1
        c2: [x, y] of city2
        return: the distance between c1 and c2
        """
        return ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2) ** (1 / 2)

    def __str__(self):
        view = " ".join([str(i) for i in range(self.length())])
        for i in range(self.height()):
            view += "\n" + str(i) + " " + " ".join([str(n) for n in self.data[i]])
        return view

    def find_route_len(self, path):
        """
        Find the length of path
        path: list with indexes of cities
        return: route length
        """
        route_length, start = 0, path[0]
        for end in range(1, len(path)):
            route_length += self.data[start][path[end]]
            start = path[end]
        try:
            route_length += self.data[path[0]][end]
        except NameError:
            pass
        return route_length

    def find_nearest_unvisited(self, city, visited):
        """
        Finds nearest unvisited city
        city: starting point
        visited: list with indexes of visited cities
        return: the nearest city
        """
        cities = [i for i in range(self.length()) if i not in visited]
        return min(list(zip([self.data[city][i] for i in cities], cities)))[1]

    def find_smallest_increase(self, subtour, new_city):
        """
        len, int -> [int, list]
        subtour: our current path
        new_city: the new city to be inserted
        return:  [len of new path, new path]
        """
        permutations = []
        for i in range(len(subtour)):
            path = subtour[0:i] + [new_city] + subtour[i::]
            permutations.append((self.find_route_len(path), path))
        return min(permutations)








