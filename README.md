# song-alarm-clock
Alarm clock that randomly selects user-chosen songs

## To run:

```
python -m flask run -p <your port> -h 0.0.0.0
```

TODO:

## Always running script:

* ~~Receive POST requests on port 8080~~ Done!
* (Verify it's from the website maybe??)
* Store it in database


## Script that runs every day at 6:30am:

* Make the cronjob to have it run
* Pick a random url from the database
* Use youtube-dl to download the audio
* Play it