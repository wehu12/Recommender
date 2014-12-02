import graphlab as gl


wd = "/Users/linahu/Documents/Developer/CareerBuilder/"
n_recs = 150

def write_to_file(model,testusers,filename):
    with open(filename, "w") as outfile:
        outfile.write("UserId, JobIds\n")
        for userID in list(testusers):
            jobs = model1.recommend(users=[userID],k=n_recs)['JobID']
            outfile.write(str(userID) + "," + " ".join([x for x in jobs]) + "\n")


jobs = gl.SFrame.read_csv(wd + "jobs.tsv",header=True, delimiter='\t')
userHistory =gl.SFrame.read_csv(wd + "user_history.tsv",header=True, delimiter='\t')
apps =gl.SFrame.read_csv(wd + "apps.tsv",header=True, delimiter='\t')
users =gl.SFrame.read_csv(wd + "users.tsv",header=True, delimiter='\t')

trainset =apps[apps['Split']=="Train"]
testset=apps[apps['Split']=="Test"]

testusers = set(testset['UserID'])
#split test users based on WindowID
testusers1 = set(testset[testset['WindowID']=='1']['UserID'])



#simple recommender
model1 = gl.recommender.create(apps,user_id = 'UserID',item_id='JobID')

#write recommendations to file
write_to_file(model1,testusers1,wd+"Basic CF.csv")
