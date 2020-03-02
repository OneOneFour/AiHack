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


library(gridExtra)

theme_black = function(base_size = 12, base_family = "") {
  
  theme_grey(base_size = base_size, base_family = base_family) %+replace%
    
    theme(
      # Specify axis options
      axis.line = element_blank(),  
      axis.text.x = element_text(size = base_size*0.8, color = "white", lineheight = 0.9),  
      axis.text.y = element_text(size = base_size*0.8, color = "white", lineheight = 0.9),  
      axis.ticks = element_line(color = "white", size  =  0.2),  
      axis.title.x = element_text(size = base_size, color = "white", margin = margin(0, 10, 0, 0)),  
      axis.title.y = element_text(size = base_size, color = "white", angle = 90, margin = margin(0, 10, 0, 0)),  
      axis.ticks.length = unit(0.3, "lines"),   
      # Specify legend options
      legend.background = element_rect(color = NA, fill = "black"),  
      legend.key = element_rect(color = "white",  fill = "black"),  
      legend.key.size = unit(1.2, "lines"),  
      legend.key.height = NULL,  
      legend.key.width = NULL,      
      legend.text = element_text(size = base_size*0.8, color = "white"),  
      legend.title = element_text(size = base_size*0.8, face = "bold", hjust = 0, color = "white"),  
      legend.position = "right",  
      legend.text.align = NULL,  
      legend.title.align = NULL,  
      legend.direction = "vertical",  
      legend.box = NULL, 
      # Specify panel options
      panel.background = element_rect(fill = "black", color  =  NA),  
      panel.border = element_rect(fill = NA, color = "white"),  
      panel.grid.major = element_line(color = "grey35"),  
      panel.grid.minor = element_line(color = "grey20"),  
      panel.margin = unit(0.5, "lines"),   
      # Specify facetting options
      strip.background = element_rect(fill = "grey30", color = "grey10"),  
      strip.text.x = element_text(size = base_size*0.8, color = "white"),  
      strip.text.y = element_text(size = base_size*0.8, color = "white",angle = -90),  
      # Specify plot options
      plot.background = element_rect(color = "black", fill = "black"),  
      plot.title = element_text(size = base_size*1.2, color = "white"),  
      plot.margin = unit(rep(1, 4), "lines")
      
    )
  
}

age2 <- age %>% select(as.character(40_44, 45_49, 50_54, 55_59, 60_64, 65_69))
age3 <- age %>% select("40_45")
ggplot(age, aes(x=AGE_GROUP_5, y=NUMBER_OF_PATIENTS)) + geom_boxplot()

ggplot(age, aes(x=AGE_GROUP_5, y=log(NUMBER_OF_PATIENTS))) + geom_boxplot(colour="darkgrey")+
  labs(x="Log(Number of Patients)", y="Age group (bands of 5)") + 
  theme_black()


