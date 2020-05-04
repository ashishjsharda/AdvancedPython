from googlesearch import search
query='how old is michael jordan'
search_result_list = list(search(query, tld="com", num=10, stop=3, pause=1))
print(search_result_list)
for i in search(query,tld="com",num=10,pause=2):
    print(i)
