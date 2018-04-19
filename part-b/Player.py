
class _Player:
    """Wrapper for a Player class to simplify initialization"""
    def __init__(self, player_class, colour):
        self.player = player_class(colour)
    def update(self, move):
        self.player.update(move)
    def action(self, turns):
        action = self.player.action(turns)
        return action
