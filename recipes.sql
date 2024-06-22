-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: recipes
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `recipe`
--

DROP TABLE IF EXISTS `recipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recipe` (
  `RECIPE_ID` int NOT NULL AUTO_INCREMENT,
  `RECIPE_NAME` varchar(255) DEFAULT NULL,
  `USER_ID` int DEFAULT NULL,
  `TAG` varchar(1) DEFAULT NULL,
  `TYPE` varchar(1) DEFAULT NULL,
  `INGREDIENTS` mediumtext,
  `PROCESS` mediumtext,
  PRIMARY KEY (`RECIPE_ID`),
  KEY `USER_ID` (`USER_ID`),
  CONSTRAINT `recipe_ibfk_1` FOREIGN KEY (`USER_ID`) REFERENCES `users` (`USER_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recipe`
--

LOCK TABLES `recipe` WRITE;
/*!40000 ALTER TABLE `recipe` DISABLE KEYS */;
INSERT INTO `recipe` VALUES (1,'COOKIE DOUGH',0,'V','B','1 cup all-purpose flour\n    ¾ cup packed brown sugar\n    ½ cup butter\n    1 teaspoon vanilla extract\n    ½ teaspoon salt\n    2 tablespoons milk\n    ½ cup milk chocolate chips\n    ½ cup white chocolate chips','STEP 1\n    To heat-treat your flour so it is safe to use: Place flour in a microwave-safe dish and cook for 1 minute and 15 seconds, \n    stirring it every 15 seconds. Set aside.\n\n    STEP 2\n    Beat sugar and butter with an electric mixer in a large bowl until creamy. Beat in vanilla extract and salt. \n    Add heat-treated flour; mix until a crumbly dough forms. Stir in milk until dough is just combined\n    fold in milk chocolate chips and white chocolate chips.\n    '),(2,'MACRONI',0,'V','B','1 (8 ounce) box elbow macaroni\n    ¼ cup butter\n    ¼ cup all-purpose flour\n    ½ teaspoon salt\n    ground black pepper to taste\n    2 cups milk\n    2 cups shredded Cheddar cheese','STEP 1\n    Bring a large pot of lightly salted water to a boil. Cook elbow macaroni in the boiling water, \n    stirring occasionally until cooked through but firm to the bite, 8 minutes.\n\n    STEP 2\n    At the same time, melt butter in a saucepan over medium heat. Add flour, salt, and pepper and stir until smooth, about 5 minutes.\n    Pour in milk slowly, while stirring continuously. Continue to cook and stir until mixture is smooth and bubbling, about 5 minutes, \n    making sure the milk doesn\'t burn.\n\n    STEP 3\n    Add Cheddar cheese and stir until melted, 2 to 4 minutes.\n\n    STEP 4\n    Drain macaroni and fold into cheese sauce until coated.\n    '),(3,'CHITRANA',0,'V','D','3 cup leftover rice\n    ½ lemon\n    2 tbsp coriander (finely chopped)\n    peanuts','STEP 1\n    firstly, take 3 cup of leftover rice and add 2 tbsp prepared lemon rice gojju and peanuts.\n\n    STEP 2\n    also add ½ lemon juice and 2 tbsp coriander. mix well.\n\n    STEP 3\n    finally, enjoy lemon rice with coconut chutney.\n    '),(4,'CURD RICE',0,'V','L','1/2 cup boiled rice\n    1 cup thick curd\n    1/2 + 1/2 cup milk boiled and cooled\n    1 tbsp butter\n    1 tbsp coriander leaves finely chopped\n    1 tsp ginger finely chopped\n    1 no green chilli finely chopped','STEP 1\n    Take boiled rice and mash it\n    Now add 1/2 cup milk(boiled, cooled).\n    Add 1 cup thick curd.\n    Add 1 tbsp butter along with required salt.\n\n    STEP 2\n    Mix this well first. It should be goey not too thick.\n    Add 1/4 cup more curd if needed.\n    Add 1 tbsp coriander leaves, 1 tsp finely chopped curry leaves along with 1 green chilli finely chopped and 1 tsp ginger finely chopped.\n    Set aside. \n\n    STEP 3\n    For tadka : Heat 2 tsp oil – add 1 tsp mustard seeds let it crackle. Once it crackles add 1/2 tsp urad dal.\n    Add a pinch of hing.\n    Add 2 small red chillies along with few curry leaves. Let it splutter. Fry until dals turn golden brown.\n    Add tadka to curd rice.\n    Mix well. Creamy yummy curd rice is ready.\n    '),(5,'RAGI MUDDE',0,'V','L','1/4 cup rice\n    1 cup ragi\n    1/2 cup water\n    salt','Heat water in a heavy bottom pan. Add salt and oil and bring it to a boil.\n    Add in rice and simmer for couple of mins.\n    Now tip all the ragi flour into the water and don\'t stir it, \n    just cover the pan with a lid and simmer on low heat for 5 to 6 mins.\n    Remove it off the heat, use back of the spoon to stir it well into the water.\n    Now put it back on heat and cook for couple more mins.\n    Take it off the heat and cover it with a lid. Set aside for 5 mins.\n    Now remove this to a bowl.\n    Cool it down a bit. Now shape this into ball and serve with any spicy curries.\n    '),(6,'MEEN POLLICHATHU',0,'N','D','Fish 2 whole(300 grams)\n    Onion 3 big\n    Tomato 2 medium\n    Garlic 10-12\n    Green chilli 2\n    Ginger garlic paste 1.5 tsp\n    Red chilli powder 2 tsp\n    Coriander powder 1 tsp\n    Turmeric powder 1/2 tsp\n    Salt as required\n    Garam masala 1/4 tsp\n    Curry leaves handful\n    Oil 2.5 tbsp\n    Coriander leaves 3 tbsp finely chopped','Mix all the masala given under marination to form a thick paste and coat the fish\n    In the tawa add little oil and shallow fry the fish on both sides till golden.\n    Heat remaining oil and add finely chopped garlic, green chillies, and curry leaves.\n    Then add finely chopped onions and saute till golden.\n    Next, add ginger garlic paste and saute till the raw smell goes.\n    Then add tomatoes and saute till mushy.\n    Add salt, red chilli powder, coriander powder, turmeric powder, and garam masala to it.\n    Add little water to it and cook till masala is nicely coated and oil oozing out.\n    Garnish with coriander leaves and switch off the flame.\n    Delicious onion tomato masala is ready.\n    Take a banana leaf and show it in flame for few seconds to soften it so it doesn\'t tear while folding.\n    Take a wilted banana leaf and add the masala to it.\n    Place the fish on top of it.\n    Cover it with masala again.\n    Then wrap the banana leaves and fold them. Seal it with a toothpick.\n    Heat a dosa pan or flat pan and place the wrapped banana leaf\n    Close it with a lid and cook on low flame for 4-5 minutes.\n    Flip the fish and cook again for 4-5 minutes.\n    Remove from the flame and serve it hot.\n    Meen pollichathu is ready.\n    '),(7,'AVALAKKI UPPITU',0,'V','B','2 cups avalakki/ poha\n    Salt to taste\n    2 tbsp lemon juice\n    2 tbsp oil\n    1 tsp mustard seeds\n    1 tbsp chana dal/ split desi chickpeas\n    1 tbsp urad dal/ split matpe beans\n    2-4 green chilis (minced)\n    A few curry leaves\n    2 medium yellow onion (finely diced)\n    1/2 tsp turmeric\n    1/2 cup peas\n    A handful of finely chopped cilantro','Add 2 cups of avalakki/ poha to a bowl. Rinse with water and drain. Repeat twice to wash the avalakki.\n    Then, add fresh water. Add enough water to completely cover the avalakki/poha. Let it soak for 5 minutes.\n    After 5 minutes, drain the water in a strainer/colander and transfer the avalakki to a dry container. Let dry for 2-3 minutes.\n    Then, add 2 tbsp lemon juice and salt to taste. Mix well. Keep aside.\n    Heat 2 tbsp oil in a sauté pan at a medium flame.\n    Add 1 tsp mustard seeds to the oil.\n    Once the mustard seeds crackle, add 1 tbsp chana dal and 1 tbsp urad dal. Sauté for a few minutes.\n    The dal should change color slightly and become golden.\n    Add 2-4 green chilis (minced), a few curry leaves, and 2 medium yellow onions (finely diced). Sauté till translucent.\n    Add 1/2 tsp turmeric. Sauté till the raw smell of turmeric disappears.\n    Add in 1/2 cup of green peas. Reduce the flame (to prevent the dal from burning), and cook for a few minutes.\n    Once the peas are cooked, take off flame. Mix in the avalakki/ poha.\n    Add more salt and lemon if required. Garnish with a handful of finely chopped coriander.\n    ');
/*!40000 ALTER TABLE `recipe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `response`
--

DROP TABLE IF EXISTS `response`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `response` (
  `RECIPE_ID` int DEFAULT NULL,
  `COMMENTS` mediumtext,
  `RATING` int DEFAULT NULL,
  KEY `RECIPE_ID` (`RECIPE_ID`),
  CONSTRAINT `response_ibfk_1` FOREIGN KEY (`RECIPE_ID`) REFERENCES `recipe` (`RECIPE_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `response`
--

LOCK TABLES `response` WRITE;
/*!40000 ALTER TABLE `response` DISABLE KEYS */;
INSERT INTO `response` VALUES (1,'YUMMM',5),(1,'NOICE',4),(2,'NOICE',5),(2,'TASTYYYY',4),(3,'SUPPERB',4),(3,'YUMMMM',3),(4,'BESSSTT',3),(4,'TASTYYYY',4),(5,'NOICE',3),(5,'SUPPERB',4),(6,'DELICIOUSSS',3),(6,'YUMMMMM',4),(7,'BESSTT',3),(7,'SUPPERB',4);
/*!40000 ALTER TABLE `response` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `USER_ID` int NOT NULL,
  `USER_NAME` varchar(25) DEFAULT NULL,
  `PASSWORD` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`USER_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (0,'ADMIN','1234'),(26,'ZABI','bruh');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-22 12:48:14
