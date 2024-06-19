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

    def clr_scr(self):
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

        divisi = input("Divisi: ")
        prodi = input("Prodi: ")
        angkatan = input("Angkatan: ")

        with open(self.member_database, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, npm, phonenum, divisi, prodi, angkatan])
        print(f"\n{name} has been added to the database.")

    def view_members(self):
        try:
            with open(self.member_database, mode='r') as file:
                reader = csv.reader(file)
                members = list(reader)
                members.sort(key=lambda x: x[0])
                for row in members:
                    print(", ".join(row))
        except FileNotFoundError:
            print("\n Tidak Ada Anggota!.")

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

    def update_member(self):
        name = input("Enter the name of the member to update: ")
        try:
            member_found = False
            updated_data = []
            with open(self.member_database, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) > 0:
                        if name.lower() == row[0].lower():
                            member_found = True
                            print("Current data:")
                            print("Name:", row[0])
                            print("NPM:", row[1])
                            print("Phone Number:", row[2])
                            print("Divisi:", row[3])
                            print("Prodi:", row[4])
                            print("Angkatan:", row[5])

                            new_name = input("Enter new name : ")
                            if new_name:
                                row[0] = new_name
                            new_npm = input("Enter new NPM : ")
                            if new_npm:
                                row[1] = new_npm
                            new_phonenum = input("Enter new phone number : ")
                            if new_phonenum:
                                row[2] = new_phonenum
                            new_divisi = input("Enter new divisi : ")
                            if new_divisi:
                                row[3] = new_divisi
                            new_prodi = input("Enter new prodi : ")
                            if new_prodi:
                                row[4] = new_prodi
                            new_angkatan = input("Enter new angkatan : ")
                            if new_angkatan:
                                row[5] = new_angkatan

                            updated_data.append(row)
                        else:
                            updated_data.append(row)

            if member_found:
                with open(self.member_database, "w", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerows(updated_data)
                print(f"\n{name} has been updated in the database.")
            else:
                print(f"\n{name} not found in the database.")
        except FileNotFoundError:
            print("\nNo members found. The database is empty.")

    def delete_member(self):
        name = input("Enter Name to Delete: ")
        try:
            member_found =False
            updated_data = []
            with open(self.member_database, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) > 0:
                        if name.lower() != row[0].lower():
                            updated_data.append(row)
                        else:
                            member_found = True

            if member_found:
                with open(self.member_database, "w", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerows(updated_data)
                print(f"\n{name} Telah Dihapus dari Keanggotaan!.")
            else:
                print(f"\n{name} Tidak Ditemukan!.")
        except FileNotFoundError:
            print("\nNo members found. The database is empty.")

def main():
    anggota = Anggota()
    while True:
        anggota.display_menu()
        choice = input("\nEnter your choice: ")

        if choice == '1':
            anggota.clr_scr()
            anggota.add_member()
        elif choice == '2':
            anggota.clr_scr()
            anggota.view_members()
        elif choice == '3':
            anggota.clr_scr()
            anggota.search_members()
        elif choice == '4':
            anggota.clr_scr()
            anggota.update_member()
        elif choice == '5':
            anggota.clr_scr()
            anggota.delete_member()
        elif choice == '6':
            break
        else:
            print("\nInvalid choice! Please try again.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
