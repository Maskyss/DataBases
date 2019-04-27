command = (
            # """
            # CREATE DATABASE Films
            # """,
            """ 
            CREATE TABLE IF NOT EXISTS award (
                    award_id SERIAL PRIMARY KEY,
                    title VARCHAR(255) NOT NULL
                    )
            """,

            # """
            # CREATE TYPE gen AS ENUM ('f', 'm');
            # """,
            """ 
            CREATE TABLE IF NOT EXISTS film (
                film_id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                producer VARCHAR(255) NOT NULL,
                date DATE,
                award BOOL,
                award_id INTEGER,
                FOREIGN KEY(award_id)
                    REFERENCES award(award_id)
                        ON UPDATE CASCADE
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS producer (
                    producer_id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    award_id INTEGER,
                    FOREIGN KEY(award_id)
                    REFERENCES award(award_id)
                        ON UPDATE CASCADE
            )
            """)


# INNER JOIN producer ON film.producer = producer.name
str_between = """SELECT date, title
 FROM film
 
 WHERE film.award_id IS NOT NULL AND extract(year from date)
 BETWEEN 2011 and 2019"""
# select * from film
# where LOWER(title)  like('faigy') or LOWER(producer) like('faigy')
str_prod_from = """SELECT producer
                FROM film
                INNER JOIN producer ON film.producer = producer.name
                """


