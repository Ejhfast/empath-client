def default_tokenizer(doc):
    return doc.split()

def bigram_tokenizer(doc):
    tokens = doc.split()
    for t1,t2 in zip(tokens,tokens[1:]):
        yield t1
        yield t1+"_"+t2
    yield tokens[-1]
