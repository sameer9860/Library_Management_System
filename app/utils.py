import heapq
from collections import deque

# ---------- Heuristic for Best-First Search ----------
def heuristic_score(query, book):
    query = query.lower()
    title = book.title.lower()
    author = book.author.lower()
    category = book.category.lower()
    description = book.description.lower()
    published_date = str(book.published_date).lower()
    
    score = 0
    for word in query.split():
        if word in title:
            score += 5
        if word in author:
            score += 3
        if word in category:
            score += 2
        if word in description:
            score += 1
        if word in published_date:
            score += 1
    return score

# ---------- Best-First Search ----------
def best_first_search(query, books):
    pq = []
    for book in books:
        score = heuristic_score(query, book)
        if score > 0:
            # add title as tie-breaker
            heapq.heappush(pq, (-score, book.title, book))
            
    results = []
    while pq:
        score, _, book = heapq.heappop(pq)
        results.append(book)
    return results

# ---------- Build Graph ----------
def build_graph(books):
    graph = {}
    for book in books:
        graph[book] = []
        for other in books:
            if book != other:
                # connect if same category or same author
                if book.category == other.category or book.author == other.author:
                    graph[book].append(other)
    return graph

# ---------- DFS ----------
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    results = [start]
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            results.extend(dfs(graph, neighbor, visited))
    return results

# ---------- BFS ----------
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    results = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            results.append(node)
            queue.extend(graph.get(node, []))
    return results
