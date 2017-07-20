import json
import html2text
import re

h = html2text.HTML2Text()
h.body_width = 0

input_file = open('json_original.json').read()
output_file = open('output.txt', 'w')
object_file = open('output.json', 'w')
final_file = open('final.txt', 'w')

data = json.loads(input_file)
i = 0

for post in data['data']['posts']:
    post['markdown'] = h.handle(post['markdown'])

    post['markdown'] = re.sub('\[banner-.*]', ' ', post['markdown'])
    post['markdown'] = re.sub('\[video-.*]', ' ', post['markdown'])
    post['markdown'] = re.sub('\[recommended-posts .*]', ' ', post['markdown'])
    post['markdown'] = re.sub('\[widget-.*]', ' ', post['markdown'])


    output_file.write(post['markdown'])
object_file.write(json.dumps(data))

print("Done")
