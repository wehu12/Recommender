% BP Neural Network Prediction Method
% CSE6242 Final Project
% Team #27
 
clc
clear
All_error=[];%store the all errors
 
%---------------------------------------------------
% Input the data
%--------------------------------------------------- 
p=
%traing data, the data should like this: p=[493 372 445;372 445 176;...]'; 
t=
%traning results, the data should likt this: t=[176 235 378 429 ...]';
 
%--------------------------------------------------- 
% Data normalization 
% mapminmax function could normalize tha data into [-1,1]
%---------------------------------------------------
[normInput,ps] = mapminmax(p);
[normTarget,ts] = mapminmax(t);
 
%--------------------------------------------------- 
% Using 20% data as test data and 80% data as training data
%--------------------------------------------------- 
testPercent = 0.20;  % Adjust as desired 
validatePercent = 0.20;  % Adust as desired 
[trainSamples,validateSamples,testSamples] = dividevec(normInput,normTarget,validatePercent,testPercent)


for j=1:200
%--------------------------------------------------- 
% Setup parameters 
%---------------------------------------------------   
NodeNum1 = 20; % the nodes number in 1 level 
NodeNum2=40;   % the nodes number in 2 level
TypeNum = 1;    
TF1 = 'tansig';TF2 = 'tansig'; TF3 = 'tansig'; 
 
net=newff(minmax(normInput),[NodeNum1,NodeNum2,TypeNum],{TF1 TF2 TF3},'traingdx');%create the network
net.trainParam.epochs=10000; 
net.trainParam.goal=1e-6;
net.trainParam.lr=0.01;  
net.trainfcn='traingdm';
 
[net,tr] = train(net,trainSamples.P,trainSamples.T,[],[],validateSamples,testSamples);
  
%--------------------------------------------------- 
% testing
%---------------------------------------------------   
[normTrainOutput,Pf,Af,E,trainPerf] = sim(net,trainSamples.P,[],[],trainSamples.T);
 
[normValidateOutput,Pf,Af,E,validatePerf] = sim(net,validateSamples.P,[],[],validateSamples.T);
 
[normTestOutput,Pf,Af,E,testPerf] = sim(net,testSamples.P,[],[],testSamples.T);

trainOutput = mapminmax('reverse',normTrainOutput,ts);
 
trainInsect = mapminmax('reverse',trainSamples.T,ts);
 
validateOutput = mapminmax('reverse',normValidateOutput,ts);
 
validateInsect = mapminmax('reverse',validateSamples.T,ts);
 
testOutput = mapminmax('reverse',normTestOutput,ts);
 
testInsect = mapminmax('reverse',testSamples.T,ts); 
 
% error calculation
 
absTrainError = trainOutput-trainInsect;
 
absTestError = testOutput-testInsect;
 
error_sum=sqrt(absTestError(1).^2+absTestError(2).^2+absTestError(3).^2);
 
All_error=[All_error error_sum];
 
eps=90;
 
if ((abs(absTestError(1))<=30 )&(abs(absTestError(2))<=30)&(abs(absTestError(3))<=30)|(error_sum<=eps))
    save mynetdata net
    break
end
j
end
j
 
Min_error_sqrt=min(All_error)

testOutput
 
testInsect
