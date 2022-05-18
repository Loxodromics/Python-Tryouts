import json

image_json_string = '''
{
	"title": "",
	"url": "",
	"width": 0,
	"height": 0,
	"author": ""
}
'''

with open('images.json') as json_file:
	data = json.load(json_file)

for image in data['images']:
	image["width"] *= 2

image_json = json.loads(image_json_string)
image_json["title"] = "Image Four"
image_json["url"] = "image4.tiff"
image_json["width"] = 320
image_json["height"] = 200

data["images"].append(image_json)

for image in data['images']:
	del image['author']

print(json.dumps(data, indent = 4))

with open('modified_images.json', 'w') as json_file:
	json.dump(data, json_file, indent = 4)