

class WorldServer:
    def get_tile(self, x, y):
        return {
            'altitude': 0,
            'grass': 1.0,
            'rock': 0.0,
        }
