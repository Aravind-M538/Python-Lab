class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

    def add(self, song_name):
        new_song = Song(song_name)
        if self.head is None:
            self.head = new_song
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_song
        print(song_name, "added to playlist")
           
    def insert_song(self, position, song_name):
        new_song = Song(song_name)

        if position == 1:
            new_song.next = self.head
            self.head = new_song
            print(song_name, "inserted at position", position)
            return

        temp = self.head
        count = 1

       
        while temp and count < position - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Invalid Position")
        else:
            new_song.next = temp.next
            temp.next = new_song
            print(song_name, "inserted at position", position)

    def delete_song(self, song_name):
        temp = self.head
       
        if temp and temp.name == song_name:
            self.head = temp.next
            print(song_name, "deleted from playlist")
            return
               
        prev = None
        while temp and temp.name != song_name:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Song not found")
        else:
            prev.next = temp.next
            print(song_name, "deleted from playlist")
                 
    def display(self):
        if self.head is None:
            print("Playlist is empty")
        else:
            temp = self.head
            print("\nMusic Playlist:")
            while temp:
                print(temp.name, end=" -> ")
                temp = temp.next
            print("None")


# --- Main Menu Execution Loop ---
my_playlist = Playlist()

while True:
    print("\n--- Music Playlist Menu ---")
    print("1. Add Song")
    print("2. Insert Song at Position")
    print("3. Delete Song")
    print("4. Display Playlist")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            song = input("Enter song name: ")
            my_playlist.add(song)

        elif choice == 2:
            pos = int(input("Enter position: "))
            song = input("Enter song name: ")
            my_playlist.insert_song(pos, song)

        elif choice == 3:
            song = input("Enter song name to delete: ")
            my_playlist.delete_song(song)

        elif choice == 4:
            my_playlist.display()

        elif choice == 5:
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select 1-5.")
           
    except ValueError:
        print("Please enter a valid numeric input.")
