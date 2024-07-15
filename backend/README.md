# Technical Assignment: RPS

## How To Run
- requirements: Docker or Orbstack
- should be as simple as the following commands:

```
make build
make migrate
make run
 ```
local should be running at localhost:8002/api/v1/*, postgres should be running at local:5432
database should be able to be updated via .env.
I did have a local template of my own that I used, but it was pretty bare bones, just docker development focused.
I spent some time cleaning it up for use here. 

## What is available 
  - I created 3 basic APIs (but docs are available at /api/v1/docs as well)
```
    POST /create
        - given game settings passed, initialize Game 
    GET /game/{game_token}
        - given token, return current game state,
         including scores and most recent turn
    POST /evaluate
        - given a turn, return who won, 
        nd wether or not the game is over

```
 - Addtionally, I've created a few models for the game
```
    Game
        - the initial set up for the game, includes settings json
        when the game was started and a unique identifier that is passed
        in case the game needs to be picked up again
    GameTurn
        - our score tracker for each subsiquent turn
        has a json for what each person played,
         and the winner if there was one
    GameTurnAggr
        - our score tracker for the Game, keeps a tally of
        each player wins, and has a null player for any ties
```

## Experience  
I was able to complete the basic API's in the game.
One would have the frontend create a json of settings, including player name etc. 
I am missing some basic validation of fields I'm looking for inside that json, but would have loved 
to get some time to fix that. The api returns the keys to the game which would 
be used in subsequent calls via /evaluate. 
I was not able to set up the /save function if they needed to save in the midddle of a turn
however, users should be able to reset up at their lastest score when getting their game
via the game_token get 
I also needed to drop handling the computer player. My assumption was the FE could create 
it's own 'player' and handle the random 'rps' selection. (I would just need to update
the settings to clarify if a player is input via person or automated )

all other turns go through the /evalute phase. which just returns results of the turn itself

If I had more time, I would love to actually have written some tests. I went through some manual QA
but just getting something automated would make a ton of difference when making iterations.

I also wasn't able to add in the minimal API key that I had gotten started. The deps file is there, 
but just didn't have time to throw it in. Eventually I want that to be a jwt, or session tokens if it's 
a guest who doesn't want to sign in. 

my dal layer is also very messy. I'd love to get it into a proper datamanager level for basic queries against
game/gameturn/gameaggr and then clean up the actual other functions. 

I also didn't get a chance to optimize my indicies for querying. especially if we eventually need to gain access to 
a game turn via a game uuid more often than not. I would take some more time to see if where I ended up was optimal or not. 
I'm sure there's more that I missed, and will be updating this README when I can. 

Additionally, I definitely thought I would have some time to fullstack it. That was *not* the case, hence the backend dir
there is a local frontend dir I did not push, as it just has a basic react app on top, and has not been hooked in via docker. 