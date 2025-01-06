{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b48599d6-9b5b-41b3-9f8b-69b354df7de2",
   "metadata": {},
   "outputs": [],
   "source": [
    "def verification(accounts):\n",
    "    \n",
    "    name_validation = True\n",
    "    while name_validation:\n",
    "        try:  \n",
    "            account_title = input(\"Please Enter Your Name: \").strip().title()\n",
    "    \n",
    "            if account_title == \"\":\n",
    "                raise Exception(\"Input is empty! Please make sure you have entered your name.\")\n",
    "                \n",
    "            account_found = False\n",
    "            for pin,account in accounts.items():\n",
    "                if account[\"name\"] == account_title:\n",
    "                    account_found = True\n",
    "                    user_account = account\n",
    "                    user_pin = pin\n",
    "                    name_validation = False\n",
    "                    \n",
    "            if not account_found:\n",
    "                raise Exception(f\"No account found with the name {account_title}. Please try again.\")\n",
    "        except Exception as e:\n",
    "            print(e)\n",
    "\n",
    "    pin_validation = True\n",
    "    while pin_validation:\n",
    "        try:        \n",
    "            user_ent_pin = input(\"Please enter your pin: \")\n",
    "            if user_ent_pin == \"\":\n",
    "                raise Exception(\"Input is Empty! Please make sure to enter your pin: \")\n",
    "            else:\n",
    "                user_ent_pin = int(user_ent_pin)\n",
    "\n",
    "            if user_ent_pin != user_pin:\n",
    "                raise Exception(\"Incorrect Pin! Please try again: \")\n",
    "            else:\n",
    "                \n",
    "                pin_validation = False\n",
    "        except Exception as e:\n",
    "            print(e)\n",
    "    return account_title,user_account"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6772399b-22aa-4bb1-a95f-61c2ea5ba525",
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
