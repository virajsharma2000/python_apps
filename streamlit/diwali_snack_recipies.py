recipies = {
  "recipes": [
    {
      "name": "Samosa",
      "ingredients": [
        {"item": "all-purpose flour", "quantity": "2 cups"},
        {"item": "oil", "quantity": "4 tbsp"},
        {"item": "salt", "quantity": "to taste"},
        {"item": "boiled potatoes", "quantity": "4 (mashed)"},
        {"item": "peas", "quantity": "1/2 cup"},
        {"item": "cumin seeds", "quantity": "1 tsp"},
        {"item": "garam masala", "quantity": "1 tsp"},
        {"item": "chili powder", "quantity": "1/2 tsp"},
        {"item": "coriander", "quantity": "1 tbsp"}
      ],
      "instructions": [
        "Make a stiff dough with flour, oil, and salt. Rest for 30 minutes.",
        "Heat oil, add cumin, potatoes, peas, and spices. Sauté for 2 minutes.",
        "Roll dough, cut into half-moons, fill with potato mixture.",
        "Seal and deep fry until golden brown. Serve with chutney."
      ]
    },
    {
      "name": "Kaju Katli",
      "ingredients": [
        {"item": "cashews", "quantity": "1 cup"},
        {"item": "sugar", "quantity": "1/2 cup"},
        {"item": "water", "quantity": "1/4 cup"},
        {"item": "ghee", "quantity": "1 tsp"},
        {"item": "silver leaf", "quantity": "optional"}
      ],
      "instructions": [
        "Grind cashews into fine powder.",
        "Heat sugar and water to make a syrup.",
        "Add cashew powder and stir until thick.",
        "Spread on a greased plate, cool, and cut into diamonds."
      ]
    },
    {
      "name": "Chakli",
      "ingredients": [
        {"item": "rice flour", "quantity": "2 cups"},
        {"item": "gram flour", "quantity": "1 cup"},
        {"item": "cumin", "quantity": "1 tsp"},
        {"item": "sesame seeds", "quantity": "1 tsp"},
        {"item": "butter", "quantity": "2 tbsp"},
        {"item": "salt", "quantity": "to taste"}
      ],
      "instructions": [
        "Mix flours, cumin, sesame seeds, butter, and salt.",
        "Add water to make dough. Shape using chakli press.",
        "Deep fry until golden brown."
      ]
    },
    {
      "name": "Besan Ladoo",
      "ingredients": [
        {"item": "gram flour", "quantity": "2 cups"},
        {"item": "powdered sugar", "quantity": "1 cup"},
        {"item": "ghee", "quantity": "1/2 cup"},
        {"item": "cardamom powder", "quantity": "1 tsp"}
      ],
      "instructions": [
        "Roast gram flour in ghee until aromatic.",
        "Mix in powdered sugar and cardamom powder.",
        "Shape into small balls and let cool."
      ]
    },
    {
      "name": "Shakarpara",
      "ingredients": [
        {"item": "flour", "quantity": "2 cups"},
        {"item": "sugar", "quantity": "1/2 cup"},
        {"item": "ghee", "quantity": "1/4 cup"},
        {"item": "oil", "quantity": "for frying"}
      ],
      "instructions": [
        "Mix flour, sugar, and ghee to make dough.",
        "Roll out and cut into diamond shapes.",
        "Deep fry until golden brown."
      ]
    },
    {
      "name": "Mathri",
      "ingredients": [
        {"item": "all-purpose flour", "quantity": "2 cups"},
        {"item": "oil", "quantity": "4 tbsp"},
        {"item": "cumin seeds", "quantity": "1 tsp"},
        {"item": "salt", "quantity": "to taste"}
      ],
      "instructions": [
        "Mix flour, oil, cumin seeds, and salt.",
        "Add water to make stiff dough.",
        "Roll into discs, prick with fork, and fry until crisp."
      ]
    },
    {
      "name": "Gulab Jamun",
      "ingredients": [
        {"item": "khoya", "quantity": "1 cup"},
        {"item": "flour", "quantity": "1/4 cup"},
        {"item": "baking powder", "quantity": "1/4 tsp"},
        {"item": "sugar syrup", "quantity": "2 cups sugar + 1 cup water"}
      ],
      "instructions": [
        "Mix khoya, flour, and baking powder to make dough.",
        "Shape into balls and deep fry until golden brown.",
        "Soak in warm sugar syrup for 2 hours before serving."
      ]
    },
    {
      "name": "Namak Para",
      "ingredients": [
        {"item": "flour", "quantity": "2 cups"},
        {"item": "oil", "quantity": "2 tbsp"},
        {"item": "ajwain", "quantity": "1 tsp"},
        {"item": "salt", "quantity": "to taste"}
      ],
      "instructions": [
        "Mix flour, ajwain, salt, and oil.",
        "Add water to make firm dough.",
        "Cut into strips and deep fry until crispy."
      ]
    }
  ]
}

def get_snack_recipies(snack_name):
 global recipies

 for snack in recipies['recipes']:
  if snack['name'] == snack_name:
   return [[ingredient['item'] + ' - ' + ingredient['quantity'] for ingredient in snack['ingredients']], [instruction for instruction in snack['instructions']]]
   break

def get_snack_options():
 global recipies

 return [snack['name'] for snack in recipies['recipes']]


    
