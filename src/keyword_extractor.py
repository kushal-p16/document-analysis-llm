import yake

def extract_keywords(text, top_k=10):
    kw_extractor = yake.KeywordExtractor(
        lan="en",
        n=1,
        dedupLim=0.3,
        top=top_k
    )
    keywords = kw_extractor.extract_keywords(text)
    return [kw for kw, score in keywords]