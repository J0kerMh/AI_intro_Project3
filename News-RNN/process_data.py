import xmltodict
from urllib.parse import urlparse
import pandas as pd


def get_url(doc):
    return urlparse(doc['doc']['url']).netloc

def get_content(doc):
    if not doc['doc']['content']:
        return doc['doc']['contenttitle']
    return doc['doc']['contenttitle']+doc['doc']['content']
data = { 'label' : [], 'content' : [] }

with open(r'D:\study\人工智能\news_tensite_xml.xml', encoding='utf8') as fd:
    doc = ''
    i = 0
    for line in fd:
        if (i == 6):
            i = 1
            #             print(doc)
            url=''
            content=''
            try:
                doc = xmltodict.parse(doc)
                url=get_url(doc)
                content=get_content(doc)
                # data['label'].append(get_url(doc))
                # data['content'].append(get_content(doc))
            except:
                pass
            if(url and content):

                data['label'].append(url)
                data['content'].append(content)
            doc = '' + line
        else:
            i = i + 1
            doc = doc + line

df = pd.DataFrame(data)

df.to_csv('res.csv')