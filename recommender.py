import graphlab as gl


wd = "/Users/linahu/Documents/Developer/CareerBuilder/"

jobs = gl.SFrame.read_csv(wd + "jobs.tsv",header=True, delimiter='\t')
userHistory =gl.SFrame.read_csv(wd + "user_history.tsv",header=True, delimiter='\t')
apps =gl.SFrame.read_csv(wd + "apps.tsv",header=True, delimiter='\t')
users =gl.SFrame.read_csv(wd + "users.tsv",header=True, delimiter='\t')

trainset =apps[apps['Split']=="Train"]
testset=apps[apps['Split']=="Test"]

#simple recommender
model1 = gl.recommender.create(apps,user_id = 'UserID',item_id='JobID')


with open(wd+"Basic CF output.csv", "w") as outfile:
    outfile.write("UserId, JobIds\n")
    for userID in testset['UserID']:
        jobs = model1.recommend(users=[userID],k=150)['JobID']
        outfile.write(str(userID) + "," + " ".join([x[0] for x in jobs]) + "\n")
