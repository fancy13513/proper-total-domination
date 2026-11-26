"""Independent graph/weight audit. Requires Python 3 and NumPy. Run from any cwd."""
from collections import defaultdict
from itertools import product
import numpy as np
from verify import SEEDS  # data only

# Build Manhattan edges from coordinates, including both wraparound seams.
def check_pattern(board):
    h, w = len(board),len(board[0])
    neighbors=defaultdict(set)
    for i,j in product(range(h),range(w)):
        for v in [((i+1)%h,j),(i,(j+1)%w)]:
            neighbors[i,j].add(v)
            neighbors[v].add((i,j))
    count={v:sum(board[i][j] for i,j in adj) for v,adj in neighbors.items()}
    if not all(len(adj)==4 and count[v]>0 and all(count[v]!=count[u] for u in adj)
               for v,adj in neighbors.items()):
        raise ValueError("Invalid local counts")
    return count

def audit_seeds():
    expected={(5,7):'',(5,9):'',(5,11):'',(5,13):'C',(7,7):'',(7,9):'',(7,11):'C',(9,9):'RC'}
    observed={(len(s),len(s[0])):axes for axes,s in SEEDS}
    if observed!=expected or len(SEEDS)!=8:
        raise ValueError("Incomplete coverage")
    tested=0
    for axes,seed in SEEDS:
        for r,c in product(range(3 if 'R' in axes else 1),range(3 if 'C' in axes else 1)):
            matrix=[[int(x) for x in row] for row in seed]
            for _ in range(r):
                matrix=matrix[:2]+matrix
            for _ in range(c):
                matrix=[row[:2]+row for row in matrix]
            check_pattern(matrix)
            tested+=1
    print("Graph-based expansion certificates:",tested)

def turn(col):
    return col[1:]+col[:1]

def formula(n):
    if n in (3,5):
        return None
    return 5*((n+1)//2)+{4:2,8:1,9:1,11:1}.get(n,0)

def audit_minimum():
    columns=list(product((0,1),repeat=5))
    states=[]
    ending=defaultdict(list)
    sums=[]
    for a,b,c in product(columns,repeat=3):
        s=tuple(x+y+z+w for x,y,z,w in zip(a,c,turn(b),b[-1:]+b[:-1]))
        if min(s)==0 or any(x==y for x,y in zip(s,turn(s))):
            continue
        ending[b,c].append(len(states))
        states.append((a,b,c))
        sums.append(s)
    # Incoming arcs, constructed by looking backwards one column.
    tails=[];heads=[]
    for target,(a,b,c) in enumerate(states):
        for source in ending[a,b]:
            if all(i!=j for i,j in zip(sums[source],sums[target])):
                tails.append(source);heads.append(target)
    left=np.array(tails);right=np.array(heads)
    # Charge the destination state. On closed walks each column is charged once.
    toll=np.array([sum(states[i][1]) for i in heads],dtype=np.int32)
    # Collapse starting states under vertical rotation only. Endpoints remain labelled.
    def canonical(triple):
        return min(tuple(col[i:]+col[:i] for col in triple) for i in range(5))
    starts=[i for i,s in enumerate(states) if canonical(s)==s]
    INF=1000000
    diag=np.full(51,INF)
    for origin in starts:
        d=np.full(len(states),INF,dtype=np.int32)
        d[origin]=0
        for t in range(1,51):
            nd=np.full_like(d,INF)
            np.minimum.at(nd,right,d[left]+toll)
            diag[t]=min(diag[t],nd[origin])
            if t==48:
                at48=nd.copy()
            d=nd
        if not np.array_equal(d,np.where(at48<INF,at48+5,INF)):
            raise ValueError("Translated endpoint vector did not repeat")
    for t in range(3,51):
        value=None if diag[t]==INF else int(diag[t])
        if value!=formula(t):
            raise ValueError((t,value,formula(t)))
    print(f"Tuple states {len(states)}, arcs {len(left)}, representative starts {len(starts)}")
    print("Target-weight recurrence and all announced values through n=50: OK")

if __name__=="__main__":
    audit_seeds()
    audit_minimum()
