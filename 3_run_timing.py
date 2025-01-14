def run_timing():
    result = 0
    arguments = 0

    while True:
        run = input("Enter 10km run time: ")
        
        try:
            result += float(run)
            arguments += 1
        except ValueError:
            if not run:
                print(f"Your average was {result / arguments} minutes over {arguments} runs.")
                break
            print("That's not a number!")
            continue

    return result / arguments

run_timing()


