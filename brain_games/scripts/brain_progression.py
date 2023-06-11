#!/usr/bin/env python3
import random
import prompt


def main():
    print("Welcome to the Brain Games!")

    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")

    print("What number is missing in the progression?")
    correct_answers_counter = 0

    while correct_answers_counter != 3:
        start = random.randint(1, 30)
        step = random.randint(1, 5)
        proggression = [str(start + step*i) for i in range(10)]
        hidden_el_index = random.randint(0, 9)
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
                f"{answer} is wrong answer ;(. " +
                f"Correct answer was {hidden_el}.\n" +
                f"Let's try again, {name}!"
            )
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
