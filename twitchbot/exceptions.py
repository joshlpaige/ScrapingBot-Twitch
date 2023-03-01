class twitchbotError(Exception):
    """ General error class for twitchbot."""


class InvalidCategory(twitchbotError):
    """ Error for when the specified category is invalid """


class VideoPathAlreadyExists(twitchbotError):
    """ Error for when a path already exists. """


class NoClipsFound(twitchbotError):
    """ Error for when no clips are found. """
