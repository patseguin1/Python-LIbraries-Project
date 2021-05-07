import mcstatus

# A few of the largest / most active Minecraft servers
servers = ["us.mineplex.com", "mc.hypixel.net", "2b2t.org", "us.shotbow.net"]

for server in servers:
    mc_server = mcstatus.MinecraftServer.lookup(server)
    players = mc_server.status().players.online
    version = mc_server.status().version.name

    print("The server has {} online players on version {}".format(players, version))