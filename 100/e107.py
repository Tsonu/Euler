import copy

class MapNode:
    def __init__(self, node_id):
        self.id = node_id
        self.other_nodes = []

    def add_connection(self, other_node, weight):
        if len(filter(lambda x: x[0] == other_node, self.other_nodes)) > 0:
            return
        self.other_nodes.append([other_node, weight])
        other_node.other_nodes.append([self, weight])

    def can_remove(self, other_node):
        if len(self.other_nodes) > 1 and len(filter(lambda x: x[0] == other_node, self.other_nodes)) > 0:
            return True
        return False

    def remove_connection(self, other_node):
        if len(self.other_nodes) > 1:
            self.other_nodes = filter(lambda x: x[0] == other_node, self.other_nodes)
            return True
        return False

def sum_list(node_list):
    s = 0
    for node in node_list:
        for connection in node[1].other_nodes:
            s += connection[1]
    return s

min = 10e8
def find_min(node_list, current_node):
    global min
    for connection in current_node[1].other_nodes:
        if current_node[1].can_remove(connection[0]):
            new_list = copy.deepcopy(node_list)
            new_current = find_node(new_list, current_node[1].id)
            new_target = find_node(new_list, connection[0].id)
            new_current[1].remove_connection(new_target[1])
            s = sum_list(new_list)
            if s < min:
                min = s
                print min
            find_min(new_list, new_target)




all_nodes = []


def find_node(node_list, node_name):
    for i in range(0, len(all_nodes)):
        if node_list[i][0] == node_name:
            return node_list[i]
    return None


f = open('e107_network.txt', 'r')
lines = [a for a in f.read().split('\n')]
cells = [a.split(',') for a in lines]
network = [[0 if cell == '-' else int(cell) for cell in line] for line in cells]

for i in range(0, len(network)):
    for j in range(0, len(network[i])):
        if network[i][j] != 0:
            top_node = find_node(all_nodes, i)
            if top_node is None:
                top_node = [i, MapNode(i)]
                all_nodes.append(top_node)

            left_node = find_node(all_nodes, j)
            if left_node is None:
                left_node = [j, MapNode(j)]
                all_nodes.append(left_node)

            top_node[1].add_connection(left_node[1], network[i][j])

first_sum = sum([sum(x) for x in network])
print first_sum
find_min(all_nodes, all_nodes[0])
print all_nodes



