# в данной программе проводится анализ модельных данных данных о соотношении 
#среднего и высшего образования в американских школах.
#Про часть испытуемых известно, поступили они в университет или нет 
#(переменная admit, 1 = поступили, 0 = не поступили), а про остальных 
#таких данных нет (NA).
#на основании созданной логистической регрессионной модели
# был создан файл (в результате работы создается файл, в котором 


install.packages("ROCR")

library(ROCR)

df = read.csv("https://stepik.org/media/attachments/lesson/11478/data.csv")

df$admit = factor(df$admit)
str(df$admit)
df$rank = factor(df$rank)
    
model_df = glm(admit ~ rank * gpa, df, family = "binomial")
    
df_na = subset(df, is.na(df$admit) == TRUE)
    
df_na$prob = predict(model_df, newdata = df_na, type = "response")

pred_fit <- prediction(df_na$prob, df_na$prob_resp)
perf1  <- performance(pred_fit, x.measure = "cutoff", measure = "spec")
perf2  <- performance(pred_fit, x.measure = "cutoff", measure = "sens")
perf3  <- performance(pred_fit, x.measure = "cutoff", measure = "acc")

plot(perf1, col = "red", lwd =2)
plot(add=T, perf2 , col = "green", lwd =2)
plot(add=T, perf3, lwd =2)

legend(x = 0.6,y = 0.3, c("spec", "sens", "accur"), 
       lty = 1, col =c('red', 'green', 'black'), bty = 'n', cex = 1, lwd = 2)

#построенный график позволяет определить уровень вероятност как 0.4    
df_na$prob_resp = factor(ifelse(df_na$prob > 0.4, 1, 0), labels = c("N", "Y"))

install.packages("readr")
library (readr)

write_csv(df_na, "D:/R/Data_completed_for_NA.csv")

df_check = read.csv("D:/R/Data_completed_for_NA.csv")

sum(df_na$prob_resp)