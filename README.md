# Python Discord Bot

>Discord is a proprietary freeware voice-over-Internet Protocol (VoIP) application designed for gaming communities, that specializes in text and audio communication between users in a chat channel.

>Small basic python discord bot that joins private server. Never programmed anything in python before so the discord python API seemed like a good learning exercise.

### Features

- Programmed several commands
  - !online - See who is online.
  - !random - Pick a random user.
  - !ban - Ban a user from the server. (Checks if person saying command is a moderator)
  - !unban - Unban a user from the server. (Checks if person saying command is a moderator, must include ID number in the name to work)
  - !joinvoice - Send me to a voice channel. (need channel id#)
  - !kick - Kick a user from the server. (Checks if person saying command is a moderator)
  - !song - picks a random song from songs file.
  - !addsong - write a song to the song file. (youtube link prefered)
  - !calc - calculate an equation, supported operators = +, /, -, *, %

- Programmed several alerts on server/member changes
  -name changes (includes what it was originally to what it was changed to)
  -role changes (includes what it was originally to what it was changed to)
  -new member joins
  -member leaves
  -new channel made 
  -channel deleted
  -channel name or description change (includes what it was originally to what it was changed to)
