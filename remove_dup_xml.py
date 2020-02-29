#!/usr/bin/env python

import xml.etree.ElementTree as ET
import itertools

tree = ET.parse('My Places.kml')
ET.register_namespace('', "http://earth.google.com/kml/2.2")
root = tree.getroot()

tags = []
dups = []

# Get tags with Point
for i in range(0, len(root[0])):
	#print(root[0][i].tag)
	if (len(root[0][i]) > 2) and (root[0][i].tag == "{http://earth.google.com/kml/2.2}Placemark"):
		if (root[0][i].find(".//{http://earth.google.com/kml/2.2}Point") != None):
			tags.append(root[0][i].find(".//{http://earth.google.com/kml/2.2}Point")[0].text)


# Get duplicate tags
for i in range(0, len(tags)):
	if tags[i] in tags[:i]:
		dups.append(i)

# Remove duplicate tags
for i in range(len(root[0]), 0, -1):
	if (i in dups):
		#print(i, dups[dups.index(i)])
		root[0].remove(root[0][i])

# Write new XML file
tree.write('My Places unique.kml', default_namespace='', xml_declaration=None, short_empty_elements=False)
