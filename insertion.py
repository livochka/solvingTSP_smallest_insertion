from tbl import Table


def tsp(data):
    """
    (list) -> list, int
    data: [x, y] coordinates of the city
    return: path, len of the path
    """
    point = 0
    subtour, length = [0], 0
    distance_table = Table(data)

    size, visited = len(data), 1
    while visited < size:
        nearest = distance_table.find_nearest_unvisited(point, subtour)
        length, subtour = distance_table.find_smallest_increase(subtour, nearest)
        visited += 1
    subtour.append(subtour[0])
    return subtour, length

