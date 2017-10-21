# toronto_election_ward

### Setup

Just run it on AWS until we decide to fill this section properly :P

* Follow [this](https://help.github.com/articles/connecting-to-github-with-ssh/)
up to step 3 if you don't have an SSH key 

* Switching to postgres is in progress (I probably won't have a chance to connect to RDS until Sunday). For now, you can run the streamer locally with postgres if you have it installed. If your postgres username is 'postgres', the password is 'password', and your database is called 'election_ward' you can set up your tables with `psql -U postgres -p password -d election_ward -f db/tweets.sql`. The streamer should insert tweets correctly. 

## Dependencies (not comprehensive)

### Python (Can be pip installed)

* tweepy
* pymongo (if using mongo)
* psycopg2 (if using postgres)

### Node/npm

* https://nodejs.org/en/download/
* You can run `npm install` after installing npm to get the rest

### MongoDB

### PostgreSQL

## Troubleshooting
Coming soon...

## Tasks (maybe not necessary but would be nice to have)

* Process hashtags and add them to a separate table
* Detect retweets; if the retweet doesn't exist in the database, add it. Otherwise increment some `retweet_count` column on the original tweet instead of adding an entire new tweet.
* Add installation instructions
* Teach me SQLAlchemy
