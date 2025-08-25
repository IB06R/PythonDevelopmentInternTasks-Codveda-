{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM5T9HDRcY370aZRVqrYHqa"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vzkJhjJaUyuf",
        "outputId": "52a5c62a-6947-4149-c658-2c9ec26d011e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Welcome to the Number Guessing Game!\n",
            "I'm thinking of a number between 1 and 100. You have 10 attempts.\n",
            "Enter your guess: 12\n",
            "Too low! Try again.\n",
            "Enter your guess: 24\n",
            "Too high! Try again.\n",
            "Enter your guess: 20\n",
            "Too low! Try again.\n",
            "Enter your guess: 21\n",
            "Too low! Try again.\n",
            "Enter your guess: 22\n",
            "Too low! Try again.\n",
            "Enter your guess: 23\n",
            "Congratulations! You guessed the number in 6 attempts.\n"
          ]
        }
      ],
      "source": [
        "import random\n",
        "\n",
        "def number_guessing_game():\n",
        "    \"\"\"Plays a number guessing game with the user.\"\"\"\n",
        "    secret_number = random.randint(1, 100)\n",
        "    max_attempts = 10\n",
        "    attempts = 0\n",
        "\n",
        "    print(\"Welcome to the Number Guessing Game!\")\n",
        "    print(f\"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts.\")\n",
        "\n",
        "    while attempts < max_attempts:\n",
        "        try:\n",
        "            guess = int(input(\"Enter your guess: \"))\n",
        "            attempts += 1\n",
        "\n",
        "            if guess == secret_number:\n",
        "                print(f\"Congratulations! You guessed the number in {attempts} attempts.\")\n",
        "                return\n",
        "            elif guess < secret_number:\n",
        "                print(\"Too low! Try again.\")\n",
        "            else:\n",
        "                print(\"Too high! Try again.\")\n",
        "        except ValueError:\n",
        "            print(\"Invalid input. Please enter an integer.\")\n",
        "\n",
        "    print(f\"Sorry, you ran out of attempts. The secret number was {secret_number}.\")\n",
        "\n",
        "# Start the game\n",
        "number_guessing_game()"
      ]
    }
  ]
}