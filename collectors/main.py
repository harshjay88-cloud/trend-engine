from collectors.youtube_suggest import get_suggestions

keywords = get_suggestions("music")

print("Trending suggestions:")

for k in keywords:
    print("-",k)
