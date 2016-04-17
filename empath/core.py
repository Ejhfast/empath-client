import os
import sys
from collections import defaultdict
from . import helpers as util
import requests
import json

class Empath:
    def __init__(self, backend_url="http://localhost:8000"):
        self.cats = defaultdict(list)
        self.invcats = defaultdict(list)
        self.backend_url = backend_url
        self.base_dir = os.path.dirname(util.__file__)
        self.load(self.base_dir+"/data/categories.tsv")

    def load(self,file):
        with open(file,"r") as f:
            for line in f:
                cols = line.strip().split("\t")
                name = cols[0]
                terms = cols[1:]
                for t in terms:
                    self.cats[name].append(t)
                    self.invcats[t].append(name)

    def analyze(self,doc,tokenizer="default",normalize=True):
        if tokenizer == "default":
            tokenizer = util.default_tokenizer
        elif tokenizer == "bigrams":
            tokenizer = util.bigram_tokenizer
        if not hasattr(tokenizer,"__call__"):
            raise Exception("invalid tokenizer")
        count = {}
        tokens = 0.0
        for cat in self.cats.keys(): count[cat] = 0.0
        for tk in tokenizer(doc):
            tokens += 1.0
            for cat in self.invcats[tk]:
                count[cat]+=1.0
        if normalize:
            for cat in count.keys():
                count[cat] = count[cat] / tokens
        return count

    def create_category(self,seeds):
        resp = requests.get(self.backend_url + "/create_category", json={"terms":seeds})
        return json.loads(resp.text)
