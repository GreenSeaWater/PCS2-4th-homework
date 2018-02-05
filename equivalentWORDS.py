# The problem being solved here can be thought of as a graph problem, in which each word is a node of the graph and
# two nodes are connected if and only if they are of the same length and differ by one letter.
# The idea is you pick two words and try to get from one to the other by using a chain of valid words.
# Only substitutions are allowed.
from collections import defaultdict
from collections import deque

# english words dictionary downloaded from 'https://goo.gl/hBvqqr'
file = open('words.csv', 'r')
dictionary = set([word.lower() for word in file.read().split()])


# Represent the relationships between the words as a graph.
def constructGraph(dictionary):
    graph = defaultdict(list)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for word in dictionary:
        for i in range(len(word)):
            for char in alphabet:
                change = word[:i] + char + word[i+1:]  # Generate all possible one letter changes of current word
                if change in dictionary and change != word:  # At each step you must transform one word into another word, you
                                                        # are not allowed to transform a word into a non-word
                    graph[word].append(change)  # for adding edge to graph

    return graph
# The graph obtained is a hash table whose keys are the nodes of the graph, and the value for a given key is just the
# list of valid transformations of that word.


myGraph = constructGraph(dictionary)


# The idea is to use BFS.
# Return the shortest path to reach the target 'endWord' from 'startWord' using minimum number of moves.
# Return an empty list if no such transformation sequence exists.
def get_path(graph, startWord, endWord):
    # Create a queue for BFS and insert 'startWord' as source vertex
    queue = deque([[startWord]])
    visited = set()
    while queue:
        path = queue.popleft()
        node = path[-1]
        # if the last word is the destination, return the path
        if node == endWord:
            return path

        for word in graph[node]:
            if word not in visited:
                queue.append(path + [word])
                visited.add(word)

    # no possible conversion
    return []


transformations = [('head', 'tail'), ('fast', 'slow'), ('fool', 'sage'), ('cold', 'warm'), ('new', 'old')]
for (start, end) in transformations:
    print('The shortest path from ' + start + ' to ' + end + ' is:')
    path = get_path(myGraph, start, end)
    print(' -> '.join(path))
