from itertools import islice

def partitions(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]

def window(seq, n):
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result

def default_tokenizer(doc):
    return doc.split()

def bigram_tokenizer(doc):
    tokens = doc.split()
    for t1,t2 in zip(tokens,tokens[1:]):
        yield t1
        yield t1+"_"+t2
    yield tokens[-1]

def window_tokenizer(window_size, targets):
    def window_func(doc,target_dic={t:t for t in targets}):
        tokens = doc.split()
        for w in partitions(tokens, window_size):
            if any([x in target_dic for x in w]):
                for w_ in w:
                    yield w_
    return window_func
