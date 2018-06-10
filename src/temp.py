

data = {
    'id':'200180909',
    'name':'jerry',
    'age':20
}
table = 'students'
valus = ','.join(['%s']*len(data))
print(valus)