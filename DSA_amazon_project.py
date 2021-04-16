{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "import string"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "# This function will generate a unique id for each user \n",
    "def generateId():\n",
    "    tokens = list(string.ascii_letters + string.digits)\n",
    "    user_id = ''\n",
    "    for i in range(6):\n",
    "        user_id += random.choice(tokens)\n",
    "    return user_id\n",
    "# print(generateId())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Amazon:\n",
    "    def __init__(self):\n",
    "        self.id = None\n",
    "        self.name = None\n",
    "        self.email = None\n",
    "        self.order_cart = None\n",
    "        # initially the user is \"not a prime user\"\n",
    "        # prime user -> 0\n",
    "        # non-prime user -> 1\n",
    "        self.is_prime_user = 1\n",
    "    \n",
    "    def getDetails(self):\n",
    "        self.id = generateId();\n",
    "        self.name = input(\"Enter your name please :\")\n",
    "        self.email = input(\"Enter your email address : \")\n",
    "        \n",
    "        \n",
    "    def buyPrime(self):\n",
    "        self.is_prime_user = 0\n",
    "        \n",
    "    def buyItems(self):\n",
    "        self.order_cart = [i for i in input(\"Enter what you want to buy : \").split(\", \")]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "user_list = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "def findUserPosition(new_user):\n",
    "    position = 0\n",
    "    for i in range(len(user_list)):\n",
    "        if user_list[i].is_prime_user <= new_user.is_prime_user:\n",
    "            position += 1\n",
    "    return position       \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your name please :aman\n",
      "Enter your email address : aman@gmail.com\n",
      "Want to order something ? y/n : y\n",
      "Enter what you want to buy : mobile\n",
      "Want to buy prime ? y/n : n\n",
      "Want to add more users ? y/n : y\n",
      "Enter your name please :ritik\n",
      "Enter your email address : rtk@gmail.com\n",
      "Want to order something ? y/n : y\n",
      "Enter what you want to buy : shoes\n",
      "Want to buy prime ? y/n : n\n",
      "Want to add more users ? y/n : y\n",
      "Enter your name please :mayank\n",
      "Enter your email address : mynk@gmail.com\n",
      "Want to order something ? y/n : y\n",
      "Enter what you want to buy : earphone\n",
      "Want to buy prime ? y/n : y\n",
      "Want to add more users ? y/n : n\n"
     ]
    }
   ],
   "source": [
    "ch = 'y'\n",
    "while ch == 'y':\n",
    "    new_user = Amazon()\n",
    "    new_user.getDetails()\n",
    "    \n",
    "    inp = input(\"Want to order something ? y/n : \")\n",
    "    if inp == 'y':\n",
    "        new_user.buyItems()\n",
    "    \n",
    "    inp = input(\"Want to buy prime ? y/n : \")\n",
    "    if inp == 'y':\n",
    "        new_user.buyPrime()\n",
    "    \n",
    "    # While taking input itself we will arrange the prime and non-prime users :)\n",
    "    position = findUserPosition(new_user)\n",
    "    user_list.insert(position, new_user)\n",
    "    \n",
    "    inp = input(\"Want to add more users ? y/n : \")\n",
    "    if inp == 'n':\n",
    "        break\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "mayank 0 ['earphone']\n",
      "aman 1 ['mobile']\n",
      "ritik 1 ['shoes']\n"
     ]
    }
   ],
   "source": [
    "for user in user_list:\n",
    "    print(user.name, user.is_prime_user, user.order_cart)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# No need to sort the user_list actually :( \n",
    "# We can use priority queue using which we will be giving more priority to Prime users :)\n",
    "# And thus our time complexity of the code will be reduced to O(n)\n",
    "# where n is the number of users\n",
    "\n",
    "# ----------------------------------------------------------------------------\n",
    "# user_list = sorted(user_list, key = lambda each_user: each_user.is_prime_user)\n",
    "# ----------------------------------------------------------------------------"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello  mayank , your order is shipped under Prime Delivery\n",
      "Hello  aman , your order is shipped\n",
      "Hello  ritik , your order is shipped\n"
     ]
    }
   ],
   "source": [
    "for user in user_list:\n",
    "    if user.is_prime_user == 0:\n",
    "        print(\"Hello \", user.name, \", your order is shipped under Prime Delivery\")\n",
    "    else:\n",
    "        print(\"Hello \", user.name, \", your order is shipped\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
