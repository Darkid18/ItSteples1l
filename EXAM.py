import requests
# from bs4 import BeautifulSoup
import sqlite3

print("Welcome to 'Gameinfo search' system!\nOn this search system you can find information about something in games!\nType [/help] for more information!")

# THE PART WHERE I WAS WORKING WITH DATABASE
connection = sqlite3.connect("Exam_DB.sl3")
cur = connection.cursor()
# cur.execute("CREATE TABLE web_sites (site TEXT);")
# connection.commit()
# cur.execute("INSERT INTO web_sites (site) VALUES ('https://half-life.fandom.com/wiki/Half-Life');")
# connection.commit()
# cur.execute("UPDATE web_sites SET site = 'https://ultrakill.fandom.com/wiki/Home' WHERE rowid=2;")
# connection.commit()
# cur.execute("UPDATE web_sites SET site = 'https://omori.fandom.com/wiki/OMORI' WHERE rowid=3;")
# connection.commit()
# I have created a few rowids... and I made this to delete them
# cur.execute("DELETE FROM web_sites WHERE rowid = 4;")
# connection.commit()
# cur.execute("DELETE FROM web_sites WHERE rowid = 5;")
# connection.commit()
cur.execute("SELECT rowid, site FROM web_sites;")
connection.commit()
res = cur.fetchall()
# print(res)
connection.close()



# THE PART WITH SEARCH SYSTEM



while True:
    user_search = input("Enter what do you want/need:   ")
    result = []


    if user_search == "/help":
        print("System version = 1.0\nCreated by C0nn0R\nSpecial thanks to ItStep\nVersion : RELEASE 1.0\nLast time updated : None\nContacts : 0123123123\nList of games in our database:\nUltrakill\nOmori\nHalf-Life\nLibraries used: requests, sqlite3\nPlans for future:\n1.User's websites\n2.Make bigger database")

    else:
        for site in res:
            site_url = site[1]
            response = requests.get(site_url)
            response_text = response.text
            search_word_count = response_text.lower().count(user_search.lower())
            result.append((site_url, search_word_count))
            most_result = max(result, key=lambda x: x[1])
        if most_result or result == 0:
            print("No results found")
        else:
            print("The site with most amount of your search:    ", most_result)
