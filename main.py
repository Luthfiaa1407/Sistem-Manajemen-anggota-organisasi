import csv

class Anggota:
    def __init__(self):
        self.choice_one = "Add New Member"
        self.choice_two = "View Members Data"
        self.choice_three = "Search Members"
        self.choice_four = "Update Member"
        self.choice_five = "Delete Member"
        self.choice_six = "Quit"
        self.member_database = 'member.csv'

    def display_menu(self):
        print("\nCHOOSE AN OPTION:\n")
        print("1. " + self.choice_one)
        print("2. " + self.choice_two)
        print("3. " + self.choice_three)
        print("4. " + self.choice_four)
        print("5. " + self.choice_five)
        print("6. " + self.choice_six)

    def clr_scr():
        print("\n")

    def add_member(self):
        name = input("Member Name: ")
        if not name.replace(" ", "").isalpha():
            print("\nNama Tidak Valid!")
            return

        npm = input("NPM Member: ")

        phonenum = input("Nomor Handphone Member: ")
        if len(phonenum) == 12 and phonenum.isdigit():
            phone = phonenum
        else:
            print("\nNomor Handphone Harus 12 Digit!")
            return

        Divisi = input("Divisi: ")
        prodi = input("Prodi: ")
        angkatan = input("Angkatan: ")

        with open(self.member_database, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, npm, phonenum, prodi, angkatan])
        print(f"\n{name} telah ditambahkan ke database.")

    def view_members(self):
        try:
            with open(self.member_database, mode='r') as file:
                reader = csv.reader(file)
                members = list(reader)
                members.sort(key=lambda x: x[0])
                for row in members:
                    print(", ".join(row))
        except FileNotFoundError:
            print("\nAnggota Tidak Ditemukan!.")

def search_members(self):
        search_term = input("Enter the name to search: ").lower()
        found = False
        try:
            with open(self.member_database, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if search_term in row[0].lower():
                        print(", ".join(row))
                        found = True
            if not found:
                print("\nNothing!.")
        except FileNotFoundError:
            print("\nNo members found. The database is empty.")



def delete_member(self):
        name = input("Enter Name to Delete: ")
        try:
            member_found = False
            updated_data = []
            with open(self.member_database, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) > 0:
                        if name.lower() != row[0].lower():
                            updated_data.append(row)
                        else:
                            member_found = True

def main():
    anggota = Anggota()
    while True:
        Anggota.clr_scr()
        anggota.display_menu()
        choice = input("\nEnter your choice: ")

        if choice == '1':
            Anggota.clr_scr()
            anggota.add_member()
        elif choice == '2':
            Anggota.clr_scr()
            anggota.view_members()
        elif choice == '3':
            Anggota.clr_scr()
            anggota.search_members()
        elif choice == '4':
            Anggota.clr_scr()
            anggota.update_member()
        elif choice == '5':
            Anggota.clr_scr()
            anggota.delete_member()
        elif choice == '6':
            break
        else:
            print("\nInvalid choice! Please try again.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
