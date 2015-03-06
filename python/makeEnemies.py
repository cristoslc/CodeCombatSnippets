# TESTING: Generate a list of enemies.

def makeEnemies():
    findEnemies = [
        {'id':'Adam', 'type':'thrower'} , 
        {'id':'Betty', 'type':'shaman'} , 
        {'id':'Charlie', 'type':'ogre'} , 
        {'id':'Denise', 'type':'munchkin'} , 
        {'id':'Elton', 'type':'thrower'} , 
        {'id':'Fabrice', 'type':'shaman'} , 
        {'id':'Gino', 'type':'ogre'} , 
        {'id':'Hayley', 'type':'thrower'} , 
        {'id':'Ian', 'type':'shaman'} , 
        {'id':'Juliet', 'type':'ogre'}
        ]

    random.shuffle(findEnemies)
    return findEnemies