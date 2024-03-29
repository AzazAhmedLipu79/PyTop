# tests/test_monitor.py
import unittest
from unittest.mock import patch
import curses
import psutil
from pytop.monitor import PyTop

# class TestPyTop(unittest.TestCase):
#     def setUp(self):
#         self.monitor = PyTop()

#     def tearDown(self):
#         self.monitor.stdscr.clear()
#         curses.endwin()

#     @patch('psutil.process_iter')
#     def test_get_sorted_processes(self, mock_process_iter):
#         # Mock process objects
#         mock_processes = [
#             psutil.Process(pid=1001),
#             psutil.Process(pid=1002),
#             psutil.Process(pid=1003)
#         ]
#         mock_process_iter.return_value = mock_processes

#         # Test sorting by CPU percentage
#         self.monitor.current_sort = 0
#         sorted_processes = self.monitor.get_sorted_processes()
#         self.assertEqual(sorted_processes, [mock_processes[0], mock_processes[1], mock_processes[2]])

#         # Test sorting by memory percentage
#         self.monitor.current_sort = 1
#         sorted_processes = self.monitor.get_sorted_processes()
#         self.assertEqual(sorted_processes, [mock_processes[0], mock_processes[1], mock_processes[2]])

#         # Test sorting by PID
#         self.monitor.current_sort = 2
#         sorted_processes = self.monitor.get_sorted_processes()
#         self.assertEqual(sorted_processes, [mock_processes[0], mock_processes[1], mock_processes[2]])

#     @patch('curses.stdscr')
#     def test_sort_options_menu(self, mock_stdscr):
#         # Test sort options menu
#         self.monitor.stdscr = mock_stdscr
#         self.monitor.current_sort = 0
#         with patch('curses.KEY_UP', 65), patch('curses.KEY_DOWN', 66), patch('curses.KEY_ENTER', 10):
#             self.monitor.sort_options_menu()
#             self.assertEqual(self.monitor.current_sort, 1)
#             self.monitor.sort_options_menu()
#             self.assertEqual(self.monitor.current_sort, 0)

#     @patch('curses.stdscr')
#     def test_get_filter_text(self, mock_stdscr):
#         # Test get filter text
#         self.monitor.stdscr = mock_stdscr
#         mock_stdscr.getstr.return_value = b'python'
#         filter_text = self.monitor.get_filter_text()
#         self.assertEqual(filter_text, 'python')
def main():
    monitor = PyTop()
    try:
        monitor.run()
    finally:
        curses.endwin()
if __name__ == '__main__':
    # unittest.main()
    main()
