CREATE DATABASE `BookStoreDB` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

CREATE TABLE `Books` (
  `Genre` varchar(128) DEFAULT 'unknown',
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Title` varchar(128) DEFAULT NULL,
  `Author` varchar(50) DEFAULT NULL,
  `Price` bigint(20) DEFAULT NULL,
  `Supplier_Id` bigint(20) DEFAULT NULL,
  `Description` text DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1184 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `Orders` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `customer_id` bigint(20) NOT NULL,
  `date` datetime DEFAULT NULL,
  `orderStatus` enum('ordered','processessing','shipped') DEFAULT NULL,
  `totalPrice` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Orders_Customers_FK` (`customer_id`),
  CONSTRAINT `Orders_Customers_FK` FOREIGN KEY (`customer_id`) REFERENCES `Users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=445 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `Reviews` (
  `Book_Id` bigint(20) DEFAULT NULL,
  `Score` varchar(100) DEFAULT NULL,
  `Title` varchar(100) DEFAULT NULL,
  `Body_Text` varchar(1000) DEFAULT NULL,
  `User_Id` bigint(20) DEFAULT NULL,
  `Date` datetime DEFAULT NULL,
  `Review_Id` bigint(20) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`Review_Id`),
  KEY `Reviews_Books_FK` (`Book_Id`),
  KEY `Reviews_Customers_FK` (`User_Id`),
  CONSTRAINT `Reviews_Books_FK` FOREIGN KEY (`Book_Id`) REFERENCES `Books` (`id`),
  CONSTRAINT `Reviews_Customers_FK` FOREIGN KEY (`User_Id`) REFERENCES `Users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `Suppliers` (
  `Supplier_Id` bigint(20) NOT NULL AUTO_INCREMENT,
  `companyName` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `Phone` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Supplier_Id`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `Users` (
  `Name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `Password` varchar(100) DEFAULT NULL,
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `Address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=628 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

CREATE TABLE `orderItems` (
  `orderItem_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `quantity` int(11) DEFAULT NULL,
  `order_id` bigint(20) DEFAULT NULL,
  `book_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`orderItem_id`),
  KEY `orderItems_Books_FK` (`book_id`),
  KEY `orderItems_Orders_FK` (`order_id`),
  CONSTRAINT `orderItems_Books_FK` FOREIGN KEY (`book_id`) REFERENCES `Books` (`id`),
  CONSTRAINT `orderItems_Orders_FK` FOREIGN KEY (`order_id`) REFERENCES `Orders` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=696 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;