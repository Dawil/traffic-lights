from itertools import islice
import unittest
import main

class TestCase(unittest.TestCase):

    def test_render(self):
        assert main.render('NS', 'GREEN') == 'NS: GREEN'

    def test_warn_yellow_on_green(self):
        assert main.warn_yellow(main.GREEN) == main.YELLOW

    def test_warn_yellow_on_red(self):
        assert main.warn_yellow(main.RED) == main.RED

    def test_warn_yellow_on_yellow(self):
        assert main.warn_yellow(main.YELLOW) == main.YELLOW

    def test_switch_on_red(self):
        assert main.switch(main.RED) == main.GREEN

    def test_switch_on_yellow(self):
        assert main.switch(main.YELLOW) == main.RED

    def test_interval(self):
        events = [0, 0.4, 0.5, 0.9, 1]
        events.reverse()
        for i in islice(main.interval_iter(0.5, 0.1), 5):
            assert i == events.pop()


if __name__ == '__main__':
    unittest.main()
