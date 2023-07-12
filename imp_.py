import datetime as dt
from PIL import Image
import mysql.connector
import tkinter as tk
from customtkinter import *

db = mysql.connector.connect(
    host='localhost',
    user='sqluser',
    password='password'
)

mc = db.cursor()
mc.execute("DROP DATABASE IF EXISTS RECIPES")
mc.execute("CREATE DATABASE IF NOT EXISTS RECIPES")
mc.close()
db.disconnect()

db = mysql.connector.connect(
    host='localhost',
    user='sqluser',
    password='password',
    database="RECIPES"
)

mc = db.cursor()


def database():

    # DATABASE CONNECTION AND INTERFACING

    # Establishing initial connection
    db = mysql.connector.connect(
        host='localhost',
        user='sqluser',
        password='password',
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


database()


def login(name, password):
    p, ID = '', 0
    mc.execute(f"SELECT PASSWORD,USER_ID FROM USERS WHERE USER_NAME='{name}'")
    for i in mc:
        p, ID = i[0], i[1]
    if p == password:
        return True, ID
    else:
        return False, ID


def register(i, name, password):
    q = "INSERT INTO USERS(USER_ID,USER_NAME,PASSWORD) VALUES(%s,%s,%s)"
    val = (i, name, password)
    try:
        mc.execute(q, val)
    except mysql.connector.errors.IntegrityError:
        return "user id already taken"
    except:
        return "Something went wrong"
    else:
        db.commit()
        return "User registered successfully"


def segemented_button_callback(value):
    if (value == "Login"):
        label.configure(text="")
        return login_select()
    else:
        label.configure(text="")
        return register_select()


def login_clicked():
    val, i = login(str(login_user_name.get()).upper(),
                   login_password.get())
    if val:
        label.configure(text="Logged in succesfully")
        LOGIN.destroy()
        explore(i)
    else:
        label.configure(text="Incorrect data")


def register_clicked():
    val = register(register_user_id.get(), register_user_name.get(
    ).upper(), register_user_password.get())
    label.configure(text=val)


def login_select():
    global login_user_name
    login_user_name = StringVar(value="Username")
    global login_password
    login_password = StringVar(value="Password")

    lu = CTkEntry(
        LOGIN, font=general_font, corner_radius=20, width=200, textvariable=login_user_name)
    lu.bind("<FocusIn>", lambda e: login_user_name.set(""))
    lu.place(relx=.36, rely=.5)

    lp = CTkEntry(
        LOGIN, font=general_font, corner_radius=20, width=200, textvariable=login_password)
    lp.place(relx=.36, rely=.6)
    lp.bind("<FocusIn>", lambda e: login_password.set(""))

    CTkButton(
        LOGIN, text="Login", font=general_font, corner_radius=20, width=200, command=login_clicked).place(relx=.36, rely=.7)


def register_select():
    global register_user_id
    register_user_id = StringVar(value="Enter UserId")
    global register_user_name
    register_user_name = StringVar(value="Enter desired Username")
    global register_user_password
    register_user_password = StringVar(value="Enter desired password")
    rui = CTkEntry(
        LOGIN, font=general_font, corner_radius=20, width=200, textvariable=register_user_id)
    rui.place(relx=.36, rely=.5)
    rui.bind("<FocusIn>", lambda e: register_user_id.set(""))

    ru = CTkEntry(
        LOGIN, font=general_font, corner_radius=20, width=200, textvariable=register_user_name)
    ru.place(relx=.36, rely=.6)
    ru.bind("<FocusIn>", lambda e: register_user_name.set(""))

    rp = CTkEntry(
        LOGIN, font=general_font, corner_radius=20, width=200, textvariable=register_user_password)
    rp.place(relx=.36, rely=.7)
    rp.bind("<FocusIn>", lambda e: register_user_password.set(""))
    CTkButton(
        LOGIN, text="Register", font=general_font, corner_radius=20, width=200, command=register_clicked).place(relx=.36, rely=.8)


def explore_button_click():
    Explore_choice = CTk()
    Explore_choice.geometry("700x550")
    Explore_choice.title("Options")
    veg = BooleanVar(Explore_choice)
    nonveg = BooleanVar(Explore_choice)
    radio_var = IntVar(Explore_choice)
    general_font = CTkFont(family="Sans-serif", size=15)
    display_font = CTkFont(family="Sans-serif", size=20)
    CTkLabel(Explore_choice, text="Please enter a choice to proceed",
             font=display_font).place(relx=.35, rely=.10)
    CTkCheckBox(Explore_choice, text="Vegetarian", font=general_font,
                variable=veg, onvalue=True).place(relx=.2, rely=.4)
    CTkCheckBox(Explore_choice, text="Non-Vegetarian", font=general_font,
                variable=nonveg, onvalue=True).place(relx=.2, rely=.5)
    CTkRadioButton(Explore_choice, text="Breakfast", variable=radio_var,
                   value=1, font=general_font).place(relx=.50, rely=.40)
    CTkRadioButton(Explore_choice, text="Lunch", variable=radio_var,
                   value=2, font=general_font).place(relx=.50, rely=.50)
    CTkRadioButton(Explore_choice, text="Dinner", variable=radio_var,
                   value=3, font=general_font).place(relx=.50, rely=.60)

    def submit_button_click():
        v1, v2, v3 = veg.get(), nonveg.get(), radio_var.get()
        if not v1 and not v2:
            pass
        elif v3 not in [1, 2, 3]:
            pass
        Display_recipe = CTk()
        Display_recipe.geometry("700x550")
        Display_recipe.title("Cookbook")
        general_font = CTkFont(family="Sans-serif", size=15)
        display_font = CTkFont(family="Sans-serif", size=30)
        CTkLabel(
            Display_recipe, text="Displaying for selected options", font=display_font, underline=True).place(relx=0.25, rely=0.02)

        def show_clicked():
            mc.execute(
                f"SELECT INGREDIENTS,PROCESS,RECIPE_ID FROM RECIPE WHERE RECIPE_NAME = '{check.get(ANCHOR)}'")
            for i in mc:
                ingredients, process, recipe_id = i
            mc.execute(
                f"SELECT RATING FROM RESPONSE WHERE RECIPE_ID = '{recipe_id}'")
            avg_rating = []
            for i in mc:
                avg_rating.append(i[0])
            avg_rating = sum(avg_rating)/len(avg_rating)
            recipi_ingridients.configure(state='normal')
            recipi_process.configure(state="normal")
            recipi_ingridients.delete("0.0", END)
            recipi_process.delete("0.0", END)
            rating.configure(text=f"{avg_rating}/5")
            recipi_process.insert("0.0", process)
            recipi_ingridients.insert("0.0", ingredients)
            recipi_ingridients.configure(state='disabled')
            recipi_process.configure(state="disabled")

        def comment_rating():
            response = CTk()
            response.geometry("600x300")
            response.title("Cookbook")
            general_font = CTkFont(family="Sans-serif", size=15)
            display_font = CTkFont(family="Sans_serif", size=30)
            CTkLabel(
                response, text="Please enter rating and Comment", font=display_font, underline=True).place(relx=0.1, rely=0.02)

            def slider_event(value):
                CTkLabel(response, text=int(
                    value), font=general_font).place(relx=.50, rely=.15)

            def submit_clicked():
                comment = textbox.get("0.0", END)
                rating = int(rating_slider.get())
                recipe_name = check.get(ANCHOR)
                mc.execute(
                    f"SELECT RECIPE_ID FROM RECIPE WHERE RECIPE_NAME = '{recipe_name}'")
                for i in mc:
                    recipe_id = i[0]
                print(recipe_id)
                mc.execute(
                    f"INSERT INTO RESPONSE(RECIPE_ID,COMMENTS,RATING) VALUES({recipe_id},'{comment}',{rating})")
                db.commit()
                response.destroy()

            rating_slider = CTkSlider(
                response, from_=0, to=5, number_of_steps=5, command=slider_event)
            rating_slider.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
            CTkButton(
                response, text="Submit", corner_radius=20, command=submit_clicked).place(relx=.385, rely=.75)
            textbox = CTkTextbox(
                response, width=200, height=100, corner_radius=20)
            textbox.place(relx=.33, rely=.35)
            textbox.bind("<FocusIn>", lambda e: textbox.delete("0.0", "end"))
            textbox.insert("0.0", "Please add your comment/suggestion")
            textbox.get("0.0", "end")
            response.mainloop()

        show = CTkButton(
            Display_recipe, text="SHOW", corner_radius=20, command=show_clicked)
        show.place(relx=.05, rely=.85)

        CTkButton(Display_recipe, text="Add a rating and comment", corner_radius=20,
                  fg_color='#3b3b3b', font=general_font, command=comment_rating, width=10).place(relx=.635, rely=.15)
        rating = CTkLabel(Display_recipe, text=f"-/5", corner_radius=20, width=50,
                          fg_color='#3b3b3b', font=general_font)
        rating.place(relx=.55, rely=.15)
        recipi_ingridients = CTkTextbox(
            Display_recipe, width=275, height=170, corner_radius=20, font=general_font)
        recipi_ingridients.place(relx=.55, rely=.25)
        recipi_ingridients.insert("0.0", "Ingredients....")
        recipi_ingridients.configure(state="disabled")

        recipi_process = CTkTextbox(
            Display_recipe, width=275, height=170, corner_radius=20, font=general_font)
        recipi_process.place(relx=.55, rely=.60)
        recipi_process.insert("0.0", "Process....")
        recipi_process.configure(state="disabled")

        check = tk.Listbox(Display_recipe, bg='#3b3b3b', fg='white', height=15, font=(
            'Sans-serif', 15), bd=3)
        check.place(relx=.05, rely=.15)

        def add_check_list_filter(tag, type):
            if len(tag) == 2:
                mc.execute(
                    f"SELECT RECIPE_NAME FROM RECIPE WHERE (TAG = '{tag[0]}' OR TAG = '{tag[1]}') AND TYPE = '{type}'")
                result_list = []
                for i in mc:
                    result_list.append(i[0])
                for i in result_list:
                    check.insert(END, i)
            else:
                mc.execute(
                    f"SELECT RECIPE_NAME FROM RECIPE WHERE TAG ='{tag[0]}' AND TYPE = '{type}'")
                result_list = []
                for i in mc:
                    result_list.append(i[0])
                for i in result_list:
                    check.insert(END, i)

        if v1 and v2 and v3 == 1:
            add_check_list_filter(['V', 'N'], 'B')
        elif v1 and v2 and v3 == 2:
            add_check_list_filter(['V', 'N'], 'L')
        elif v1 and v2 and v3 == 3:
            add_check_list_filter(['V', 'N'], 'D')
        elif v1 and v3 == 1:
            add_check_list_filter(['V'], 'B')
        elif v1 and v3 == 2:
            add_check_list_filter(['V'], 'L')
        elif v1 and v3 == 3:
            add_check_list_filter(['V'], 'D')
        elif v2 and v3 == 1:
            add_check_list_filter(['N'], 'B')
        elif v2 and v3 == 2:
            add_check_list_filter(['N'], 'L')
        elif v2 and v3 == 3:
            add_check_list_filter(['N'], 'D')
        else:
            pass
        Explore_choice.destroy()
        Display_recipe.mainloop()
    CTkButton(Explore_choice, text="go", corner_radius=30,
              command=submit_button_click).place(relx=.40, rely=.70)
    Explore_choice.mainloop()


def add_button_clicked(user_id):
    Display_recipe_search = CTk()
    v = BooleanVar()
    nv = BooleanVar()
    rv = IntVar()

    def add_to_collection(recipe_name, tag, type, ingredients, process):
        mc.execute(
            f"INSERT INTO RECIPE(USER_ID,RECIPE_NAME,TAG,TYPE,INGREDIENTS,PROCESS) VALUES({user_id},'{recipe_name}','{tag}','{type}','{ingredients}','{process}' )")
        mc.execute(
            f"SELECT RECIPE_ID FROM RECIPE WHERE RECIPE_NAME = '{recipe_name}'")
        for i in mc:
            recipe_id = i[0]
        mc.execute(
            f"INSERT INTO RESPONSE(RECIPE_ID,COMMENTS,RATING) VALUES({recipe_id},'NOICE',3)")
        db.commit()
        Display_recipe_search.destroy()

    def gobutton_clicked():
        v1, v2, v3, ingredients, process, recipe_name = v.get(), nv.get(), rv.get(
        ), ingridients_name.get("0.0", END), procedure.get("0.0", END), recipi_name.get()
        if v1 and v3 == 1:
            add_to_collection(recipe_name, 'V', 'B', ingredients, process)
        elif v1 and v3 == 2:
            add_to_collection(recipe_name, 'V', 'L', ingredients, process)
        elif v1 and v3 == 3:
            add_to_collection(recipe_name, 'V', 'D', ingredients, process)
        elif v2 and v3 == 1:
            add_to_collection(recipe_name, 'N', 'B', ingredients, process)
        elif v2 and v3 == 2:
            add_to_collection(recipe_name, 'N', 'L', ingredients, process)
        elif v2 and v3 == 3:
            add_to_collection(recipe_name, 'N', 'D', ingredients, process)

        print(f"{v1}\n{v2}\n{v3}\n{ingredients}\n{process}\n{recipe_name} ")

    general_font = CTkFont(family="Sans-serif", size=15)
    display_font = CTkFont(family="Sans-serif", size=20)
    CTkLabel(
        Display_recipe_search, text="Add Recipie", font=display_font).place(relx=.45, rely=.05)
    recipi_name = CTkEntry(Display_recipe_search, placeholder_text="Enter recipie name",
                           font=general_font, corner_radius=30, width=300, height=40)
    recipi_name.place(relx=.31, rely=.125)
    CTkCheckBox(Display_recipe_search, text="Vegetarian", font=general_font,
                variable=v, onvalue=True, hover_color="green").place(relx=.335, rely=.25)
    CTkCheckBox(Display_recipe_search, text="Non-Vegetarian", font=general_font,
                variable=nv, onvalue=True, hover_color="red").place(relx=.335, rely=.30)
    CTkRadioButton(
        Display_recipe_search, text="Breakfast", variable=rv, value=1, font=general_font).place(relx=.575, rely=.25)
    CTkRadioButton(
        Display_recipe_search, text="Lunch", variable=rv, value=2, font=general_font).place(relx=.575, rely=.3)
    CTkRadioButton(
        Display_recipe_search, text="Dinner", variable=rv, value=3, font=general_font).place(relx=.575, rely=.35)
    ingridients_name = CTkTextbox(
        Display_recipe_search, width=300, height=200, corner_radius=20, font=general_font)
    ingridients_name.place(relx=.05, rely=.435)
    ingridients_name.insert(
        "0.0", "Ingredient-1 amount\nIngredient-2 amount\n....")
    ingridients_name.bind(
        "<FocusIn>", lambda e: ingridients_name.delete("0.0", "end"))
    procedure = CTkTextbox(
        Display_recipe_search, width=300, height=200, corner_radius=20, font=general_font)
    procedure.place(relx=.55, rely=.435)
    procedure.insert("0.0", "STEP 1\n.......\nSTEP 2\n.....")
    procedure.bind("<FocusIn>", lambda e: procedure.delete("0.0", "end"))
    CTkButton(
        Display_recipe_search, text="Add to collection", corner_radius=30, command=gobutton_clicked).place(relx=.40, rely=.925)
    Display_recipe_search.geometry("700x550")
    Display_recipe_search.title("Cookbook")
    Display_recipe_search.mainloop()


def display_recipe_search():
    Display_recipe_search = CTk()
    Display_recipe_search.geometry("700x550")
    Display_recipe_search.title("Cookbook")
    general_font = CTkFont(family="Sans-serif", size=15)
    display_font = CTkFont(family="Sans-serif", size=30)

    rating = CTkLabel(Display_recipe_search, text=f"-/5", corner_radius=20, width=50,
                      fg_color='#3b3b3b', font=general_font)
    rating.place(relx=.55, rely=.15)
    recipi_ingridients = CTkTextbox(
        Display_recipe_search, width=265, height=150, corner_radius=20, font=general_font)
    recipi_ingridients.place(relx=.55, rely=.25)
    recipi_ingridients.insert("0.0", "Ingredients....")
    recipi_ingridients.configure(state="disabled")

    recipi_process = CTkTextbox(
        Display_recipe_search, width=265, height=150, corner_radius=20, font=general_font)
    recipi_process.place(relx=.55, rely=.60)
    recipi_process.insert("0.0", "Process....")
    recipi_process.configure(state="disabled")

    check = tk.Listbox(Display_recipe_search, bg='#3b3b3b', fg='white', height=15, font=(
        'Sans-serif', 15), bd=3)
    check.place(relx=.05, rely=.15)
    recipe_list = []

    mc.execute(
        f"SELECT RECIPE_NAME FROM RECIPE WHERE RECIPE_NAME LIKE '%{str(search_bar.get()).upper()}%'")
    for i in mc:
        recipe_list.append(i[0])
    if len(recipe_list) == 0:
        suggestion.configure(
            text="No such recipe found, Click on add recipe to your recipe")
        return
    print(recipe_list)
    for i in recipe_list:
        check.insert(END, i)

    CTkLabel(
        Display_recipe_search, text="Displaying matched recipes", font=display_font, underline=True).place(relx=0.25, rely=0.02)

    def show_clicked():
        mc.execute(
            f"SELECT INGREDIENTS,PROCESS,RECIPE_ID FROM RECIPE WHERE RECIPE_NAME = '{check.get(ANCHOR)}'")
        for i in mc:
            ingredients, process, recipe_id = i
        mc.execute(
            f"SELECT RATING FROM RESPONSE WHERE RECIPE_ID = '{recipe_id}'")
        avg_rating = []
        for i in mc:
            avg_rating.append(i[0])
        avg_rating = sum(avg_rating)/len(avg_rating)
        recipi_ingridients.configure(state='normal')
        recipi_process.configure(state="normal")
        recipi_ingridients.delete("0.0", END)
        recipi_process.delete("0.0", END)
        rating.configure(text=f"{avg_rating}/5")
        recipi_process.insert("0.0", process)
        recipi_ingridients.insert("0.0", ingredients)
        recipi_ingridients.configure(state='disabled')
        recipi_process.configure(state="disabled")

    show = CTkButton(
        Display_recipe_search, text="SHOW", corner_radius=20, command=show_clicked)
    show.place(relx=.05, rely=.85)

    def comment_rating():
        response = CTk()
        response.geometry("600x300")
        response.title("Cookbook")
        general_font = CTkFont(family="Sans-serif", size=15)
        display_font = CTkFont(family="Sans_serif", size=30)
        CTkLabel(
            response, text="Please enter rating and Comment", font=display_font, underline=True).place(relx=0.1, rely=0.02)

        def slider_event(value):
            CTkLabel(response, text=int(
                value), font=general_font).place(relx=.50, rely=.15)

        def submit_clicked():
            comment = textbox.get("0.0", END)
            rating = int(rating_slider.get())
            recipe_name = check.get(ANCHOR)
            mc.execute(
                f"SELECT RECIPE_ID FROM RECIPE WHERE RECIPE_NAME = '{recipe_name}'")
            for i in mc:
                recipe_id = i[0]
            print(recipe_id)
            mc.execute(
                f"INSERT INTO RESPONSE(RECIPE_ID,COMMENTS,RATING) VALUES({recipe_id},'{comment}',{rating})")
            db.commit()
            response.destroy()

        rating_slider = CTkSlider(
            response, from_=0, to=5, number_of_steps=5, command=slider_event)
        rating_slider.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
        CTkButton(
            response, text="Submit", corner_radius=20, command=submit_clicked).place(relx=.385, rely=.75)
        textbox = CTkTextbox(
            response, width=200, height=100, corner_radius=20)
        textbox.place(relx=.33, rely=.35)
        textbox.bind("<FocusIn>", lambda e: textbox.delete("0.0", "end"))
        textbox.insert("0.0", "Please add your comment/suggestion")
        textbox.get("0.0", "end")
        response.mainloop()
    CTkButton(Display_recipe_search, text="Add a rating and comment", corner_radius=20,
              fg_color='#3b3b3b', font=general_font, command=comment_rating, width=10).place(relx=.635, rely=.15)

    Display_recipe_search.mainloop()


def explore(user_id):

    mc.execute(f"SELECT USER_NAME FROM USERS WHERE USER_ID = {user_id}")
    for i in mc:
        un = i[0]
    Explore = CTk()
    Explore.geometry("700x550")
    Explore.title("Cookbook")
    general_font = CTkFont(family="Sans-serif", size=15)
    display_font = CTkFont(family="Segoe Script", size=40)
    global search_bar
    search_bar = StringVar(value="Enter Recipe to search")
    sb = CTkEntry(Explore, font=general_font, corner_radius=30, height=35,
                  width=400, fg_color="transparent", textvariable=search_bar)
    sb.place(relx=.225, rely=.45)
    s = CTkTextbox(Explore)
    sb.bind("<FocusIn>", lambda e: search_bar.set(""))
    CTkLabel(Explore, text="Name Cookbook",
             font=display_font).place(relx=.25, rely=.30)
    CTkButton(master=Explore, text="Explore", font=general_font,
              corner_radius=30, command=explore_button_click).place(relx=.27, rely=.575)
    CTkButton(master=Explore, text="Add Recipie",
              font=general_font, corner_radius=30, command=lambda: add_button_clicked(user_id)).place(relx=.545, rely=.575)
    my_image = CTkImage(dark_image=Image.open(
        "search-icon-png-29.png"), size=(15, 15))

    CTkButton(Explore, image=my_image, text="", fg_color="transparent",
              width=20, height=5, corner_radius=50, command=display_recipe_search).place(relx=.745, rely=.46)
    date = dt.datetime.now()
    CTkLabel(
        Explore, text=f"Hello {un} It is {date:%A, %B %d, %Y}", font=general_font).place(relx=.55, rely=.05)
    global suggestion
    suggestion = CTkLabel(Explore, text="",
                          font=general_font)
    suggestion.place(relx=.25, rely=.20)
    Explore.mainloop()


# Login window
LOGIN = CTk()
LOGIN.geometry("700x550")
LOGIN.title("CookBook")
welcome_font = CTkFont(family="Sans-serif", size=50)
general_font = CTkFont(family="Sans-serif", size=15)
label = CTkLabel(
    LOGIN, text="", font=general_font, underline=True)
label.place(relx=0.35, rely=0.05)

CTkLabel(
    LOGIN, text="Welcome", font=welcome_font, underline=True).place(relx=0.35, rely=0.1)
CTkLabel(LOGIN, text="Please choose an option to continue",
         font=general_font, underline=True).place(relx=.33, rely=.25)

CTkSegmentedButton(LOGIN, values=["Login", "Register"], command=segemented_button_callback,
                   corner_radius=20, selected_hover_color="#70a7ff").place(relx=.36, rely=.35, width=250)
login_register_choose_var = StringVar(value="Login")

LOGIN.mainloop()
mc.close()
db.disconnect()