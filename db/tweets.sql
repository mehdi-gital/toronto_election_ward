--Sets resets the database schemas
--Run this with psql
--Make sure you connect to the correct database within sql (use -d flag to specify)

DROP TABLE IF EXISTS Tweets, Hashtags, Users CASCADE;

CREATE TABLE Users (
    user_id bigint PRIMARY KEY,
    user_screen_name varchar(50),
    user_location varchar(50),
    user_time_zone varchar(60),
    user_followers_count integer,
    user_status_count integer
);

CREATE TABLE Tweets (
    id bigint PRIMARY KEY,
    created_at timestamptz,
    text VARCHAR(255),
    user_id bigint,
    FOREIGN KEY (user_id) REFERENCES Users (user_id),
    retweet_count integer
);

CREATE TABLE Hashtags (
    text VARCHAR(30),
    tweet_id bigint,
    FOREIGN KEY (tweet_id) REFERENCES Tweets (id)
);

