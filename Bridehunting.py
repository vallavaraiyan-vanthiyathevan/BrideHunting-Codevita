#calculate no. of qualities
def cal_no_of_qualities(l,j,k,r,m):
    n=0
    
    if j-1>=0:
        if l[j-1][k]==1:
            n+=1
        if k+1<m:
            if l[j-1][k+1]==1:
                n+=1
        if k-1>=0:
            if j-1!=0 or k-1!=0:
                if l[j-1][k-1]==1:
                    n+=1
    if k-1>=0:
        if l[j][k-1]==1:
            n+=1
        if j+1<r:
            if l[j+1][k-1]==1:
                n+=1
    if j+1<r:
        if l[j+1][k]==1:
            n+=1
        if k+1<m:
            if l[j+1][k+1]==1:
                n+=1
    if k+1<m:
        if l[j][k+1]==1:
            n+=1

    return n
    

def check_ls_dist(q1,r1,c1,q2,r2,c2):
    if r1+c1 < r2+c2:
        return q1,r1,c1
    else:
        return q2,r2,c2
    

N,M=map(int,input().split(" "))
lst=[]
for i in range(0,N):
    lst.append(list(map(int,input().split(" "))))
lst=tuple(lst)
quality_no=0
lsrow=0
lscol=0
#iterate over bride
for j in range(0,N):
    for k in range(0,M):
        if j==0 and k==0:
            continue
        else:
            if lst[j][k]==1:
                quality_no_buff = cal_no_of_qualities(lst,j,k,N,M)
                
                if quality_no_buff>quality_no:
                    quality_no = quality_no_buff
                    lsrow=j
                    lscol=k
                elif quality_no_buff==quality_no and quality_no!=0:
                    quality_no,lsrow,lscol = check_ls_dist(quality_no,lsrow,lscol,quality_no_buff,j,k)
                else:
                    pass

print("{0}:{1}:{2}".format(lsrow+1,lscol+1,quality_no))
