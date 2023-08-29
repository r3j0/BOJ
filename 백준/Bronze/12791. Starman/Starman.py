source = [[] for _ in range(2017)]
source[1967].append("1967 DavidBowie")
source[1969].append("1969 SpaceOddity")
source[1970].append("1970 TheManWhoSoldTheWorld")
source[1971].append("1971 HunkyDory")
source[1972].append("1972 TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars")
source[1973].append("1973 AladdinSane")
source[1973].append("1973 PinUps")
source[1974].append("1974 DiamondDogs")
source[1975].append("1975 YoungAmericans")
source[1976].append("1976 StationToStation")
source[1977].append("1977 Low")
source[1977].append("1977 Heroes")
source[1979].append("1979 Lodger")
source[1980].append("1980 ScaryMonstersAndSuperCreeps")
source[1983].append("1983 LetsDance")
source[1984].append("1984 Tonight")
source[1987].append("1987 NeverLetMeDown")
source[1993].append("1993 BlackTieWhiteNoise")
source[1995].append("1995 1.Outside")
source[1997].append("1997 Earthling")
source[1999].append("1999 Hours")
source[2002].append("2002 Heathen")
source[2003].append("2003 Reality")
source[2013].append("2013 TheNextDay")
source[2016].append("2016 BlackStar")

import sys
input = sys.stdin.readline

q = int(input().rstrip())
for _ in range(q):
    s, e = map(int, input().rstrip().split())
    cnt = 0
    for i in range(s, e+1):
        cnt += len(source[i])
    print(cnt)
    for i in range(s, e+1):
        for o in source[i]:
            print(o)