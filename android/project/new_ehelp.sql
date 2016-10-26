-- MySQL dump 10.13  Distrib 5.6.24, for Win64 (x86_64)
--
-- Host: localhost    Database: ehelp
-- ------------------------------------------------------
-- Server version	5.5.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `account`
--

DROP TABLE IF EXISTS `account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account` varchar(100) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  `chat_token` varchar(100) DEFAULT NULL,
  `salt` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account` (`account`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account`
--

LOCK TABLES `account` WRITE;
/*!40000 ALTER TABLE `account` DISABLE KEYS */;
INSERT INTO `account` VALUES (72,'aaa','f3611afbe6910f6ab1531372e48e65a0','tmG5PbPv1zWTmSi4O6/J+AxDSlzJO+c4eiOET2yX7voMnxhh1WBHWCQ1RSoJW7kF78WGonKt6SbuJnKDUAa9Dg==','iyLFboRC'),(73,'111','7f2c4bc48b4c452448b2aa0d65da7ef8','lbe31nzFzcdibLFYUS3kT+RgfvzP32M+B6kCt5/NOhiY4zzu6wYpVwxoAeYbdt5koJ/hEKE11JJRjxNkdSyWSA==','JQlHqLMF'),(74,'222','f3e93e56f2ec56c832782e9cc7ad6f56','VqBJfGWHHARnSpf67o87muRgfvzP32M+B6kCt5/NOhiY4zzu6wYpV1rFfbFJ/X6xNs6a2gnp/jJRjxNkdSyWSA==','tweTdUZP'),(75,'333','7866f2a6a4c455443b73bc99843fbe3f','XEOc7sHIlGFtCk1W96+qdo7gwmqD7eXk09aKxnvU5ETN26HSYgy6+B4gnYMGcxieroDd1VDKZaY=','dfYNAVqz'),(76,'zzz','4bf356c57d7216e60258518c335a43dd','gxJdy81fOTuTweDYHiotP+RgfvzP32M+B6kCt5/NOhg6VpstVL/5CE+GqovV0zKpC9aQ8zyOvVxRjxNkdSyWSA==','NMBnibxR'),(77,'xxx','cb0b92be036ca6472c85738b20af3e7a','jEldF0rYNamuZgrJu2axiQxDSlzJO+c4eiOET2yX7voMnxhh1WBHWIS7wgjmz5WaBBtnL2Ml7W3uJnKDUAa9Dg==','ErVXeTjK'),(78,'ccc','a4c9c5cfb3fe718fb1cc141e9a1545a3','ICxeZEHxWaoKD4GL/XCFDAxDSlzJO+c4eiOET2yX7voMnxhh1WBHWHTAqgPDT6DfOp8WDF4zI6vuJnKDUAa9Dg==','cxCJMlIE'),(79,'vvv','ddb23003c6ded6c9c7e75c6ef979cec1','mRayn7q0MkWNDHFx4zci9Y7gwmqD7eXk09aKxnvU5EQ5hbniCm5m8qaYmx2RHzpV6CxgrKWd1Is=','hTioLwEa'),(80,'bbb','39d874706037c38715ff0a1249bcefcb','WnrcdAXHuTKZwkiWmfyt9o7gwmqD7eXk09aKxnvU5EQ5hbniCm5m8sBS5FPtBxr6aPy6RgHxDoA=','IfRrLNAt'),(81,'nnn','1623b994d465586cfce4d52ec9baae92','W2E9d7WT3hJNNd2+eRttHwxDSlzJO+c4eiOET2yX7voMnxhh1WBHWHERTn/BYGv4OcfMNSv0ZPTuJnKDUAa9Dg==','mGrZfQXk'),(82,'rrr','6dcf06e46cf09566d2cb14eea6b97404','iaU4DLhnBNmZwkiWmfyt9o7gwmqD7eXk09aKxnvU5EQ5hbniCm5m8jBuHx45x1iyxuefeXssilI=','MDmPlvRp'),(83,'zxc','a85f4cfbf189f9f26e0c10ac54ce8ea1','wT/rSnLVORTzOjtSEoI1zeRgfvzP32M+B6kCt5/NOhg6VpstVL/5CHgakTJe3DURcSgluUO2fNRRjxNkdSyWSA==','NIBAVfqX'),(84,'q','fab73741fcf1f719a7ac854571a23717','PPF/PLk26F6l8T9AjvLLEwxDSlzJO+c4eiOET2yX7voMnxhh1WBHWNsY2+yDYA4VcDga6uf8qWPuJnKDUAa9Dg==','KqbOwzNL'),(85,'t','7c866e6ada9a01b86d49089fe5b3ab3e','IR8pnJo91drv1Rz8wHRVkuRgfvzP32M+B6kCt5/NOhg6VpstVL/5CC+sFDTOj9lwy0fWxfC18a5RjxNkdSyWSA==','iHBhMFLn'),(86,'yyy','65f285eb399af5c4174bc42237acb96f','A5EGvK014N3Nv4dO/kC9247gwmqD7eXk09aKxnvU5EQ5hbniCm5m8kOwm3nMz25ztWPO1ciBq+Q=','AXqhQWzZ'),(87,'1','9d059d131ea64fddbfcfe76af7c721fd','DzJHxoiupUNnRg6z9NR3FQxDSlzJO+c4eiOET2yX7voMnxhh1WBHWJ0sOENxiHtBrqyscoO4/bLuJnKDUAa9Dg==','DJYTaoUK'),(88,'2','9ac4167d3d685303330b6497571c5c4b','roYifLQxMZVtCk1W96+qdo7gwmqD7eXk09aKxnvU5EQtzN2Ovaccz3th59aXZaia1Qk0ERjARg4=','eLhyBJKO'),(89,'3','a8fc613fe5ef1d49bbc2bde7f6510f4a','UKlBN2vRZZ11wvqJ8bt7oQxDSlzJO+c4eiOET2yX7voMnxhh1WBHWBDvzidmJrP0vRG+6SZeZYzuJnKDUAa9Dg==','ZJmCxLNG'),(90,'4','e73721418e762d82af5ff6fc49670b90','PuJygLRdoQcUI7PQoeiRbeRgfvzP32M+B6kCt5/NOhg6VpstVL/5CNo6MetSbnpV/raliJeeAM5RjxNkdSyWSA==','gIRMExYk'),(91,'5','fe9c33c94ef3c754425e1e013dbb727c','tnomOggRW57H/bN0aZQNOuRgfvzP32M+B6kCt5/NOhg6VpstVL/5CJIt6DQbPy2bwuFpII4k0txRjxNkdSyWSA==','WFRvjLha'),(92,'6','cb2831cdeca44f5c900ba8864a00334c','+mwxGKYzrzeNBhoA+bW/lQxDSlzJO+c4eiOET2yX7voMnxhh1WBHWNEa1M4OsMC5X0yu+5qJ2+DuJnKDUAa9Dg==','gjZelwLd'),(93,'7','1ecbe37ff7df323068fec0e1cb1a2e3f','3zvhZelUkUpCQkLwhElxKuRgfvzP32M+B6kCt5/NOhiKZPssDep/0ESBk2RsmrhaBaG84i3iqYBRjxNkdSyWSA==','FPOiYAqS'),(94,'8','f0b3c2a8c89a4790c3cf055cd65e6e0b','5I0kp/+MVPQ5E8i7uO37heRgfvzP32M+B6kCt5/NOhiKZPssDep/0JNN+1ieOXvcFfEmyiMAF1BRjxNkdSyWSA==','XABdqHua'),(95,'10','ba4538a871d55c26c79f17f1e0f70748','UbYGvjKDk/jzOjtSEoI1zeRgfvzP32M+B6kCt5/NOhiKZPssDep/0NZv4Nf2nVUTZ/WtzaGvzuhRjxNkdSyWSA==','DmPoVzKS'),(96,'11','9a40e5f4f164a61fd21e44dcd07d10c7','vJGDCm7JhaN+ywi094r9VeRgfvzP32M+B6kCt5/NOhiKZPssDep/0MQMvkv1PUTFRtBRISD8cX1RjxNkdSyWSA==','HgXSVWuj'),(97,'12','1ab7ab148d70c8a320fb1f3e13a4259c','/O1SBz4RGHg+VFdHejcDA+RgfvzP32M+B6kCt5/NOhiKZPssDep/0EYZxqjO4AXCKID0Lb729aNRjxNkdSyWSA==','WOZylfDb'),(98,'13','c997569ca70cd3e21af6b3e246ba6e02','589MsqjitC9tCk1W96+qdo7gwmqD7eXk09aKxnvU5ESBvD7M70u/Qyy85856m6/i0/Nuaz16DMk=','ouGLYWtF'),(99,'14','e800e2f2afe583396df645fc9303f0ac','4yLo1SS36mSTweDYHiotP+RgfvzP32M+B6kCt5/NOhiKZPssDep/0OVx9kGu3jitLdgpt2kngd1RjxNkdSyWSA==','nzPbjHqM');
/*!40000 ALTER TABLE `account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `answer`
--

DROP TABLE IF EXISTS `answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `answer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `event_id` int(11) NOT NULL,
  `author_id` int(11) NOT NULL,
  `content` varchar(500) DEFAULT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_adopted` tinyint(1) DEFAULT '0',
  `liking_num` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `event_idx` (`event_id`),
  KEY `author_id_fx` (`author_id`),
  CONSTRAINT `author_id_fx` FOREIGN KEY (`author_id`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `event_id_fx` FOREIGN KEY (`event_id`) REFERENCES `event` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer`
--

LOCK TABLES `answer` WRITE;
/*!40000 ALTER TABLE `answer` DISABLE KEYS */;
/*!40000 ALTER TABLE `answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coin_exchange`
--

DROP TABLE IF EXISTS `coin_exchange`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `coin_exchange` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sender` int(11) NOT NULL,
  `receiver` int(11) NOT NULL,
  `lovecoin` int(11) NOT NULL DEFAULT '0',
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `e_from_idx` (`sender`),
  KEY `e_to_idx` (`receiver`),
  CONSTRAINT `coin_exchange_from_fk` FOREIGN KEY (`sender`) REFERENCES `account` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `coin_exchange_to_fk` FOREIGN KEY (`receiver`) REFERENCES `account` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coin_exchange`
--

LOCK TABLES `coin_exchange` WRITE;
/*!40000 ALTER TABLE `coin_exchange` DISABLE KEYS */;
/*!40000 ALTER TABLE `coin_exchange` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coin_trade`
--

DROP TABLE IF EXISTS `coin_trade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `coin_trade` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `eventid` int(11) NOT NULL,
  `from` int(11) NOT NULL,
  `to` int(11) NOT NULL,
  `lovecoin` int(11) NOT NULL DEFAULT '0',
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `eventid_idx` (`eventid`),
  KEY `from_idx` (`from`),
  KEY `to_idx` (`to`),
  CONSTRAINT `coin_trade_eventid_fk` FOREIGN KEY (`eventid`) REFERENCES `event` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `coin_trade_from_fk` FOREIGN KEY (`from`) REFERENCES `account` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `coin_trade_to_fk` FOREIGN KEY (`to`) REFERENCES `account` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coin_trade`
--

LOCK TABLES `coin_trade` WRITE;
/*!40000 ALTER TABLE `coin_trade` DISABLE KEYS */;
/*!40000 ALTER TABLE `coin_trade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `event_id` int(11) NOT NULL,
  `author` int(11) NOT NULL,
  `content` text,
  `time` datetime DEFAULT NULL,
  `parent_author` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `event_id_idx` (`event_id`),
  KEY `author_idx` (`author`),
  KEY `comment_parent_author_fk` (`parent_author`),
  CONSTRAINT `comment_author_fk` FOREIGN KEY (`author`) REFERENCES `account` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `comment_eventid_fk` FOREIGN KEY (`event_id`) REFERENCES `event` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `comment_parent_author_fk` FOREIGN KEY (`parent_author`) REFERENCES `account` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=133 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES (1,474,72,'aa','2015-10-05 13:46:15',72),(2,474,72,'bb','2015-10-05 13:46:34',72),(3,474,72,'cc','2015-10-05 13:46:38',72),(4,472,72,'haha','2015-10-05 13:46:48',72),(5,472,72,'hehe','2015-10-05 13:46:54',72),(6,471,72,'now','2015-10-05 16:18:40',72),(7,475,72,'aa','2015-10-19 19:52:09',72),(8,475,72,'aaa','2015-10-20 00:07:39',72),(9,475,73,'111','2015-10-20 00:15:31',72),(10,475,72,'haha','2015-10-20 00:16:11',72),(11,476,72,'aaa','2015-10-21 19:54:20',72),(12,476,72,'ccc','2015-10-21 19:55:05',72),(13,476,72,'aaa','2015-10-21 19:55:20',72),(14,476,72,'ddd','2015-10-21 19:55:36',72),(15,476,72,'111','2015-10-21 19:55:47',72),(16,476,72,'1','2015-10-21 21:18:54',72),(17,479,72,'1','2015-10-21 21:29:10',73),(18,480,72,'aa','2015-10-22 02:25:08',72),(19,480,72,'aaa','2015-10-22 02:25:35',72),(20,480,72,'aaa','2015-10-22 02:25:45',72),(21,480,72,'hehe','2015-10-22 02:25:59',72),(22,480,72,'hehehe','2015-10-22 02:26:19',72),(23,481,73,'e','2015-10-22 02:28:40',73),(24,481,72,'a','2015-10-22 02:29:52',73),(25,481,72,'a','2015-10-22 02:31:18',73),(26,483,73,'aaa','2015-10-22 02:32:35',73),(27,483,73,'aaa','2015-10-22 02:32:45',73),(28,483,73,'aaa','2015-10-22 02:33:29',73),(29,483,73,'aaa','2015-10-22 02:33:33',73),(30,483,73,'hehe','2015-10-22 02:36:13',73),(31,483,73,'yes','2015-10-22 02:36:18',73),(32,483,72,'ha','2015-10-22 02:36:32',73),(33,483,72,'ddd','2015-10-22 02:37:17',73),(34,483,73,'aa','2015-10-22 02:37:31',73),(35,483,72,'111','2015-10-22 10:25:22',73),(36,483,72,'222','2015-10-22 10:25:26',73),(37,484,73,'11','2015-10-22 11:08:01',72),(38,492,73,'aa','2015-10-22 12:22:56',74),(39,494,75,'22','2015-10-23 00:36:19',74),(40,494,75,'111','2015-10-23 00:36:36',74),(41,494,75,'222','2015-10-23 00:38:54',74),(42,501,75,'啊啊','2015-10-23 03:36:12',75),(43,502,75,'啊啊啊','2015-10-23 03:39:01',75),(44,502,75,'啊啊啊','2015-10-23 03:39:31',75),(45,512,72,'aaa','2015-10-24 10:18:07',73),(46,512,72,'haha','2015-10-24 10:29:50',73),(47,512,72,'haha','2015-10-24 10:31:08',73),(48,512,72,'a','2015-10-24 10:55:20',73),(49,512,72,'haha','2015-10-24 11:07:04',73),(50,512,72,'aa','2015-10-24 11:14:25',73),(51,512,72,'aa','2015-10-24 11:14:27',73),(52,512,72,'haha','2015-10-24 11:14:32',73),(53,511,72,'aa','2015-10-24 15:50:22',75),(54,513,72,'aa','2015-10-24 17:08:30',72),(55,513,72,'aaa','2015-10-24 17:19:01',72),(56,513,75,'11','2015-10-24 17:19:11',72),(57,513,73,'11','2015-10-25 01:52:04',72),(58,514,73,'1','2015-10-25 11:47:46',73),(59,515,73,'','2015-10-31 20:20:17',75),(60,515,73,'ll','2015-10-31 20:20:22',75),(61,515,73,'aaa','2015-11-05 00:07:58',75),(62,515,73,'?','2015-11-05 00:08:30',75),(63,515,73,'？','2015-11-05 00:54:02',75),(64,516,80,'呵呵哒','2015-11-07 00:04:43',80),(65,518,72,'什么','2015-11-08 03:01:29',87),(66,520,80,'什么 ','2015-11-08 03:58:17',72),(67,520,80,'呵呵','2015-11-08 03:58:43',72),(68,520,80,'呵呵了','2015-11-08 04:00:02',72),(69,520,89,'哈哈','2015-11-08 04:02:33',72),(70,520,87,'哈哈','2015-11-08 04:19:26',72),(71,520,90,'什么啊','2015-11-08 18:19:49',72),(72,520,90,'','2015-11-08 18:19:56',72),(73,520,90,'什么啊','2015-11-08 18:20:10',72),(74,520,90,'哈哈哈','2015-11-08 18:20:22',72),(75,520,90,'what?','2015-11-08 18:20:35',72),(76,520,90,'呵呵哒','2015-11-08 18:21:24',72),(77,520,90,'haha','2015-11-08 18:40:00',72),(78,520,90,'haha','2015-11-08 18:42:02',72),(79,520,90,'呵呵','2015-11-08 18:46:52',72),(80,520,90,'哈哈哈','2015-11-08 18:47:24',72),(81,519,90,'哈哈','2015-11-08 18:48:38',72),(82,520,90,'哈哈','2015-11-08 18:50:22',72),(83,520,90,'哈哈','2015-11-08 18:51:27',72),(84,520,90,'呵呵呵','2015-11-08 18:51:56',72),(85,520,90,'哈哈哈','2015-11-08 18:52:58',72),(86,519,90,'哈哈','2015-11-08 19:01:43',72),(87,520,90,'哈哈哈','2015-11-08 20:05:15',72),(88,520,91,'？','2015-11-09 10:17:29',72),(89,520,91,'嗯嗯到达','2015-11-09 10:17:37',72),(90,522,91,'嗯嗯的','2015-11-09 10:31:12',91),(91,522,91,'what?','2015-11-09 10:31:44',91),(92,524,91,'???','2015-11-09 10:34:53',91),(93,524,91,'?','2015-11-09 10:38:13',91),(94,524,91,'?','2015-11-09 10:42:45',91),(95,524,72,'aaa','2015-11-09 10:58:20',91),(96,524,72,'呵呵哒','2015-11-09 10:58:36',91),(97,524,90,'？','2015-11-09 11:00:42',91),(98,526,90,'嗯','2015-11-09 11:09:45',90),(99,526,92,'？','2015-11-09 11:13:52',90),(100,526,92,'？','2015-11-09 11:13:59',90),(101,526,91,'？','2015-11-09 11:14:36',90),(102,526,92,'好哒','2015-11-09 11:15:42',90),(103,527,92,'？','2015-11-09 11:18:31',92),(104,527,92,'？','2015-11-09 11:24:31',92),(105,528,92,'？','2015-11-09 11:32:09',92),(106,528,92,'？','2015-11-09 11:33:40',92),(107,528,92,'?','2015-11-09 11:36:40',92),(108,527,92,'?','2015-11-09 11:37:38',92),(109,528,92,'?','2015-11-09 11:37:53',92),(110,527,92,'?','2015-11-09 11:39:21',92),(111,528,92,'?','2015-11-09 11:40:29',92),(112,528,92,'?','2015-11-09 11:42:17',92),(113,528,92,'?','2015-11-09 11:43:16',92),(114,528,92,'？','2015-11-09 11:51:14',92),(115,528,92,'？','2015-11-09 11:52:02',92),(116,528,92,'？？','2015-11-09 11:53:25',92),(117,528,92,'？','2015-11-09 11:55:21',92),(118,528,92,'？','2015-11-09 11:56:13',92),(119,528,92,'啥','2015-11-09 11:58:07',92),(120,528,92,'好哒','2015-11-09 11:59:36',92),(121,529,95,'?','2015-11-10 12:54:03',93),(122,530,95,'?','2015-11-10 13:00:57',95),(123,530,95,'？','2015-11-10 13:01:20',95),(124,530,95,'?','2015-11-11 18:49:48',95),(125,530,96,'?','2015-11-11 19:39:17',95),(126,530,96,'？','2015-11-11 19:44:57',95),(127,530,96,'？','2015-11-11 19:57:11',95),(128,530,97,'?','2015-11-11 20:51:59',95),(129,530,97,'?','2015-11-11 20:53:37',95),(130,530,98,'?','2015-11-11 21:08:58',95),(131,530,99,'11','2015-11-11 22:51:40',95),(132,530,97,'?','2015-11-11 22:58:15',95);
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `donate_event`
--

DROP TABLE IF EXISTS `donate_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `donate_event` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from` int(11) NOT NULL,
  `to` int(11) NOT NULL,
  `donate_love_coin` int(11) DEFAULT NULL,
  `donate_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `from_idx` (`from`),
  KEY `to_idx` (`to`),
  CONSTRAINT `donate_event_from_fk` FOREIGN KEY (`from`) REFERENCES `account` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `donate_event_to_fk` FOREIGN KEY (`to`) REFERENCES `account` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `donate_event`
--

LOCK TABLES `donate_event` WRITE;
/*!40000 ALTER TABLE `donate_event` DISABLE KEYS */;
/*!40000 ALTER TABLE `donate_event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `evaluation`
--

DROP TABLE IF EXISTS `evaluation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `evaluation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `event_id` int(11) NOT NULL,
  `from` int(11) NOT NULL,
  `to` int(11) NOT NULL,
  `value` decimal(7,4) NOT NULL DEFAULT '0.0000',
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `event_idx` (`event_id`),
  KEY `to_idx` (`to`),
  KEY `from_idx` (`from`),
  CONSTRAINT `evaluation_eventid_fk` FOREIGN KEY (`event_id`) REFERENCES `event` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `evaluation_from_fk` FOREIGN KEY (`from`) REFERENCES `account` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `evaluation_to_fk` FOREIGN KEY (`to`) REFERENCES `account` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `evaluation`
--

LOCK TABLES `evaluation` WRITE;
/*!40000 ALTER TABLE `evaluation` DISABLE KEYS */;
/*!40000 ALTER TABLE `evaluation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event`
--

DROP TABLE IF EXISTS `event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `event` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `launcher` int(11) NOT NULL,
  `title` varchar(200) DEFAULT NULL,
  `content` varchar(500) DEFAULT NULL,
  `type` int(11) NOT NULL DEFAULT '0',
  `time` datetime DEFAULT NULL,
  `last_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `longitude` decimal(10,7) DEFAULT '999.9999999',
  `latitude` decimal(10,7) DEFAULT '999.9999999',
  `state` int(11) NOT NULL DEFAULT '0',
  `follow_number` int(11) NOT NULL DEFAULT '0',
  `support_number` int(11) NOT NULL DEFAULT '0',
  `group_pts` decimal(7,4) NOT NULL DEFAULT '0.0000',
  `demand_number` int(11) NOT NULL DEFAULT '0',
  `love_coin` int(11) NOT NULL DEFAULT '0',
  `comment` varchar(500) DEFAULT NULL,
  `location` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `launcher_idx` (`launcher`),
  CONSTRAINT `event_launcher_fk` FOREIGN KEY (`launcher`) REFERENCES `account` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=531 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event`
--

LOCK TABLES `event` WRITE;
/*!40000 ALTER TABLE `event` DISABLE KEYS */;
INSERT INTO `event` VALUES (471,72,'aa','as',0,'2015-10-03 19:13:58','2015-10-03 11:13:58',999.9999999,999.9999999,0,0,0,0.0000,0,3,NULL,NULL),(472,72,'aa','aa',0,'2015-10-03 19:14:04','2015-10-03 11:14:04',999.9999999,999.9999999,0,0,0,0.0000,0,3,NULL,NULL),(473,72,'aa','aa',0,'2015-10-03 19:51:01','2015-10-03 11:51:01',999.9999999,999.9999999,0,0,0,0.0000,0,3,NULL,NULL),(474,72,'aaa','bbb',0,'2015-10-05 10:55:16','2015-10-05 02:55:16',999.9999999,999.9999999,0,0,0,0.0000,0,3,NULL,NULL),(475,72,'ccc','ddd',0,'2015-10-06 20:51:10','2015-10-06 12:51:10',999.9999999,999.9999999,0,0,0,0.0000,0,3,NULL,NULL),(476,72,'aaa','bbb',0,'2015-10-20 12:59:25','2015-10-20 04:59:25',999.9999999,999.9999999,0,0,0,0.0000,0,3,NULL,NULL),(477,73,'1','2',0,'2015-10-21 21:24:23','2015-10-21 13:24:23',999.9999999,999.9999999,0,0,0,0.0000,0,3,NULL,NULL),(478,73,'111','222',0,'2015-10-21 21:26:19','2015-10-21 13:26:19',999.9999999,999.9999999,0,0,0,0.0000,0,3,NULL,NULL),(479,73,'1','2',0,'2015-10-21 21:27:17','2015-10-21 13:27:18',999.9999999,999.9999999,0,0,0,0.0000,0,3,NULL,NULL),(480,72,'11','22',0,'2015-10-21 21:29:31','2015-10-21 13:29:31',999.9999999,999.9999999,0,0,0,0.0000,0,1,NULL,NULL),(481,73,'he','he',0,'2015-10-22 02:28:11','2015-10-21 18:28:11',999.9999999,999.9999999,0,0,0,0.0000,0,3,NULL,NULL),(482,73,'aaa','aaaa',0,'2015-10-22 02:32:13','2015-10-21 18:32:13',999.9999999,999.9999999,0,0,0,0.0000,0,3,NULL,NULL),(483,73,'aa','aa',0,'2015-10-22 02:32:20','2015-10-21 18:32:20',999.9999999,999.9999999,0,0,0,0.0000,0,3,NULL,NULL),(484,72,'1111','2222',0,'2015-10-22 10:59:33','2015-10-22 02:59:33',999.9999999,999.9999999,0,0,0,0.0000,0,1,NULL,NULL),(485,73,'11','22',0,'2015-10-22 11:19:24','2015-10-22 03:19:24',999.9999999,999.9999999,0,0,0,0.0000,0,2,NULL,NULL),(486,74,'11','22',0,'2015-10-22 11:44:51','2015-10-22 03:44:51',999.9999999,999.9999999,0,0,0,0.0000,0,3,NULL,NULL),(487,74,'11','22',0,'2015-10-22 11:45:02','2015-10-22 03:45:02',999.9999999,999.9999999,0,0,0,0.0000,0,0,NULL,NULL),(488,74,'11','22',0,'2015-10-22 12:02:26','2015-10-22 04:02:26',999.9999999,999.9999999,0,0,0,0.0000,0,3,NULL,NULL),(489,74,'11','22',0,'2015-10-22 12:02:51','2015-10-22 04:02:51',999.9999999,999.9999999,0,0,0,0.0000,0,3,NULL,NULL),(490,74,'11111111','222222222',0,'2015-10-22 12:03:01','2015-10-22 04:03:01',999.9999999,999.9999999,0,0,0,0.0000,0,3,NULL,NULL),(491,74,'11','22',0,'2015-10-22 12:20:44','2015-10-22 04:20:44',999.9999999,999.9999999,0,0,0,0.0000,0,3,NULL,NULL),(492,74,'11','22',0,'2015-10-22 12:21:06','2015-10-22 04:21:07',999.9999999,999.9999999,0,0,0,0.0000,0,3,NULL,NULL),(493,74,'11','11',0,'2015-10-22 12:29:53','2015-10-22 04:29:53',999.9999999,999.9999999,0,0,0,0.0000,0,0,NULL,NULL),(494,74,'11','11',0,'2015-10-22 12:30:10','2015-10-22 04:30:10',999.9999999,999.9999999,0,0,0,0.0000,0,2,NULL,NULL),(495,75,'aa','aaa',0,'2015-10-23 00:39:07','2015-10-22 16:39:07',999.9999999,999.9999999,0,0,0,0.0000,0,0,NULL,NULL),(496,75,'11','11',0,'2015-10-23 03:24:01','2015-10-22 19:24:01',999.9999999,999.9999999,0,0,0,0.0000,0,0,NULL,NULL),(497,75,'中山大学','中山',0,'2015-10-23 03:24:36','2015-10-22 19:24:36',999.9999999,999.9999999,0,0,0,0.0000,0,0,NULL,NULL),(498,75,NULL,NULL,0,'2015-10-23 03:28:57','2015-10-22 19:28:57',999.9999999,999.9999999,0,0,0,0.0000,0,0,NULL,NULL),(499,75,'aaaaa','aa',0,'2015-10-23 03:29:21','2015-10-22 19:29:22',999.9999999,999.9999999,0,0,0,0.0000,0,0,NULL,NULL),(500,75,NULL,NULL,0,'2015-10-23 03:29:50','2015-10-22 19:29:50',999.9999999,999.9999999,0,0,0,0.0000,0,0,NULL,NULL),(501,75,'中山大学','软件学院',0,'2015-10-23 03:36:02','2015-10-22 19:36:02',999.9999999,999.9999999,0,0,0,0.0000,0,0,NULL,NULL),(502,75,'数据科学与计算机学院','中山大学',0,'2015-10-23 03:38:47','2015-10-22 19:38:48',999.9999999,999.9999999,0,0,0,0.0000,0,0,NULL,NULL),(503,75,'中山大学','中山',0,'2015-10-23 03:54:25','2015-10-22 19:54:25',999.9999999,999.9999999,0,0,0,0.0000,0,0,NULL,NULL),(504,75,'软件学院','数据学院',0,'2015-10-23 03:56:04','2015-10-22 19:56:04',999.9999999,999.9999999,0,0,0,0.0000,0,0,NULL,NULL),(505,75,'中山大学','中山大学',0,'2015-10-23 04:00:40','2015-10-22 20:00:40',999.9999999,999.9999999,0,0,0,0.0000,0,0,NULL,NULL),(506,75,'中山大学2','中山大学',0,'2015-10-23 04:04:10','2015-10-22 20:04:11',999.9999999,999.9999999,0,0,0,0.0000,0,0,NULL,NULL),(507,75,'中山大学3','中山大学',0,'2015-10-23 04:37:22','2015-10-22 20:37:22',999.9999999,999.9999999,0,0,0,0.0000,0,0,NULL,NULL),(508,75,'软件学院','软件工程',0,'2015-10-23 19:24:45','2015-10-23 11:24:45',999.9999999,999.9999999,0,0,0,0.0000,0,0,NULL,NULL),(509,75,'软件学院','软件工程实习',0,'2015-10-23 19:25:27','2015-10-23 11:25:27',999.9999999,999.9999999,0,0,0,0.0000,0,0,NULL,NULL),(510,75,'aa','aaaaa',0,'2015-10-23 20:07:18','2015-10-23 12:07:19',999.9999999,999.9999999,0,0,0,0.0000,0,16,NULL,NULL),(511,75,'aa','aa',0,'2015-10-23 20:15:53','2015-10-23 12:15:53',999.9999999,999.9999999,0,0,0,0.0000,0,0,NULL,NULL),(512,73,'中山大学','软件学院',0,'2015-10-23 21:04:34','2015-10-23 13:04:35',999.9999999,999.9999999,0,0,0,0.0000,0,0,NULL,NULL),(513,72,'aa','aaa',0,'2015-10-24 17:08:22','2015-10-24 09:08:22',999.9999999,999.9999999,0,0,0,0.0000,0,0,NULL,NULL),(514,73,'11','11',0,'2015-10-25 01:52:18','2015-10-24 17:52:18',999.9999999,999.9999999,0,0,0,0.0000,0,0,NULL,NULL),(515,75,'11','11',0,'2015-10-25 10:22:46','2015-10-25 02:22:46',999.9999999,999.9999999,0,0,0,0.0000,0,0,NULL,NULL),(516,80,'这是什么呢','是吧 哈哈哈哈哈哈哈哈  是的 啊啊啊啊 啊 啊',0,'2015-11-06 23:54:37','2015-11-06 15:54:37',999.9999999,999.9999999,0,0,0,0.0000,0,3,NULL,NULL),(517,73,'哈哈','打底',0,'2015-11-07 22:11:17','2015-11-07 14:11:17',999.9999999,999.9999999,0,0,0,0.0000,0,0,NULL,NULL),(518,87,'你好吗','哈哈',0,'2015-11-07 23:26:07','2015-11-07 15:26:07',999.9999999,999.9999999,0,0,0,0.0000,0,3,NULL,NULL),(519,72,'','',0,'2015-11-08 03:01:47','2015-11-07 19:01:47',999.9999999,999.9999999,0,0,0,0.0000,0,0,NULL,NULL),(520,72,'哈哈','什么',0,'2015-11-08 03:03:26','2015-11-07 19:03:26',999.9999999,999.9999999,0,0,0,0.0000,0,0,NULL,NULL),(521,91,'在吗','？',0,'2015-11-09 10:17:49','2015-11-09 02:17:50',999.9999999,999.9999999,0,0,0,0.0000,0,0,NULL,NULL),(522,91,'什么啊','哈哈',0,'2015-11-09 10:30:59','2015-11-09 02:31:00',999.9999999,999.9999999,0,0,0,0.0000,0,3,NULL,NULL),(523,91,'嗯嗯','好吧',0,'2015-11-09 10:32:08','2015-11-09 02:32:09',999.9999999,999.9999999,0,0,0,0.0000,0,3,NULL,NULL),(524,91,'嗯嗯的','what',0,'2015-11-09 10:34:46','2015-11-09 02:34:47',999.9999999,999.9999999,0,0,0,0.0000,0,1,NULL,NULL),(525,90,'不是吧','你说',0,'2015-11-09 11:00:54','2015-11-09 03:00:54',999.9999999,999.9999999,0,0,0,0.0000,0,3,NULL,NULL),(526,90,'这里是易组的官方告知','嗯嗯嗯嗯是的',0,'2015-11-09 11:09:38','2015-11-09 03:09:38',999.9999999,999.9999999,0,0,0,0.0000,0,2,NULL,NULL),(527,92,'易组更新版','嗯嗯嗯',0,'2015-11-09 11:16:19','2015-11-09 03:16:19',999.9999999,999.9999999,0,0,0,0.0000,0,1,NULL,NULL),(528,92,'易助','嗯嗯',0,'2015-11-09 11:21:46','2015-11-09 03:21:46',999.9999999,999.9999999,0,0,0,0.0000,0,1,NULL,NULL),(529,93,'what','??/',0,'2015-11-09 23:21:53','2015-11-09 15:21:54',999.9999999,999.9999999,0,0,0,0.0000,0,3,NULL,NULL),(530,95,'haha','haode',0,'2015-11-10 12:54:12','2015-11-10 04:54:12',999.9999999,999.9999999,0,0,0,0.0000,0,3,NULL,NULL);
/*!40000 ALTER TABLE `event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `health`
--

DROP TABLE IF EXISTS `health`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `health` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `height` int(11) DEFAULT NULL,
  `weight` int(11) DEFAULT NULL,
  `blood_type` varchar(10) DEFAULT NULL,
  `medicine_taken` varchar(500) DEFAULT NULL,
  `medical_history` varchar(500) DEFAULT NULL,
  `anaphylaxis` varchar(500) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_uni` (`user_id`),
  KEY `user_idx` (`user_id`),
  CONSTRAINT `health_userid_fk` FOREIGN KEY (`user_id`) REFERENCES `account` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `health`
--

LOCK TABLES `health` WRITE;
/*!40000 ALTER TABLE `health` DISABLE KEYS */;
/*!40000 ALTER TABLE `health` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `illness`
--

DROP TABLE IF EXISTS `illness`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `illness` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `content` varchar(45) DEFAULT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_idx` (`user_id`),
  CONSTRAINT `illness_userid_fk` FOREIGN KEY (`user_id`) REFERENCES `account` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `illness`
--

LOCK TABLES `illness` WRITE;
/*!40000 ALTER TABLE `illness` DISABLE KEYS */;
/*!40000 ALTER TABLE `illness` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loving_bank`
--

DROP TABLE IF EXISTS `loving_bank`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `loving_bank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) NOT NULL,
  `score_rank` int(11) NOT NULL DEFAULT '0',
  `score_exchange` int(11) NOT NULL DEFAULT '0',
  `love_coin` int(11) NOT NULL DEFAULT '0',
  `family_love_coin` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `userid_idx` (`userid`),
  CONSTRAINT `loving_bank_userid_fk` FOREIGN KEY (`userid`) REFERENCES `account` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loving_bank`
--

LOCK TABLES `loving_bank` WRITE;
/*!40000 ALTER TABLE `loving_bank` DISABLE KEYS */;
INSERT INTO `loving_bank` VALUES (34,72,0,20,0,0),(35,73,0,20,0,0),(36,74,0,20,0,0),(37,75,0,16,4,0),(38,76,0,0,20,0),(39,77,0,0,20,0),(40,78,0,0,20,0),(41,79,0,0,20,0),(42,80,0,3,17,0),(43,81,0,0,20,0),(44,82,0,0,20,0),(45,83,0,0,20,0),(46,84,0,0,20,0),(47,85,0,0,20,0),(48,86,0,0,20,0),(49,87,0,3,17,0),(50,88,0,0,20,0),(51,89,0,0,20,0),(52,90,0,5,15,0),(53,91,0,7,13,0),(54,92,0,2,18,0),(55,93,0,3,17,0),(56,94,0,0,20,0),(57,95,0,3,17,0),(58,96,0,0,20,0),(59,97,0,0,20,0),(60,98,0,0,20,0),(61,99,0,0,20,0);
/*!40000 ALTER TABLE `loving_bank` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sign_in`
--

DROP TABLE IF EXISTS `sign_in`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sign_in` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_idx` (`user_id`),
  CONSTRAINT `sign_in_user_fk` FOREIGN KEY (`user_id`) REFERENCES `account` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sign_in`
--

LOCK TABLES `sign_in` WRITE;
/*!40000 ALTER TABLE `sign_in` DISABLE KEYS */;
/*!40000 ALTER TABLE `sign_in` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `static_relation`
--

DROP TABLE IF EXISTS `static_relation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `static_relation` (
  `user_a` int(11) NOT NULL,
  `user_b` int(11) NOT NULL,
  `type` int(11) NOT NULL DEFAULT '0',
  `time` datetime DEFAULT NULL,
  PRIMARY KEY (`user_a`,`user_b`),
  KEY `relation_userb_fk` (`user_b`),
  KEY `relation_usera_fk` (`user_a`),
  CONSTRAINT `relation_usera_fk` FOREIGN KEY (`user_a`) REFERENCES `account` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `relation_userb_fk` FOREIGN KEY (`user_b`) REFERENCES `account` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `static_relation`
--

LOCK TABLES `static_relation` WRITE;
/*!40000 ALTER TABLE `static_relation` DISABLE KEYS */;
/*!40000 ALTER TABLE `static_relation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `support_relation`
--

DROP TABLE IF EXISTS `support_relation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `support_relation` (
  `event_id` int(11) NOT NULL,
  `supportee` int(11) NOT NULL,
  `supporter` int(11) NOT NULL,
  `type` int(11) NOT NULL DEFAULT '0',
  `time` datetime NOT NULL,
  PRIMARY KEY (`supporter`, `supportee`, `event_id`),
  KEY `relation_supportee_fk` (`supportee`),
  KEY `relation_supporter_fk` (`supporter`),
  KEY `relation_event_id_fk` (`event_id`),
  CONSTRAINT `relation_eventid_fk` FOREIGN KEY (`event_id`) REFERENCES `event` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `relation_supportee_fk` FOREIGN KEY (`supportee`) REFERENCES `account` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `relation_supporter_fk` FOREIGN KEY (`supporter`) REFERENCES `account` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `support_relation`
--

LOCK TABLES `support_relation` WRITE;
/*!40000 ALTER TABLE `support_relation` DISABLE KEYS */;
/*!40000 ALTER TABLE `support_relation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `nickname` varchar(45) DEFAULT NULL,
  `gender` int(11) DEFAULT '1',
  `age` int(11) DEFAULT '0',
  `phone` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `location` varchar(45) DEFAULT NULL,
  `longitude` decimal(10,7) DEFAULT '999.9999999',
  `latitude` decimal(10,7) DEFAULT '999.9999999',
  `occupation` int(11) DEFAULT '0',
  `reputation` decimal(7,4) DEFAULT '0.0000',
  `avatar` varchar(200) DEFAULT NULL,
  `identity_id` varchar(45) DEFAULT NULL,
  `type` int(11) DEFAULT '0',
  `isVerify` tinyint(4) DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `nickname` (`nickname`),
  CONSTRAINT `user_id_fk` FOREIGN KEY (`id`) REFERENCES `account` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (72,'啊啊啊','aaa',1,0,'18826234601','535802703%40qq.com',NULL,999.9999999,999.9999999,0,0.0000,'C:workprojectstaticimagesheadaaa.png','11111111',0,1),(73,'符永宁','111',1,0,'11111111111','535802703%40qq.com',NULL,999.9999999,999.9999999,0,0.0000,'C:workprojectstaticimageshead111.png','4600000000000000',0,1),(74,'aaaaaaaaaaaaaaaaaaaaaa','222',1,0,'18826211111','535802703%40qq.com',NULL,999.9999999,999.9999999,0,0.0000,'C:workprojectstaticimageshead222.png','4600000000000000',0,1),(75,NULL,'333',1,0,'11','535802703%40qq.com',NULL,999.9999999,999.9999999,0,0.0000,NULL,NULL,0,0),(76,'aaaaaaaaaa','zzz',1,0,'18826211111','535802703%40qq.com',NULL,999.9999999,999.9999999,0,0.0000,'C:workprojectstaticimagesheadzzz.png','11111111111111111111',0,1),(77,NULL,'xxx',1,0,'1111111','535802703%40qq.com',NULL,999.9999999,999.9999999,0,0.0000,NULL,NULL,0,0),(78,NULL,'ccc',1,0,'111111111','535802703%40qq.com',NULL,999.9999999,999.9999999,0,0.0000,NULL,NULL,0,0),(79,NULL,'vvv',1,0,'1111','535802703%40qq.com',NULL,999.9999999,999.9999999,0,0.0000,NULL,NULL,0,0),(80,'符永宁','bbb',1,0,'111111','535802703%40qq.com',NULL,999.9999999,999.9999999,0,0.0000,'C:workprojectstaticimagesheadbb.png','4600000000000000',0,1),(81,NULL,'nnn',1,0,'1111111','535802703%40qq.com',NULL,999.9999999,999.9999999,0,0.0000,NULL,NULL,0,0),(82,'bbbb','rrr',1,0,'111','535802703%40qq.com',NULL,999.9999999,999.9999999,0,0.0000,'C:workprojectstaticimageshead\rrr.png','11111111111111111111',0,1),(83,'符永宁','zxc',1,0,'111111','535802703%40qq.com',NULL,999.9999999,999.9999999,0,0.0000,'C:workprojectstaticimagesheadzxc.png','4600000000000000',0,1),(84,NULL,'q',1,0,'1111','535802703%40qq.com',NULL,999.9999999,999.9999999,0,0.0000,NULL,NULL,0,0),(85,'符永宁','t',1,0,'111','535802703%40qq.com',NULL,999.9999999,999.9999999,0,0.0000,'C:workprojectstaticimageshead	.png','4600000000000000',0,1),(86,NULL,'yyy',1,0,'111','535802703%40qq.com',NULL,999.9999999,999.9999999,0,0.0000,NULL,NULL,0,0),(87,'符永宁','1',1,0,'111','535802703%40qq.com',NULL,999.9999999,999.9999999,0,0.0000,'87.png','460002199312114111',0,1),(88,'符永宁','2',1,0,'11','535802703%40qq.com',NULL,999.9999999,999.9999999,0,0.0000,'C:work	estprojectstaticimageshead2.png','460002199312114111',0,1),(89,'符永宁','3',1,0,'111','535802703%40qq.com',NULL,999.9999999,999.9999999,0,0.0000,'C:work	estprojectstaticimageshead3.png','460002199312114111',0,1),(90,'符永宁','4',1,0,'18826211111','535802703%40qq.com',NULL,999.9999999,999.9999999,0,0.0000,'90.png','460002000000114111',0,1),(91,'符永宁','5',1,0,'111','535802703%40qq.com',NULL,999.9999999,999.9999999,0,0.0000,'91.png','460002000000114111',0,1),(92,'符永宁','6',1,0,'18826211111','535802703%40qq.com',NULL,999.9999999,999.9999999,0,0.0000,'92.png','460002000000114111',0,1),(93,'符永宁','7',1,0,'111111','535802703@qq.com',NULL,999.9999999,999.9999999,0,0.0000,'93.png','460002000000114111',0,1),(94,NULL,'8',1,0,'11111','535802703%40qq.com',NULL,999.9999999,999.9999999,0,0.0000,NULL,NULL,0,0),(95,'符永宁','10',1,0,'11111','535802703@qq.com',NULL,999.9999999,999.9999999,0,0.0000,'95.png','460002000000114111',0,1),(96,'符永宁','11',1,0,'18826234111','535802703@qq.com',NULL,999.9999999,999.9999999,0,0.0000,'96.png','460002197704015615',0,1),(97,'符永宁','12',1,0,'111','535802703%40qq.com',NULL,999.9999999,999.9999999,0,0.0000,'97.png','460002197704015615',0,1),(98,'符永宁','13',1,0,'111','535802703@qq.com',NULL,999.9999999,999.9999999,0,0.0000,'ed3d2c21991e3bef5e069713af9fa6ca.png','460002197704015615',0,1),(99,'符永宁','14',1,0,'1111111111','535802703%40qq.com',NULL,999.9999999,999.9999999,0,0.0000,'ac627ab1ccbdb62ec96e702f07f6425b.png','460002197704015615',0,1);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_extension`
--

DROP TABLE IF EXISTS `user_extension`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_extension` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userId` int(11) NOT NULL,
  `checkIn` int(11) DEFAULT '0',
  `concernNum` int(11) DEFAULT '0',
  `name` varchar(45) DEFAULT NULL,
  `profiles` mediumblob,
  PRIMARY KEY (`id`),
  KEY `extension_id_fk` (`userId`),
  CONSTRAINT `extension_id_fk` FOREIGN KEY (`userId`) REFERENCES `account` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_extension`
--

LOCK TABLES `user_extension` WRITE;
/*!40000 ALTER TABLE `user_extension` DISABLE KEYS */;
INSERT INTO `user_extension` VALUES (1,72,0,0,NULL,NULL),(2,73,0,0,NULL,NULL),(3,74,0,0,NULL,NULL),(4,75,0,0,NULL,NULL),(5,76,0,0,NULL,NULL),(6,77,0,0,NULL,NULL),(7,78,0,0,NULL,NULL),(8,79,0,0,NULL,NULL),(9,80,0,0,NULL,NULL),(10,81,0,0,NULL,NULL),(11,82,0,0,NULL,NULL),(12,83,0,0,NULL,NULL),(13,84,0,0,NULL,NULL),(14,85,0,0,NULL,NULL),(15,86,0,0,NULL,NULL),(16,87,0,0,NULL,NULL),(17,88,0,0,NULL,NULL),(18,89,0,0,NULL,NULL),(19,90,0,0,NULL,NULL),(20,91,0,0,NULL,NULL),(21,92,0,0,NULL,NULL),(22,93,0,0,NULL,NULL),(23,94,0,0,NULL,NULL),(24,95,0,0,NULL,NULL),(25,96,0,0,NULL,NULL),(26,97,0,0,NULL,NULL),(27,98,0,0,NULL,NULL),(28,99,0,0,NULL,NULL);
/*!40000 ALTER TABLE `user_extension` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `verify_email`
--

DROP TABLE IF EXISTS `verify_email`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `verify_email` (
  `id` int(11) NOT NULL,
  `email` varchar(45) NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `idencode` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `verify_email`
--

LOCK TABLES `verify_email` WRITE;
/*!40000 ALTER TABLE `verify_email` DISABLE KEYS */;
INSERT INTO `verify_email` VALUES (97,'535802703%40qq.com','2015-11-11 14:49:21','RvMP');
/*!40000 ALTER TABLE `verify_email` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `verify_user`
--

DROP TABLE IF EXISTS `verify_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `verify_user` (
  `id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `identity_id` varchar(45) NOT NULL,
  `avatar` varchar(200) NOT NULL,
  `status` varchar(10) NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `idencode` varchar(5) NOT NULL,
  `email` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `verify_user`
--

LOCK TABLES `verify_user` WRITE;
/*!40000 ALTER TABLE `verify_user` DISABLE KEYS */;
INSERT INTO `verify_user` VALUES (94,'符永宁','460002000000114111','94.png','wait','2015-11-09 16:04:19','UmqS','535802703%40qq.com'),(93,'符永宁','460002000000114111','93.png','wait','2015-11-09 16:06:33','sGQy','535802703@qq.com');
/*!40000 ALTER TABLE `verify_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-11-14  0:47:24
