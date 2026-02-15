{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ccc2f609",
   "metadata": {},
   "outputs": [],
   "source": [
    "# module5_mod.py\n",
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
    "        return -1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "571eb834",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
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
