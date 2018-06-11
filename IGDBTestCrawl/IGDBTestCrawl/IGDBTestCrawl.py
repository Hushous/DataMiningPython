from igdb_api_python.igdb import igdb

igdb = igdb("d6c559be64b7dc44efe1828bd44f85da")

result = igdb.games({
    'ids':[27193,23212,1942]
})






for game in result.body:
    print("Retrieved: " + game["name"])
