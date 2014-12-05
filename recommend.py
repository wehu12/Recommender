import graphlab as gl


n_recs = 150
def write_to_file(model,testusers,filename,users_data):
    with open(filename, "w") as outfile:
        outfile.write("UserId, JobIds\n")
        for userID in test_users:
            jobs = model.recommend(users=[userID],k=n_recs,new_user_data=users_data)['JobID']
            outfile.write(str(userID) + "," + " ".join([str(x) for x in jobs]) + "\n")

wd = "/Users/sevensevens/CSE6242_Proj/data/"
users =gl.SFrame.read_csv(wd + "cleaned_Test_users_Location.csv",header=True, delimiter=',')
model = gl.load_model('rf_Location.model')
test_apps = gl.SFrame.read_csv(wd + "cleaned_Test_apps_1000.csv",header=True, delimiter=',')
test_users = test_apps['UserID']

write_to_file(model, test_users, "rf_Location_result.csv", users)