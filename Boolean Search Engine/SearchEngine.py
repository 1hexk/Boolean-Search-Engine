import json , time

def create_index(corpus):
    inverted_index = {}
    for index,document in enumerate(corpus):
        obj = ' '.join(document.values()).lower().split() # Join the values of the document and split them into words (lowercase)
        for word in obj:
            if word not in inverted_index:      # If the word is not in the index, add it
                inverted_index[word] = set()
            inverted_index[word].add(index)     # Add the document to the set of documents that contain the word
    return inverted_index

def boolean_search(index, query):
    terms = query.lower().split()        # Split the lower case of the query into words
    
    results = set()
    for term in terms: 

        if '&' in term: # AND case
            subterms = term.split('&')      # Split the term by the & operator
            subresults = None
            for subterm in subterms:        # fetch the documents that contain the subterms
                if subterm not in index:    # If a subterm in the query is not in the index, then it is not in any document
                    index[subterm] = set()
                if subresults is None:
                    subresults = set(index[subterm])
                else:
                    subresults.intersection_update(index[subterm]) # Intersect the documents that contain the subterms with the documents that contain the other subterms
            if subresults:
                results.update(subresults)
        else: # In OR case
            if term in index:
                results.update(index[term])

    return results

def parse_json():
    corpus = []

    with open('news.json', 'r') as f:
        for line in f:
            try:
                data = json.loads(line)
                corpus.append(data)
            except json.JSONDecodeError:
                print("Invalid JSON line:", line)
    return corpus

def main():

    start = time.perf_counter()
    corpus = parse_json()
    end = time.perf_counter()
    print("Number of Documents:", len(corpus))
    print("Time to Parse Json File:", end - start,'second\n')

    start = time.perf_counter()
    inverted_index = create_index(corpus)
    end = time.perf_counter()
    print("Time to Create Index:", end - start,'second\n')

    while True:
        query = input("Enter your query (type -1 to exit): ")
        if query == '-1':
            break
        start = time.perf_counter()
        result = boolean_search(inverted_index, query)
        end = time.perf_counter()
        #print("Documents:\n" +'\n'.join(str(corpus[i]) for i in result))
        #print("\nDocuments by Number:\n", result)
        print("Number of Documents:", len(result))
        print("Time to Search:", (end - start)*10**6,'micro seconds\n')

main()