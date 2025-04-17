-- MySQL dump 10.13  Distrib 8.4.4, for Linux (x86_64)
--
-- Host: localhost    Database: hotel_booking_app
-- ------------------------------------------------------
-- Server version	8.4.4

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
-- Table structure for table `additionalservices`
--

DROP TABLE IF EXISTS `additionalservices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `additionalservices` (
  `id` int NOT NULL AUTO_INCREMENT,
  `service_name` varchar(255) NOT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `create_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  CONSTRAINT `additionalservices_chk_1` CHECK ((`price` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `additionalservices`
--

LOCK TABLES `additionalservices` WRITE;
/*!40000 ALTER TABLE `additionalservices` DISABLE KEYS */;
INSERT INTO `additionalservices` VALUES (1,'City Tour',20.00,'2025-04-16 20:42:10','2025-04-16 20:42:32'),(2,'Airport Pickup',25.00,'2025-04-16 20:42:10','2025-04-16 20:42:32'),(3,'Driver',20.00,'2025-04-16 20:42:10','2025-04-16 20:42:32'),(4,'Car',30.00,'2025-04-16 20:42:10','2025-04-16 20:42:32'),(5,'Hotel Pickup',25.00,'2025-04-16 20:42:10','2025-04-16 20:42:32');
/*!40000 ALTER TABLE `additionalservices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `busy_room`
--

DROP TABLE IF EXISTS `busy_room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `busy_room` (
  `id` int NOT NULL AUTO_INCREMENT,
  `hotel_id` int DEFAULT NULL,
  `room_type_id` int DEFAULT NULL,
  `busy_from` date DEFAULT NULL,
  `busy_to` date DEFAULT NULL,
  `state` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT 'Free',
  `room_number` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `invoice_id` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `hotel_id` (`hotel_id`),
  KEY `room_type_id` (`room_type_id`),
  CONSTRAINT `busy_room_ibfk_1` FOREIGN KEY (`hotel_id`) REFERENCES `hotels` (`id`) ON DELETE SET NULL,
  CONSTRAINT `busy_room_ibfk_2` FOREIGN KEY (`room_type_id`) REFERENCES `roomtypes` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=251 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `busy_room`
--

LOCK TABLES `busy_room` WRITE;
/*!40000 ALTER TABLE `busy_room` DISABLE KEYS */;
INSERT INTO `busy_room` VALUES (1,1,51,'2025-04-19','2025-04-22','Busy','1','1'),(2,1,51,NULL,NULL,'Free','2',NULL),(3,1,51,NULL,NULL,'Free','3',NULL),(4,1,51,NULL,NULL,'Free','4',NULL),(5,1,51,NULL,NULL,'Free','5',NULL),(6,1,52,'2025-04-20','2025-04-25','Busy','1','2'),(7,1,52,NULL,NULL,'Free','2',NULL),(8,1,52,NULL,NULL,'Free','3',NULL),(9,1,52,NULL,NULL,'Free','4',NULL),(10,1,52,NULL,NULL,'Free','5',NULL),(11,1,53,NULL,NULL,'Free','1',NULL),(12,1,53,NULL,NULL,'Free','2',NULL),(13,1,53,NULL,NULL,'Free','3',NULL),(14,1,53,NULL,NULL,'Free','4',NULL),(15,1,53,NULL,NULL,'Free','5',NULL),(16,1,54,NULL,NULL,'Free','1',NULL),(17,1,54,NULL,NULL,'Free','2',NULL),(18,1,54,NULL,NULL,'Free','3',NULL),(19,1,54,NULL,NULL,'Free','4',NULL),(20,1,54,NULL,NULL,'Free','5',NULL),(21,1,55,NULL,NULL,'Free','1',NULL),(22,1,55,NULL,NULL,'Free','2',NULL),(23,1,55,NULL,NULL,'Free','3',NULL),(24,1,55,NULL,NULL,'Free','4',NULL),(25,1,55,NULL,NULL,'Free','5',NULL),(26,2,56,NULL,NULL,'Free','1',NULL),(27,2,56,NULL,NULL,'Free','2',NULL),(28,2,56,NULL,NULL,'Free','3',NULL),(29,2,56,NULL,NULL,'Free','4',NULL),(30,2,56,NULL,NULL,'Free','5',NULL),(31,2,57,NULL,NULL,'Free','1',NULL),(32,2,57,NULL,NULL,'Free','2',NULL),(33,2,57,NULL,NULL,'Free','3',NULL),(34,2,57,NULL,NULL,'Free','4',NULL),(35,2,57,NULL,NULL,'Free','5',NULL),(36,2,58,NULL,NULL,'Free','1',NULL),(37,2,58,NULL,NULL,'Free','2',NULL),(38,2,58,NULL,NULL,'Free','3',NULL),(39,2,58,NULL,NULL,'Free','4',NULL),(40,2,58,NULL,NULL,'Free','5',NULL),(41,2,59,NULL,NULL,'Free','1',NULL),(42,2,59,NULL,NULL,'Free','2',NULL),(43,2,59,NULL,NULL,'Free','3',NULL),(44,2,59,NULL,NULL,'Free','4',NULL),(45,2,59,NULL,NULL,'Free','5',NULL),(46,2,60,NULL,NULL,'Free','1',NULL),(47,2,60,NULL,NULL,'Free','2',NULL),(48,2,60,NULL,NULL,'Free','3',NULL),(49,2,60,NULL,NULL,'Free','4',NULL),(50,2,60,NULL,NULL,'Free','5',NULL),(51,3,61,NULL,NULL,'Free','1',NULL),(52,3,61,NULL,NULL,'Free','2',NULL),(53,3,61,NULL,NULL,'Free','3',NULL),(54,3,61,NULL,NULL,'Free','4',NULL),(55,3,61,NULL,NULL,'Free','5',NULL),(56,3,62,NULL,NULL,'Free','1',NULL),(57,3,62,NULL,NULL,'Free','2',NULL),(58,3,62,NULL,NULL,'Free','3',NULL),(59,3,62,NULL,NULL,'Free','4',NULL),(60,3,62,NULL,NULL,'Free','5',NULL),(61,3,63,NULL,NULL,'Free','1',NULL),(62,3,63,NULL,NULL,'Free','2',NULL),(63,3,63,NULL,NULL,'Free','3',NULL),(64,3,63,NULL,NULL,'Free','4',NULL),(65,3,63,NULL,NULL,'Free','5',NULL),(66,3,64,NULL,NULL,'Free','1',NULL),(67,3,64,NULL,NULL,'Free','2',NULL),(68,3,64,NULL,NULL,'Free','3',NULL),(69,3,64,NULL,NULL,'Free','4',NULL),(70,3,64,NULL,NULL,'Free','5',NULL),(71,3,65,NULL,NULL,'Free','1',NULL),(72,3,65,NULL,NULL,'Free','2',NULL),(73,3,65,NULL,NULL,'Free','3',NULL),(74,3,65,NULL,NULL,'Free','4',NULL),(75,3,65,NULL,NULL,'Free','5',NULL),(76,4,66,NULL,NULL,'Free','1',NULL),(77,4,66,NULL,NULL,'Free','2',NULL),(78,4,66,NULL,NULL,'Free','3',NULL),(79,4,66,NULL,NULL,'Free','4',NULL),(80,4,66,NULL,NULL,'Free','5',NULL),(81,4,67,NULL,NULL,'Free','1',NULL),(82,4,67,NULL,NULL,'Free','2',NULL),(83,4,67,NULL,NULL,'Free','3',NULL),(84,4,67,NULL,NULL,'Free','4',NULL),(85,4,67,NULL,NULL,'Free','5',NULL),(86,4,68,NULL,NULL,'Free','1',NULL),(87,4,68,NULL,NULL,'Free','2',NULL),(88,4,68,NULL,NULL,'Free','3',NULL),(89,4,68,NULL,NULL,'Free','4',NULL),(90,4,68,NULL,NULL,'Free','5',NULL),(91,4,69,NULL,NULL,'Free','1',NULL),(92,4,69,NULL,NULL,'Free','2',NULL),(93,4,69,NULL,NULL,'Free','3',NULL),(94,4,69,NULL,NULL,'Free','4',NULL),(95,4,69,NULL,NULL,'Free','5',NULL),(96,4,70,NULL,NULL,'Free','1',NULL),(97,4,70,NULL,NULL,'Free','2',NULL),(98,4,70,NULL,NULL,'Free','3',NULL),(99,4,70,NULL,NULL,'Free','4',NULL),(100,4,70,NULL,NULL,'Free','5',NULL),(101,5,71,NULL,NULL,'Free','1',NULL),(102,5,71,NULL,NULL,'Free','2',NULL),(103,5,71,NULL,NULL,'Free','3',NULL),(104,5,71,NULL,NULL,'Free','4',NULL),(105,5,71,NULL,NULL,'Free','5',NULL),(106,5,72,NULL,NULL,'Free','1',NULL),(107,5,72,NULL,NULL,'Free','2',NULL),(108,5,72,NULL,NULL,'Free','3',NULL),(109,5,72,NULL,NULL,'Free','4',NULL),(110,5,72,NULL,NULL,'Free','5',NULL),(111,5,73,NULL,NULL,'Free','1',NULL),(112,5,73,NULL,NULL,'Free','2',NULL),(113,5,73,NULL,NULL,'Free','3',NULL),(114,5,73,NULL,NULL,'Free','4',NULL),(115,5,73,NULL,NULL,'Free','5',NULL),(116,5,74,NULL,NULL,'Free','1',NULL),(117,5,74,NULL,NULL,'Free','2',NULL),(118,5,74,NULL,NULL,'Free','3',NULL),(119,5,74,NULL,NULL,'Free','4',NULL),(120,5,74,NULL,NULL,'Free','5',NULL),(121,5,75,NULL,NULL,'Free','1',NULL),(122,5,75,NULL,NULL,'Free','2',NULL),(123,5,75,NULL,NULL,'Free','3',NULL),(124,5,75,NULL,NULL,'Free','4',NULL),(125,5,75,NULL,NULL,'Free','5',NULL),(126,6,76,NULL,NULL,'Free','1',NULL),(127,6,76,NULL,NULL,'Free','2',NULL),(128,6,76,NULL,NULL,'Free','3',NULL),(129,6,76,NULL,NULL,'Free','4',NULL),(130,6,76,NULL,NULL,'Free','5',NULL),(131,6,77,NULL,NULL,'Free','1',NULL),(132,6,77,NULL,NULL,'Free','2',NULL),(133,6,77,NULL,NULL,'Free','3',NULL),(134,6,77,NULL,NULL,'Free','4',NULL),(135,6,77,NULL,NULL,'Free','5',NULL),(136,6,78,NULL,NULL,'Free','1',NULL),(137,6,78,NULL,NULL,'Free','2',NULL),(138,6,78,NULL,NULL,'Free','3',NULL),(139,6,78,NULL,NULL,'Free','4',NULL),(140,6,78,NULL,NULL,'Free','5',NULL),(141,6,79,NULL,NULL,'Free','1',NULL),(142,6,79,NULL,NULL,'Free','2',NULL),(143,6,79,NULL,NULL,'Free','3',NULL),(144,6,79,NULL,NULL,'Free','4',NULL),(145,6,79,NULL,NULL,'Free','5',NULL),(146,6,80,NULL,NULL,'Free','1',NULL),(147,6,80,NULL,NULL,'Free','2',NULL),(148,6,80,NULL,NULL,'Free','3',NULL),(149,6,80,NULL,NULL,'Free','4',NULL),(150,6,80,NULL,NULL,'Free','5',NULL),(151,7,81,NULL,NULL,'Free','1',NULL),(152,7,81,NULL,NULL,'Free','2',NULL),(153,7,81,NULL,NULL,'Free','3',NULL),(154,7,81,NULL,NULL,'Free','4',NULL),(155,7,81,NULL,NULL,'Free','5',NULL),(156,7,82,NULL,NULL,'Free','1',NULL),(157,7,82,NULL,NULL,'Free','2',NULL),(158,7,82,NULL,NULL,'Free','3',NULL),(159,7,82,NULL,NULL,'Free','4',NULL),(160,7,82,NULL,NULL,'Free','5',NULL),(161,7,83,NULL,NULL,'Free','1',NULL),(162,7,83,NULL,NULL,'Free','2',NULL),(163,7,83,NULL,NULL,'Free','3',NULL),(164,7,83,NULL,NULL,'Free','4',NULL),(165,7,83,NULL,NULL,'Free','5',NULL),(166,7,84,NULL,NULL,'Free','1',NULL),(167,7,84,NULL,NULL,'Free','2',NULL),(168,7,84,NULL,NULL,'Free','3',NULL),(169,7,84,NULL,NULL,'Free','4',NULL),(170,7,84,NULL,NULL,'Free','5',NULL),(171,7,85,NULL,NULL,'Free','1',NULL),(172,7,85,NULL,NULL,'Free','2',NULL),(173,7,85,NULL,NULL,'Free','3',NULL),(174,7,85,NULL,NULL,'Free','4',NULL),(175,7,85,NULL,NULL,'Free','5',NULL),(176,8,86,NULL,NULL,'Free','1',NULL),(177,8,86,NULL,NULL,'Free','2',NULL),(178,8,86,NULL,NULL,'Free','3',NULL),(179,8,86,NULL,NULL,'Free','4',NULL),(180,8,86,NULL,NULL,'Free','5',NULL),(181,8,87,NULL,NULL,'Free','1',NULL),(182,8,87,NULL,NULL,'Free','2',NULL),(183,8,87,NULL,NULL,'Free','3',NULL),(184,8,87,NULL,NULL,'Free','4',NULL),(185,8,87,NULL,NULL,'Free','5',NULL),(186,8,88,NULL,NULL,'Free','1',NULL),(187,8,88,NULL,NULL,'Free','2',NULL),(188,8,88,NULL,NULL,'Free','3',NULL),(189,8,88,NULL,NULL,'Free','4',NULL),(190,8,88,NULL,NULL,'Free','5',NULL),(191,8,89,NULL,NULL,'Free','1',NULL),(192,8,89,NULL,NULL,'Free','2',NULL),(193,8,89,NULL,NULL,'Free','3',NULL),(194,8,89,NULL,NULL,'Free','4',NULL),(195,8,89,NULL,NULL,'Free','5',NULL),(196,8,90,NULL,NULL,'Free','1',NULL),(197,8,90,NULL,NULL,'Free','2',NULL),(198,8,90,NULL,NULL,'Free','3',NULL),(199,8,90,NULL,NULL,'Free','4',NULL),(200,8,90,NULL,NULL,'Free','5',NULL),(201,9,91,NULL,NULL,'Free','1',NULL),(202,9,91,NULL,NULL,'Free','2',NULL),(203,9,91,NULL,NULL,'Free','3',NULL),(204,9,91,NULL,NULL,'Free','4',NULL),(205,9,91,NULL,NULL,'Free','5',NULL),(206,9,92,NULL,NULL,'Free','1',NULL),(207,9,92,NULL,NULL,'Free','2',NULL),(208,9,92,NULL,NULL,'Free','3',NULL),(209,9,92,NULL,NULL,'Free','4',NULL),(210,9,92,NULL,NULL,'Free','5',NULL),(211,9,93,NULL,NULL,'Free','1',NULL),(212,9,93,NULL,NULL,'Free','2',NULL),(213,9,93,NULL,NULL,'Free','3',NULL),(214,9,93,NULL,NULL,'Free','4',NULL),(215,9,93,NULL,NULL,'Free','5',NULL),(216,9,94,NULL,NULL,'Free','1',NULL),(217,9,94,NULL,NULL,'Free','2',NULL),(218,9,94,NULL,NULL,'Free','3',NULL),(219,9,94,NULL,NULL,'Free','4',NULL),(220,9,94,NULL,NULL,'Free','5',NULL),(221,9,95,NULL,NULL,'Free','1',NULL),(222,9,95,NULL,NULL,'Free','2',NULL),(223,9,95,NULL,NULL,'Free','3',NULL),(224,9,95,NULL,NULL,'Free','4',NULL),(225,9,95,NULL,NULL,'Free','5',NULL),(226,10,96,NULL,NULL,'Free','1',NULL),(227,10,96,NULL,NULL,'Free','2',NULL),(228,10,96,NULL,NULL,'Free','3',NULL),(229,10,96,NULL,NULL,'Free','4',NULL),(230,10,96,NULL,NULL,'Free','5',NULL),(231,10,97,NULL,NULL,'Free','1',NULL),(232,10,97,NULL,NULL,'Free','2',NULL),(233,10,97,NULL,NULL,'Free','3',NULL),(234,10,97,NULL,NULL,'Free','4',NULL),(235,10,97,NULL,NULL,'Free','5',NULL),(236,10,98,NULL,NULL,'Free','1',NULL),(237,10,98,NULL,NULL,'Free','2',NULL),(238,10,98,NULL,NULL,'Free','3',NULL),(239,10,98,NULL,NULL,'Free','4',NULL),(240,10,98,NULL,NULL,'Free','5',NULL),(241,10,99,NULL,NULL,'Free','1',NULL),(242,10,99,NULL,NULL,'Free','2',NULL),(243,10,99,NULL,NULL,'Free','3',NULL),(244,10,99,NULL,NULL,'Free','4',NULL),(245,10,99,NULL,NULL,'Free','5',NULL),(246,10,100,NULL,NULL,'Free','1',NULL),(247,10,100,NULL,NULL,'Free','2',NULL),(248,10,100,NULL,NULL,'Free','3',NULL),(249,10,100,NULL,NULL,'Free','4',NULL),(250,10,100,NULL,NULL,'Free','5',NULL);
/*!40000 ALTER TABLE `busy_room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  `email` varchar(100) NOT NULL,
  `birth_date` date DEFAULT NULL,
  `current_address` text,
  `citizen_id` varchar(20) NOT NULL,
  `old_password_1` varchar(255) DEFAULT NULL,
  `old_password_2` varchar(255) DEFAULT NULL,
  `old_password_3` varchar(255) DEFAULT NULL,
  `customer_type` int DEFAULT '3',
  `role` varchar(50) DEFAULT 'customers',
  `create_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `phone_number` (`phone_number`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `citizen_id` (`citizen_id`),
  KEY `customer_type` (`customer_type`),
  CONSTRAINT `customers_ibfk_1` FOREIGN KEY (`customer_type`) REFERENCES `discounts` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (4,'ducmanh2873','Luongducmanh2003.','Lương Đức Mạnh1','0925940864','luongducmanh02@gmail.com','2003-07-28','Viet Nam','038203026041','Ducmanh2872003.',NULL,NULL,3,'customers','2025-04-15 17:36:38','2025-04-15 20:08:16'),(5,'minhtu12345','Minhtu12345','Minh Tú','0928374712','minhtu09042003@gmail.com',NULL,NULL,'0294837132341','Minhtu12345.',NULL,NULL,3,'customers','2025-04-15 17:36:38','2025-04-16 19:37:54'),(6,'phong','Lang_ngoang!the?','Nguyễn Hải Phong','0941107983','phong11d2@gmail.com','2025-04-24','VIETNAM1','56416541',NULL,NULL,NULL,3,'customers','2025-04-15 17:36:38','2025-04-15 17:37:26'),(7,'taitamtu','tai123456@','pham van tai','0123456789','tai220203@gmail.com',NULL,NULL,'01234567899',NULL,NULL,NULL,3,'customers','2025-04-15 17:36:50','2025-04-15 17:37:26'),(8,'ducmanhne213','Ducmanh2003.','0129312104124','0925940865','luongducmanh03@gmail.com',NULL,NULL,'Lương Đức Manhhh',NULL,NULL,NULL,3,'customer','2025-04-15 18:06:05','2025-04-15 18:06:05'),(9,'admin','Admin123456789','ADMIN','Admin123456789','admin@hotelbooking.com','2003-07-28','VietNam1','ADMIN',NULL,NULL,NULL,3,'admin','2025-04-15 18:12:26','2025-04-16 09:17:38'),(10,'ducmanhne212','Ducmanh2873.','Luowng DDuwcs Manhj','0925940888','ditmemayconlon1234@gmail.com',NULL,NULL,'02391284102401',NULL,NULL,NULL,3,'customers','2025-04-16 08:11:09','2025-04-16 08:11:09'),(19,'admintu','Admin123456789','312878174912741287','01283128318','admintu@gmailc.om','2025-01-13',NULL,'Nguyen Minh Tu',NULL,NULL,NULL,3,'admin','2025-04-17 07:09:40','2025-04-17 08:37:43'),(20,'Tuu','Nguyenminhtu@','Minhtu','0988055986','soibeetiiii@gmail.com',NULL,NULL,'086473962847',NULL,NULL,NULL,3,'customers','2025-04-17 08:51:38','2025-04-17 08:51:38');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discounts`
--

DROP TABLE IF EXISTS `discounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `discounts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_type` varchar(50) NOT NULL,
  `discount` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `customer_type` (`customer_type`),
  CONSTRAINT `discounts_chk_1` CHECK ((`discount` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discounts`
--

LOCK TABLES `discounts` WRITE;
/*!40000 ALTER TABLE `discounts` DISABLE KEYS */;
INSERT INTO `discounts` VALUES (1,'VIP',10.00),(2,'Regular',5.00),(3,'New Customer',0.00);
/*!40000 ALTER TABLE `discounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hotels`
--

DROP TABLE IF EXISTS `hotels`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hotels` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `address` varchar(250) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `area` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `hotline` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `rate` decimal(2,1) DEFAULT NULL,
  `image_url` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `status` enum('Available','Fully booked') CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT 'Available',
  `review_score` decimal(3,2) DEFAULT NULL,
  `hotel_price` text COLLATE utf8mb4_unicode_ci,
  `create_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hotline` (`hotline`),
  CONSTRAINT `hotels_chk_1` CHECK ((`rate` between 0 and 5)),
  CONSTRAINT `hotels_chk_2` CHECK ((`review_score` between 0 and 10))
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hotels`
--

LOCK TABLES `hotels` WRITE;
/*!40000 ALTER TABLE `hotels` DISABLE KEYS */;
INSERT INTO `hotels` VALUES (1,'Grand Hotel','123 Nguyen Trai, Ha Noi','Ha Noi','0987654321',4.0,'/Hotel/Grand_Hotel/grand_hotel.jpg','','Available',8.90,'2 - 3','2025-04-16 15:06:45','2025-04-17 08:24:53'),(2,'Ocean View','456 Tran Phu, Da Nang','Da Nang','0971234567',4.0,'/Hotel/Ocean_View/ocean_view.jpg','Beachfront hotel with stunning views','Available',9.10,'1 - 2','2025-04-16 15:06:45','2025-04-16 15:08:19'),(3,'Mountain Retreat','789 Hoang Lien, Lao Cai','Lao Cai','0963456789',4.0,'/Hotel/Mountain_Retreat/mountain_retreat.jpg','Quiet retreat in the mountains','Fully booked',8.50,'1 - 2','2025-04-16 15:06:45','2025-04-16 15:08:19'),(4,'Sunshine Hotel','321 Le Loi, Ho Chi Minh City','Ho Chi Minh City','0956781234',4.0,'/Hotel/Sunshine_Hotel/sunshine_hotel.jpg','Modern hotel in downtown Saigon','Available',7.80,'1 - 2','2025-04-16 15:06:45','2025-04-16 15:08:19'),(5,'Paradise Resort','555 Bai Dai, Phu Quoc','Phu Quoc','0945678912',4.0,'/Hotel/Paradise_Resort/paradise_resort.jpg','Luxury resort with a private beach','Available',9.50,'1 - 2','2025-04-16 15:06:45','2025-04-16 15:08:19'),(6,'Lakeview Inn','222 West Lake, Ha Noi','Ha Noi','0934567891',3.0,'/Hotel/Lakeview_Inn/lakeview_inn.jpg','Quiet hotel with lake views','Fully booked',7.20,'1 - 2','2025-04-16 15:06:45','2025-04-16 15:08:19'),(7,'Skyline Hotel','777 Dien Bien Phu, Da Nang','Da Nang','0923456789',4.0,'/Hotel/Skyline_Hotel/skyline_hotel.jpg','High-rise hotel with city views','Available',8.70,'1 - 2','2025-04-16 15:06:45','2025-04-16 15:08:19'),(8,'Royal Palace','999 Nguyen Hue, Ho Chi Minh City','Ho Chi Minh City','0912345678',4.0,'/Hotel/Royal_Palace/royal_palace.jpg','Royal-style luxury hotel','Available',9.00,'3 - 5','2025-04-16 15:06:45','2025-04-16 15:08:19'),(9,'Cozy Homestay','123 Ly Thuong Kiet, Hue','Hue','0909876543',3.0,'/Hotel/Cozy_Homestay/cozy_homestay.jpg','Cozy homestay ideal for travelers','Available',6.80,'1 - 2','2025-04-16 15:06:45','2025-04-16 15:08:19'),(10,'Eco Lodge','888 National Forest, Da Lat','Da Lat','0898765432',4.0,'/Hotel/Eco_Lodge/eco_lodge.jpg','Eco-friendly lodge in nature','Fully booked',8.30,'1 - 2','2025-04-16 15:06:45','2025-04-16 15:08:19');
/*!40000 ALTER TABLE `hotels` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `invoice_additionalservices`
--

DROP TABLE IF EXISTS `invoice_additionalservices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invoice_additionalservices` (
  `invoice_id` int NOT NULL,
  `service_id` int NOT NULL,
  PRIMARY KEY (`invoice_id`,`service_id`),
  KEY `service_id` (`service_id`),
  CONSTRAINT `invoice_additionalservices_ibfk_1` FOREIGN KEY (`invoice_id`) REFERENCES `invoices` (`id`) ON DELETE CASCADE,
  CONSTRAINT `invoice_additionalservices_ibfk_2` FOREIGN KEY (`service_id`) REFERENCES `additionalservices` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invoice_additionalservices`
--

LOCK TABLES `invoice_additionalservices` WRITE;
/*!40000 ALTER TABLE `invoice_additionalservices` DISABLE KEYS */;
INSERT INTO `invoice_additionalservices` VALUES (2,1),(1,2),(1,3),(2,3),(1,4),(2,4);
/*!40000 ALTER TABLE `invoice_additionalservices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `invoices`
--

DROP TABLE IF EXISTS `invoices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `invoices` (
  `id` int NOT NULL AUTO_INCREMENT,
  `customer_id` int NOT NULL,
  `room_type_id` int NOT NULL,
  `check_in` date NOT NULL,
  `check_out` date NOT NULL,
  `total_price` decimal(10,2) DEFAULT NULL,
  `hotel_id` int NOT NULL,
  `state` enum('DA THANH TOAN','CHUA THANH TOAN') CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT 'CHUA THANH TOAN',
  `create_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_for_someone_else` tinyint(1) DEFAULT '0',
  `other_person_name` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `other_person_ccid` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `room_number` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `customer_id` (`customer_id`),
  KEY `room_type_id` (`room_type_id`),
  KEY `hotel_id` (`hotel_id`),
  CONSTRAINT `invoices_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`) ON DELETE CASCADE,
  CONSTRAINT `invoices_ibfk_2` FOREIGN KEY (`room_type_id`) REFERENCES `roomtypes` (`id`) ON DELETE CASCADE,
  CONSTRAINT `invoices_ibfk_3` FOREIGN KEY (`hotel_id`) REFERENCES `hotels` (`id`) ON DELETE CASCADE,
  CONSTRAINT `invoices_chk_1` CHECK ((`total_price` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `invoices`
--

LOCK TABLES `invoices` WRITE;
/*!40000 ALTER TABLE `invoices` DISABLE KEYS */;
INSERT INTO `invoices` VALUES (1,4,51,'2025-04-19','2025-04-22',435.00,1,'CHUA THANH TOAN','2025-04-17 17:43:00','2025-04-17 17:48:33',0,NULL,NULL,'1'),(2,4,52,'2025-04-20','2025-04-25',570.00,1,'CHUA THANH TOAN','2025-04-17 18:54:07','2025-04-17 18:54:07',0,NULL,NULL,'1');
/*!40000 ALTER TABLE `invoices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log`
--

DROP TABLE IF EXISTS `log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `log` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `customer_id` int DEFAULT NULL,
  `action` text NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `customer_id` (`customer_id`),
  CONSTRAINT `log_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`) ON DELETE SET NULL
) ENGINE=InnoDB AUTO_INCREMENT=135 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log`
--

LOCK TABLES `log` WRITE;
/*!40000 ALTER TABLE `log` DISABLE KEYS */;
INSERT INTO `log` VALUES (130,'2025-04-17 18:22:56',9,'Logout'),(131,'2025-04-17 18:25:36',9,'Login'),(132,'2025-04-17 18:40:40',4,'Login'),(133,'2025-04-17 19:00:16',4,'Logout'),(134,'2025-04-17 19:00:20',9,'Login');
/*!40000 ALTER TABLE `log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `invoices_id` int NOT NULL,
  `total_money` decimal(12,2) NOT NULL,
  `pay_description` text,
  `state` varchar(50) DEFAULT 'success',
  `create_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `type_of_payment` varchar(50) DEFAULT NULL,
  `card_number` varchar(20) DEFAULT NULL,
  `card_type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `invoices_id` (`invoices_id`),
  CONSTRAINT `payment_ibfk_1` FOREIGN KEY (`invoices_id`) REFERENCES `invoices` (`id`) ON DELETE CASCADE,
  CONSTRAINT `check_card_number_required` CHECK (((`type_of_payment` <> _utf8mb4'card') or (`card_number` is not null))),
  CONSTRAINT `check_card_type_required` CHECK (((`type_of_payment` <> _cp850'card') or (`card_type` is not null)))
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment`
--

LOCK TABLES `payment` WRITE;
/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roomtypes`
--

DROP TABLE IF EXISTS `roomtypes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roomtypes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `hotel_id` int NOT NULL,
  `capacity` int DEFAULT NULL,
  `bed_type` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `rating` int DEFAULT NULL,
  `availability` int DEFAULT NULL,
  `services` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `price` decimal(10,2) DEFAULT NULL,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `area` float DEFAULT '20',
  `img_url` text COLLATE utf8mb4_unicode_ci,
  `create_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `update_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `hotel_id` (`hotel_id`),
  CONSTRAINT `roomtypes_ibfk_1` FOREIGN KEY (`hotel_id`) REFERENCES `hotels` (`id`) ON DELETE CASCADE,
  CONSTRAINT `roomtypes_chk_1` CHECK ((`rating` between 1 and 5)),
  CONSTRAINT `roomtypes_chk_2` CHECK ((`price` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=102 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roomtypes`
--

LOCK TABLES `roomtypes` WRITE;
/*!40000 ALTER TABLE `roomtypes` DISABLE KEYS */;
INSERT INTO `roomtypes` VALUES (51,1,2,'King',5,4,'WiFi, TV, Mini Bar',120.00,'Deluxe Room',20,'/Hotel/Grand_Hotel/deluxe_room.jpg','2025-04-16 16:22:39','2025-04-17 17:43:00'),(52,1,3,'Queen',4,4,'WiFi, TV, Balcony',100.00,'Family Room',20,'/Hotel/Grand_Hotel/family_room.jpg','2025-04-16 16:22:39','2025-04-17 18:54:07'),(53,1,1,'Single',3,5,'WiFi, Desk',80.00,'Standard Room',20,'/Hotel/Grand_Hotel/standard_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(54,1,2,'Twin',4,5,'WiFi, TV, Coffee Maker',90.00,'Twin Room',20,'/Hotel/Grand_Hotel/twin_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(55,1,4,'Double',5,5,'WiFi, TV, Sofa',150.00,'Suite',20,'/Hotel/Grand_Hotel/suite.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(56,2,2,'King',5,5,'WiFi, TV, Mini Bar',130.00,'Deluxe Room',20,'/Hotel/Ocean_View/deluxe_room.jpg','2025-04-16 16:22:39','2025-04-17 11:39:13'),(57,2,3,'Queen',4,5,'WiFi, TV, Balcony',110.00,'Family Room',20,'/Hotel/Ocean_View/family_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(58,2,1,'Single',3,5,'WiFi, Desk',85.00,'Standard Room',20,'/Hotel/Ocean_View/standard_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(59,2,2,'Twin',4,5,'WiFi, TV, Coffee Maker',95.00,'Twin Room',20,'/Hotel/Ocean_View/twin_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(60,2,4,'Double',5,5,'WiFi, TV, Sofa',160.00,'Suite',20,'/Hotel/Ocean_View/suite.jpg','2025-04-16 16:22:39','2025-04-16 16:22:39'),(61,3,2,'King',5,5,'WiFi, TV, Mini Bar',125.00,'Deluxe Room',20,'/Hotel/Mountain_Retreat/deluxe_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(62,3,3,'Queen',4,5,'WiFi, TV, Balcony',105.00,'Family Room',20,'/Hotel/Mountain_Retreat/family_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(63,3,1,'Single',3,5,'WiFi, Desk',75.00,'Standard Room',20,'/Hotel/Mountain_Retreat/standard_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(64,3,2,'Twin',4,5,'WiFi, TV, Coffee Maker',88.00,'Twin Room',20,'/Hotel/Mountain_Retreat/twin_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(65,3,4,'Double',5,5,'WiFi, TV, Sofa',140.00,'Suite',20,'/Hotel/Mountain_Retreat/suite.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(66,4,2,'King',5,5,'WiFi, TV, Mini Bar',135.00,'Deluxe Room',20,'/Hotel/Sunshine_Hotel/deluxe_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(67,4,3,'Queen',4,5,'WiFi, TV, Balcony',115.00,'Family Room',20,'/Hotel/Sunshine_Hotel/family_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(68,4,1,'Single',3,5,'WiFi, Desk',78.00,'Standard Room',20,'/Hotel/Sunshine_Hotel/standard_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(69,4,2,'Twin',4,5,'WiFi, TV, Coffee Maker',92.00,'Twin Room',20,'/Hotel/Sunshine_Hotel/twin_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(70,4,4,'Double',5,5,'WiFi, TV, Sofa',155.00,'Suite',20,'/Hotel/Sunshine_Hotel/suite.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(71,5,2,'King',5,5,'WiFi, TV, Mini Bar',128.00,'Deluxe Room',20,'/Hotel/Paradise_Resort/deluxe_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(72,5,3,'Queen',4,5,'WiFi, TV, Balcony',108.00,'Family Room',20,'/Hotel/Paradise_Resort/family_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(73,5,1,'Single',3,5,'WiFi, Desk',82.00,'Standard Room',20,'/Hotel/Paradise_Resort/standard_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(74,5,2,'Twin',4,5,'WiFi, TV, Coffee Maker',87.00,'Twin Room',20,'/Hotel/Paradise_Resort/twin_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(75,5,4,'Double',5,5,'WiFi, TV, Sofa',148.00,'Suite',20,'/Hotel/Paradise_Resort/suite.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(76,6,2,'King',5,5,'WiFi, TV, Mini Bar',132.00,'Deluxe Room',20,'/Hotel/Lakeview_Inn/deluxe_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(77,6,3,'Queen',4,5,'WiFi, TV, Balcony',112.00,'Family Room',20,'/Hotel/Lakeview_Inn/family_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(78,6,1,'Single',3,5,'WiFi, Desk',79.00,'Standard Room',20,'/Hotel/Lakeview_Inn/standard_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(79,6,2,'Twin',4,5,'WiFi, TV, Coffee Maker',93.00,'Twin Room',20,'/Hotel/Lakeview_Inn/twin_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(80,6,4,'Double',5,5,'WiFi, TV, Sofa',152.00,'Suite',20,'/Hotel/Lakeview_Inn/suite.jpg','2025-04-16 16:22:39','2025-04-16 16:22:39'),(81,7,2,'King',5,5,'WiFi, TV, Mini Bar',127.00,'Deluxe Room',20,'/Hotel/Skyline_Hotel/deluxe_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(82,7,3,'Queen',4,5,'WiFi, TV, Balcony',106.00,'Family Room',20,'/Hotel/Skyline_Hotel/family_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(83,7,1,'Single',3,5,'WiFi, Desk',81.00,'Standard Room',20,'/Hotel/Skyline_Hotel/standard_room.jpg','2025-04-16 16:22:39','2025-04-16 16:22:39'),(84,7,2,'Twin',4,5,'WiFi, TV, Coffee Maker',85.00,'Twin Room',20,'/Hotel/Skyline_Hotel/twin_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(85,7,4,'Double',5,5,'WiFi, TV, Sofa',145.00,'Suite',20,'/Hotel/Skyline_Hotel/suite.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(86,8,2,'King',5,5,'WiFi, TV, Mini Bar',122.00,'Deluxe Room',20,'/Hotel/Royal_Palace/deluxe_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(87,8,3,'Queen',4,5,'WiFi, TV, Balcony',102.00,'Family Room',20,'/Hotel/Royal_Palace/family_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(88,8,1,'Single',3,5,'WiFi, Desk',77.00,'Standard Room',20,'/Hotel/Royal_Palace/standard_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(89,8,2,'Twin',4,5,'WiFi, TV, Coffee Maker',89.00,'Twin Room',20,'/Hotel/Royal_Palace/twin_room.jpg','2025-04-16 16:22:39','2025-04-16 16:22:39'),(90,8,4,'Double',5,5,'WiFi, TV, Sofa',138.00,'Suite',20,'/Hotel/Royal_Palace/suite.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(91,9,2,'King',5,5,'WiFi, TV, Mini Bar',133.00,'Deluxe Room',20,'/Hotel/Cozy_Homestay/deluxe_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(92,9,3,'Queen',4,5,'WiFi, TV, Balcony',109.00,'Family Room',20,'/Hotel/Cozy_Homestay/family_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(93,9,1,'Single',3,5,'WiFi, Desk',83.00,'Standard Room',20,'/Hotel/Cozy_Homestay/standard_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(94,9,2,'Twin',4,5,'WiFi, TV, Coffee Maker',91.00,'Twin Room',20,'/Hotel/Cozy_Homestay/twin_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(95,9,4,'Double',5,5,'WiFi, TV, Sofa',149.00,'Suite',20,'/Hotel/Cozy_Homestay/suite.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(96,10,2,'King',5,5,'WiFi, TV, Mini Bar',140.00,'Deluxe Room',20,'/Hotel/Eco_Lodge/deluxe_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(97,10,3,'Queen',4,5,'WiFi, TV, Balcony',120.00,'Family Room',20,'/Hotel/Eco_Lodge/family_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(98,10,1,'Single',3,5,'WiFi, Desk',88.00,'Standard Room',20,'/Hotel/Eco_Lodge/standard_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(99,10,2,'Twin',4,5,'WiFi, TV, Coffee Maker',94.00,'Twin Room',20,'/Hotel/Eco_Lodge/twin_room.jpg','2025-04-16 16:22:39','2025-04-17 17:22:05'),(100,10,4,'Double',5,5,'WiFi, TV, Sofa',160.00,'Suite',20,'/Hotel/Eco_Lodge/suite.jpg','2025-04-16 16:22:39','2025-04-16 16:22:39');
/*!40000 ALTER TABLE `roomtypes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-17 22:27:03
