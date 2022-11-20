from game.parachute import Parachute
from game.word import Word
from game.terminal_service import TerminalService

class Director:
    def __init__(self):
        
        self.word = Word()
        self.parachute = Parachute()
        self.terminal_service = TerminalService()
        self.is_playing = True
        self.letter = ""
        self.attempts = 0

    def start_game(self):

        print(self.word.hidden_word)
        print(self.parachute.value)

        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):

        if not self.is_playing:
            return

        self.letter = self.terminal_service.get_input("Choose a letter [a-z]: ")

    def do_updates(self):

        if not self.is_playing:
            return
        
        for l in range(len(self.word.value)):
            if self.letter.lower() == self.word.value[l]:
                self.word.reveal_letter(self.letter)

        if self.letter not in self.word.value:
            self.attempts += 1
            self.parachute.cut_parachute(self.attempts)

    def do_outputs(self):

        if not self.is_playing:
            return

        self.terminal_service.print_text(self.word.hidden_word)
        self.terminal_service.print_text(self.parachute.value)

        if self.word.hidden_word.lower() == self.word.value.lower():
            self.terminal_service.print_text(f"You win!\nThe word was: {self.word.value}")
            self.is_playing = False

        if self.attempts == 5:
            self.terminal_service.print_text("You lose.")
            self.is_playing = False