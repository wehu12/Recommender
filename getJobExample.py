import json
from bs4 import BeautifulSoup
import string
from geopy.geocoders import Nominatim

wd = "/Users/sevensevens/CSE6242_Proj/data/"
f = open(wd + 'jobs.tsv')
idLocStr = "202246 152528 757625 779460 881717 1078744 819687 547357 927736 95122 553828 264263 554851 196707 317343 138900 642706 333399 761456 62246 874230 373102 886133 1091394 790697 1077937 177507 1050736 247250 170621 902041 44108 152527 464652 502743 815489 409210 908618 158623 916294 260099 790399 509715 457044 460488 254425 710382 334906 145170 203311 196469 190096 634994 1037735 600010 803091 932547 457596 11624 868804 475371 639471 254815 605322 872036 1053896 280565 784632 843399 909295 702760"
idLoc = [int(i) for i in idLocStr.split()]
idLocEduStr = "757625 819687 547357 553828 779460 44108 1091394 1050736 1078744 202246 886133 170621 790697 554851 815489 62246 264263 196707 373102 95122 317343 1077937 177507 152528 761456 39029 409210 874230 247250 138900 333399 749031 642706 881717 152527 406695 334906 475371 1010073 908618 803091 790399 560006 1053896 464652 502743 145170 464856 916294 260099 909295 196469 710382 509715 457596 254425 457044 639471 702760 967582 296865 400568 932547 927736 634994 600010 902041 254815 784632 158623 911679"
idLocEdu = [int(i) for i in idLocEduStr.split()]
idAll = [1050736, 1078744, 779460, 317343, 152528, 757625, 553828]
new_index = [0, 2, 4, 5, 6, 7]
header = f.readline().rstrip().split()
new_header_list = [header[i] for i in new_index]
new_header = ','.join(new_header_list)

fp = open('jobExample.json', 'wb')
dic = dict()
for line in f:
	l = line.rstrip().split('\t')
	if int(l[0]) in idLoc:

		dic[l[0]] = dict()
		for i in new_index:
			if i == 4:
				l[i] = l[i].replace('\\r', '')
				text = BeautifulSoup(l[i])
				new_text = filter(lambda x: x in string.printable, text.get_text()).encode('ascii')
				l[i] = new_text
				content = "Title: " + l[2] + "\nRequirement: " + l[4]
				dic[l[0]]["Content"] = content
				continue
			if i > 4:
				addr = l[5] + ' ' + l[6] + ' '+ l[7]
				# print addr
				# geolocator = Nominatim()
				# location = geolocator.geocode(addr)
				# print [location.latitude, location.longitude]
				dic[l[0]]["geo"] = addr#[location.latitude, location.longitude]
				break
			dic[l[0]][header[i]] = l[i]
		dic[l[0]]["type"] = "Location"


	if int(l[0]) in idLocEdu:
		if int(l[0]) in idLoc:
			dic[l[0]]["type"] = "Education"
			continue
		dic[l[0]] = dict()
		for i in new_index:
			if i == 2:
				continue
				
			if i == 4:
				l[i] = l[i].replace('\\r', '')
				text = BeautifulSoup(l[i])
				new_text = filter(lambda x: x in string.printable, text.get_text()).encode('ascii')
				l[i] = new_text
				content = "Title: " + l[2] + "\nRequirement: " + l[4]
				dic[l[0]]["Content"] = content
				continue
			if i > 4:
				addr = l[5] + ' ' + l[6] + ' '+ l[7]
				# geolocator = Nominatim()
				# location = geolocator.geocode(addr)
				# print [location.latitude, location.longitude]
				dic[l[0]]["geo"] = addr#[location.latitude, location.longitude]
				break
			dic[l[0]][header[i]] = l[i]
		dic[l[0]]["type"] = "Education"
	if int(l[0]) in idAll:
		if int(l[0]) in idLoc or int(l[0]) in idLocEdu:
			dic[l[0]]["type"] = "Experience"
			continue
		dic[l[0]] = dict()
		for i in new_index:
			if i == 4:
				l[i] = l[i].replace('\\r', '')
				text = BeautifulSoup(l[i])
				new_text = filter(lambda x: x in string.printable, text.get_text()).encode('ascii')
				l[i] = new_text
				content = "Title: " + l[2] + "\nRequirement: " + l[4]
				dic[l[0]]["Content"] = content
				continue
			if i > 4:
				addr = l[5] + ' ' + l[6] + ' '+ l[7]
				# geolocator = Nominatim()
				# location = geolocator.geocode(addr)
				# print [location.latitude, location.longitude]
				dic[l[0]]["geo"] = addr#[location.latitude, location.longitude]
				break
			dic[l[0]][header[i]] = l[i]
		dic[l[0]]["type"] = "Experience"
json.dump(dic, fp)

