install.packages("mongolite")
mydata <- read.csv("F://DatasetR//binary.csv",header=TRUE)
c=mongo(collection="project2",db="practice2")
c$insert(mydata)

##Logistic Regression
##Classify student application as admit or reject
##Independent variable ##gre gpa rank
#mydata <- read.csv("F://DatasetR//binary.csv",header=TRUE)
str(mydata)
mydata$admit <- as.factor(mydata$admit)
mydata$rank <- as.factor(mydata$rank)
#two way table to check whether we have null values or not
xtabs(~admit + rank,data = mydata)
#Partition data train 80% test 20%
set.seed(1234)
ind <- sample(2,nrow(mydata),replace=T,prob=c(0.8,0.2))
train <- mydata[ind==1,]
test <- mydata[ind==2,]
#logistic regression model glm
mymodel <- glm(admit ~ gpa + rank,data=train,family="binomial")
summary(mymodel)
#Prediction
p1 <- predict(mymodel,train,type='response')
head(p1)
#misprediction error train data
pred1 <- ifelse(p1>0.5,1,0)
tab1 <- table(Predicted=pred1,Actual=train$admit)
tab1
#misprediction error test data
p2 <- predict(mymodel,test,type="response")
pred2 <- ifelse(p2>0.5,1,0)
tab2 <- table(Predicted=pred2,Actual=test$admit)
tab2
