/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : log

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2022-08-27 01:09:52
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for smart_gate_bmi
-- ----------------------------
DROP TABLE IF EXISTS `smart_gate_bmi`;
CREATE TABLE `smart_gate_bmi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vn` varchar(255) DEFAULT NULL,
  `cid` varchar(255) DEFAULT NULL,
  `bw` varchar(255) DEFAULT NULL,
  `bh` varchar(255) DEFAULT NULL,
  `bmi` varchar(255) DEFAULT NULL,
  `d_update` datetime DEFAULT NULL,
  `d_sync` datetime DEFAULT NULL,
  `note1` varchar(255) DEFAULT NULL,
  `note2` varchar(255) DEFAULT NULL,
  `note3` varchar(255) DEFAULT NULL,
  `hn` varchar(255) DEFAULT NULL,
  `fullname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for smart_gate_bp
-- ----------------------------
DROP TABLE IF EXISTS `smart_gate_bp`;
CREATE TABLE `smart_gate_bp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vn` varchar(255) DEFAULT NULL,
  `cid` varchar(255) DEFAULT NULL,
  `tp` varchar(255) DEFAULT NULL,
  `bps` varchar(255) DEFAULT NULL,
  `bpd` varchar(255) DEFAULT NULL,
  `pulse` varchar(255) DEFAULT NULL,
  `d_update` datetime DEFAULT NULL,
  `d_sync` datetime DEFAULT NULL,
  `note1` varchar(255) DEFAULT NULL,
  `note2` varchar(255) DEFAULT NULL,
  `note3` varchar(255) DEFAULT NULL,
  `hn` varchar(255) DEFAULT NULL,
  `fullname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for smart_gate_sp
-- ----------------------------
DROP TABLE IF EXISTS `smart_gate_sp`;
CREATE TABLE `smart_gate_sp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vn` varchar(255) DEFAULT NULL,
  `cid` varchar(255) DEFAULT NULL,
  `sp` varchar(255) DEFAULT NULL,
  `pulse` varchar(255) DEFAULT NULL,
  `d_update` datetime DEFAULT NULL,
  `d_sync` datetime DEFAULT NULL,
  `note1` varchar(255) DEFAULT NULL,
  `note2` varchar(255) DEFAULT NULL,
  `note3` varchar(255) DEFAULT NULL,
  `hn` varchar(255) DEFAULT NULL,
  `fullname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 ROW_FORMAT=DYNAMIC;

-- ----------------------------
-- Table structure for smart_gate_tp
-- ----------------------------
DROP TABLE IF EXISTS `smart_gate_tp`;
CREATE TABLE `smart_gate_tp` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vn` varchar(255) DEFAULT NULL,
  `cid` varchar(255) DEFAULT NULL,
  `tp` varchar(255) DEFAULT NULL,
  `d_update` datetime DEFAULT NULL,
  `d_sync` date DEFAULT NULL,
  `note1` varchar(255) DEFAULT NULL,
  `note2` varchar(255) DEFAULT NULL,
  `note3` varchar(255) DEFAULT NULL,
  `hn` varchar(255) DEFAULT NULL,
  `fullname` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 ROW_FORMAT=DYNAMIC;
