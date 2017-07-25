import json
import html2text
import re
import xlsxwriter

h = html2text.HTML2Text()
h.body_width = 0

input_file = open('json_original.json').read()
output_file = open('output.txt', 'w')
object_file = open('output.json', 'w')

workbook = xlsxwriter.Workbook('extracted_banners.xlsx')
worksheet = workbook.add_worksheet()

row = 0
col = 0

data = json.loads(input_file)
i = 0


for post in data['data']['posts']:
    banners = []
    title = 'https://www.policygenius.com/blog/'+post['slug']
    search = '\[banner-.*?]', '\[Banner-.*?]', '\[video-.*?]', '\[recommended-posts .*?]', '\[widget-.*?]', '\[hotspot .*?]'
    for ban in search:
        banners += re.findall(ban, post['markdown'])
    if banners:
        worksheet.write(row, col,     title)
        worksheet.write(row, col + 1,     ','.join(banners))
        row += 1


    post['markdown'] = h.handle(post['markdown'])

    post['markdown'] = re.sub('\[banner-.*?]', ' ', post['markdown'])
    post['markdown'] = re.sub('\[Banner-.*?]', ' ', post['markdown'])
    post['markdown'] = re.sub('\[video-.*?]', ' ', post['markdown'])
    post['markdown'] = re.sub('\[recommended-posts .*?]', ' ', post['markdown'])
    post['markdown'] = re.sub('\[widget-.*?]', ' ', post['markdown'])
    post['markdown'] = re.sub('\[hotspot .*?]', ' ', post['markdown'])
    post['image'] = re.sub('https://pg-lib', 'https://policygenius-blog', str(post['image']))



    output_file.write(post['markdown'])
object_file.write(json.dumps(data))
workbook.close()


print("Done")
