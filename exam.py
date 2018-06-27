from bs4 import BeautifulSoup
import requests

def USA_sj(url_1):
    result_1 = {}
    res_1 = requests.get(url_1)
    res_1.encoding = 'utf-8'
    soup = BeautifulSoup(res_1.text, 'html.parser')
    result_1['年份'] = soup.select('table')[0].select('tbody')[0].select('tr')[0].text.split()
    result_1['美国GDP(10亿美元)'] = soup.select('table')[0].select('tbody')[0].select('tr')[19].text.split()
    result_1['美国人均GDP(美元)'] = soup.select('table')[0].select('tbody')[0].select('tr')[14].text.split()
    return result_1

def CHN_sj(url_2):
    result_2 = {}
    res_2 = requests.get(url_2)
    res_2.encoding = 'utf-8'
    soup = BeautifulSoup(res_2.text, 'html.parser')
    result_2['年份'] = soup.select('table')[0].select('tbody')[0].select('tr')[0].text.split()
    result_2['中国GDP(10亿美元)'] = soup.select('table')[0].select('tbody')[0].select('tr')[8].text.split()
    result_2['中国人均GDP(美元)'] = soup.select('table')[0].select('tbody')[0].select('tr')[3].text.split()
    return result_2


USA_data = USA_sj('http://www.8pu.com/country/USA/')
CHN_data = CHN_sj('http://www.8pu.com/country/CHN/')

del(USA_data['年份'][10])
del(USA_data['美国GDP(10亿美元)'][0])
del(USA_data['美国人均GDP(美元)'][0])
del(CHN_data['年份'][10])
del(CHN_data['中国GDP(10亿美元)'][0])
del(CHN_data['中国人均GDP(美元)'][0])

del(USA_data['美国GDP(10亿美元)'][10])
del(USA_data['美国人均GDP(美元)'][10])
del(CHN_data['中国GDP(10亿美元)'][10])
del(CHN_data['中国人均GDP(美元)'][10])

# print(USA_data)
# print(CHN_data)

data = {**USA_data, **CHN_data}
# 字典合并
# print(data)

key_value = list(data.keys())
# 将列表键变为列表
value_list = list(data.values())
# 将列表值变为列表
# print(key_value)
# print(value_list)

value_list_0= list(map(eval, value_list[0]))
value_list_1= list(map(eval, value_list[1]))
value_list_2= list(map(eval, value_list[2]))
value_list_3= list(map(eval, value_list[3]))
value_list_4= list(map(eval, value_list[4]))
print(value_list_0)
print(value_list_1)
print(value_list_2)
print(value_list_3)
print(value_list_4)