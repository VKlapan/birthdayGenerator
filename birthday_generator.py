import random

class BirthdayWishGenerator:
    def __init__(self):
        self.word1 = [
            'the most beautiful person ever', 'the best friend one can dream of', 
            'the one of kindest people we know', 'a beautiful person inside and out', 
            'the coolest person of all time', 'the life of the party'
        ]
        self.word2 = [
            'laughter', 'strength', 'humor', 'style', 'adventurism', 
            'wisdom', 'empathy', 'loyalty',
        ]
        self.word3 = [
            ', ambition and drive', ', ability to listen and understand',
            ' and ability to make anyone feel welcome', ' and a genuine support for your friends'
        ]    
        self.word4 = [
            'drinking shots', 'to laugh until you scream', 'to order more food than you can eat',
            'to always be on time', 'to always be gorgeous', 'to google anything in seconds',
            'to laugh at trash', 'to do a girl math', 'to wear kids clothes and stay stylish',
            'to go to the social event after the party', 'to be awesome', 
            'to lift heavier weight than yourself'
        ]
        self.word5 = [
            'endless love and friendship', 'countless reasons to smile', 
            'all the laughs you bring us', 'a life as amazing as you are', 
            'all the magic of life', 'reasons to celebrate every day', 
            'a world of wonderful surprises'
        ]
        self.word6 = [
            'unforgettable adventures', 'lots of wonderful moments', 'new experiences'
        ]
        self.word7 = [
            'personal growth', 'exiting challenges'
        ]

    def generate_wish(self, name):
        return f'''Dear {name}! Happy Birthday! 
You are {random.choice(self.word1)}. 
We admire your {random.choice(self.word2)}{random.choice(self.word3)}. 
We all know your superpower is {random.choice(self.word4)}, and we love it!
We wish you happiness, health, wealth, and endless joy, {random.choice(self.word5)}, {random.choice(self.word6)}, and {random.choice(self.word7)}. 
We love you and are hoping to share more moments like this!''' 