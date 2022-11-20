class Parachute:

    def __init__(self):
        
        self.values = [
            """
            ____
           /____\\
           \    /
            \  /
             0
            /|\\
            / \\
            """,
            """
            
           /____\\
           \    /
            \  /
             0
            /|\\
            / \\
            """,
            """
           \    /
            \  /
             0
            /|\\
            / \\
            """,
             """
            \  /
             0
            /|\\
            / \\
            """,
             """
             x
            /|\\
            / \\
            """
        ]
        self.value = self.values[0]

    def cut_parachute(self, attempts):

        if attempts > 1:
            self.value = self.values[attempts-1]
        else:
            self.value = self.values[attempts]