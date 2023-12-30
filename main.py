from src import Yahoo

queries = [
  "Mango",
  "Watermelon",
]

Yahoo.search(queries, max=10)
