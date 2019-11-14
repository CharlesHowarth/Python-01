site_list = [
    "Youtube",
    "Bitchute",
    "Discogs"
    ]

extend_list = [
    "Imdb",
    "Metacritic",
    "Rcp"
    ]

print(site_list)

site_list.append("Minds")
site_list.append("Amazon")
print(site_list)

site_list.remove("Minds")
print(site_list)

site_list.reverse()
print(site_list)

print("Bitchute Occurences: " + str(site_list.count("Bitchute"))    )

site_list.extend(extend_list)
print(site_list)

site_list.insert(3,"Duck Duck Go")
print(site_list)

print(site_list.index("Youtube"))

site_list.sort()
print(site_list)

new_list = ""
print(new_list)
new_list = site_list.copy()
print(new_list)

print("")



p
