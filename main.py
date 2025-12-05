import utils.prep_helpers as ph

def main():
    # Fill in!
    day = '1'
    year = '2025'

    # Where script ?!
    root, project = ph.which_folder(day, year)

    # Need AOC env:SESSIONID Token
    ph.pull_input(day, year)

    # Run
    ph.run_script(root, project)

if __name__ == '__main__':
    main()
