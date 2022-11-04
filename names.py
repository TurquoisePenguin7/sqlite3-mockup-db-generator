from mimesis import Person    # type: ignore
from mimesis import Address # type: ignore
from tqdm import tqdm
import sys
import sqlite3

def get_names(db_name = sys.argv[1], number_of_people = sys.argv[2]) -> None:
    """
    This function will get the database name supplied, number of values needed to be created, will create a database with a specified data table, that will be supplied with specific values.
    Feel free to change it to your hearts content.
    """
    con = sqlite3.connect(f"{db_name}.db")
    cur = con.cursor()
    try:
        cur.execute("CREATE TABLE data(name, country, city, postal_code, address, region, telephone_number)")
    except sqlite3.OperationalError:
        print('Database exists, skipping database creation...')
        print('Appending values to the existing database.)

    try:
        for name in tqdm(range(int(number_of_people))): 
            name = Person()
            address = Address()
            query = """INSERT INTO data(name, country, city, postal_code, address, region, telephone_number) VALUES(?, ?, ?, ?, ?, ?, ?)"""
            cur.execute(query, (name.full_name(), address.country(allow_random=True), address.city(), address.postal_code(), address.address(), address.region(), name.telephone(mask='1-###-###-####')))
    finally:
        con.commit()
        print("Finished with db creation")                    
    
if __name__ == "__main__":
    get_names()
