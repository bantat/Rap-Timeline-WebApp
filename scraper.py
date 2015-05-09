__author__ = 'torebanta'

import urllib2
import psycopg2

def scrapeSummaryFromWiki(artist_name):
    print "Getting summary for " + artist_name
    title = artist_name
    params = { "format":"json", "action":"query", "prop":"extracts", "exintro":"", "explaintext":""}
    params["titles"] = "%s" % urllib2.quote(title.encode("utf8"))
    querystring = "&".join("%s=%s" % (k, v) for k, v in params.items())
    url = "http://en.wikipedia.org/w/api.php?%s" % querystring
    response = urllib2.urlopen(url)

    for line in response:
        text_split = line.split(":", 7)
        extract_front = text_split[len(text_split) - 1]

    for i in range(len(extract_front) - 1, 0, -1):
        if extract_front[i] != "}":
            extract = extract_front[:i]
            break

    extract = extract[1:]

    # extract = extract.decode('string_escape').encode('ascii','ignore')
    # extract = extract.replace("\u","")

    return extract

def getImageUrlFromWiki(article_title):
    print "Getting image for " + article_title
    title = article_title
    params = { "format":"json", "action":"query", "prop":"pageimages", "piprop":"original"}
    params["titles"] = "%s" % urllib2.quote(title.encode("utf8"))
    querystring = "&".join("%s=%s" % (k, v) for k, v in params.items())
    url = "http://en.wikipedia.org/w/api.php?%s" % querystring
    response = urllib2.urlopen(url)

    for line in response:
        text_split = line.split(":", 8)
        extract_front = text_split[len(text_split) - 1]

    for i in range(len(extract_front) - 1, 0, -1):
        if extract_front[i] != "}":
            extract = extract_front[:i]
            break

    extract = extract[1:]

    return extract

def getImageNameFromUrl(url):
    text_split = url.split("/")
    extract = text_split[len(text_split) - 1]

    return extract

def generateSqlFromAlbums(file_path):

    albums = []

    sql_str = "DROP TABLE IF EXISTS albums;\n"
    sql_str += "CREATE TABLE albums (name text, description text, image text, year int, artist text);\n"

    with open(file_path) as file:
        for line in file:
            line_split = line.split(";")
            album_name = line_split[0]
            album_year = line_split[1]
            album_artist = line_split[2]
            album_list = [album_name, album_year, album_artist]
            albums.append(album_list)

    db_connection = psycopg2.connect(user="bantat",database="bantat",password="mike494java")

    cursor = db_connection.cursor()

    for album in albums:
        name = album[0].strip()
        description = scrapeSummaryFromWiki(name)
        image = getImageUrlFromWiki(name)
        year = album[1]
        artist = album[2].strip()
        # name = name.replace("'","''").replace('"',"\"\"")
        # description = description.replace("'","''").replace('"',"\"\"")
        # image = image.replace("'","''").replace('"',"\"\"")
        # artist = artist.replace("'","''").replace('"',"\"\"")
        sql_str += cursor.mogrify("INSERT INTO albums (name, description, image, year, artist) VALUES (%s, %s, %s, %s, %s)", (name, description, image, year, artist))
        sql_str += ";\n"

    return sql_str

def generateImageLinksFromAlbums(file_path):

    albums = []
    with open(file_path) as file:
        for line in file:
            line_split = line.split(";")
            album_name = line_split[0]
            albums.append(album_name)

    output = open("album_links.txt","w")

    for album in albums:
        name = album.strip()
        output.write(getImageUrlFromWiki(name) + "\n")

    output.close()

def generateImageLinksFromArtists(file_path):

    artists = []

    with open(file_path) as file:
        for line in file:
            artist_name = line
            artists.append(artist_name)

    output = open("artist_links.txt","w")

    for artist in artists:
        name = artist.strip()
        output.write(getImageUrlFromWiki(name) + "\n")

    output.close()

def generateSqlFromArtists(file_path):

    artists = []
    sql_str = "DROP TABLE IF EXISTS artists;\n"
    sql_str += "CREATE TABLE artists (name text, description text, image text);\n"

    with open(file_path) as file:
        for line in file:
            artist_name = line
            print "Reading in artist " + artist_name
            artists.append(artist_name)

    db_connection = psycopg2.connect(user="bantat",database="bantat",password="mike494java")

    cursor = db_connection.cursor()

    for artist in artists:
        name = artist.strip()
        description = scrapeSummaryFromWiki(name)
        image = getImageUrlFromWiki(name)
        # name = name.replace("'","''").replace('"',"\"\"")
        # description = description.replace("'","''").replace('"',"\"\"")
        # image = image.replace("'","''").replace('"',"\"\"")

        sql_str += cursor.mogrify("INSERT INTO artists (name, description, image) VALUES (%s, %s, %s)", (name, description, image))
        sql_str += ";\n"

    return sql_str


if __name__ == "__main__":
    output = open("populate.sql","w")
    print "Generating Artist SQL"
    output.write(generateSqlFromArtists("artists.txt"))
    print "Generating Album SQL"
    output.write(generateSqlFromAlbums("albums.txt"))