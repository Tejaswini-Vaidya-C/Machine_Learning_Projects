install.packages("mongolite")
library("datasets")
data(iris)
c=mongo(collection="project",db="practice")
c$insert(iris)
plot(iris$Sepal.Length, iris$Sepal.Width)
hist(iris$Petal.Length)
irisVer <- subset(iris, Species == "versicolor")
irisSet <- subset(iris, Species == "setosa")
irisVir <- subset(iris, Species == "virginica")
par(mfrow=c(1,3),mar=c(6,3,2,1))
boxplot(irisVer[,1:4], main="Versicolor",ylim = c(0,8),las=2)
boxplot(irisSet[,1:4], main="Setosa",ylim = c(0,8),las=2)
boxplot(irisVir[,1:4], main="Virginica",ylim = c(0,8),las=2)

iris1 <- iris[-5]
View(iris1)
iris1 <- as.data.frame(scale(iris1))
View(iris1)
# K means Clustering
install.packages("NbClust")
install.packages("cluster")
library(NbClust)
library(cluster)
wssplot <- function(data,nc=15,seed=1234){
  wss <- (nrow(data)-1)*sum(apply(data,2,var))
  for(i in 2:nc){
    set.seed(seed)
    wss[i] <- sum(kmeans(data,centers=i)$withinss)
  }
  plot(1:nc,wss,type="b",xlab="no of clusters",ylab="within group of sum of squares")
}
wssplot(iris1,nc=15,seed=1234)
iriskmeans <- kmeans(iris1,7)
attributes(iriskmeans)
iriskmeans$cluster
iriskmeans$betweenss
clusplot(iris1,iriskmeans$cluster,lines=0)
