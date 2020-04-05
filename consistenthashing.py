from hashring import HashRing

memcache_servers = ['192.168.0.246:11212',
                    '192.168.0.247:11212',
                    '192.168.0.249:11212']

ring = HashRing(memcache_servers)
server = ring.get_node("my_key")
print(server)
node=ring.get_node_pos("mk")
print(node)
