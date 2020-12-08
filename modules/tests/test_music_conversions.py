# Unit testing for conversions

from musicconversions import *

def test_youtube_naming():
    urls = ['https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'https://www.youtube.com/watch?v=kffacxfA7G4', 'https://www.youtube.com/watch?v=h9ZGKALMMuc',
    'https://www.youtube.com/watch?v=E9s1ltPGQOo', 'https://www.youtube.com/watch?v=VKbWF1jwMhE']
    names = ["Rick Astley - Never Gonna Give You Up (Video)", "Justin Bieber - Baby (Official Music Video) ft. Ludacris",
    "Frank Sinatra - The Way You Look Tonight", "Mii Channel Music", "Aaliyah - One In A Million"]
    for index in range(len(urls)):
        assert get_results_youtube(urls[index]) == names[index]

def test_spotify_search():
    names = ["Rick Astley - Never Gonna Give You Up (Video)", "Justin Bieber - Baby (Official Music Video) ft. Ludacris",
    "Frank Sinatra - The Way You Look Tonight", "Mii Channel Music", "Aaliyah - One In A Million"]
    results = [
        ['Never Gonna Give You Up by Rick Astley', 'Never Gonna Give You Up - 7" Mix by Rick Astley', 'Never Gonna Give You Up by Rick Astley', 'Never Gonna Give You Up by Rick Astley', 'Never Gonna Give You Up - Pianoforte by Rick Astley', 'Never Gonna Give You Up - Pianoforte by Rick Astley', 'Never Gonna Give You Up by Rick Astley', 'Never Gonna Give You Up by Rick Astley', 'Never Gonna Give You Up - Pianoforte by Rick Astley', 'Never Gonna Give You Up by Rick Astley'],
        ['Baby by Justin Bieber, Ludacris', 'Baby - Acoustic Version by Justin Bieber', 'Baby by Justin Bieber, Ludacris', 'Baby by Justin Bieber, Ludacris', 'Baby by Justin Bieber, Ludacris', 'Baby by Justin Bieber, Ludacris', 'Baby by Justin Bieber, Ludacris', 'Baby by Justin Bieber, Ludacris', 'Baby by Justin Bieber, Ludacris', 'Baby by Justin Bieber, Ludacris'],
        ['The Way You Look Tonight by Frank Sinatra', 'The Way You Look Tonight by Frank Sinatra', 'The Way You Look Tonight - Remastered 2008 by Frank Sinatra', 'The Way You Look Tonight - Remastered 2008 by Frank Sinatra', 'The Way You Look Tonight by Frank Sinatra', 'The Way You Look Tonight (Lullaby version of Frank Sinatra) by Twinkle Twinkle Little Rock Star', 'The Way You Look Tonight by Christopher West', 'The Way You Look Tonight by Frank Sinatra', 'Frank Sinatra Dedication to Soldiers at Halloran Hospital, Staten Island, NY / The Way You Look Tonight (with Axel Stordahl & His Orchestra) by Frank Sinatra, Axel Stordahl And His Orchestra', 'The Way You Look Tonight by 101 Strings Orchestra'],
        ['Mii Channel (From "Nintendo Wii Mii Channel") by insaneintherainmusic, Gabe Nekrutman, Chris Allison', 'Mii Channel Theme by insaneintherainmusic, Gabe Nekrutman, Chris Allison', 'Mii Channel (From "Nintendo Wii") [Piano Version] by Streaming Music Studios', 'Mii Channel by FamilyJules, insaneintherainmusic, Adriana Figueroa, Zorsy', 'Mii Channel (From "Nintendo Wii Channels") [For Flute & Piano Duet] by Kazumi Totaka, daigoro789', 'Mii Channel (From "Nintendo Wii Channels") [For Piano Solo] by Kazumi Totaka, daigoro789'],
        ['Big Bad Mama by Foxy Brown, Dru Hill', 'So Bad by Camron, Nicki Minaj, Yummy', 'Secret Admirer by Lloyd, Pitbull', 'Penelope by 4 Wings', 'Aaliyah by Parris Chariz, ChasingRyan', 'You by Aaron Carpenter', 'Big Bad Mama - Radio Edit by Foxy Brown, Dru Hill', 'Secret Admirer by Pitbull, Lloyd', "Penelope - Original Mix from Cafe' Del Mar by 4 Wings", 'Do It Like We by WESTSIDE BOOGIE']
    ]
    for index in range(len(names)):
        out = get_results_spotify(names[index])
        assert out == results[index]

