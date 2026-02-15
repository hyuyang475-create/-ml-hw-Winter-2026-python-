{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "67d57ba9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# module5_call.py\n",
    "\n",
    "from module5_mod import NumberCollection\n",
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
    "    # Read N\n",
    "    N = read_positive_integer(\"Enter a positive integer N: \")\n",
    "\n",
    "    collection = NumberCollection()\n",
    "\n",
    "    # Read N numbers\n",
    "    for i in range(N):\n",
    "        num = read_integer(f\"Enter number {i + 1}: \")\n",
    "        collection.insert_number(num)\n",
    "\n",
    "    # Read X\n",
    "    X = read_integer(\"Enter integer X to search: \")\n",
    "\n",
    "    # Search and output result\n",
    "    result = collection.find_number(X)\n",
    "    print(result)\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
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
