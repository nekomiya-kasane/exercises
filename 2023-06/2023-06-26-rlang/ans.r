library(ggplot2)
library(magrittr)
library(ggplot2)
library(ggthemes)
library(data.table)
library(dplyr)
library(tidyr)
library(plotly)
library(psych)
library(LogicReg)
library(GGally)
library(boot)
library(leaps)
library(hrbrthemes)

movies <- read.csv("https://raw.githubusercontent.com/idc9/stor390/master/data/movies.csv")
summary(movies)
head(movies)
colnames(movies)

sum(is.na(movies))
movies <- na.omit(movies)

## The relevence of two ratings
main_genre <- movies %>%
      count(genre) %>%
      arrange(desc(n)) %>%
      filter(n > 20) %>%
      pull(genre) # nolint: line_length_linter.
main_genre_movies <- movies %>% filter(genre %in% main_genre)

tomato_desc <- c("Certified Fresh", "Fresh", "Rotten")
general_desc <- c("Good", "Medium", "Poor")
main_genre_movies$critics_rating <- factor(
      main_genre_movies$critics_rating,
      levels = tomato_desc, labels = general_desc
)
main_genre_movies <- main_genre_movies %>% mutate(vote_weight = imdb_num_votes / max(imdb_num_votes)) # nolint: line_length_linter.

lm_fit_w <- lm(imdb_rating ~ audience_score,
      data = main_genre_movies,
      weights = imdb_num_votes
)
summary(lm_fit_w)
lm_fit <- lm(imdb_rating ~ audience_score,
      data = main_genre_movies,
)
summary(lm_fit)
cor(main_genre_movies$imdb_rating, main_genre_movies$audience_score)

img <- ggplot(data = main_genre_movies, aes(
      x = audience_score, y = imdb_rating, s = imdb_num_votes
)) +
      geom_jitter(mapping = aes(
            x = audience_score, y = imdb_rating,
            color = genre, size = imdb_num_votes, shape = critics_rating
      ), alpha = 0.5) +
      stat_smooth(
            method = "lm", color = "#0095ff", fill = "#0095ff", alpha = 0.2
      ) +
      stat_smooth(
            method = "lm", color = "orange",
            mapping = aes(weight = imdb_num_votes),
            fill = "orange",
            alpha = 0.2
      ) +
      scale_x_continuous() +
      scale_y_continuous() +
      scale_size(range = c(2, 7)) +
      theme_light() +
      theme(
            legend.position = "right", legend.key = element_blank(),
            axis.text = element_text(size = 10),
            axis.title = element_text(size = 12)
      ) +
      labs(
            x = "Rotten Tomatoes - Rating", y = "IMDB-Rating",
            title = "IMDB vs Rotten Tomatoes Rating", color = "Genres",
            shape = "Quality of Reviews (Rotten Tomatoes)",
            size = "Number of IMDB votes"
      )
img

ggsave("imdb-tomato.svg", img)

## actor's
data_selected <- movies %>% select(actor1, actor2, actor3, actor4, actor5, genre, title) # nolint: line_length_linter.
data_melted <- data_selected %>%
      pivot_longer(cols = starts_with("actor"), names_to = "actor_num", values_to = "actor_name") %>%
      select(-actor_num)
data_aggregated <- data_melted %>%
      group_by(actor_name, genre, title) %>%
      summarise() %>%
      group_by(actor_name) %>%
      count() %>%
      arrange(desc(n))
print(data_aggregated, n = 100)

## movies count predict
movie_counts <- movies %>%
      group_by(thtr_rel_year) %>%
      count()
movie_counts$thtr_rel_year <- as.Date(
      paste0(movie_counts$thtr_rel_year, "-01-01")
)
movie_counts <- movie_counts[order(movie_counts$thtr_rel_year), ]
movie_counts_ts <- ts(movie_counts$n,
      start = c(year(movie_counts$thtr_rel_year[1]), 1), frequency = 1
)
ar_model <- ar(movie_counts_ts, order.max = 10)
ar_model
future_ts <- predict(ar_model, n.ahead = 7)
future_ts
future_df <- data.frame(
      thtr_rel_year = seq(as.Date("2015-01-01"), by = "year", length.out = 7),
      n = future_ts$pred
)
future_df

ggplot(data = movie_counts, aes(thtr_rel_year, n)) +
      geom_line(color = "#0095ff", size = 1) +
      xlim(c(as.Date("1970-01-01"), as.Date("2021-01-01"))) +
      geom_line(
            data = future_df, aes(x = thtr_rel_year, y = n),
            color = "orange", size = 1
      ) +
      scale_x_continuous() +
      scale_y_continuous() +
      scale_size(range = c(2, 7)) +
      theme_light() +
      theme(
            legend.position = "right", legend.key = element_blank(),
            axis.text = element_text(size = 10),
            axis.title = element_text(size = 12)
      ) +
      labs(
            x = "Year", y = "Movie Count",
            title = "Movie Count Prediction by AR model", color = "Genres",
      )

# factor analysis
movies$best_pic_win <- ifelse(movies$best_pic_win == "yes", 1, 0)
movies$best_pic_nom <- ifelse(movies$best_pic_nom == "yes", 1, 0)
movies$best_actor_win <- ifelse(movies$best_actor_win == "yes", 1, 0)
movies$best_actress_win <- ifelse(movies$best_actress_win == "yes", 1, 0)
movies$best_dir_win <- ifelse(movies$best_dir_win == "yes", 1, 0)
movies$top200_box <- ifelse(movies$top200_box == "yes", 1, 0)
movies$priorty <- movies$best_pic_win + movies$best_actor_win +
      movies$best_actress_win + movies$best_dir_win + movies$top200_box +
      0.5 * movies$best_pic_nom

group1 <- subset(movies, priorty >= 0.5)
group2 <- subset(movies, priorty < 0.5)

t.test((group1 %>% filter(imdb_num_votes > 2000))$imdb_num_votes,
      (group2 %>% filter(imdb_num_votes > 2000))$imdb_num_votes,
      paired = FALSE, var.equal = FALSE, weights = priorty
)
t.test(group1$imdb_num_votes, group2$imdb_num_votes,
      paired = FALSE, var.equal = FALSE, weights = priorty
)

# Data set 2
library(ISLR2)
summary(Auto)

auto <- data.frame(Auto)
sum(is.na(auto))
auto <- na.omit(auto)

auto$cylinders_f <- as.factor(auto$cylinders)
auto$origin_f <- as.factor(auto$origin)
summary(auto)
nrow(auto)

pairs(~ mpg + displacement + weight +
      horsepower + acceleration, data = auto)

# Validation set
train <- sample(c(TRUE, FALSE), nrow(auto), replace = TRUE)
summary(train)
test <- !train
regfit_best <- regsubsets(mpg ~ ., data = auto[train, ], nvmax = 19)
lm_fit <- lm(mpg ~ horsepower, auto, train)
mean((mpg - predict(lm_fit, auto))[-train]^2)
summary(lm_fit)
confint(lm_fit)

# k-fold
errs <- rep(0, 10)
for (i in 1:10) {
      glm_fit <- glm(mpg ~ poly(horsepower, i), data = auto)
      errs[i] <- cv.glm(auto, glm_fit, K = 10)$delta[1]
}
errs

# bootstrap
boot_fn_1 <- function(data, index) {
      coef(lm(mpg ~ horsepower, data = auto, subset = index))
}
boot_fn_2 <- function(data, index) {
      coef(lm(mpg ~ horsepower + I(horsepower^2),
            data = auto,
            subset = index
      ))
}
boot_fn_1(auto, seq_len(nrow(auto)))
boot_fn_1(auto, sample(nrow(auto), nrow(auto), replace = T))
boot(auto, boot_fn_1, 1000)
summary(lm(mpg ~ horsepower, data = auto))$coef
boot_fn_2(auto, seq_len(nrow(auto)))
boot_fn_2(auto, sample(nrow(auto), nrow(auto), replace = T))
boot(auto, boot_fn_2, 1000)
summary(lm(mpg ~ horsepower + I(horsepower^2), data = auto))$coef

## IRIS
library(MVTests)
iris_img_1 <- ggplot(iris, aes(
      x = Sepal.Length, y = Sepal.Width,
      color = Species
)) +
      geom_point(size = 6) +
      theme_light() +
      scale_x_continuous() +
      scale_y_continuous() +
      scale_size(range = c(2, 7)) +
      labs(
            x = "Sepal.Length", y = "Sepal.Width",
            title = "Sepal size", color = "Species",
      )
iris_img_1

iris_img_2 <- ggplot(iris, aes(
      x = Petal.Length, y = Petal.Width,
      color = Species
)) +
      geom_point(size = 6) +
      theme_light() +
      scale_x_continuous() +
      scale_y_continuous() +
      scale_size(range = c(2, 7)) +
      labs(
            x = "Petal.Length", y = "Petal.Width",
            title = "Sepal size", color = "Species",
      )
iris_img_2

iris_img_3 <- ggpairs(iris, mapping = aes(color = Species))
iris_img_3

ggsave("iris_1.svg", iris_img_1)
ggsave("iris_2.svg", iris_img_2)
ggsave("iris_3.svg", iris_img_3)

summary(iris)
library(NbClust)
library(factoextra)
library(cluster)
library(class)
library(dendextend)
library(e1071)

library(rpart)
library(rpart.plot)

library(colorspace)
library(ggraph)
library(GGally)

nrow(iris)

# knn
train <- sample(150, 50)
test <- sample(150, 50)
xs <- iris[, 1:4]
knn_model <- knn(train = xs[train, ], test = xs[test, ], iris$Species[train])
knn_model

res <- table(knn_model, iris$Species[test])
knitr::kable(
      res,
      caption = "kNN classification result",
      booktabs = TRUE
)

# decision tree
indx <- sample(150, 100)
train <- iris[indx, ]
test <- iris[-indx, ]
dt_model <- rpart::rpart(Species ~ .,
      data = train,
      method = "class"
)
rpart.plot::rpart.plot(dt_model, main = "Conditional Inference Tree for Iris")

p <- predict(dt_model, test, type = "class")
res <- table(p, test$Species)
knitr::kable(
      res,
      caption = "Decision tree result",
      booktabs = TRUE
)

library(party)
tree <- ctree(Species ~ ., data = iris)
plot(tree, main = "Conditional Inference Tree for Iris")
table(predict(tree), iris$Species)

# Naive Bayes
library(MASS)
iris_beyes <- lda(Species ~ ., data = iris, prior = c(1, 1, 1) / 3)
table <- table(iris$Species, predict(iris_beyes, iris)$class)
knitr::kable(table, caption = "Navie Beyes result", booktabs = TRUE)
sum(diag(prop.table(table)))

library(e1071)
naive_iris <- NaiveBayes(iris$Species ~ ., data = iris)
plot(naive_iris)

# svm
library(tune)
set.seed(2)
iris_svm <- svm(Species ~ ., data = iris)
pre_forest <- predict(iris_svm, iris, type = "class")
table <- table(pre.forest, iris$Species)
knitr::kable(
      res,
      caption = "SVM result",
      booktabs = TRUE
)
sum(diag(prop.table(table)))
plot(iris_svm, iris, Petal.Width ~ Petal.Length,
      slice = list(Sepal.Width = 3, Sepal.Length = 4)
)

iris_svm <- tune.svm(Species ~ .,
      data = train,
      gamma = 10^(-6:-1), cost = 10^(1:2)
)
summary(iris_svm)
iris_tuned <- svm(Species ~ ., data = train, gamma = 0.01, cost = 10)
summary(iris_tuned)
pred <- predict(iris_tuned, test)
table <- table(pred, test$Species)
knitr::kable(
      table,
      caption = "SVM result 2",
      booktabs = TRUE
)

# Quadratic
decisionplot_ggplot <- function(model,
                                vars,
                                data,
                                resolution = 100,
                                showgrid = TRUE,
                                ...,
                                modes.means) {
      if (missing(model) || missing(vars) || missing(data)) {
            stop("model, vars or data is missing")
      }
      if (!(is.character(vars) && length(vars) == 2) && !("formula" %in% class(vars) && length(vars <- all.vars(vars)) == 2)) {
            stop("vars should be either a formula or a character vector oflength 2.")
      }
      if (!is.data.frame(data)) {
            stop("data does not seem to comform with standard types.")
      }

      t <- terms(model)
      if (!all((other.vars <- attr(t, "term.labels")) %in% colnames(data))) {
            stop("data is missing one or more variables in model.")
      }
      lhs <- as.character(t[[2]])
      # Set up data for prediction, for the data in vars
      prd.vars <- lapply(data[, vars], function(x) {
            if (is.character(x) || is.factor(x)) {
                  unique(x)
            } else {
                  r <- range(x)
                  seq(r[1], r[2], length.out = resolution)
            }
      })
      names(prd.vars) <- vars
      # set up data for prediction for the remaining data
      if (missing(modes.means)) {
            other.vars <- other.vars[!other.vars %in% vars]
            if (length(other.vars)) {
                  modes.means <- lapply(data[, other.vars], function(x) {
                        if (is.character(x)) {
                              unique(x)[1]
                        } else if (is.factor(x)) {
                              levels(x)[1]
                        } else {
                              mean(x)
                        }
                  })
                  names(modes.means) <- other.vars
            } else {
                  modes.means <- NULL
            }
      } else {
            if (is.null(other.vars)) {
                  stop("other.vars is null but modes.means was provided. Please leave this missing.")
            }
            if (!all(other.vars %in% names(modes.means))) {
                  stop("modes.means are lacking one or more variables.")
            }
            modes.means <- as.list(modes.means)
            if (any(lengths(modes.means) > 1)) {
                  stop("modes.means should only contain a single values for all variables.")
            }
      }
      prd.data <- expand.grid(c(prd.vars, modes.means))
      p <- predict(model, prd.data, ...)
      prd.data$nm <- if (is.list(p)) {
            p$class
      } else {
            p
      }
      names(prd.data)[ncol(prd.data)] <- lhs
      # Create the final plot.
      gg <- ggplot(aes_string(vars[1], vars[2]), data = data) +
            geom_point(aes_string(col = lhs, shape = lhs), size = 3) +
            geom_contour(aes_string(vars[1], vars[2], z = paste0("as.integer(", lhs, ") + 1L")), data = prd.data, inherit.aes = FALSE)
      if (showgrid) {
            gg <- gg +
                  geom_point(aes_string(vars[1], vars[2], col = lhs), data = prd.data, shape = 20, size = 0.5)
      }
      gg
}

iris_qda <- qda(Species ~ ., data = iris, cv = T)
table <- table(iris$Species, predict(iris_qda, iris)$class)
knitr::kable(
      table,
      caption = "Quadratic result ",
      booktabs = TRUE
)
sum(diag(prop.table(table)))
img <- decisionplot_ggplot(iris_qda, Sepal.Length ~ Petal.Length, iris, showgrid = TRUE)
img
ggsave("iris_slpl.svg", img)
img <- decisionplot_ggplot(iris_qda, Sepal.Width ~ Petal.Width, iris, showgrid = TRUE)
img
ggsave("iris_swpw.svg", img)
# Logistic
library(nnet)
iris_log <- multinom(Species ~ ., data = train)
summary(iris_log)
pred <- predict(iris_log, test, type = "class")
table <- table(pred, test$Species)
knitr::kable(
      table,
      caption = "Logistic regression result ",
      booktabs = TRUE
)
sum(diag(prop.table(table)))
