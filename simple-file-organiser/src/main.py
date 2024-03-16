import cli
import gui
import sys

def main():
    if len(sys.argv) >= 1:
        cli.run()
    else:
        gui.run()

if __name__ == "__main__":
    main()
