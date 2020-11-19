# DROP TABLES

songplay_table_drop = "DROP table if exists songplays"
user_table_drop = "DROP table if exists users"
song_table_drop = "DROP table if exists songs"
artist_table_drop = "DROP table if exists artists"
time_table_drop = "DROP table if exists time"

# CREATE TABLES

songplay_table_create = (""" CREATE SEQUENCE songplay_id_seq;
                                CREATE TABLE songplays(
                                            songplay_id INT NOT NULL DEFAULT NEXTVAL('songplay_id_seq'),
                                            start_time BIGINT ,
                                            user_id varchar ,
                                            level varchar,
                                            song_id varchar,
                                            artist_id varchar,
                                            session_id int ,
                                            location varchar,
                                            user_agent text );
                                            """)

user_table_create = (""" CREATE TABLE users(
                                            user_id int PRIMARY KEY ,
                                            first_name varchar,
                                            last_name varchar,
                                            gender varchar,
                                            level varchar);
                                            """)

song_table_create = ( """ CREATE TABLE IF NOT EXISTS songs (
                                            song_id VARCHAR NOT NULL PRIMARY KEY, 
                                            title VARCHAR NOT NULL, 
                                            artist_id VARCHAR NOT NULL, 
                                            year int, 
                                            duration float);
                                            """)


artist_table_create = ( """CREATE TABLE IF NOT EXISTS artists (
                                            artist_id VARCHAR NOT NULL PRIMARY KEY, 
                                            name VARCHAR NOT NULL, 
                                            location VARCHAR, 
                                            latitude FLOAT, 
                                            longitude FLOAT);
                                            """)

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (
                                            start_time BIGINT, 
                                            hour int, 
                                            day int, 
                                            week int, 
                                            month int, 
                                            year int, 
                                            weekday INT);
                                            """ )



# INSERT RECORDS
songplay_table_insert = (""" INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING; """ )

user_table_insert = (""" INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO NOTHING;""" )

song_table_insert = (""" INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO NOTHING;""" )

artist_table_insert = (""" INSERT INTO artists(artist_id, name, location , latitude , longitude ) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING; """ )

time_table_insert = (""" INSERT INTO time(start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;""" )

# FIND SONGS

song_select = (""" SELECT s.song_id, a.artist_id FROM songs s JOIN artists a ON s.artist_id = a.artist_id WHERE s.title = %s AND a.name = %s AND s.duration = %s; """)
                

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
#create_table_queries = [songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
#drop_table_queries = [songplay_table_drop]