import csv



with open('3rd.csv', 'r', encoding="utf8") as file:
    reader = csv.reader(file)
    counter = 0
    m_lastnames = []


    for row in reader:
        #print(row[0])
        if counter != 0:
            #break

            if str(row[0])[0].lower() == "m":
                #print(row)
                m_lastnames.append(row)
                #break
        
        counter += 1

#sorts the names by the number of them
m_lastnames.sort(key= lambda x: x[1])
#print(m_lastnames)

lol = 0
for x in range(len(m_lastnames)):
    
    if int((m_lastnames[x])[1]) == 75:
        print(m_lastnames[x])
        lol += 1

print(f"I got it down to {lol}")



