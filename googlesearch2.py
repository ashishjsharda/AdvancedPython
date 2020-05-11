from googlesearch import  search
query="Ashish Sharda"
results=search(query,tld='com',num=10,pause=2.0)
for i in results:
    print(i)
print(results)
