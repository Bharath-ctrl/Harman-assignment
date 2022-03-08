#nested dict
studentdata=[
    {'name':'Abax',
    'marks':[
        { 'english':20,'math':23 }
    ]
    },
    {'name':'Bmax',
    'marks':[
        { 'english':32,'math':33 }
    ]
    }
]
for i in studentdata:
    print(i['name']) #print only the name from the studentdata dict
    for j in i['marks']: #marks is another dict in the studentdata, so we are printing marks of english for both the students
        print(j['english'])