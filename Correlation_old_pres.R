setwd("/Users/imyyounge/Documents/4_Masters/ai_hack/AiHack")
age <- read.csv("gp_prac_age_distribution.csv")
ftw <- read.csv("040201.csv")
summary(age)
summary(ftw)
head(ftw)
dim(ftw)

library(ggplot2)
library(dplyr)

age[age$AGEINT =='ALL'] <- NULL

age2 <- subset(age, AGEINT < 45, select=c(ONS_CODE, AGE_GROUP_5, NUMBER_OF_PATIENTS))
as.numeric(levels(age$AGE_GROUP_5))[age$AGE_GROUP_5]
model1 <- lm(AGE_GROUP_5 ~ NUMBER_OF_PATIENTS, data=age2)




age2 <- age %>% select(as.character(40_44, 45_49, 50_54, 55_59, 60_64, 65_69))
age3 <- age %>% select("40_45")
ggplot(age, aes(x=AGE_GROUP_5, y=NUMBER_OF_PATIENTS)) + geom_boxplot()

ggplot(age, aes(x=AGE_GROUP_5, y=log(NUMBER_OF_PATIENTS))) + geom_boxplot(colour="##0072B2")+
  labs(x="Log(Number of Patients)", y="Age group (bands of 5)") + 
  theme_dark()


