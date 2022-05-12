import rcon

with rcon.MCRcon("zyhmc.xyz", "zhangyihao", 25575) as rc:
    print(rc.command("list"))