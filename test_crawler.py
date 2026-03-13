from backend.crawler.heilbronn_crawler import crawl_mvp_events

events = crawl_mvp_events()

print("Events found:")
print(events[:5])