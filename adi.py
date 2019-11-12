dict={'roll':[1,2,3,4],'name':['ram','hari','sita'],'gen':['male','male','female','female']}
for i in range(len(dict['roll'])):
    if dict['gen'][i]=='male':
        print(dict['marks'][i])
        print(dict['name'][i])
        print(dict['gen'][i])
