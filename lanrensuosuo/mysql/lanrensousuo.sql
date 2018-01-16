/*
 Navicat MySQL Data Transfer

 Source Server         : 127.0.0.1
 Source Server Version : 50173
 Source Host           : 127.0.0.1
 Source Database       : lanrensousuo

 Target Server Version : 50173
 File Encoding         : utf-8

 Date: 01/16/2018 17:24:32 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `lr_content`
-- ----------------------------
DROP TABLE IF EXISTS `lr_content`;
CREATE TABLE `lr_content` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `ctime` int(11) NOT NULL,
  `sortid` int(11) NOT NULL,
  `img` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `lr_content`
-- ----------------------------
BEGIN;
INSERT INTO `lr_content` VALUES ('7', '百度', 'http://www.baidu.com', '1599878987', '7', 'baidu.ico'), ('6', '百度', 'http://www.baidu.com', '1599878987', '6', 'baidu.ico'), ('5', '百度', 'http://www.baidu.com', '1599878987', '3', 'baidu.ico'), ('3', '百度', 'http://www.baidu.com', '1599878987', '1', 'baidu.ico');
COMMIT;

-- ----------------------------
--  Table structure for `lr_sort`
-- ----------------------------
DROP TABLE IF EXISTS `lr_sort`;
CREATE TABLE `lr_sort` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `ctime` int(11) NOT NULL,
  `typeid` int(11) NOT NULL COMMENT '分类的类别  用于列表的分类',
  `parentid` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `lr_sort`
-- ----------------------------
BEGIN;
INSERT INTO `lr_sort` VALUES ('1', '搜图', '1592345678', '1', '0'), ('3', '学术搜索', '1592345678', '1', '0'), ('6', '数据搜索', '1516086429', '1', '0'), ('7', '资源搜索', '1516086440', '1', '0');
COMMIT;

-- ----------------------------
--  Table structure for `lr_user`
-- ----------------------------
DROP TABLE IF EXISTS `lr_user`;
CREATE TABLE `lr_user` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `mail` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `lr_user`
-- ----------------------------
BEGIN;
INSERT INTO `lr_user` VALUES ('1', 'lisu860619', 'e10adc3949ba59abbe56e057f20f883e', 'sky-xiaobai@qq.com'), ('3', 'lisu860619', '698d51a19d8a121ce581499d7b701668', 'sky-xiaoai@qq.com');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
