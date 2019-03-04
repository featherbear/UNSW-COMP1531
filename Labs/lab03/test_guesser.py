import random, string

from abc import ABC, abstractmethod
from numberGuesser import run_game, MIN, MAX, NUM_VALUES, handle_guess, find_closest


class Player(ABC):
    def __init__(self):
        self.guess = 5

    def write(self, output):
        self.change_guess(output)

    def make_guess(self, prompt=''):
        return str(self.guess)

    @abstractmethod
    def change_guess(self, output):
        pass


class PersistantPlayer(Player):

    def change_guess(self, output):
        output = output.strip().strip(string.punctuation)
        if (output.endswith('higher')):
            self.guess += 1
        elif (output.endswith('lower')):
            self.guess -= 1
        elif (output.startswith('Congratulations')):
            self.guess = 'q'


class Cheater(Player):

    def set_vals(self, vals):
        self.values = vals[:]
        self.guess = vals[0]
        self.guess_count = 0

    def change_guess(self, output):
        assert not (output.endswith('lower') or output.endswith('higher')), 'I guessed {} but it was not in {}'.format(str(self.guess), str(self.values))
        if (output.startswith('Congratulations')):
            assert self.guess_count == len(self.values)
            self.guess = 'q'
        elif output.startswith('You found'):
            self.guess_count += 1
            if self.guess_count < len(self.values):
                self.guess = self.values[self.guess_count]


def test_handle():
    values = [1, 2, 3, 4, 5]
    new_values = handle_guess(1, values)
    assert (len(new_values) == len(values) - 1)
    new_values = handle_guess(6, new_values)
    assert (len(new_values) == len(values) - 1)
    new_values = handle_guess(2, new_values)
    assert (len(new_values) == len(values) - 2)


def test_closest():
    values = [1, 4, 8, 9]
    assert (find_closest(2, values) == 1)
    assert (find_closest(3, values) == 4)
    assert (find_closest(9, values) == 9)


def test_guess_playing(mocker):
    pplayer = PersistantPlayer()
    mocker.patch('builtins.input', pplayer.make_guess)
    mocker.patch('sys.stdout', pplayer)
    values = sorted(random.sample(range(MIN, MAX+1), NUM_VALUES))
    run_game(values)
    values = sorted(random.sample(range(MIN, MAX+1), NUM_VALUES))
    run_game(values)
    values = sorted(random.sample(range(MIN, MAX+1), NUM_VALUES))
    run_game(values)


def test_cheater(mocker):
    cheater = Cheater()
    mocker.patch('builtins.input', cheater.make_guess)
    mocker.patch('sys.stdout', cheater)
    values = sorted(random.sample(range(MIN, MAX+1), NUM_VALUES))
    cheater.set_vals(values)
    run_game(values)
    values = sorted(random.sample(range(MIN, MAX+1), NUM_VALUES))
    cheater.set_vals(values)
    run_game(values)
    values = sorted(random.sample(range(MIN, MAX+1), NUM_VALUES))
    cheater.set_vals(values)
    run_game(values)

