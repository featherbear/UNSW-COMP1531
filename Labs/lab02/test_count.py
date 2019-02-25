from count import *

inputs = [
    'HelloOo!',
    'I love 1531 :D',
    'Vestibulum lobortis odio ut elit elementum vestibulum. Nunc at turpis egestas, tempus lectus vitae, dictum magna. Quisque lobortis metus sed urna maximus lacinia. Curabitur accumsan neque et odio dapibus, non congue velit dapibus. Aenean efficitur ligula ante, eu vestibulum nisl sagittis a. Ut ultricies sodales sapien ac viverra. Sed eleifend arcu turpis, id blandit tortor pellentesque sit amet. Etiam fringilla mi ut dui porttitor scelerisque. Etiam vitae efficitur nisi. Nulla convallis in diam in hendrerit. Aenean non metus nibh. Fusce vehicula, sapien et semper convallis, enim eros commodo sapien, et dapibus tellus nunc a lorem. Sed sit amet ante dapibus augue laoreet sagittis.',
    '! %!1 234@D !412a 2%() A?1dSa sdfl d12j- ;lkdfd mc,la4p o42?dz.',
    'this is a simple paragraph that is meant to be nice and easy to type which is why there will be mommas no periods or any capital letters so i guess this means that it cannot really be considered a paragraph but just a series of run on sentences this should help you get faster at typing as im trying not to use too many difficult words in it although i think that i might start making it hard by including some more difficult letters I am typing pretty quickly so forgive me for any mistakes i think that i will not just tell you a story about the time i went to the zoo and found a monkey and a fox playing together they were so cute and i think that they were not supposed to be in the same cage but they somehow were and i loved watching them horse around forgive the pun well i hope that it has been highly enjoyable typing this paragraph and i wish you the best of luck getting the best score that you possibly can - taken from https://10fastfingers.com/text/119-A-simple-Paragraph-to-practice-simple-typing' 
]

output_count_char = [
'H 1\ne 1\nl 2\no 2\nO 1\n! 1\n',
'I 1\n  3\nl 1\no 1\nv 1\ne 1\n1 2\n5 1\n3 1\n: 1\nD 1\n',
'V 1\ne 66\ns 44\nt 51\ni 63\nb 12\nu 46\nl 33\nm 24\n  102\no 24\nr 25\nd 18\nn 36\nv 10\n. 13\nN 2\nc 19\na 46\np 13\ng 8\n, 8\nQ 1\nq 4\nx 1\nC 1\nA 2\nf 6\nU 1\nS 2\nE 2\nh 3\nF 1\n',
'! 3\n  10\n% 2\n1 4\n2 5\n3 1\n4 4\n@ 1\nD 1\na 3\n( 1\n) 1\nA 1\n? 2\nd 6\nS 1\ns 1\nf 2\nl 3\nj 1\n- 1\n; 1\nk 1\nm 1\nc 1\n, 1\np 1\no 1\nz 1\n. 1\n',
't 96\nh 48\ni 64\ns 53\n  187\na 63\nm 24\np 27\nl 29\ne 82\nr 38\ng 25\nn 49\no 55\nb 13\nc 19\nd 19\ny 28\nw 13\nu 24\nj 3\nf 15\nk 9\nI 1\nq 1\nv 3\nz 1\nx 2\n- 8\n: 1\n/ 4\n1 3\n0 1\n. 1\n9 1\nA 1\nP 1\n',
]

output_count_insensitive = [
'h 1\ne 1\nl 2\no 3\n! 1\n',
'i 1\n  3\nl 1\no 1\nv 1\ne 1\n1 2\n5 1\n3 1\n: 1\nd 1\n',
'v 11\ne 68\ns 46\nt 51\ni 63\nb 12\nu 47\nl 33\nm 24\n  102\no 24\nr 25\nd 18\nn 38\n. 13\nc 20\na 48\np 13\ng 8\n, 8\nq 5\nx 1\nf 7\nh 3\n',
'! 3\n  10\n% 2\n1 4\n2 5\n3 1\n4 4\n@ 1\nd 7\na 4\n( 1\n) 1\n? 2\ns 2\nf 2\nl 3\nj 1\n- 1\n; 1\nk 1\nm 1\nc 1\n, 1\np 1\no 1\nz 1\n. 1\n',
't 96\nh 48\ni 65\ns 53\n  187\na 64\nm 24\np 28\nl 29\ne 82\nr 38\ng 25\nn 49\no 55\nb 13\nc 19\nd 19\ny 28\nw 13\nu 24\nj 3\nf 15\nk 9\nq 1\nv 3\nz 1\nx 2\n- 8\n: 1\n/ 4\n1 3\n0 1\n. 1\n9 1\n',
]

outputs_count_ordered = [
'o 3\nl 2\nh 1\ne 1\n! 1\n',
'  3\n1 2\ni 1\nl 1\no 1\nv 1\ne 1\n5 1\n3 1\n: 1\nd 1\n',
'  102\ne 68\ni 63\nt 51\na 48\nu 47\ns 46\nn 38\nl 33\nr 25\nm 24\no 24\nc 20\nd 18\n. 13\np 13\nb 12\nv 11\ng 8\n, 8\nf 7\nq 5\nh 3\nx 1\n',
'  10\nd 7\n2 5\n1 4\n4 4\na 4\n! 3\nl 3\n% 2\n? 2\ns 2\nf 2\n3 1\n@ 1\n( 1\n) 1\nj 1\n- 1\n; 1\nk 1\nm 1\nc 1\n, 1\np 1\no 1\nz 1\n. 1\n',
'  187\nt 96\ne 82\ni 65\na 64\no 55\ns 53\nn 49\nh 48\nr 38\nl 29\np 28\ny 28\ng 25\nm 24\nu 24\nc 19\nd 19\nf 15\nb 13\nw 13\nk 9\n- 8\n/ 4\nj 3\nv 3\n1 3\nx 2\nq 1\nz 1\n: 1\n0 1\n. 1\n9 1\n',
]

def test_count_char(mocker):
    checker = Checker()
    mocker.patch('sys.stdout', checker)

    for i in range(len(inputs)):
        count_char(inputs[i])
        checker.check(output_count_char[i])
        checker.clear()


def test_count_char_insensitive(mocker):
    checker = Checker()
    mocker.patch('sys.stdout', checker)

    for i in range(len(inputs)):
        count_char_insensitive(inputs[i])
        checker.check(output_count_insensitive[i])
        checker.clear()


def test_count_char_ordered(mocker):
    checker = Checker()
    mocker.patch('sys.stdout', checker)

    for i in range(len(inputs)):
        count_char_ordered(inputs[i])
        checker.check(outputs_count_ordered[i])
        checker.clear()


class Checker():

    def __init__(self):
        self._buffer = ''

    def write(self, output):
        self._buffer += output

    def clear(self):
        self._buffer = ''

    def check(self, output):
        assert self._buffer == output