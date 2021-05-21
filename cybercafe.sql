/*
 Navicat MySQL Data Transfer

 Source Server         : asd
 Source Server Type    : MySQL
 Source Server Version : 80011
 Source Host           : localhost:3306
 Source Schema         : cybercafe

 Target Server Type    : MySQL
 Target Server Version : 80011
 File Encoding         : 65001

 Date: 18/06/2019 09:59:04
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for bill
-- ----------------------------
DROP TABLE IF EXISTS `bill`;
CREATE TABLE `bill`  (
  `B_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Start_Time` datetime(0) NULL DEFAULT NULL,
  `End_Time` datetime(0) NULL DEFAULT NULL,
  `Total_Amount` float NULL DEFAULT NULL,
  `Card_ID` int(11) NULL DEFAULT NULL,
  `PC_ID` int(11) NULL DEFAULT NULL,
  `Staff` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`B_ID`) USING BTREE,
  INDEX `Card_ID`(`Card_ID`) USING BTREE,
  INDEX `PC_ID`(`PC_ID`) USING BTREE,
  INDEX `Staff`(`Staff`) USING BTREE,
  CONSTRAINT `bill_ibfk_1` FOREIGN KEY (`Card_ID`) REFERENCES `card` (`card_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `bill_ibfk_2` FOREIGN KEY (`PC_ID`) REFERENCES `computer` (`pc_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `bill_ibfk_3` FOREIGN KEY (`Staff`) REFERENCES `staff` (`staff_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 9016 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of bill
-- ----------------------------
INSERT INTO `bill` VALUES (9001, '2019-06-04 19:19:04', '2019-06-04 22:18:23', 10.5, 20170233, 10002, 140217);
INSERT INTO `bill` VALUES (9002, '2019-06-04 19:24:21', '2019-06-04 23:23:32', 14, 20170234, 10003, 140217);
INSERT INTO `bill` VALUES (9003, '2019-06-05 08:25:28', '2019-06-05 14:21:37', 30, 20170592, 10008, 140219);
INSERT INTO `bill` VALUES (9004, '2019-06-05 09:12:59', '2019-06-05 13:09:15', 24, 20170237, 10012, 140219);
INSERT INTO `bill` VALUES (9005, '2019-06-05 11:28:15', '2019-06-05 17:26:26', 36, 20162623, 10011, 140219);
INSERT INTO `bill` VALUES (9006, '2019-06-05 14:29:32', '2019-06-05 18:26:42', 14, 20170456, 10001, 140222);
INSERT INTO `bill` VALUES (9007, '2019-06-06 07:41:54', '2019-06-06 19:31:11', 42, 20170562, 10003, 140223);
INSERT INTO `bill` VALUES (9008, '2019-06-06 12:32:48', '2019-06-09 17:29:56', 25, 20174526, 10007, 140218);
INSERT INTO `bill` VALUES (9009, '2019-06-06 18:33:43', '2019-06-06 22:25:48', 24, 20173265, 10013, 140221);
INSERT INTO `bill` VALUES (9010, '2019-06-12 07:07:00', '2019-06-12 09:04:00', 10, 20170233, 10008, 140218);
INSERT INTO `bill` VALUES (9011, '2019-06-12 18:39:00', '2019-06-12 19:11:00', 6, 20170592, 10013, 140222);
INSERT INTO `bill` VALUES (9012, '2019-06-14 13:07:00', NULL, NULL, 20170233, 10001, 140223);
INSERT INTO `bill` VALUES (9013, '2019-06-14 17:10:00', NULL, NULL, 20170456, 10003, 140223);
INSERT INTO `bill` VALUES (9014, '2019-06-15 20:06:00', NULL, NULL, 20170285, 10007, 140218);
INSERT INTO `bill` VALUES (9015, '2019-06-16 10:09:00', NULL, NULL, 20170562, 10008, 140221);

-- ----------------------------
-- Table structure for card
-- ----------------------------
DROP TABLE IF EXISTS `card`;
CREATE TABLE `card`  (
  `Card_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Password` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Using_Status` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Checkout_Status` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Account_Balance` float NULL DEFAULT NULL,
  `C_ID` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`Card_ID`) USING BTREE,
  INDEX `C_ID`(`C_ID`) USING BTREE,
  INDEX `Card_ID`(`Card_ID`) USING BTREE,
  CONSTRAINT `card_ibfk_1` FOREIGN KEY (`C_ID`) REFERENCES `customer` (`c_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 20186257 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of card
-- ----------------------------
INSERT INTO `card` VALUES (20161556, 'wutongyu123', 'Free', 'Paid', 22.6, 1009);
INSERT INTO `card` VALUES (20162623, 'liuyiliang123', 'Free', 'Paid', 32.6, 1012);
INSERT INTO `card` VALUES (20170227, 'daiyijun123', 'Using', 'Unpaid', 12.6, 1007);
INSERT INTO `card` VALUES (20170233, 'hhy123', 'Using', 'Unpaid', 29.7, 1001);
INSERT INTO `card` VALUES (20170234, 'guoxu123', 'Using', 'Unpaid', 11.6, 1003);
INSERT INTO `card` VALUES (20170236, 'yangling123', 'Free', 'Paid', 14.3, 1002);
INSERT INTO `card` VALUES (20170237, 'liyanlin123', 'Free', 'Unpaid', 30.5, 1004);
INSERT INTO `card` VALUES (20170285, 'liuziwen123', 'Using', 'Unpaid', 19.4, 1005);
INSERT INTO `card` VALUES (20170456, 'fangxiaomeng123', 'Using', 'Unpaid', 11.8, 1010);
INSERT INTO `card` VALUES (20170562, 'yangzhaoqian123', 'Using', 'Unpaid', 48.2, 1006);
INSERT INTO `card` VALUES (20170592, 'lvzixuan123', 'Free', 'Paid', 14.6, 1013);
INSERT INTO `card` VALUES (20173265, 'gaolei123', 'Using', 'Unpaid', 26.3, 1011);
INSERT INTO `card` VALUES (20174526, 'lirui123', 'Free', 'Paid', 2.1, 1008);
INSERT INTO `card` VALUES (20183966, '123456', 'Free', 'Paid', 7.7, 1014);

-- ----------------------------
-- Table structure for computer
-- ----------------------------
DROP TABLE IF EXISTS `computer`;
CREATE TABLE `computer`  (
  `PC_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Price_per_hour` float NOT NULL,
  `Card_ID` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`PC_ID`) USING BTREE,
  INDEX `Card_ID`(`Card_ID`) USING BTREE,
  CONSTRAINT `Card_ID` FOREIGN KEY (`Card_ID`) REFERENCES `card` (`card_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 10015 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of computer
-- ----------------------------
INSERT INTO `computer` VALUES (10001, 3.5, 20170233);
INSERT INTO `computer` VALUES (10002, 3.5, NULL);
INSERT INTO `computer` VALUES (10003, 3.5, 20170456);
INSERT INTO `computer` VALUES (10004, 3.5, NULL);
INSERT INTO `computer` VALUES (10005, 3.5, NULL);
INSERT INTO `computer` VALUES (10006, 5, NULL);
INSERT INTO `computer` VALUES (10007, 5, 20170285);
INSERT INTO `computer` VALUES (10008, 5, 20170562);
INSERT INTO `computer` VALUES (10009, 5, NULL);
INSERT INTO `computer` VALUES (10010, 5, NULL);
INSERT INTO `computer` VALUES (10011, 6, NULL);
INSERT INTO `computer` VALUES (10012, 6, NULL);
INSERT INTO `computer` VALUES (10013, 6, NULL);
INSERT INTO `computer` VALUES (10014, 6.5, NULL);

-- ----------------------------
-- Table structure for customer
-- ----------------------------
DROP TABLE IF EXISTS `customer`;
CREATE TABLE `customer`  (
  `C_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Cname` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Age` int(11) NOT NULL,
  `Gender` varchar(7) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`C_ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2425 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of customer
-- ----------------------------
INSERT INTO `customer` VALUES (1001, '胡寒阳', 19, 'Male');
INSERT INTO `customer` VALUES (1002, '杨令', 20, 'Male');
INSERT INTO `customer` VALUES (1003, '郭旭', 20, 'Male');
INSERT INTO `customer` VALUES (1004, '李彦霖', 20, 'Male');
INSERT INTO `customer` VALUES (1005, '刘子文', 19, 'Female');
INSERT INTO `customer` VALUES (1006, '杨肇谦', 20, 'Male');
INSERT INTO `customer` VALUES (1007, '戴怡君', 19, 'Female');
INSERT INTO `customer` VALUES (1008, '李睿', 20, 'Female');
INSERT INTO `customer` VALUES (1009, '吴侗雨', 22, 'Male');
INSERT INTO `customer` VALUES (1010, '方晓萌', 19, 'Male');
INSERT INTO `customer` VALUES (1011, '高磊', 20, 'Male');
INSERT INTO `customer` VALUES (1012, '刘义良', 20, 'Male');
INSERT INTO `customer` VALUES (1013, '吕子萱', 20, 'Female');
INSERT INTO `customer` VALUES (1014, '吴承昱', 18, 'Female');

-- ----------------------------
-- Table structure for order_t
-- ----------------------------
DROP TABLE IF EXISTS `order_t`;
CREATE TABLE `order_t`  (
  `Order_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Card_ID` int(11) NULL DEFAULT NULL,
  `Order_Time` datetime(0) NULL DEFAULT NULL,
  `S_ID` int(11) NULL DEFAULT NULL,
  `Quantity` int(11) NOT NULL,
  `Amount` int(11) NOT NULL,
  `Order_Status` varchar(12) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`Order_ID`) USING BTREE,
  INDEX `Card_ID`(`Card_ID`) USING BTREE,
  INDEX `S_ID`(`S_ID`) USING BTREE,
  CONSTRAINT `order_t_ibfk_1` FOREIGN KEY (`Card_ID`) REFERENCES `card` (`card_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `order_t_ibfk_2` FOREIGN KEY (`S_ID`) REFERENCES `snacks` (`s_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 7011 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of order_t
-- ----------------------------
INSERT INTO `order_t` VALUES (7001, 20170233, '2019-06-04 20:39:55', 2, 3, 12, 'Finished');
INSERT INTO `order_t` VALUES (7002, 20170237, '2019-06-05 11:43:09', 3, 1, 5, 'Finished');
INSERT INTO `order_t` VALUES (7003, 20162623, '2019-06-05 16:44:13', 6, 8, 4, 'Finished');
INSERT INTO `order_t` VALUES (7004, 20174526, '2019-06-09 15:45:32', 5, 2, 4, 'Finished');
INSERT INTO `order_t` VALUES (7005, 20170592, '2019-06-12 16:40:45', 4, 2, 8, 'Finished');
INSERT INTO `order_t` VALUES (7006, 20170233, '2019-06-13 11:51:52', 1, 1, 6, 'Finished');
INSERT INTO `order_t` VALUES (7007, 20170456, '2019-06-13 11:53:54', 5, 2, 4, 'Finished');
INSERT INTO `order_t` VALUES (7008, 20170233, '2019-06-14 19:14:55', 3, 3, 15, 'Finished');
INSERT INTO `order_t` VALUES (7009, 20170233, '2019-06-14 19:35:19', 4, 1, 4, 'Unfinished');
INSERT INTO `order_t` VALUES (7010, 20170233, '2019-06-16 10:30:30', 3, 3, 15, 'Unfinished');

-- ----------------------------
-- Table structure for snacks
-- ----------------------------
DROP TABLE IF EXISTS `snacks`;
CREATE TABLE `snacks`  (
  `S_ID` int(11) NOT NULL AUTO_INCREMENT,
  `SName` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `SPrice` float NOT NULL,
  `Snack_Status` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`S_ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of snacks
-- ----------------------------
INSERT INTO `snacks` VALUES (1, '薯片', 5.5, 'Saleout');
INSERT INTO `snacks` VALUES (2, '可乐', 4, 'Onsale');
INSERT INTO `snacks` VALUES (3, '方便面', 5, 'Onsale');
INSERT INTO `snacks` VALUES (4, '雪碧', 4, 'Onsale');
INSERT INTO `snacks` VALUES (5, '矿泉水', 2, 'Onsale');
INSERT INTO `snacks` VALUES (6, '辣条', 0.5, 'Onsale');
INSERT INTO `snacks` VALUES (7, '火腿肠', 1.5, 'Saleout');
INSERT INTO `snacks` VALUES (8, '果汁', 3.5, 'Onsale');

-- ----------------------------
-- Table structure for staff
-- ----------------------------
DROP TABLE IF EXISTS `staff`;
CREATE TABLE `staff`  (
  `Staff_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Staff_Name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Staff_Age` int(11) NOT NULL,
  `Staff_Gender` varchar(7) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `Password` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`Staff_ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 140225 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of staff
-- ----------------------------
INSERT INTO `staff` VALUES (140217, '张三', 30, 'Male', 'zhangsan123');
INSERT INTO `staff` VALUES (140218, '李四', 25, 'Male', 'lisi1234');
INSERT INTO `staff` VALUES (140219, '王五', 24, 'Female', 'wangwu123');
INSERT INTO `staff` VALUES (140220, '赵六', 28, 'Male', 'zhaoliu123');
INSERT INTO `staff` VALUES (140221, '孙七', 21, 'Female', 'sunqi123');
INSERT INTO `staff` VALUES (140222, '周八', 33, 'Male', 'zhouba123');
INSERT INTO `staff` VALUES (140223, '吴九', 24, 'Female', 'wujiu123');
INSERT INTO `staff` VALUES (140224, '郑十', 27, 'Male', 'zhengshi123');

SET FOREIGN_KEY_CHECKS = 1;
