import heapq

def heuristic_score(query,book):
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

def best_first_search(query,books):
    pq = []
    
    for book in books:
        score = heuristic_score(query,book)
        if score > 0:
            heapq.heappush(pq, (-score, book))
            
    results = []
    while pq:
        score, book = heapq.heappop(pq)
        results.append(book)    
    return results
    