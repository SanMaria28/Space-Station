-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: localhost    Database: space_station
-- ------------------------------------------------------
-- Server version	8.0.44

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
-- Table structure for table `crew`
--

DROP TABLE IF EXISTS `crew`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `crew` (
  `crew_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(15) NOT NULL,
  `role` varchar(20) DEFAULT NULL,
  `nationality` varchar(15) DEFAULT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`crew_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `crew`
--

LOCK TABLES `crew` WRITE;
/*!40000 ALTER TABLE `crew` DISABLE KEYS */;
INSERT INTO `crew` VALUES (1,'Arjun','Commander','India','pass101'),(2,'Lina','Pilot','USA','pass102'),(3,'Kenji','Engineer','Japan','pass103'),(4,'Maria','Scientist','Spain','pass104'),(5,'Omar','Medic','UAE','pass105'),(6,'Sofia','Navigator','Brazil','pass106'),(7,'Raj','Engineer','India','pass107'),(8,'Emma','Scientist','UK','pass108'),(9,'Noah','Tech','Canada','pass109'),(10,'Chen','Researcher','China','pass110'),(11,'Leo','Pilot','France','pass111'),(12,'Ava','Biologist','Austra','pass112'),(13,'Ivan','Engineer','Russia','pass113'),(14,'Maya','Doctor','India','pass114'),(15,'Lucas','Navigator','Germany','pass115');
/*!40000 ALTER TABLE `crew` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `experiment`
--

DROP TABLE IF EXISTS `experiment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `experiment` (
  `experiment_id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(15) DEFAULT NULL,
  `field` varchar(20) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `mission_id` int DEFAULT NULL,
  `crew_id` int DEFAULT NULL,
  PRIMARY KEY (`experiment_id`),
  KEY `mission_id` (`mission_id`),
  KEY `crew_id` (`crew_id`),
  CONSTRAINT `experiment_ibfk_1` FOREIGN KEY (`mission_id`) REFERENCES `mission` (`mission_id`),
  CONSTRAINT `experiment_ibfk_2` FOREIGN KEY (`crew_id`) REFERENCES `crew` (`crew_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experiment`
--

LOCK TABLES `experiment` WRITE;
/*!40000 ALTER TABLE `experiment` DISABLE KEYS */;
INSERT INTO `experiment` VALUES (1,'ZeroPlants','Biology','Active',1,2),(2,'MarsSoil','Geology','Active',1,3),(3,'MoonWater','Chemistry','Done',2,5),(4,'MoonRad','Physics','Active',2,6),(5,'AstMetal','Chemistry','Active',3,8),(6,'MineSim','Engineering','Pending',3,9),(7,'SolarTest','Physics','Active',4,11),(8,'DeepSignal','Astronomy','Active',5,14);
/*!40000 ALTER TABLE `experiment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mission`
--

DROP TABLE IF EXISTS `mission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mission` (
  `mission_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `purpose` varchar(20) DEFAULT NULL,
  `launch_date` date DEFAULT NULL,
  `crew_id` int DEFAULT NULL,
  PRIMARY KEY (`mission_id`),
  KEY `crew_id` (`crew_id`),
  CONSTRAINT `mission_ibfk_1` FOREIGN KEY (`crew_id`) REFERENCES `crew` (`crew_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mission`
--

LOCK TABLES `mission` WRITE;
/*!40000 ALTER TABLE `mission` DISABLE KEYS */;
INSERT INTO `mission` VALUES (1,'MarsOne','PlanetStudy','2026-03-10',1),(2,'MoonBase','HabitatStudy','2026-04-15',4),(3,'AstScan','MineralSurvey','2026-05-20',7),(4,'SolarX','SunObserve','2026-06-05',10),(5,'DeepSky','GalaxyMap','2026-07-18',13);
/*!40000 ALTER TABLE `mission` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-02-01 20:10:19
