import random

class BirthdayWishGenerator:
    def __init__(self):
        self.word0 = ['Nastya']
        self.word1 = [
    'the role model (Logan)','Nastya and you are amazing (Kelsey C)', 'one of the smartest people we know', 'such a good friend and always make me laugh (Kelsey)', 'one of the best women we know', 
    'my favorite person and the best person I have ever met (Ryan)', 'the best sister ever, you are the most kind person, you are the person I trust (Nadya)', 
    'the best friend one can dream of', 'the one of kindest people we know', 
    'a beautiful person inside and out', 'more than a fried, but sister we never had (Olya and Telya)','my soulmate (Telya)','the life of the party', 'one of the sweetest people I have ever met (Aisha)',

        ]
        self.word2 = [
    'laughter', 'strength', 'humor', 'style', 'adventurism', 'wisdom','empathy' ,'loyalty',
        ]
        self.word3 = [
    ', ambition and drive',', ability to listen and understand', ' and ability to make anyone feel welcome',' and a genuine support for your friends and family'
        ]    
        self.word4 = [
    'taking shots (Olya)', 'your laugh that can blow away a building and will definitely put a smile on any face. If you are not laughing with Nastya, you are laughing at her (Kelsey and Aisha)', 
    'to order more food than you can eat',
    'to always be on time', 'to google anything in seconds', 'putting up with me for over ten years. Also pretty good at burping (Ryan)',
    'to laugh at trash', 'to be there for all of your friends and family (Kelsey)', 'to be smart (Nadya)', 'to read people (Gigi)',
        ]
        self.word5 = [
    'endless love and friendship', 'countless reasons to smile', 'all the laughs you bring us', 'a life as amazing as you are', 
    'all the magic of life', 'reasons to celebrate every day', 'a world of wonderful surprises'
        ]
        self.word6 = [
    'unforgettable adventures','lots of wonderful moments', 'new experiences'
        ]
        self.word7 = [
    'personal growth','exiting challenges'
        ]

    def generate_wish(self):
        header = f"Dear {random.choice(self.word0)}! Happy Birthday!"
        body1 = f'''
You are {random.choice(self.word1)}. 
We admire your {random.choice(self.word2)}{random.choice(self.word3)}. 
We all know your superpower is {random.choice(self.word4)}.'''
        body2 = f'''
We wish you happiness, health, wealth, and endless joy, {random.choice(self.word5)}, {random.choice(self.word6)}, and {random.choice(self.word7)}. 
We love you!'''
        return header, body1, body2
