import json

# JSON as a sting
image_json_string = '''
{
	"title": "",
	"url": "",
	"width": 0,
	"height": 0,
	"author": ""
}
'''

# Open JSON from a file
with open('assets.json') as json_file:
	data = json.load(json_file)

# Modify one type of items
for image in data['images']:
	image["width"] *= 2

# remove items
for image in data['images']:
	del image['author']

# Load JSON form a string and modify data
image_json = json.loads(image_json_string)
image_json["title"] = "Image Four"
image_json["url"] = "image4.tiff"
image_json["width"] = 320
image_json["height"] = 200

# add the JSON
data["images"].append(image_json)

# modify nested data
for movie in data['movies']:
	movie['size'][0] *= 2

# pretty print
print(json.dumps(data, indent = 4))

# counting items
print("Num images: " + str(len(data['images'])))

# write JSON to a file (pretty)
with open('modified_assets.json', 'w') as json_file:
	json.dump(data, json_file, indent = 4)