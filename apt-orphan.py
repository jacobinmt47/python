import apt

#go through apt database print out packages that are not listed as a dependency

cache = apt.Cache()
cache.open()

dep = set()

for k in cache:
    if(k.installed):
        v = k.versions[0]
        ds = v.dependencies
        for d in ds:
            dep.add(d.rawstr)

for l in cache:
    if(l.installed):
        if(not (l.name in dep)):
            print(l.name)