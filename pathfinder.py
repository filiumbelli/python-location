text = '''a-b
a-c-f-j
a-d-g-k
a-e
b-c-d-e
b-f-h-k
b-j
e-g-h-j
e-k
j-k'''

# --- create Adj ---

Adj = dict()

lines = []

for row in text.strip().split('\n'):
    all_items = set(row.split('-'))
    lines.append(all_items)
    for item in all_items:
        if item not in Adj:
            Adj[item] = set()
        rest = all_items - set(item)
        Adj[item].update(rest)
        #Adj[item].update(all_items)
        #Adj[item].remove(item)

print('--- nodes ---')
nodes = sorted(Adj.keys())
print(nodes)

print('--- lines ---')
for line in lines:
    print(line)

print('--- Adj ---')
for key in sorted(Adj.keys()):
    print(key, list(sorted(Adj[key])))


# --- create triangles ---

triangles = list()
A = {x:set() for x in nodes} # create empty A(v)

for s in nodes:
    for t in Adj[s]:
        if s < t:
            for v in A[s] & A[t]:
                # check if nodes not on one line
                is_line = False
                for line in lines:
                    if s in line and t in line and v in line:
                        is_line = True
                        break
                if not is_line:
                    triangles.append(tuple(sorted( (s,v,t) )))
                    #print(*triangles[-1])
            A[t].add(s)

# --- count triangles ---

print('--- number of triangles ---')
print(len(triangles))
#print(len(set(triangles)))

# --- show triangles in alphabetic order ---

print('--- triangles ---')
for triangle in sorted(triangles):
    print(*triangle)
