import time
startTime=time.time()
def mySplit(s,ds):
    res = [s]
    for d in ds:
        t = []
        for x in res:
            t.extend(x.split(d))
        res = t
    return [x for x in res if x]

s='ab;cd|efg|hi,jklmn\topq;rst,uvw\txyz'
print(mySplit(s,',;\t|'))


##def mySplit(s,ds):
##	res = [s]
##	for d in ds:
##		t = []
##		for z in map(lambda x: x.split(d),res):
##			t.extend(z)
##		res = t
##	return [x for x in res if x]
##
##s='ab;cd|efg|hi,jklmn\topq;rst,uvw\txyz'
##print(mySplit(s,',;\t|'))


##def mySplit(s,ds):
##	res = [s]
##	for d in ds:
##		t = []
##		list(map(lambda x: t.extend(x.split(d)),res))
##		res = t
##	return [x for x in res if x]
##
##s='ab;cd|efg|hi,jklmn\topq;rst,uvw\txyz'
##print(mySplit(s,',;\t|'))
endTime=time.time()
print(endTime - startTime)
