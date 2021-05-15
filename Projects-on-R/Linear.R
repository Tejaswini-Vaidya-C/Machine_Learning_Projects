#Connecting to MongoDb
install.packages("mongolite")
library(readxl)
pressure <- read_excel("F://DatasetR//pressure.xlsx") #Upload the data
c=mongo(collection="project1",db="practice1")
c$insert(pressure)
install.packages("readxl")
#Plotting the graph of the dataset
plot(pressure$Temperature, pressure$Pressure)
#Histogram of Pressure column
hist(pressure$Pressure)
lmTemp = lm(Pressure~Temperature, data = pressure)
View(pressure)
plot(pressure, pch = 16, col = "maroon") #Plot the results
abline(lmTemp) #Add a regression line
summary(lmTemp)
