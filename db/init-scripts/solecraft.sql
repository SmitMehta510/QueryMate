-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: solecraft
-- ------------------------------------------------------
-- Server version	8.0.36-0ubuntu0.22.04.1

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
-- Table structure for table `discounts`
--
USE solecraft;
DROP TABLE IF EXISTS `discounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `discounts` (
  `discount_id` int NOT NULL AUTO_INCREMENT,
  `shoe_id` int NOT NULL,
  `pct_discount` decimal(5,2) DEFAULT NULL,
  PRIMARY KEY (`discount_id`),
  KEY `shoe_id` (`shoe_id`),
  CONSTRAINT `discounts_ibfk_1` FOREIGN KEY (`shoe_id`) REFERENCES `shoes` (`shoe_id`),
  CONSTRAINT `discounts_chk_1` CHECK ((`pct_discount` between 0 and 100))
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discounts`
--

LOCK TABLES `discounts` WRITE;
/*!40000 ALTER TABLE `discounts` DISABLE KEYS */;
INSERT INTO `discounts` VALUES (1,1,10.00),(2,2,15.00),(3,3,20.00),(4,4,5.00),(5,5,25.00),(6,6,10.00),(7,7,30.00),(8,8,35.00),(9,9,40.00),(10,10,45.00);
/*!40000 ALTER TABLE `discounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shoes`
--

DROP TABLE IF EXISTS `shoes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shoes` (
  `shoe_id` int NOT NULL AUTO_INCREMENT,
  `brand` enum('Nike','Adidas','Puma','Reebok') NOT NULL,
  `color` enum('Red','Blue','Black','White') NOT NULL,
  `size` enum('6','7','8','9','10') NOT NULL,
  `price` decimal(5,2) DEFAULT NULL,
  `stock_quantity` int NOT NULL,
  PRIMARY KEY (`shoe_id`),
  UNIQUE KEY `brand_color_size` (`brand`,`color`,`size`),
  CONSTRAINT `shoes_chk_1` CHECK ((`price` between 20.00 and 100.00))
) ENGINE=InnoDB AUTO_INCREMENT=879 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoes`
--

LOCK TABLES `shoes` WRITE;
/*!40000 ALTER TABLE `shoes` DISABLE KEYS */;
INSERT INTO `shoes` VALUES (1,'Reebok','Red','6',51.90,43),(2,'Puma','White','8',85.69,55),(3,'Nike','Black','6',45.26,52),(4,'Adidas','Black','6',40.28,21),(5,'Reebok','Red','9',36.79,100),(6,'Adidas','Black','8',98.16,71),(7,'Adidas','Red','9',30.10,42),(8,'Adidas','White','8',85.29,53),(9,'Reebok','Blue','6',23.27,17),(10,'Adidas','Red','10',92.09,93),(11,'Reebok','Black','9',46.25,69),(12,'Adidas','Blue','7',95.01,99),(13,'Nike','Black','10',40.69,81),(14,'Nike','Blue','9',67.63,64),(15,'Nike','Red','7',50.29,74),(17,'Puma','White','10',86.54,37),(18,'Nike','Red','6',71.75,12),(19,'Nike','White','6',95.61,31),(20,'Adidas','White','9',92.73,36),(22,'Puma','Blue','10',28.60,16),(23,'Nike','White','7',70.20,48),(24,'Nike','White','10',48.62,41),(25,'Puma','Blue','8',41.91,18),(26,'Puma','White','9',21.40,81),(27,'Reebok','Red','8',45.13,23),(30,'Reebok','Blue','8',28.59,81),(31,'Puma','Black','8',47.05,38),(34,'Nike','Black','9',65.97,96),(36,'Nike','White','9',59.30,20),(37,'Nike','Red','8',84.05,69),(38,'Reebok','Blue','7',68.54,97),(39,'Reebok','White','6',45.78,48),(40,'Nike','Blue','10',90.90,89),(42,'Adidas','White','7',86.50,22),(43,'Nike','Black','8',76.06,96),(45,'Reebok','White','9',98.15,71),(46,'Adidas','Red','7',52.65,97),(47,'Puma','Red','8',66.18,30),(52,'Adidas','Red','8',91.57,34),(53,'Puma','Blue','6',39.60,96),(54,'Nike','Blue','8',93.77,86),(55,'Adidas','Black','10',73.76,64),(59,'Puma','Red','9',44.95,46),(60,'Nike','Red','10',52.18,63),(61,'Puma','White','7',70.61,44),(64,'Reebok','Red','10',56.29,81),(71,'Puma','Red','6',46.91,47),(74,'Reebok','Black','10',58.88,80),(80,'Reebok','Blue','10',88.98,83),(81,'Adidas','White','10',90.64,78),(82,'Nike','Blue','7',91.99,39),(83,'Reebok','Black','8',84.70,41),(85,'Reebok','Red','7',78.41,59),(86,'Puma','White','6',68.49,83),(97,'Adidas','Red','6',46.87,67),(876,'Reebok','White','10',100.00,24),(877,'Puma','Blue','9',85.69,99),(878,'Nike','Blue','6',99.00,0);
/*!40000 ALTER TABLE `shoes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-15 23:20:41
