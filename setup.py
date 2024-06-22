import mysql.connector


DB_USER = "YOUR MYSQL USER_NAME"
DB_PASSWORD = "YOUR MYSQL PASSWORD"


db = mysql.connector.connect(
    host='localhost',
    user=DB_USER,
    password=DB_PASSWORD
)

mc = db.cursor()
mc.execute("DROP DATABASE IF EXISTS RECIPES")
mc.execute("CREATE DATABASE IF NOT EXISTS RECIPES")
mc.close()
db.disconnect()

db = mysql.connector.connect(
    host='localhost',
    user=DB_USER,
    password=DB_PASSWORD,
    database="RECIPES"
)

mc = db.cursor()


def database():

    # DATABASE CONNECTION AND INTERFACING

    # Establishing initial connection
    db = mysql.connector.connect(
        host='localhost',
        user=DB_USER,
        password=DB_PASSWORD
    )

    # Creating database
    mc = db.cursor()
    mc.execute("DROP DATABASE IF EXISTS RECIPES")
    mc.execute("CREATE DATABASE IF NOT EXISTS RECIPES")
    mc.close()
    db.disconnect()

    # Connecting to database
    db = mysql.connector.connect(
        host='localhost',
        user='sqluser',
        password='password',
        database="RECIPES"
    )

    mc = db.cursor()
    mc.execute(
        "CREATE TABLE IF NOT EXISTS USERS(USER_ID INT PRIMARY KEY,USER_NAME VARCHAR(25),PASSWORD VARCHAR(25)) ")

    mc.execute("CREATE TABLE IF NOT EXISTS RECIPE(RECIPE_ID INT AUTO_INCREMENT PRIMARY KEY,RECIPE_NAME VARCHAR(255),USER_ID INT,TAG VARCHAR(1),TYPE VARCHAR(1),INGREDIENTS MEDIUMTEXT ,PROCESS MEDIUMTEXT,FOREIGN KEY(USER_ID) REFERENCES USERS(USER_ID))")

    mc.execute("CREATE TABLE IF NOT EXISTS RESPONSE(RECIPE_ID INT, COMMENTS MEDIUMTEXT, RATING INT, FOREIGN KEY(RECIPE_ID) REFERENCES RECIPE(RECIPE_ID))")

    mc.execute(
        "INSERT INTO USERS(USER_ID,USER_NAME,PASSWORD) VALUES(0,'ADMIN','1234')")


    mc.execute('''INSERT INTO RECIPE (USER_ID,RECIPE_NAME,TAG,TYPE,INGREDIENTS,PROCESS) VALUES(0,'COOKIE DOUGH','V','B',"1 cup all-purpose flour
    ¾ cup packed brown sugar
    ½ cup butter
    1 teaspoon vanilla extract
    ½ teaspoon salt
    2 tablespoons milk
    ½ cup milk chocolate chips
    ½ cup white chocolate chips",
    "STEP 1
    To heat-treat your flour so it is safe to use: Place flour in a microwave-safe dish and cook for 1 minute and 15 seconds, 
    stirring it every 15 seconds. Set aside.

    STEP 2
    Beat sugar and butter with an electric mixer in a large bowl until creamy. Beat in vanilla extract and salt. 
    Add heat-treated flour; mix until a crumbly dough forms. Stir in milk until dough is just combined
    fold in milk chocolate chips and white chocolate chips.
    ")''')

    mc.execute('''INSERT INTO RECIPE (USER_ID,RECIPE_NAME,TAG,TYPE,INGREDIENTS,PROCESS) VALUES(0,'MACRONI','V','B',"1 (8 ounce) box elbow macaroni
    ¼ cup butter
    ¼ cup all-purpose flour
    ½ teaspoon salt
    ground black pepper to taste
    2 cups milk
    2 cups shredded Cheddar cheese",
    "STEP 1
    Bring a large pot of lightly salted water to a boil. Cook elbow macaroni in the boiling water, 
    stirring occasionally until cooked through but firm to the bite, 8 minutes.

    STEP 2
    At the same time, melt butter in a saucepan over medium heat. Add flour, salt, and pepper and stir until smooth, about 5 minutes.
    Pour in milk slowly, while stirring continuously. Continue to cook and stir until mixture is smooth and bubbling, about 5 minutes, 
    making sure the milk doesn't burn.

    STEP 3
    Add Cheddar cheese and stir until melted, 2 to 4 minutes.

    STEP 4
    Drain macaroni and fold into cheese sauce until coated.
    ")''')

    mc.execute('''INSERT INTO RECIPE (USER_ID,RECIPE_NAME,TAG,TYPE,INGREDIENTS,PROCESS) VALUES(0,'CHITRANA','V','D',"3 cup leftover rice
    ½ lemon
    2 tbsp coriander (finely chopped)
    peanuts",
    "STEP 1
    firstly, take 3 cup of leftover rice and add 2 tbsp prepared lemon rice gojju and peanuts.

    STEP 2
    also add ½ lemon juice and 2 tbsp coriander. mix well.

    STEP 3
    finally, enjoy lemon rice with coconut chutney.
    ")''')

    mc.execute('''INSERT INTO RECIPE (USER_ID,RECIPE_NAME,TAG,TYPE,INGREDIENTS,PROCESS) VALUES(0,'CURD RICE','V','L',"1/2 cup boiled rice
    1 cup thick curd
    1/2 + 1/2 cup milk boiled and cooled
    1 tbsp butter
    1 tbsp coriander leaves finely chopped
    1 tsp ginger finely chopped
    1 no green chilli finely chopped",
    "STEP 1
    Take boiled rice and mash it
    Now add 1/2 cup milk(boiled, cooled).
    Add 1 cup thick curd.
    Add 1 tbsp butter along with required salt.

    STEP 2
    Mix this well first. It should be goey not too thick.
    Add 1/4 cup more curd if needed.
    Add 1 tbsp coriander leaves, 1 tsp finely chopped curry leaves along with 1 green chilli finely chopped and 1 tsp ginger finely chopped.
    Set aside. 

    STEP 3
    For tadka : Heat 2 tsp oil – add 1 tsp mustard seeds let it crackle. Once it crackles add 1/2 tsp urad dal.
    Add a pinch of hing.
    Add 2 small red chillies along with few curry leaves. Let it splutter. Fry until dals turn golden brown.
    Add tadka to curd rice.
    Mix well. Creamy yummy curd rice is ready.
    ")''')

    mc.execute('''INSERT INTO RECIPE (USER_ID,RECIPE_NAME,TAG,TYPE,INGREDIENTS,PROCESS) VALUES(0,'RAGI MUDDE','V','L',
    "1/4 cup rice
    1 cup ragi
    1/2 cup water
    salt",
    "Heat water in a heavy bottom pan. Add salt and oil and bring it to a boil.
    Add in rice and simmer for couple of mins.
    Now tip all the ragi flour into the water and don't stir it, 
    just cover the pan with a lid and simmer on low heat for 5 to 6 mins.
    Remove it off the heat, use back of the spoon to stir it well into the water.
    Now put it back on heat and cook for couple more mins.
    Take it off the heat and cover it with a lid. Set aside for 5 mins.
    Now remove this to a bowl.
    Cool it down a bit. Now shape this into ball and serve with any spicy curries.
    ")''')

    mc.execute('''INSERT INTO RECIPE (USER_ID,RECIPE_NAME,TAG,TYPE,INGREDIENTS,PROCESS) VALUES(0,'MEEN POLLICHATHU','N','D',
    "Fish 2 whole(300 grams)
    Onion 3 big
    Tomato 2 medium
    Garlic 10-12
    Green chilli 2
    Ginger garlic paste 1.5 tsp
    Red chilli powder 2 tsp
    Coriander powder 1 tsp
    Turmeric powder 1/2 tsp
    Salt as required
    Garam masala 1/4 tsp
    Curry leaves handful
    Oil 2.5 tbsp
    Coriander leaves 3 tbsp finely chopped",
    "Mix all the masala given under marination to form a thick paste and coat the fish
    In the tawa add little oil and shallow fry the fish on both sides till golden.
    Heat remaining oil and add finely chopped garlic, green chillies, and curry leaves.
    Then add finely chopped onions and saute till golden.
    Next, add ginger garlic paste and saute till the raw smell goes.
    Then add tomatoes and saute till mushy.
    Add salt, red chilli powder, coriander powder, turmeric powder, and garam masala to it.
    Add little water to it and cook till masala is nicely coated and oil oozing out.
    Garnish with coriander leaves and switch off the flame.
    Delicious onion tomato masala is ready.
    Take a banana leaf and show it in flame for few seconds to soften it so it doesn't tear while folding.
    Take a wilted banana leaf and add the masala to it.
    Place the fish on top of it.
    Cover it with masala again.
    Then wrap the banana leaves and fold them. Seal it with a toothpick.
    Heat a dosa pan or flat pan and place the wrapped banana leaf
    Close it with a lid and cook on low flame for 4-5 minutes.
    Flip the fish and cook again for 4-5 minutes.
    Remove from the flame and serve it hot.
    Meen pollichathu is ready.
    ")''')

    mc.execute('''INSERT INTO RECIPE (USER_ID,RECIPE_NAME,TAG,TYPE,INGREDIENTS,PROCESS) VALUES(0,'AVALAKKI UPPITU','V','B',
    "2 cups avalakki/ poha
    Salt to taste
    2 tbsp lemon juice
    2 tbsp oil
    1 tsp mustard seeds
    1 tbsp chana dal/ split desi chickpeas
    1 tbsp urad dal/ split matpe beans
    2-4 green chilis (minced)
    A few curry leaves
    2 medium yellow onion (finely diced)
    1/2 tsp turmeric
    1/2 cup peas
    A handful of finely chopped cilantro",
    "Add 2 cups of avalakki/ poha to a bowl. Rinse with water and drain. Repeat twice to wash the avalakki.
    Then, add fresh water. Add enough water to completely cover the avalakki/poha. Let it soak for 5 minutes.
    After 5 minutes, drain the water in a strainer/colander and transfer the avalakki to a dry container. Let dry for 2-3 minutes.
    Then, add 2 tbsp lemon juice and salt to taste. Mix well. Keep aside.
    Heat 2 tbsp oil in a sauté pan at a medium flame.
    Add 1 tsp mustard seeds to the oil.
    Once the mustard seeds crackle, add 1 tbsp chana dal and 1 tbsp urad dal. Sauté for a few minutes.
    The dal should change color slightly and become golden.
    Add 2-4 green chilis (minced), a few curry leaves, and 2 medium yellow onions (finely diced). Sauté till translucent.
    Add 1/2 tsp turmeric. Sauté till the raw smell of turmeric disappears.
    Add in 1/2 cup of green peas. Reduce the flame (to prevent the dal from burning), and cook for a few minutes.
    Once the peas are cooked, take off flame. Mix in the avalakki/ poha.
    Add more salt and lemon if required. Garnish with a handful of finely chopped coriander.
    ")''')

    """
    1       COOKIE DOUGH     
    2       MACRONI          
    3       CHITRANA         
    4       CURD RICE        
    5       RAGI MUDDE       
    6       Meen Pollichathu 
    7       Avalakki Uppittu 
    """

    mc.execute(
        "INSERT INTO RESPONSE(RECIPE_ID,COMMENTS,RATING) VALUES(1,'YUMMM',5)")
    mc.execute(
        "INSERT INTO RESPONSE(RECIPE_ID,COMMENTS,RATING) VALUES(1,'NOICE',4)")

    mc.execute(
        "INSERT INTO RESPONSE(RECIPE_ID,COMMENTS,RATING) VALUES(2,'NOICE',5)")
    mc.execute(
        "INSERT INTO RESPONSE(RECIPE_ID,COMMENTS,RATING) VALUES(2,'TASTYYYY',4)")

    mc.execute(
        "INSERT INTO RESPONSE(RECIPE_ID,COMMENTS,RATING) VALUES(3,'SUPPERB',4)")
    mc.execute(
        "INSERT INTO RESPONSE(RECIPE_ID,COMMENTS,RATING) VALUES(3,'YUMMMM',3)")

    mc.execute(
        "INSERT INTO RESPONSE(RECIPE_ID,COMMENTS,RATING) VALUES(4,'BESSSTT',3)")
    mc.execute(
        "INSERT INTO RESPONSE(RECIPE_ID,COMMENTS,RATING) VALUES(4,'TASTYYYY',4)")

    mc.execute(
        "INSERT INTO RESPONSE(RECIPE_ID,COMMENTS,RATING) VALUES(5,'NOICE',3)")
    mc.execute(
        "INSERT INTO RESPONSE(RECIPE_ID,COMMENTS,RATING) VALUES(5,'SUPPERB',4)")

    mc.execute(
        "INSERT INTO RESPONSE(RECIPE_ID,COMMENTS,RATING) VALUES(6,'DELICIOUSSS',3)")
    mc.execute(
        "INSERT INTO RESPONSE(RECIPE_ID,COMMENTS,RATING) VALUES(6,'YUMMMMM',4)")

    mc.execute(
        "INSERT INTO RESPONSE(RECIPE_ID,COMMENTS,RATING) VALUES(7,'BESSTT',3)")
    mc.execute(
        "INSERT INTO RESPONSE(RECIPE_ID,COMMENTS,RATING) VALUES(7,'SUPPERB',4)")

    db.commit()

if __name__=="__main__":
    database()
    print("Done")