from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rating = Column(Float)


class Projections(Base):
    __tablename__ = "projections"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    movie = relationship("Movie", backref="projects")
    type = Column(String)
    date = Column(String)
    time = Column(String)


class Reservations(Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    projection_id = Column(Integer, ForeignKey("projections.id"))
    reservation = relationship("Projections", backref="reserv")
    row = Column(Integer)
    col = Column(Integer)


engine = create_engine("sqlite:///cinema.db")
# will create all tables
Base.metadata.create_all(engine)

# Session is our Data Mapper
session = Session(bind=engine)


session.add_all([
    Movie(name="The Hunger Games: Catching Fire", rating=7.9),
    Movie(name="Wreck-It Ralph", rating=7.8),
    Movie(name="Her", rating=8.3)])

session.commit()

hunger_games = session.query(Movie).filter(
    Movie.name == "The Hunger Games: Catching Fire").one()
hunger_games.projects = [
    Projections(
        type="3D", date="2014-04-01", time="19:10"),
    Projections(
        type="2D", date="2014-04-01", time="19:00"),
    Projections(
        type="4DX", date="2014-04-02", time="21:00")]
session.commit()

wreck_it = session.query(Movie).filter(Movie.name == "Wreck-It Ralph").one()
wreck_it.projects = [
    Projections(type="3D", date="2014-04-02", time="22:00"),
    Projections(type="2D", date="2014-04-02", time="19:30")]

her = session.query(Movie).filter(Movie.name == "Her").one()
her.projects = [Projections(type="2D", date="2014-04-05", time="20:20")]
session.commit()


hg_proj = session.query(Projections).filter(Projections.id==1).one()

hg_proj.reserv = [Reservations(username="RadoRado", row=2, col=1), Reservations(
    username="RadoRado",  row=7, col=8), Reservations(username="RadoRado", row=3, col=5)]

session.commit()

# reservation4 = Reservations(username="Ivo", projection_id=3, row=1, col=1)
# reservation5 = Reservations(username="Ivo", projection_id=3, row=1, col=2)
# reservation6 = Reservations(
#     username="Mysterious", projection_id=5, row=2, col=3)
# reservation7 = Reservations(
#     username="Mysterious", projection_id=5, row=2, col=4)
def show_movies():
    all_movies = session.query(Movies).all()
    for movie in all_movies:
        print(movie)
