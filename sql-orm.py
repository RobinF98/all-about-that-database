from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql+psycopg2://postgres:1234@localhost/chinook")
base = declarative_base()

# Creating class based models using base subclass
class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key = True)
    Name = Column(String)

class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key = True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))

class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key = True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key = False)
    GenreId = Column(Integer, primary_key = False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key = False)
    Bytes = Column(Integer, primary_key = False)
    UnitPrice = Column(Float)
    

Session = sessionmaker(db)

# open above created session
session = Session()

base.metadata.create_all(db)

# query 1
# artists = session.query(Artist)
# for artist in artists:
#     print(artist.ArtistId, artist.Name, sep="|")

# query 2
artist = session.query(Artist).filter_by(Name="Queen").first()
print(artist.ArtistId, artist.Name, sep="|")