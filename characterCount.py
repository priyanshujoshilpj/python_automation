import pprint

message= "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
count={}

for character in message.upper():
	count.setdefault(character, 0)
	count[character] = count[character] + 1

pprint.pprint(count)
