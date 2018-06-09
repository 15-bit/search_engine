# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []

def traverse(o, tree_types=(list, tuple)): #get through each element of list in it's sublists
    if isinstance(o, tree_types):
        for value in o:
            for subvalue in traverse(value, tree_types):
                yield subvalue
    else:
        yield o

def add_to_index(index,keyword,url):
    for i in index:        
        if i[0] == keyword:
            if url not in i[1]:
                i[1].append(url)
                return
            return

    index.append([keyword, [url]])
    return




