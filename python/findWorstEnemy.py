# Return highest-priority enemy (gives priority to ranged enemies).

# TODO: Build a dictionary of enemy types containing a nested list of all the enemies of that type. Then iterate through them in order of preference, and return the nearest one.

def findWorstEnemy():
    worstEnemyLists = {}
    worstEnemies = []

    enemies = self.findEnemies()
    attackOrder = ['thrower', 'shaman', 'ogre']

    worstEnemyLists['nobody'].append(None)

    for enemy in enemies:
        worstEnemyLists[enemy.type] = []
        worstEnemyLists[enemy.type].append(enemy)

    for eType in attackOrder:
        if len(worstEnemyLists[eType]) > 0:
            worstEnemy = self.findNearest(worstEnemyLists[eType])
            return worstEnemy

    return None