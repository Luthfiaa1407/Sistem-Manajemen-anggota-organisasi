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
