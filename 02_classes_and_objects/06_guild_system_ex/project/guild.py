from project.player import Player


class Guild:
    def __init__(self, name:str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild != "Unaffiliated":
            if player.guild == self.name:
                return f"Player {player.name} is already in the guild."
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {player.guild}"

    def kick_player(self, player_name:str):
        player_kicked = False
        for guild_member in self.players:
            if guild_member.name == player_name:
                self.players.remove(guild_member)
                guild_member.guild = "Unaffiliated"
                player_kicked = True
                return f"Player {guild_member.name} has been removed from the guild."
        if not player_kicked:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        result += "\n".join([player.player_info() for player in self.players])
        return result

