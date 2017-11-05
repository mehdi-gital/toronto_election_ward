# toronto_election_ward

This repository holds code for our election ward project. You can learn more about our group/projects [here](http://torontodatascientistswithoutborders.github.io/projects/).

This README is for technical documentation. We have more general/in-depth information about this project on our [wiki](http://electionward.pbworks.com/w/page/120480486/Toronto%20Election%20Ward%20Project).

### Setup

Just run it on AWS until we decide to fill this section properly :P

* If you are interested in taking part but have no idea what's going on, ask someone for an invite to our slack channel. 

* Follow [this](https://help.github.com/articles/connecting-to-github-with-ssh/)
up to step 3 if you don't have an SSH key. Send your `id_rsa.pub` file to someone on slack to get access to AWS.

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

## To-do

Here are a few immediately obvious coding tasks that would benefit us. There is a more comprehensive to-do list for this project on the [wiki](http://electionward.pbworks.com/w/page/120480696/Tasks).

Contributions are welcome, even if they are very small. 

* Process hashtags and add them to a separate table
* Detect retweets; if the retweet doesn't exist in the database, add it. Otherwise increment some `retweet_count` column on the original tweet instead of adding an entire new tweet.
* Add an easy way to dump data to files that can be downloaded?
* Improve documentation

