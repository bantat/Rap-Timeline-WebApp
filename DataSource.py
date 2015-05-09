class DataSource:
    def __init__(self, artistID):
        this.artist = artistName
        this.artistID = artistID
        commonWords = []
        relatedArtists = []
        albums = []
        artistFilePath = ""
        artistInfo = ""
        
    def getArtist(self):
        """This method takes the artist name that has been stored as string, and returns
        that string.
        """
        # TODO Replace this with a real SQL call.
        artist = "NOT A REAL ARTIST"
        
        return artist
    
    def getArtistInfo(self):
        """This method takes the artist name, and creates a string that has a 300
        character description of the artist.
        """
        
        return artistInfo
    
    def getRelatedArtists(self):
        """This method takes the artist that has been passed, and returns a list of
        similar artist objects.
        """
    
        
        return relatedArtists
        
    def getCommonWords(self):
        """This method uses the artist string, goes through each song for the artist, and
        determines the common words for that artist. This returns a list with the most
        common word at the first index, and the least common word at the last index.
        """
        
        return commonWords
    
    def getAlbums(self):
        """This method takes the artist string this.artist, and finds the albums that the
        artist has produced, and returns them as a list.
        """
        
        return albums
    
    def getArtistImage(self):
        """This method uses the artist name to find the wikipedia image of the artist, and
        returns the the relative to the image.
        """
        
        return artistfilePath
    
    def getAlbumCover(self, album):
        """This method uses the artist name this.artist and an album name to find the
        cover to the album that has been provided. It then returns the relative filepath
        to this image.
        """
        
        return albumfilePath
    
    def getAlbumInfo(self, album):
        """This method takes the artist name and album name, and uses this information to
        get a 300 character blurb about the album, and then returns this as a string.
        """
        
        return albumInfo