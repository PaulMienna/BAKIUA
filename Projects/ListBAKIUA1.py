# User input for dogs' name.
dogNameInput=(input("Enter dogs' name."))


# Using a random number generator we can collect 5 random values assuming the longest lifespan for these dogs are 13 years.
dogName= {
    "Charlie": 1,
    "Bella": 13,
    "Milo": 5,
    "Teddy": 8,
    "Cooper": 6
}


if dogNameInput in dogName:
    dogYears = dogName[dogNameInput]


    humanYears = dogYears / 7 # if 1 human year is equivalent to 7 dog years, we can calculate it as such.
    print(f'{dogName} is {dogYears} dog years, which is the equivalent to {humanYears} human years old')
else:
    print(f'{dogName} is not in the list')
