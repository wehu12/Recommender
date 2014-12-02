import csv

def writeFile(UserID,jobList,fr):
		fr.write(UserID)
		fr.write(',')
		for item in jobList:
			fr.write(str(item))
			fr.write('\t')
		fr.write('\n')	




def process_txt_data():
	with open("./data/apps.tsv", "r") as infile:
		with open('./data/app_cleaned.csv','w') as fr:
			reader = csv.reader(infile, delimiter="\t",
			quoting=csv.QUOTE_NONE, quotechar="")
			reader.next() # burn the header
			i = 0
			UserID_tmp='767'
			jobList=[]
			for line in reader:
				(UserID, WindowId,Split, ApplicationDate, Jobid)=line
				# print line
				if Split=='Test':
					if UserID==UserID_tmp:
						jobList.append(Jobid)

					if UserID!=UserID_tmp:
						writeFile(UserID_tmp, jobList,fr)
						jobList=[]
						jobList.append(Jobid)
						UserID_tmp=UserID

					
process_txt_data()
