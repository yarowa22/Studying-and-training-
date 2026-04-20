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
