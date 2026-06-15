from turtle import*
speed(100)
bgcolor('black')
c=['red','orange','green','yellow','blue','purple'] 
pensize(5)
for i in range(200):
    color(c[i%6])
    fd(i)
    lt(100)
    fd(i)
    rt(160)
done()
