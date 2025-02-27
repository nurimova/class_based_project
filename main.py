
import csv

class Users(object):
    def __init__(self, file_path):
        
        # open file 
        # Read and parse the CSV file
        self.file_path = file_path
        self.users = self._read_csv()
    def _read_csv(self):
        users = []
        file=open(self.file_path, mode='r')
        reader = csv.DictReader(file)
        for row in reader:
                users.append(row)
        return users

    def first_name_all(slef):

        # Users data parse

        # retrun first_name all list type
        
        return [user['first_name'] for user in self.users]

    def last_name_all(slef):

        # Users data parse

        # retrun last_name all list type
        
        return [user['last_name'] for user in self.users]

    def gender_male_count(slef):

        # Users data parse

        # retrun gender mael count 
        
        return sum(1 for user in self.users if user['gender'].lower() == 'male')

    def gender_female_count(slef):

        # Users data parse

        # retrun gender femael count 
        
        return sum(1 for user in self.users if user['gender'].lower() == 'female')

    def get_all_domen_name(slef):

        # Users data parse

        # Return all unique domain names from the data.

        # sample: username@gmail.com -> domen_name = 'gmail'

        return list(set(user['email'].split('@')[-1] for user in self.users))

    def get_job(slef):

        # Get all unique jobs from user data

        # Return answer

        return list(set(user['job'] for user in self.users))

    def get_one_user(self, id: int):

        # Return the user ID data equal to the id value.
        for user in self.users:
            if int(user['id']) == user_id:
                return user
        return None
    

