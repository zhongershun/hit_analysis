import requests
import pygal
import re
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
#执行API调用并存储响应
url="https://api.github.com/search/repositories?q=language:python&sort=stars"
r=requests.get(url)
print("Status code:",r.status_code)
#将API响应存储在一个变量中
response_dict=r.json()
print("Total repositories:",response_dict['total_count'])
#探索有关仓库的信息
repo_dicts=response_dict['items']
print("Repositories returned:%d\n\n"%len(repo_dicts))
for repo_dict in repo_dicts:
    if repo_dict['name']=='requests':
        pass
    else:
        print('\nName:',repo_dict['name'])
        print('Owner:',repo_dict['owner']['login'])
        print('Stars:',repo_dict['stargazers_count'])
        print('Repository:',repo_dict['html_url'])
        print('Description:',repo_dict['description'])
names,plot_dicts=[],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict={
        'value':repo_dict['stargazers_count'],
        'label':str(repo_dict['description']),
        'xlink':repo_dict['html_url']
        }
    plot_dicts.append(plot_dict)
my_style=LS('#333366',base_style=LCS)
chart=pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
chart.title='Most-Starred Python Projects on GitHub'
chart.x_labels=names
chart.add('',plot_dicts)
chart.render_to_file('python_repos2.svg')