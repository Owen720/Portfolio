-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: attendence_system
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `student_id` varchar(45) NOT NULL,
  `name` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('awkin','AU Wing Kin','awkin123'),('badatt','BHATT Arun Datt','badatt123'),('ccfung','CHAN Chun Fung','ccfung123'),('cchang','CHEUNG Chin Hang','cchang123'),('ccho','CHONG Chi Ho','ccho123'),('ccleuk','CHOI Chun Leuk','ccleuk123'),('chkai','CHEUNG Ho Kai','chkai123'),('chlok','CHUNG Shun Lok','chlok123'),('ckming','CHAN Kam Ming','ckming123'),('cphong','CHOI Pak Hong Erick','cphong123'),('csfung','CHEUNG Siu Fung','csfung123'),('ctlong','CHAN Tsz Long','ctlong123'),('cychi','CHAN Yuet Chi','cychi123'),('cyide','CAI Yide','cyide123'),('fcnam','FAN Cheuk Nam','fcnam123'),('fhwang','FAN Ho Wang','fhwang123'),('fktai','FUNG Kwan Tai','fktai123'),('fstung','FONG Siu Tung','fstung123'),('hjingshen','HE Jingshen','hjingshen123'),('hmho','HO Man Ho','hmho123'),('htking','HO Tsz King','htking123'),('hwsan','HOI Wai San','hwsan123'),('jhwang','JE Ho Wang','jhwang123'),('kkchun','KONG Kin Chun','kkchun123'),('ktwai','KWONG Tak Wai','ktwai123'),('lhchak','LO Hon Chak','lhchak123'),('lhchuen','LIN Hon Chuen','lhchuen123'),('lhming','LEE Ho Ming','lhming123'),('lhongzhou','LI Hongzhou','lhongzhou123'),('lhyin','LEE Ho Yin','lhyin123'),('ljinkun','LIU Jinkun','ljinkun123'),('lmwai','LAM Man Wai','lmwai123'),('lpchung','LAM Pui Chung','lpchung123'),('lpwai','LEUNG Pak Wai Ryan','lpwai123'),('ltwo','LING Tsz Wo','ltwo123'),('lwshing','LEUNG Wing Shing','lwshing123'),('lwsum','LAU Wai Sum','lwsum123'),('lychit','LEUNG Yui Chit','lychit123'),('lyman','LI Yuen Man','lyman123'),('mtfung','MAK Tsz Fung','mtfung123'),('ntfung','NG Tai Fung','ntfung123'),('oxiaolong','OUYANG Xiaolong','oxiaolong123'),('phman','PANG Chu Man','phman123'),('srafiq','SHERAAZ-RAFIQ','srafiq123'),('ssingh','SIMARJEET-SINGH','ssingh123'),('tapak','TANG Audric Pak Hang','tapak123'),('ttho','TANG Tsz Ho','ttho123'),('wckit','WONG Chun Kit','wckit123'),('whjun','WONG Hin Jun','whjun123'),('wskwan','WONG Shuk Kwan','wskwan123'),('wyhang','WONG Yin Hang Marco','wyhang123'),('xjiaying','XU Jiaying','xjiaying123'),('xqichen','XIE Qichen','xqichen123'),('xyutong','XING Yutong','xyutong123'),('ycho','YUEN Chun Ho','ycho123'),('yhaochen','YAN Haochen','yhaochen123'),('ysman','YIP Sze Man','ysman123'),('ysshing','YIP Shi Shing','ysshing123'),('ythei','YEUNG Tak Hei','ythei123'),('zhuipeng','ZHOU Huipeng','zhuipeng123');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-25 22:18:41
