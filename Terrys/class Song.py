class Song:
    def __init__(self, title, artist, duration_seconds):
        self.title = title
        self.artist = artist
        self.duration_seconds = duration_seconds
    def show_details(self):
        return f"Song Title : {self.title}, Artist : {self.artist}, Duration : {self.duration_seconds}"
class Playlist:
    def __init__(self, playlist_name):
        self.playlist_name = playlist_name
        
        self.songs = []
    def add_song(self, song_object):
        self.songs.append(song_object)
    def list_of_songs(self):
        for song in self.songs:
            print(song.show_details())
    def remove_song(self, title):
        for song in self.songs:
            if song.title == title:
                self.songs.remove(song)
                
                
song1 = Song("Bohemian Rhapsody" , "Queen", 354)
song2 = Song("Blinding Lights", "The Weekend", 200)
song3 = Song("Shape of You", "Ed Sheeran", 234)

my_playlist = Playlist("My Favourites")
my_playlist.add_song(song1)
my_playlist.add_song(song2)
my_playlist.add_song(song3)

print("---After adding songs---")
my_playlist.list_of_songs()

my_playlist.remove_song("Blinding Lights")

print("---After removing song")
my_playlist.list_of_songs()


class Robot:
    def __init__(self, name, model, battery_level):
        self.name = name
        self.model = model
        self.battery_level = battery_level
    def perform_task(self):
        return "placeholder"
    def describe(self):
        return f"Name: {self.name}, Model: {self.model}, Battery level: {self.battery_level}"
class MedicalRobot(Robot):
    def __init__(self, name, model, battery_level, specialization):
        super().__init__(name, model, battery_level)
        self.specialization = specialization
    def perform_task(self):
        return f"Name : {self.name} is performing a medical procedure in the {self.specialization} field"
medical_robot = MedicalRobot("ARIA", "MedBot-7", "95", "Cardiology")
print(medical_robot.perform_task())
print(medical_robot.describe())


class Sensor:
    def __init__(self, sensor_id, location,):
        self.sensor_id = sensor_id
        self.location = location
    def display_info(self):
        return f"Sensors ID {self.sensor_id}, Sensors location {self.location}"
class TrafficSensor(Sensor):
    def __init__(self, sensor_id, location, vehicle_count):
        super().__init__(sensor_id, location)
        self.vehicle_count = vehicle_count
    def report_traffic(self):
        return f"Current vehicle count: {self.vehicle_count}"    
    
class AirQualitySensor(Sensor):
    def __init__(self, sensor_id, location, pollution_index):
        super().__init__(sensor_id, location)
        self.pollution_index = pollution_index
    def check_air_quality(self):
        return f"Current pollution index is : {self.pollution_index}"
            
traf_sensor = TrafficSensor(5523, "City Center", 453)
air_qual_sensor = AirQualitySensor(2542, "Docklands", "Moderate")

print(traf_sensor.display_info())
print(traf_sensor.report_traffic())
print(air_qual_sensor.check_air_quality())
#done


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def get_details(self):
        return f"Book info: Title:{self.title}, Author: {self.author}, Pages: {self.pages}"
class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []
    def add_book(self, book_object):
        self.books.append(book_object)
        
    def list_books(self):
        for book in self.books:
            print(book.get_details())
        #return f"List of books : {self.books}"
    def remove_book(self, title):       
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
        
book1 = Book("Any", "Pushkin", 640)
book2 = Book("Anny", "BlaBla", 400)
book3 = Book("Masha i medvedi", "Pupirka", 7004)

my_library = Library("SupaDupa")

my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

print("---Books are---")
my_library.list_books()

my_library.remove_book("Anny")

print("---Books after remove--")
my_library.list_books()


class Room:
    def __init__(self, room_number, available=True):
        self.room_number = room_number
        self.available = available
    def book_room(self):
        self.available = False
    def cancel_booking(self):
        self.available = True
class Guest:
    def __init__(self, name):
        self.name = name
        self.room = None
    def book(self, room):
        self.room = room
        if room.available:
            room.book_room()
            print(f"{self.name} booked room {room.room_number}")
        else:
            print("Room is not available")            
        
    def cancel(self):
        if self.room is not None:
            self.room.cancel_booking()
            print(f"{self.name} canceled room {self.room.room_number}")
        else:
            print("No room booked")
            
room1 = Room(105)
guest1 = Guest("Terry")

guest1.book(room1)
print("Room available:" ,room1.available)

guest1.cancel()
print("Room available after cancellation:", room1.available)

