# soal no. 1
def fungsiKausKaki(totalKausKaki):
    ckk=set(sorted(totalKausKaki))
    a=0
    b=0
    for i in ckk:
        x=totalKausKaki.count(i)
        a=x//2
        if a>0:
          b+=a
    print(str(b)+" Pasang Kaos Kaki")
    return b

fungsiKausKaki([10,20,20,10,10,30,50,10,20])

# soal no. 2
def mainanAnak(hMainan, budget):
    harga=sorted(hMainan)
    total=0
    for i in harga:
        if budget-i > 0:
            budget-=i
            total+=1
    print(str(total)+" Mainan")
    return total

mainanAnak([1,12,5,111,200,1000,10], 50)