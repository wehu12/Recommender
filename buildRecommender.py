import graphlab as gl


wd = "/Users/sevensevens/CSE6242_Proj/data/"
n_recs = 150


jobs = gl.SFrame.read_csv(wd + "cleaned_jobs.csv",header=True, delimiter=',')
apps =gl.SFrame.read_csv(wd + "cleaned_Train_apps.csv",header=True, delimiter=',')
users =gl.SFrame.read_csv(wd + "cleaned_Train_users_Location.csv",header=True, delimiter=',')

# ranking factorization recommender
model = gl.recommender.ranking_factorization_recommender.create(apps,user_id = 'UserID',item_id='JobID',user_data=users,item_data=jobs)

#write recommender to file
model.save('rf_Location.model')
