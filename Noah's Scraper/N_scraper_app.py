import json
import requests
from tkinter import *
from bs4 import BeautifulSoup

root = Tk()
root.title('Wiki Hyperlink Finder')
root.geometry('650x500')

def scrape_site(event):
	all_wiki_links = []
	link_list.delete(0,END)
	link = usr_srch.get()

	response = requests.get(
		url=link,
	)
	soup = BeautifulSoup(response.content, 'html.parser')

	#find all links in page
	all_wiki_links = soup.find(id="bodyContent").find_all("a")

	#add only wiki links to list
	for wiki_link in all_wiki_links:
		if wiki_link['href'].find("/wiki/") == -1:
			continue

		link_list.insert(END, wiki_link['title'])

#label
intro_label = Label(root, text="Enter a Wiki Link", font=("Helvetica", 25), fg="grey")
intro_label.pack(pady=10)

#entry box
usr_srch = Entry(root, font=("Helvetica", 20), fg = "dodger blue")
usr_srch.pack()

#listbox
link_list = Listbox(root, width=50)
link_list.pack(pady=40)

usr_srch.bind("<Return>", scrape_site)

root.mainloop()
