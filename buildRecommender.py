import graphlab as gl


wd = "/Users/sevensevens/CSE6242_Proj/data/"
n_recs = 150


jobs = gl.SFrame.read_csv(wd + "cleaned_jobs.csv",header=True, delimiter=',')
apps =gl.SFrame.read_csv(wd + "cleaned_Train_apps.csv",header=True, delimiter=',')
userAll =gl.SFrame.read_csv(wd + "cleaned_Train_users.csv",header=True, delimiter=',')
userLoc = userAll.select_columns(['UserID', 'City', 'State', 'Country'])
userEdu = userAll.select_columns(['UserID', 'DegreeType', 'Major'])
userExp = userAll.select_columns(['UserID', 'WorkHistory', 'TotalYearsExperience', 'CurrentlyEmployed'])
userLocEdu = userAll.select_columns(['UserID', 'City', 'State', 'Country', 'DegreeType', 'Major'])
userLocExp = userAll.select_columns(['UserID', 'City', 'State', 'Country', 'WorkHistory', 'TotalYearsExperience', 'CurrentlyEmployed'])
userEduExp = userAll.select_columns(['UserID', 'DegreeType', 'Major', 'WorkHistoryCount', 'TotalYearsExperience', 'CurrentlyEmployed'])

# ranking factorization recommender
modelAll = gl.recommender.ranking_factorization_recommender.create(apps,user_id = 'UserID',item_id='JobID',user_data=userAll,item_data=jobs)
modelLoc = gl.recommender.ranking_factorization_recommender.create(apps,user_id = 'UserID',item_id='JobID',user_data=userLoc,item_data=jobs)
modelEdu = gl.recommender.ranking_factorization_recommender.create(apps,user_id = 'UserID',item_id='JobID',user_data=userEdu,item_data=jobs)
modelExp = gl.recommender.ranking_factorization_recommender.create(apps,user_id = 'UserID',item_id='JobID',user_data=userExp,item_data=jobs)
modelLocEdu = gl.recommender.ranking_factorization_recommender.create(apps,user_id = 'UserID',item_id='JobID',user_data=userLocEdu,item_data=jobs)
modelLocExp = gl.recommender.ranking_factorization_recommender.create(apps,user_id = 'UserID',item_id='JobID',user_data=userLocExp,item_data=jobs)
modelEduExp = gl.recommender.ranking_factorization_recommender.create(apps,user_id = 'UserID',item_id='JobID',user_data=userEduExp,item_data=jobs)
modelNone = gl.recommender.ranking_factorization_recommender.create(apps,user_id = 'UserID',item_id='JobID',item_data=jobs)


# write recommender to file
modelAll.save('rf_All.model')
modelLoc.save('rf_Loc.model')
modelEdu.save('rf_Edu.model')
modelExp.save('rf_Exp.model')
modelLocEdu.save('rf_Loc_Edu.model')
modelLocExp.save('rf_Loc_Exp.model')
modelEduExp.save('rf_Edu_Exp.model')
modelNone.save('rf_None.model')


