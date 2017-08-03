# -*- coding: utf-8-*-

import os, os.path
import codecs

def balRules(text):
	
	suffix_words=list(codecs.open("suffix_words.txt","r",encoding='utf-8'))
				
	###Rule to remove Lai
	for i, j in enumerate(text):
		if u'लाई' in j:
			if ord(j[-3]) == 2354 and (ord(j[-2]) == 2366 and ord(j[-1]) == 2312) : 
				text[i] = j.replace(j[-3:],"")

	###Rule to remove plural
	for i, j in enumerate(text):
		
		if u'हरू' in j or u"हरु" in j:
			
			if u'हरू' in j:
				loc=j.find(u'हरू')
			else:
				loc=j.find(u"हरु")
			if loc!=len(j):
				if j[loc+len("हरु"):] in suffix_words :
						text[i] = j.replace(j[loc:], "")
				else:
					if ord(j[-3]) == 2361 and (ord(j[-2]) == 2352 and (ord(j[-1]) == 2370 or ord(j[-1])==2369)): 
						text[i] = j.replace(j[-3:],"")
	
	###Rule no 3
		if u'ाइ' in j:
			if ord(j[-2]) == 2366 and ord(j[-1]) == 2311:	
				text[i]=j.replace(j[-2:],"")
			
	###Rule no 2
		if u'ीय' in j:
			if ord(j[-2]) == 2368 and ord(j[-1]) == 2351:
				text[i] = j.replace(j[-2:], "")
			if ord(j[-2]) == 2351 and ord(j[-1]) == 2366:
				text[i] = j.replace(j[-2:], "")


	###Rule to remove ko, ro and no
	for i, j in enumerate(text):
	    if u'ो' in j:
	    	#Checking if it has ka, ra or na
	    	if ord(j[-2]) == 2325 or ord(j[-2]) == 2352 or ord(j[-2]) == 2344:
	    		#Checking if it is ko, ro or no
	    		if ord(j[-1]) == 2379:
	    			text[i] = j.replace(j[-2:], "")

    #Checking for kaa, raa , naa and maa
	for i, j in enumerate(text):
		if u'ा' in j:
	    	#Checking if it has ka, ra, na or ma:
			if ord(j[-2]) == 2325 or ord(j[-2]) == 2352 or ord(j[-2]) == 2344 or ord(j[-2]) == 2350:
			    #Checking for the aakar:
				if ord(j[-1]) == 2366:
					text[i] = j.replace(j[-2:], "")

    #Rule to remove ki,ri,ni
	for i, j in enumerate(text):
	    if u'ी' in j:
	    	#Checking if it has ka, ra or na
	    	if ord(j[-2]) == 2325 or ord(j[-2]) == 2352 or ord(j[-2]) == 2344:
	    		#Checking for the e:
	    		if ord(j[-1]) == 2368:
	    			text[i] = j.replace(j[-2:], "")


	#Rule to remove le:
	for i, j in enumerate(text):
	    if u'ले' in j:
	    	if ord(j[-2]) == 2375 and ord(j[-2]) == 2354:
	    		text[i] = j.replace(j[-2:], "")


	#Rule to remove lagi:
	for i, j in enumerate(text):
	    if u'लागि' in j:
	    	if ord(j[-4]) == 2375 and ord(j[-3]) == 2366 and ord(j[-2])== 2327 and ord(j[-1])==2367 :
	    		text[i] = j.replace(j[-4:], "")
 
	#Rule to remove bata:
	for i, j in enumerate(text):
	    if u'बाट' in j:
	    	if ord(j[-3]) == 2348 and ord(j[-2]) == 2366 and ord(j[-1])== 2335:
	    		text[i] = j.replace(j[-3:], "")


	#Rule to remove dekhi:
	for i, j in enumerate(text):
	    if u'देखि' in j:
	    	if ord(j[-4]) == 2342 and ord(j[-3]) == 2375 and ord(j[-2])== 2326 and ord(j[-1])==2367 :
	    		text[i] = j.replace(j[-4:], "")


	#Rule to remove dwara:
	for i, j in enumerate(text):
	    if u'देखि' in j:
	    	if ord(j[-4]) == 2342 and ord(j[-4]) == 2381 and ord(j[-3]) == 2357 and ord(j[-2])== 2366 and ord(j[-1])==2352 :
	    		text[i] = j.replace(j[-5:], "")


	#Rule to remove mathi:
	for i, j in enumerate(text):
	    if u'माथी' in j:
	    	if ord(j[-4]) == 2350 and ord(j[-3]) == 2366 and ord(j[-2])== 2341 and ord(j[-1])==2368 :
	    		text[i] = j.replace(j[-4:], "")    		

	    			
	return text

