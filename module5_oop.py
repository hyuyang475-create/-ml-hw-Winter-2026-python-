{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "18d6f57e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a positive integer N: 2\n",
      "Enter number 1: 1\n",
      "Enter number 2: 2\n",
      "Enter integer X to search: 5\n",
      "-1\n"
     ]
    }
   ],
   "source": [
    "# module5_oop.py\n",
    "\n",
    "class NumberCollection:\n",
    "    def __init__(self):\n",
    "        # Data initialization\n",
    "        self.numbers = []\n",
    "\n",
    "    def insert_number(self, number):\n",
    "        # Data insertion\n",
    "        self.numbers.append(number)\n",
    "\n",
    "    def find_number(self, x):\n",
    "        # Data search\n",
    "        for index, value in enumerate(self.numbers):\n",
    "            if value == x:\n",
    "                return index + 1  # 1-based index\n",
    "        return -1\n",
    "\n",
    "\n",
    "def read_positive_integer(prompt):\n",
    "    while True:\n",
    "        try:\n",
    "            value = int(input(prompt))\n",
    "            if value > 0:\n",
    "                return value\n",
    "            else:\n",
    "                print(\"Please enter a positive integer.\")\n",
    "        except ValueError:\n",
    "            print(\"Invalid input. Please enter a valid integer.\")\n",
    "\n",
    "\n",
    "def read_integer(prompt):\n",
    "    while True:\n",
    "        try:\n",
    "            return int(input(prompt))\n",
    "        except ValueError:\n",
    "            print(\"Invalid input. Please enter a valid integer.\")\n",
    "\n",
    "\n",
    "def main():\n",
    "    # Read N (must be positive)\n",
    "    N = read_positive_integer(\"Enter a positive integer N: \")\n",
    "\n",
    "    collection = NumberCollection()\n",
    "\n",
    "    # Read N numbers one by one\n",
    "    for i in range(N):\n",
    "        num = read_integer(f\"Enter number {i + 1}: \")\n",
    "        collection.insert_number(num)\n",
    "\n",
    "    # Read X\n",
    "    X = read_integer(\"Enter integer X to search: \")\n",
    "\n",
    "    # Output result\n",
    "    result = collection.find_number(X)\n",
    "    print(result)\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a1606c2f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
