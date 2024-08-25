"""
Determines which of four characters a user is most like based on answers to five questions.

The four characters are:
- Sharp-Eyed Sam
- Curious Cam
- Keen Kai
- Inquisitive Indy

Each character has a set of preferences for the five questions. The user is asked the five questions, and based on their answers, the character they are most like is determined.

The questions are:
- How would you prefer to spend your evening?
- What's your dream job?
- What's more important?
- What's your favorite decade?
- What's your favorite way to travel?

The answers are scored as follows:
- Activity: Sam 2, Indy 2, Kai 2, Cam 1
- Job: Sam 2, Indy 2, Cam 2, Kai 2
- Value: Sam -1, Kai 1, Cam 2, Indy 1
- Decade: Cam 2, Sam 2, Kai 1, Indy 2
- Travel: Sam -2, Kai 1, Indy -1, Cam 1

The user is then told which character they are most like.
"""
activity = input("How would you prefer to spend your evening?\nA. Reading a book\nB. Attending a party")
job = input("What's your dream job?\nA. Curator at the Smithsonian\nB. Running a business")
value = input("What's more important?\nA. Money\nB. Love")
decade = input("What's your favorite decade?\nA. 1910s\nB. 2010s")
travel = input("What's your favorite way to travel?\nA. Driving\nB. Flying")

sam_like = 0
cam_like = 0
kai_like = 0
indy_like = 0

# Check activity
if activity == 'A':
    sam_like += 2
    indy_like += 2
    kai_like += 2
else:
    cam_like += 1
    indy_like += 1

# Check job
if job == 'A':
    sam_like += 2
    indy_like += 2
    cam_like += 2
else:
    kai_like += 2
    indy_like += 1
    sam_like -= 1

# Check value
if job == 'A':
    sam_like -= 1
    kai_like += 1
else:
    sam_like += 2
    cam_like += 2
    indy_like += 1

# Check decade
if decade == "A":
    cam_like = cam_like + 2
    sam_like = sam_like + 2
else:
    kai_like = kai_like + 1
    indy_like = indy_like + 2

# Check travel
if travel == "A":
    sam_like -= 2
    kai_like += 1
    indy_like -= 1
else:
    sam_like += 1
    cam_like += 1
    kai_like -= 1

if sam_like >= 3:
    print( "You're most like Sharp-Eyed Sam!" )
elif cam_like >= 3:
    print( "You're most like Curious Cam!" )
elif kai_like >= 3:
    print( "You're most like Keen Kai!" )
else:
    print( "You're most like Inquisitive Indy!" )
