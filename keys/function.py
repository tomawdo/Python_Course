from icecream import ic

train_speed = {
    "Flyingscotsman": 201,
    "TGV": 320,
    "Shinkansen": 320
}

for train in train_speed.values():
    print(str(train)[0], end="")

