{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fa6f7c4f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter N: 1\n",
      "2\n",
      "3\n",
      "-1\n"
     ]
    }
   ],
   "source": [
    "N = int(input(\"Enter N: \"))\n",
    "\n",
    "numbers = []\n",
    "for i in range(N):\n",
    "    numbers.append(int(input()))\n",
    "\n",
    "X = int(input())\n",
    "\n",
    "if X in numbers:\n",
    "    print(numbers.index(X) + 1)\n",
    "else:\n",
    "    print(-1)\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a418abc5",
   "metadata": {},
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
