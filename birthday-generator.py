import random 
word1 = [
    'the most beautiful person ever', 'the best friend one can dream of', 'the one of kindest people we know', 
    'a beautiful person inside and out', 'the coolest person of all time', 'the life of the party'
]
word2 = [
    'laughter', 'strength', 'humor', 'style', 'adventurism', 'wisdom','empathy' ,'loyalty',
    ]
word3 = [
    ', ambition and drive',', ability to listen and understand', ' and ability to make anyone feel welcome',' and a genuine support for your friends'

]    
word4 = [
    'drinking shots', 'to laugh until you scream', 'to order more food than you can eat',
    'to always be on time', 'to always be gorgeous', 'to google anything in seconds',
    'to laugh at trash', 'to do a girl math', 'to wear kids clothes and stay stylish',
    'to go to the social event after the party', 'to be awesome', 'to lift heavier weight than yourself'
]
word5 = [
    'endless love and friendship', 'countless reasons to smile', 'all the laughs you bring us', 'a life as amazing as you are', 
    'all the magic of life', 'reasons to celebrate every day', 'a world of wonderful surprises' ]
word6 = [
    'unforgettable adventures','lots of wonderful moments', 'new experiences']
word7 = [
    'personal growth','exiting challenges']

print(f'''Dear Nastya! Happy Birthday! 
You are {random.choice(word1)}. 
We admire your {random.choice(word2)}{random.choice(word3)}. 
We all know your superpower is {random.choice(word4)}, and we love it!
We wish you happiness, health, wealth, and endless joy, {random.choice(word5)}, {random.choice(word6)}, and {random.choice(word7)}. 
We love you and are hoping to share more moment like this: ''')