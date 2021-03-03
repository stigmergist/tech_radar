import json

cat = ["Languages" ,"Infrastructure" ,"Frameworks" , "Data Management"]
ring = ["Adopt","Trial","Assess","Hold"]

with open('deploy/original-list.json') as json_file:
    data = json.load(json_file)
    for item in data:
        filename = item['label'].replace(' ','_')+'.yaml'
        output = 'short_name: '+item['label']+'\n'
        output += 'categories:\n'
        output += ' - '+ cat[ item['quadrant']] +'\n'
        output += 'facets:\n'
        output += ' - axis: Adoption Policy\n'
        output += '   value : '+ ring[ item['ring']] +'\n'
        output += '   movement : '+ str(item['moved']) +'\n'
        if item.get('link',None):
            output += '   link : ' + item['link'] + '\n'
        with open("./data/"+filename, "w") as f:
            f.write(output)