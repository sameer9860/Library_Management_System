from django.shortcuts import render
from .models import Book
from .utils import best_first_search, build_graph, dfs, bfs

def index(request):
    query = request.GET.get("q", "")
    books = Book.objects.all()

    # Best-First Search
    best_results = best_first_search(query, books)

    # Graph-based DFS/BFS (start from first book if exists)
    graph = build_graph(books)
    dfs_results = []
    bfs_results = []
    if books:
        dfs_results = dfs(graph, books[0])
        bfs_results = bfs(graph, books[0])

    return render(request, "app/index.html", {
        "query": query,
        "best_results": best_results,
        "dfs_results": dfs_results,
        "bfs_results": bfs_results,
    })
