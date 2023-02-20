class Player(object):
    def __init__(self, name):
        self.name = name
        self._lives = 3  # Hiding attribute.
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        elif lives < 0:
            print("Lives cannot be negative")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self._score += delta * 1000
            self._level = level
        else:
            print("Level cannot be less than 1")

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    # Decorators achieve the same thing as classic properties but with a different  syntax
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score


        # if level > self.level:
        #     self.score += 1000 * (level - self.level)
        #     self.level = level
        # else:
        #     self.score -= 1000 * (self.level - level)
        #     if self.score < 0:
        #         self.score = 0
        #     self.level = level
        #     if self.level < 1:
        #         print("Level cannot be negative")
        #         self.level = 1
        #         self.score = 0
    # level = property(_get_lives, _set_lives)
    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score {0.score}".format(self)

