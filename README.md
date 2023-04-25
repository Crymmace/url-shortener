# url-shortener
## Project Description
This application is a basic url encoder/decoder that could be used for shortening urls.

## How it works
### Encoding
- You can run this application by running main.py
- The application will ask if you'd like to encode or decode your url.
- Selecting "encode" will then ask for a url.
- Provide the url and the program will validate the url and add it to the database along with a random code number.
- The program will then provide you with your encoded url. _ex. example.com/{code}_

### Decoding
- If you select "decode" the application will then ask for the url.
- Provide the url and the application will compare your entry with the entries in the database.
- If it finds a match it will provide you with the original url. _ex. https://youtube.com_


## What I used
I used sqlite3 for the database. Mostly because of the little time that it 
took to set up and the ease of use for a small project like this.

For url validation I used "validators."

## Extras
In the "decoding" section, you don't have to provide the url. 
Instead, you can just provide the code number. You should be able to decode that way as well.

For the random code generator, the seed that I use is determined by system time. That will soon be deprecated in
newer versions of Python so keep that in mind.

## Reasons for this project
1. I mostly just wanted to write a short program in my free time to keep my brain occupied.
2. I had absolutely no idea how tiny urls worked, and I wanted to learn.
