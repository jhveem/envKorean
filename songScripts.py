import pandas as pd

def printSongs(df, lesson):
	#just set this manually to 50 since that's probably a good number to start with
	lessonString = 'l' + str(lesson)
	results = df.sort_values([lessonString, 'word count'], ascending = False)
	count = 0
	html = ''
	for index, row in results.iterrows():
		#print(row[lessonString])
		title = str(row['title'])
		if title == 'nan':
			title = "Untitled Song"
		html += "<br><a href='"+str(index)+ "' target='_blank'>" + title + "</a>"
		html += "<p>KNOWN:" + str(round(row[lessonString] * 100, 2))+"%</p>"
		html += "<p>WORD COUNT:" + str(row['word count']) + "</p>"
		#print('')
		#print(index)
		#print("KNOWN:", str(round(row[lessonString] * 100, 2))+"%")
		count += 1
		if (count == 25):
			break
	return html