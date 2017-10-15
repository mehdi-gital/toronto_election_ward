--Sets/resets the database schemas

DROP TABLE IF EXISTS Tweets, Hashtags, Users CASCADE;

CREATE TABLE Users (
    user_id integer PRIMARY KEY,
    user_screen_name varchar(50),
    user_location varchar(50),
    user_time_zone varchar(60),
    user_UTC_offset integer,
    user_followers_count integer,
    user_status_count integer
);

CREATE TABLE Tweets (
    id SERIAL PRIMARY KEY,
    created_at timestamptz,
    text VARCHAR(140),
    user_id integer,
    FOREIGN KEY (user_id) REFERENCES Users (user_id)
);

CREATE TABLE Hashtags (
    text VARCHAR(30),
    tweet_id integer,
    FOREIGN KEY (tweet_id) REFERENCES Tweets (id)
);

