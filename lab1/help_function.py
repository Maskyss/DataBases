import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from configparser import ConfigParser
import commands
import random
import datetime
import sys
from termcolor import colored, cprint


class Functions():
    def __init__(self):
        self
    def config(filename='database.ini', section='postgresql'):
        parser = ConfigParser()
        parser.read(filename)
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
        return db

    def create_tables(self):
        """ create tables in the PostgreSQL database"""

        conn = None
        try:
            params = Functions.config()
            conn = psycopg2.connect(**params)
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)  # <-- ADD THIS LINE
            cur = conn.cursor()

            for command in commands.command:
                cur.execute(command)

            cur.close()
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def     insert_film(self):
        conn = None
        title = input("Please enter title of film: ")
        producer = input("Do you know producer?: ")
        while True:
            date = input("Do you know date of this film(format YYYY-MM-DD or answer N): ")
            if(date == "N" or date=="n"):
                year=random.randint(1930, 2019)
                date = year+"-01-01"
                break
            try:
                if(datetime.datetime.strptime( date, '%Y-%m-%d')):
                    break
            except ValueError:
                    None

        while True:
            award = input("Did you know the movie had awards(Y/N): ")
            if(award == 'Y' or award=="y"):
                awardBool = True
                break
            else:
                awardBool = False
                award_id = None
                break

        try:
            params = Functions.config()
            conn = psycopg2.connect(**params)
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)  # <-- ADD THIS LINE
            cur = conn.cursor()
            listAw =[]
            while awardBool:
                award_id = input("Did you know what is award(N/Y): ")
                cur.execute("""SELECT award_id FROM award""")
                mobile_records = cur.fetchall()
                for row in mobile_records:
                    listAw.append(row[0])

                if (award_id == "N" or award_id == "n"):
                    # cur.execute("""SELECT award_id FROM award ORDER BY award_id DESC LIMIT 1""")
                    award_id =random.choice(listAw)
                    break
                else:
                    cur.execute("""SELECT award_id, title FROM award """)
                    mobile_records = cur.fetchall()
                    maxId =1
                    for row in mobile_records:
                        print("Id = ",row[0])
                        print("Title= ",row[1])
                        maxId = row[0]
                    while True:
                        award_id = input("Number: ")
                        if int(award_id) in listAw:
                            print("kek")
                            break
                        else: print(listAw)
                    break

            print(title, producer,date,awardBool,award_id)
            if(award_id != None):
                cur.execute("""INSERT INTO film(title,producer,date,award_id)
                             VALUES(%s,%s,%s,%s) RETURNING film_id;""",
                            (title, producer, date, awardBool,award_id))
                film_id = cur.fetchone()[0]
                cur.execute("""INSERT INTO producer(name,award_id)
                                         VALUES(%s,%s) RETURNING producer_id;""",
                            (producer, award_id))
                producer_id = cur.fetchone()[0]
            else:
                cur.execute("""INSERT INTO film(title,producer,date)
                                         VALUES(%s,%s,%s,%s) RETURNING film_id;""",
                            (title, producer, date, awardBool))
                # film_id = cur.fetchone()[0]
                cur.execute("""INSERT INTO producer(name)
                                                     VALUES(%s) RETURNING producer_id;""",
                           (producer, award_id))
                # producer_id = cur.fetchone()[0]

            cur.close()
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def help_print(str):
        try:
            params = Functions.config()
            conn = psycopg2.connect(**params)
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)  # <-- ADD THIS LINE
            cur = conn.cursor()
            cur.execute("""SELECT * FROM """+str)
            mobile_records = cur.fetchall()
            for row in mobile_records:
                for i in row:
                    print(i, "\t  ", end='')
                print()
            cur.close()
            conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
                print(error)
        finally:
            if conn is not None:
                conn.close()

    def print_table(self):
            while True:
                table_title = input("What table to print:\n"
                                    "0: all\n"
                                    "1: film\n"
                                    "2: award\n"
                                    "3: producer\n")
                if (int(table_title) == 0):
                    print("Award table")
                    print("id\t title")
                    Functions.help_print("award")

                    print("Film table")
                    print("id\t title\t\t producer\t\t date\t award_id")
                    Functions.help_print("film")

                    print("Producer table")
                    print("id\t name\t award_id")
                    Functions.help_print("producer")
                    break
                elif(int(table_title) == 1):
                    print("Film table")
                    print("id\t title\t\t producer\t\t date\t awardBool\t award_id")
                    Functions.help_print("film")
                    break
                elif (int(table_title) == 2):
                    print("Award table")
                    print("id\t title")
                    Functions.help_print("award")
                    break
                elif(int(table_title) == 3):
                    print("Producer table")
                    print("id\t name\t award_id")
                    Functions.help_print("producer")
                    break


    def execute_str(self, str):

        try:
            params = Functions.config()
            conn = psycopg2.connect(**params)
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)  # <-- ADD THIS LINE
            cur = conn.cursor()
            cur.execute(str)
            mobile_records = cur.fetchall()
            for row in mobile_records:
                for i in row:
                    print(i, "\t  ", end='')
                print()
            cur.close()
            conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()



    def pdate_award(str):
        try:
            params = Functions.config()
            conn = psycopg2.connect(**params)
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)  # <-- ADD THIS LINE
            cur = conn.cursor()
            while True:
                cur.execute("""SELECT * FROM award """)
                False
            mobile_records = cur.fetchall()
            print(mobile_records)
            for row in mobile_records:
                for i in row:
                    print(i, "\t  ", end='')
                print()
            while True:
                set_id = input("What id do you want UPDATE: \n")
                what_id = input("What new id: \n")
                if(int(set_id)&int(what_id)):
                    cur.execute("""UPDATE award
                         SET award_id = %(str)
                         WHERE award_id = %(str)
                         """,{set_id,what_id})
                    False

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
    def delete_film(self):
        try:
            params = Functions.config()
            conn = psycopg2.connect(**params)
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)  # <-- ADD THIS LINE
            cur = conn.cursor()
            cur.execute("""SELECT * FROM film""")
            mobile_records = cur.fetchall()
            for row in mobile_records:
                for i in row:
                    print(i, "\t  ", end='')
                print()

            while True:
                set_id = input("What film do you want DELETE enter ID: \n")
                if(int(set_id)):
                    cur.execute("""DELETE FROM film WHERE film_id = %(str)""",{set_id})
                    False


            cur.close()
            conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def find_for_str(str):
        try:
            params = Functions.config()
            conn = psycopg2.connect(**params)
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)  # <-- ADD THIS LINE
            cur = conn.cursor()
            while True:
                cur.execute("""SELECT * FROM award WHERE title= %(str) """, {str})
                False
            mobile_records = cur.fetchall()
            print(mobile_records)
            for row in mobile_records:
                for i in row:
                    print(i, "\t  ", end='')
                print()
            cur.close()
            conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def search1(self, str):

        try:
            params = Functions.config()
            conn = psycopg2.connect(**params)
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)  # <-- ADD THIS LINE
            cur = conn.cursor()

            print(str)
            a = """select * from film where to_tsvector(title) @@ plainto_tsquery(%s) 
                                         or to_tsvector(producer) @@ plainto_tsquery(%s)"""
            cur.execute(a, (str,str))
            results = cur.fetchall()

            print("film_id | title | producer | date | award_id")
            print(results)
            for row in results:
                film_id = row[0]
                title = row[1]
                producer = row[2]
                date = row[3]
                award_id = row[4]

                # if row.find(str) or str.find(row):
                #     print(colored(row,'red'),"\t")
                # # Now print fetched result
                # if str in title:
                #     print(film_id)
                #     sys.stdout.write("\033[1;31m")
                #     print("\033[0;37;40m"+title)
                #     sys.stdout.write("\033[0;0m")
                #     print("\t\t\t\t\t" + producer + "\t" + str(date) + "\t" + str(award_id))
                # else:
                #     print(str(film_id) + "\t\t"+ title+ "\t\t\t\t\t")
                #     sys.stdout.write("\033[1;31m")
                #     print(producer)
                #     sys.stdout.write("\033[0;0m")
                #     print("\t" + str(date) + "\t" + str(award_id))


            cur.close()
            conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()




