import sys
import cProfile
import pstats

from PySide6.QtWidgets import QApplication
from gui.mainWindow import MainWindow


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    cProfile.run("main()", "profile_stats")
    stats = pstats.Stats("profile_stats")
    stats.sort_stats("cumulative").print_stats(
        10
    )  # Show top 10 time-consuming functions
