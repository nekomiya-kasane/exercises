data <- read.csv("etf.csv")

# Q1
summary(data)
plot(data$H0A0, data$JNK)

correlation_test <- cor.test(data$H0A0, data$JNK)

print(correlation_test)

# Q2
model <- lm(H0A0 ~ JNK, data=data)
plot(model$fitted.values, model$residuals, xlab="Fitted Values", ylab="Residuals",
     main="Residuals vs Fitted Values")

qqnorm(model$residuals, main="Normal Q-Q Plot of Residuals")
qqline(model$residuals)

leverages <- hatvalues(model)
barplot(leverages, names.arg=rownames(data), xlab="Observation", ylab="Leverage",
        main="Leverages for Each Observation")
abline(h = mean(leverages) * 3, col = "blue", lty = 2)

cooks_dist <- cooks.distance(model)
barplot(cooks_dist, names.arg=rownames(data), xlab="Observation", ylab="Cook's Distance",
        main="Cook's Distances for Each Observation")
abline(h = 0.5, col = "blue", lty = 2)
abline(h = 1.0, col = "red", lty = 2)

cooks_dist[cooks_dist > 0.5]

# Q3
resimean <- mean(model$residuals)
stderr <- sd(model$residuals) / sqrt(length(model$residuals))

t_statistic <- (resimean - 0) / stderr

df <- length(model$residuals) - 1

p_value <- 2 * pt(-abs(t_statistic), df)

cat("T-statistic:", t_statistic, "\n")
cat("P-value:", p_value, "\n")

# Q4
coefficients <- coef(model)
standard_errors <- sqrt(diag(vcov(model)))
print(model)
print(coefficients)
print(standard_errors)

alpha <- 0.05
t_values <- coefficients / standard_errors
p_values <- 2 * pt(-abs(t_values), df = nrow(data) - 2)
print(t_values)
print(p_values)

# Q5
anova_table <- anova(model)
print(anova_table)

rsquared <- summary(model)$r.squared
print(rsquared)

# Q6
predicted_h0a0 <- predict(model, newdata = data.frame(JNK = 37.55))
print(predicted_h0a0)

conf_level <- 0.99
conf_interval <- predict(model, newdata = data.frame(JNK = 37.55),
                         interval = "confidence", level = conf_level)
print(conf_interval)
