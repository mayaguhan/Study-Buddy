-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema sb_user
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `sb_user` ;

-- -----------------------------------------------------
-- Schema sb_user
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sb_user` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
SHOW WARNINGS;
USE `sb_user` ;

-- -----------------------------------------------------
-- Table `sb_user`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sb_user`.`user` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `sb_user`.`user` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(20) NOT NULL,
  `telegram_id` VARCHAR(20) NOT NULL,
  `contact` INT NOT NULL,
  `email` VARCHAR(30) NOT NULL,
  `photo` VARCHAR(45) NOT NULL,
  `account_num` VARCHAR(20) NOT NULL, 
  `account_type` VARCHAR(20) NOT NULL, 
  `bank_name` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`user_id`))
ENGINE = InnoDB;

SHOW WARNINGS;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `sb_user`.`user`
-- -----------------------------------------------------
START TRANSACTION;
USE `sb_user`;
INSERT INTO `sb_user`.`user` (`user_id`, `username`, `telegram_id`, `contact`, `email`, `photo`, `account_num`, `account_type`, `bank_name`) VALUES (1, 'yuquanyeo', 'yuquanyeo', 87654321, 'yuquanyeo@gmail.com', 'none.png', '214748364711', 'Personal', 'POSB');
INSERT INTO `sb_user`.`user` (`user_id`, `username`, `telegram_id`, `contact`, `email`, `photo`, `account_num`, `account_type`, `bank_name`) VALUES (2, 'student', 'student', 12345678, 'student@email.com', 'none.png', '214748364712', 'Personal', 'POSB');
INSERT INTO `sb_user`.`user` (`user_id`, `username`, `telegram_id`, `contact`, `email`, `photo`, `account_num`, `account_type`, `bank_name`) VALUES (3, 'tutor', 'tutor', 12345678, 'tutor@email.com', 'none.png', '214748364713', 'Personal', 'POSB');
INSERT INTO `sb_user`.`user` (`user_id`, `username`, `telegram_id`, `contact`, `email`, `photo`, `account_num`, `account_type`, `bank_name`) VALUES (4, 'eklum', 'eklum', 12345678, 'eklum@email.com', 'none.png', '214748364714', 'Personal', 'POSB');
INSERT INTO `sb_user`.`user` (`user_id`, `username`, `telegram_id`, `contact`, `email`, `photo`, `account_num`, `account_type`, `bank_name`) VALUES (5, 'randall', 'randall', 12345678, 'randall@email.com', 'none.png', '214748364715', 'Personal', 'POSB');
INSERT INTO `sb_user`.`user` (`user_id`, `username`, `telegram_id`, `contact`, `email`, `photo`, `account_num`, `account_type`, `bank_name`) VALUES (6, 'durant', 'durant', 12345678, 'durant@email.com', 'none.png', '214748364716', 'Personal', 'POSB');
INSERT INTO `sb_user`.`user` (`user_id`, `username`, `telegram_id`, `contact`, `email`, `photo`, `account_num`, `account_type`, `bank_name`) VALUES (100, 'studybuddy', 'studybuddy', 12345678, 'studybuddy@email.com', 'none.png', '214748364717', 'Personal', 'POSB');

COMMIT;





-- -----------------------------------------------------
-- Schema sb_homework
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `sb_homework` ;

-- -----------------------------------------------------
-- Schema sb_homework
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sb_homework` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
SHOW WARNINGS;
USE `sb_homework` ;

-- -----------------------------------------------------
-- Table `sb_homework`.`homework`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sb_homework`.`homework` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `homework` (
  `homework_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) NOT NULL,
  `subject` varchar(20) NOT NULL,
  `meeting_type` varchar(20) NOT NULL,
  `title` varchar(30) NOT NULL,
  `description` varchar(200) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `image` varchar(200) NOT NULL,
  `deadline` timestamp NOT NULL,
  `created` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `status` VARCHAR(20) NULL DEFAULT 'Unsolve',
  PRIMARY KEY (`homework_id`)
) 
ENGINE=InnoDB;

SHOW WARNINGS;





-- -----------------------------------------------------
-- Data for table `sb_homework`.`homework`
-- -----------------------------------------------------
START TRANSACTION;
USE `sb_homework`;
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (1, 1, 'Math', 'Virtual', 'Help with Math Homework', 'Description of homework', 5.00, 'homework.png', '2021-04-15 00:00:00', '2021-03-15 00:00:00', 'Unsolve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`,  `deadline`, `created`, `status`) VALUES (2, 2, 'English', 'Virtual', 'English Homework', 'Description of homework', 5.00, 'homework.png', '2021-04-15 00:00:00', '2021-03-15 00:00:00', 'Progress');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`,  `deadline`, `created`, `status`) VALUES (3, 1, 'Science', 'Non-Virtual', 'HELP SCIENCE', 'Description of homework', 6.00, 'homework.png', '2021-04-15 00:00:00', '2021-03-15 00:00:00', 'Unsolve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`,  `deadline`, `created`, `status`) VALUES (4, 3, 'English', 'Virtual', 'English Assignment', 'Description of homework', 10.00, 'homework.png', '2021-04-15 00:00:00', '2021-03-15 00:00:00', 'Solve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`,  `deadline`, `created`, `status`) VALUES (5, 2, 'Science', 'Non-Virtual', 'Science Labs', 'Description of homework', 6.50, 'homework.png', '2021-04-15 00:00:00', '2021-03-15 00:00:00', 'Unsolve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`,  `deadline`, `created`, `status`) VALUES (6, 2, 'English', 'Non-Virtual', 'HELP pls', 'Description of homework', 5.00, 'homework.png', '2021-04-15 00:00:00', '2021-03-15 00:00:00', 'Solve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`,  `deadline`, `created`, `status`) VALUES (7, 2, 'Math', 'Virtual', 'Math question', 'Description of homework', 4.50, 'homework.png', '2021-04-15 00:00:00', '2021-03-15 00:00:00', 'Solve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`,  `deadline`, `created`, `status`) VALUES (8, 2, 'Science', 'Non-Virtual', 'Science practical', 'Description of homework', 7.50, 'homework.png', '2021-04-15 00:00:00', '2021-03-15 00:00:00', 'Unsolve');


COMMIT;





-- -----------------------------------------------------
-- Schema sb_liaise
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `sb_liaise` ;

-- -----------------------------------------------------
-- Schema sb_liaise
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sb_liaise` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
SHOW WARNINGS;
USE `sb_liaise` ;

-- -----------------------------------------------------
-- Table `sb_liaise`.`liaise`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sb_liaise`.`liaise` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `sb_liaise`.`liaise` (
  `liaise_id` INT NOT NULL AUTO_INCREMENT,
  `homework_id` INT NOT NULL,
  `tutor_id` INT NOT NULL,
  `offering` DECIMAL(10,2) NOT NULL,
  `status` VARCHAR(20) NULL DEFAULT 'Pending',
  `tutor_rating` INT NULL,
  `tutor_remark` varchar(200) NULL,
  PRIMARY KEY (`liaise_id`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Data for table `sb_liaise`.`liaise`
-- -----------------------------------------------------
START TRANSACTION;
USE `sb_liaise`;
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (1, 1, 2, 6.00, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (2, 1, 3, 5.50, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (3, 1, 4, 7.00, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (4, 2, 1, 5.50, 'Accept');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (5, 2, 3, 6.00, 'Reject');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (6, 2, 4, 6.50, 'Reject');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (7, 3, 1, 6.00, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (8, 3, 4, 6.10, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (9, 3, 5, 6.50, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (10, 4, 3, 11.10, 'Reject');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (11, 4, 5, 11.00, 'Reject');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`, `tutor_rating`, `tutor_remark`) VALUES (12, 4, 1, 10.50, 'Accept', 5, 'Tutor was very experienced');

COMMIT;





-- -----------------------------------------------------
-- Schema sb_payment
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `sb_payment` ;

-- -----------------------------------------------------
-- Schema sb_payment
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sb_payment` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `sb_payment` ;

-- -----------------------------------------------------
-- Table `sb_payment`.`payment`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sb_payment`.`payment` ;

CREATE TABLE IF NOT EXISTS `sb_payment`.`payment` (
  `payment_id` VARCHAR(100) NOT NULL,
  `liaise_id` INT NOT NULL,
  `sender_id` INT NOT NULL,
  `receiver_id` INT NOT NULL,
  `created` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `status` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`payment_id`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Data for table `sb_payment`.`payment`
-- -----------------------------------------------------
START TRANSACTION;
USE `sb_payment`;
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('12345678', 12, 4, 100, '2021-03-15 00:00:00', "Complete");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('23456789', 12, 100, 4, '2021-03-15 00:00:00', "Complete");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('87654321', 4, 1, 100, '2021-03-15 00:00:00', "Hold");

COMMIT;