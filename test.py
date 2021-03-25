import string
import sys
import sql

# user 回傳list (越前面權重越小)
# UI = ['age', 'babySitting', 'clinic', 'hSituation']
# UI = ['convenienceStore']


# Table
table = {
    'life' : ['convenienceStore', 'clinic', 'postOffice', 'babySitting', 'school', 'park'],
    'neighborSayNo' : ['dead', 'trash', 'slaughterhouse', 'electricity'],
    'safety' : ['police', 'stolen'],
    'wage' : ['job', 'annualIncome'],
    'society' : ['age', 'm2'],
    'traffic' : ['accident', 'speed', 'MRT', 'train', 'rail'],
    'house' : ['price', 'transac', 'hSituation']
}

def takeSecond(elem):
    return elem[1]

# 反指標 ： 鄰避設施 竊盜率  人口密度  年齡  交通事故 房價
# neighborSayNo, stolen, society, accident, price
def action(UI):
    print("1")
    total = []
    result = []
    UI = list(enumerate(UI))

    for i, a in UI:
        j = 0
        for keys, values in table.items():
            if a in values:
                j = i + 1
                k = keys

                if k == 'life':
                    print(a)
                    temp = sql.callLife(j, a)
                    
                if k == 'neighborSayNo':
                    j = 0 - j
                    temp = sql.callNeighborSayNo(j, a)

                if k == 'safety':
                    if a == 'stolen':
                        j = 0 - j
                    temp = sql.callSafety(j, a)

                if k == 'wage':
                    temp = sql.callWage(j, a)
                    
                if k == 'society':
                    j = 0 - j
                    temp = sql.callSociety(j, a)
                    
                if k == 'traffic':
                    if a == 'accident':
                        j = 0 - j
                    temp = sql.callTraffic(j, a)
                # print(sql.callTraffic(j, a))

                if k == 'house':
                    if a == 'price':
                        j = 0 - j
                    temp = sql.callHouse(j, a)

        if not total:
                total = temp

        else:
            for x in total:
                for y in temp:
                    if(x[0] == y[0]):
                        x[1] += y[1]

    # 排序
    total.sort(key = takeSecond, reverse = True)
    print(total)

    for a in total[:5]:
        result.append(a[0])
        # print(a[0])

    print(result)
    return(result)



