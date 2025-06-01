library(dplyr)
library(ggplot2)

# View and clean iris dataset
head(iris)
filtered_data <- filter(iris, Sepal.Length > 5)
plot(iris$Sepal.Length)
