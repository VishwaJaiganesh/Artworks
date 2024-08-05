# Define categories or subjects that user can play
categories=["Geography","History","Science","Sports","Video Games","Music","TV & Movies","quit","geography","history","science","sports","video games","Music","tv & movies","Quit"]
# Define difficulty levels that user can play
difficulty=["Very Easy","Easy","Normal", "Medium", "Hard","Very Hard",'Extreme',"very easy","easy","normal", "medium", "hard","very hard",'extreme']
 
 
# Create a list of questions with their corresponding category, difficulty, answer and score
questions = [
    {
        "category": "Geography",
        "difficulty": "Very Easy",
        "question": "What continent is Japan on?",
        "answer": "Asia",
        "score":100
    },
    {
        "category": "Geography",
        "difficulty": "Easy",
        "question": "What is the tallest mountain?",
        "answer": "Mt.Everest",
         "score":250
    },
    {
        "category": "Geography",
        "difficulty": "Normal",
        "question": "Capital of Brazil?",
        "answer": "Brasilia",
         "score":500
    },
    {
        "category": "Geography",
        "difficulty": "Medium",
        "question": "What is the name of the World’s Largest Desert?",
        "answer": "Antartica",
        "score":750
    },
    {
        "category": "Geography",
        "difficulty": "Hard",
        "question": "What body of water is located west of Saudi Arabia?",
        "answer": "The Red Sea",
        "score":1000
   },
    {
        "category": "Geography",
        "difficulty": "Very Hard",
        "question": "What native language is spoken in Scotland?",
        "answer": "Scotland Gaelic",
         "score":1250
    },
    {
        "category": "Geography",
        "difficulty": "Extreme",
        "question": "How many countries and territories have the Union Jack in their flags?",
        "answer": "23",
         "score":1500
    },
     {
        "category": "History",
        "difficulty": "Very Easy",
        "question": "Who won the space race?",
        "answer": "USSR",
         "score":100
    },
    {
        "category": "History",
        "difficulty": "Easy",
        "question": "What was the term for the Spanish colonists?",
        "answer": "Conquistador",
         "score":250
    },
    {
        "category": "History",
        "difficulty": "Normal",
        "question": "Who was the ruler of the Mongol Empire?",
        "answer": "Genghis Khan",
        "score":500
    },
    {
        "category": "History",
        "difficulty": "Medium",
        "question": "What year was the battle of Hastings?",
        "answer": "1066",
         "score":750
    },
    {
        "category": "History",
        "difficulty": "Hard",
        "question": "Who died causing WW1?",
        "answer": "Franz Ferdinand",
        "score":1000
    },
    {
        "category": "History",
        "difficulty": "Very Hard",
        "question": "Who was the world’s richest person?",
        "answer": "Mansa Musa",
         "score":1250
    },
    {
        "category": "History",
        "difficulty": "Extreme",
        "question": "What years were the start and end of the Bubonic Plague?",
        "answer": "1346 to 1353",
         "score":1500
    }
     {
        "category": "TV & Movies",
        "difficulty": "Very Easy",
        "question": "What is Indian cinema called?",
        "answer": "Bollywood",
         "score":100
    },
    {
        "category": "TV & Movies",
        "difficulty": "Easy",
        "question": "Which superhero’s name is Hal Jordan?",
        "answer": "Green Lantern",
         "score":250
    },
    {
        "category": "TV & Movies",
        "difficulty": "Normal",
        "question": "What was considered, 'the world’s scariest movie'?",
        "answer": "The Exorcist",
         "score":500
    },
    {
        "category": "TV & Movies",
        "difficulty": "Medium",
        "question": "Who was the antagonist of the movie Black Panther?",
        "answer": "Killmonger",
        "score":750
    },
    {
        "category": "TV & Movies",
        "difficulty": "Hard",
        "question": "What is Voldemort’s real full name?",
        "answer": "Tom Marvolo Riddle",
                              "score":1000
    },
    {
        "category": "TV & Movies",
        "difficulty": "Very Hard",
        "question": "Which actress plays the main protagonist of the hunger games series?",
        "answer": "Jennifer Lawrence",
        "score":1250
    },
    {
        "category": "TV & Movies",
        "difficulty": "Extreme",
        "question": "Which Academy Awards ceremony did Will Smith slap Chris Rock?",
        "answer": "94",
         "score":1500
    },
     {
        "category": "Science",
        "difficulty": "Very Easy",
        "question": "What is the 6th planet from the Sun?",
        "answer": "Saturn",
        "score":100
    },
    {
        "category": "Science",
        "difficulty": "Easy",
        "question": "What is the name of the body system in charge of the skeleton?",
        "answer": "Skeletal System",
         "score":250
    },
    {
        "category": "Science",
        "difficulty": "Normal",
        "question": "Who invented the light bulb?",
        "answer": "Thomas Edison",
        "score":500
    },
    {
        "category": "Science",
        "difficulty": "Medium",
        "question": "What did Alexander Fleming invent?",
        "answer": "Penicillin",
                              "score":750
    },
    {
        "category": "Science",
        "difficulty": "Hard",
        "question": "What element is Sb?",
        "answer": "Antimony",
                              "score":1000
    },
    {
        "category": "Science",
        "difficulty": "Very Hard",
        "question": "What is the name of the chemical formula NH3",
        "answer": "Ammonia",
                              "score":1250
    },
    {
        "category": "Science",
        "difficulty": "Extreme",
        "question": "What tectonic plate is between the Pacific and North American Plates",
        "answer": "Juan de Fuca Plate",
        "score":1500
    category": "Sports",
        "difficulty": "Very Easy",
        "question": "What is the term for scoring 100 runs in Cricket?",
        "answer": "century",
        "score":100
    },
    {
        "category": "Sports",
        "difficulty": "Easy",
        "question": "Where was 2022 FIFA World Cup held?",
        "answer": "Qatar",
        "score":250
    },
    {
        "category": "Sports",
        "difficulty": "Normal",
        "question": "Who is world number 1 in Tennis at present?",
        "answer": "Novak Djokovic",
        "score":500
    },
    {
        "category": "Sports",
        "difficulty": "Medium",
        "question": "Which NBA team has a red bull in its logo?",
        "answer": "Chicago Bulls",
        "score":750
    },
    {
        "category": "Sports",
        "difficulty": "Hard",
        "question": "Number 1 AFL Club?",
        "answer": "Collingwood FC",
        "score":1000
    },
    {
        "category": "Sports",
        "difficulty": "Very Hard",
        "question": "Where were the Olympics held in the year 2000?",
        "answer": "Sydney",
        "score":1250
    },
    {
        "category": "Sports",
        "difficulty": "Extreme",
        "question": "What is the Olympic record for men's 100m freestyle?",
        "answer": "47.02 seconds",
        "score":1500
    },
     {
        "category": "Video Games",
        "difficulty": "Very Easy",
        "question": "What year did Fortnite release?",
        "answer": "2017",
        "score":100
    },
    {
        "category": "Video Games",
        "difficulty": "Easy",
        "question": "What is the name of the green mushroom powerup in Mario?",
        "answer": "1UP",
        "score":250
    },
    {
        "category": "Video Games",
        "difficulty": "Normal",
        "question": "What is the name of the main character in Halo?",
        "answer": "Masterchief",
        "score":500
    },
    {
        "category": "Video Games",
        "difficulty": "Medium",
        "question": "What are the names of the 2 dwarves in God of War?",
        "answer": "Sindri and Brok",
        "score":750
    },
    {
        "category": "Video Games",
        "difficulty": "Hard",
        "question": "What is the name of the main villain in Crash Bandicoot?",
        "answer": "Dr.Neo Cortex",
        "score":1000
    },
    {
        "category": "Video Games",
        "difficulty": "Very Hard",
        "question": "What was the first game Mario appeared in?",
        "answer": "Donkey Kong",
        "score":1250
    },
    {
        "category": "Video Games",
        "difficulty": "Extreme",
        "question": "How many potions are there in Minecraft?",
        "answer": "72",                      
        "score":1500
    },
         {
        "category": "Music",
        "difficulty": "Very Easy",
        "question": "Who is the most streamed artist on Spotify of all time?",
        "answer": "Drake",
        "score":100
    },
    {
        "category": "Music",
        "difficulty": "Easy",
        "question": "What is the most played instrument of all time?",
        "answer": "Piano",
        "score":250
    },
    {
        "category": "Music",
        "difficulty": "Normal",
        "question": "What musical family does the drum kit come under?",
        "answer": "Percussion",
        "score":500
    },
    {
        "category": "Music",
        "difficulty": "Medium",
        "question": "What decade did Tupac die?",
        "answer": "1990",
        "score":750
    },
    {
        "category": "Music",
        "difficulty": "Hard",
        "question": "Who wrote the song, 'it's now or never'?",
        "answer": "Elvis Presley",
        "score":1000
    },
   {
        "category": "Music",
        "difficulty": "Very Hard",
        "question": "How many songs are there on the Beatles' album, 'The Yellow Submarine'?",
        "answer": "13",
        "score":1250
    },
    {
        "category": "Music",
        "difficulty": "Extreme",
        "question": "Which instrument is associated with royalty?",
        "answer": "Trumpet",
        "score":1500
    }
]
# Initialize player's score
current_score=0

def trivia_game(current_score,name,categories):
 # Start the game   
# Present each question and evaluate the player's answer
# Number of rounds being played per player is a user input
    while True:
        number_of_rounds=int(input("Please enter number of rounds to play, minimum of 5: "))
        if number_of_rounds < 5:
            print("Enter value greater than 5")
        else:
            break
    
    for i in range (number_of_rounds):
        # Allow the player to select the category and difficulty level of the questions
       
        while True:
            selected_category = input("Select a category - Geography,History,TV & Movies,Science,Sports,Video Games,Music: \n(Enter 'quit' to end the game): ")
            #if selected category is in the list of categories, then it is a valid input else force user to enter valid category
            if selected_category in categories:
                break
            else:
               print("Enter correct category")
               
        #if user inputs quit when selecting category, user exits the game
        if selected_category.lower() == 'quit':
            print(f"Sorry to see you go {name}!")
            return
       
            
        while True:
             #if selected category is in the list of difficulties, then it is a valid input else force user to enter valid difficulty
            selected_difficulty = input("Select a difficulty level - Very Easy,Easy,Normal,Medium,Hard,Very Hard,Extreme: ")
            if selected_difficulty in difficulty:
                break
            else:
                print("Enter correct category")    
    