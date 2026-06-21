text = " olamide bamidele"
print(text.strip(" ").capitalize() + ".")


book_info = "john doe ; the art of programming ; 2020 ; ISN 978-3-16-148410-0 ; 350 ; 2500"
component = book_info.split(" ; ")
author = component[0].title()
book_title = component[1].title()
year_of_published = component[2]
isbn = component[3].replace("ISN", "ISBN")
no_of_pages = component[4]
cost = "#" + "{:.2f}".format(float(component[5]))
print( f"""
The book {book_title} was written by {author} and
published in {year_of_published}.
It has {no_of_pages} pages and {isbn} and costs {cost}.
""")
