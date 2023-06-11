#!/usr/bin/env python3
import random
import prompt


GAME_CONFIG = {
    "win_target": 3,
    "start_range": [1, 30],
    "step_range": [1, 5],
    "index_range": [0, 9]
}


def main(config=GAME_CONFIG):
    print("Welcome to the Brain Games!")

    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")

    print("What number is missing in the progression?")
    correct_answers_counter = 0
    (start_range_from, start_range_to) = config["start_range"]
    (step_range_from, step_range_to) = config["step_range"]
    (index_range_from, index_range_to) = config["index_range"]

    while correct_answers_counter != config["win_target"]:
        start = random.randint(start_range_from, start_range_to)
        step = random.randint(step_range_from, step_range_to)
        proggression = [str(start + step * i) for i in range(10)]
        hidden_el_index = random.randint(index_range_from, index_range_to)
        hidden_el = proggression[hidden_el_index]
        proggression[hidden_el_index] = ".."
        progression = ' '.join(proggression)

        print(f"Question: {progression}")

        answer = prompt.string("Your answer: ")

        if answer == hidden_el:
            print("Correct!")
            correct_answers_counter += 1
        else:
            print(
                f"{answer} is wrong answer ;(. "
                + f"Correct answer was {hidden_el}.\n"
                + f"Let's try again, {name}!"
            )
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
