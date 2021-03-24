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
INSERT INTO `sb_user`.`user` (`user_id`, `username`, `telegram_id`, `contact`, `email`, `photo`) VALUES (0, 'studybuddy', 'studybuddy', 87654321, 'studybuddy@email.com', 'none.png');
INSERT INTO `sb_user`.`user` (`user_id`, `username`, `telegram_id`, `contact`, `email`, `photo`) VALUES (2, 'student', 'student', 12345678, 'student@email.com', 'none.png');
INSERT INTO `sb_user`.`user` (`user_id`, `username`, `telegram_id`, `contact`, `email`, `photo`) VALUES (3, 'tutor', 'tutor', 12345678, 'tutor@email.com', 'none.png');
INSERT INTO `sb_user`.`user` (`user_id`, `username`, `telegram_id`, `contact`, `email`, `photo`) VALUES (4, 'eklum', 'eklum', 12345678, 'eklum@email.com', 'none.png');
INSERT INTO `sb_user`.`user` (`user_id`, `username`, `telegram_id`, `contact`, `email`, `photo`) VALUES (5, 'randall', 'randall', 12345678, 'randall@email.com', 'none.png');
INSERT INTO `sb_user`.`user` (`user_id`, `username`, `telegram_id`, `contact`, `email`, `photo`) VALUES (6, 'durant', 'durant', 12345678, 'durant@email.com', 'none.png');

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
  `title` varchar(30) NOT NULL,
  `description` varchar(200) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `deadline` timestamp NOT NULL,
  `created` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `status` VARCHAR(20) NULL DEFAULT 'Unsolved',
  PRIMARY KEY (`homework_id`)
) 
ENGINE=InnoDB;

SHOW WARNINGS;





-- -----------------------------------------------------
-- Data for table `sb_homework`.`homework`
-- -----------------------------------------------------
START TRANSACTION;
USE `sb_homework`;
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `title`, `description`, `price`, `deadline`, `created`, `status`) VALUES (1, 1, 'Math', 'Help with Math Homework', 'Description of homework', 5.00, '2021-04-01 00:00:00', '2021-03-15 00:00:00', 'Unsolved');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `title`, `description`, `price`, `deadline`, `created`, `status`) VALUES (2, 2, 'English', 'English Homework', 'Description of homework', 5.00, '2021-04-01 00:00:00', '2021-03-15 00:00:00', 'Unsolved');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `title`, `description`, `price`, `deadline`, `created`, `status`) VALUES (3, 1, 'Science', 'HELP SCIENCE', 'Description of homework', 6.00, '2021-04-01 00:00:00', '2021-03-15 00:00:00', 'Unsolved');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `title`, `description`, `price`, `deadline`, `created`, `status`) VALUES (4, 3, 'English', 'English Assignment', 'Description of homework', 10.00, '2021-04-01 00:00:00', '2021-03-15 00:00:00', 'Solved');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `title`, `description`, `price`, `deadline`, `created`, `status`) VALUES (5, 2, 'Science', 'Science Labs', 'Description of homework', 6.50, '2021-04-01 00:00:00', '2021-03-15 00:00:00', 'Unsolved');

COMMIT;



-- -----------------------------------------------------
-- Table `sb_homework`.`image`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sb_homework`.`image` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `sb_homework`.`image` (
  `image_id` INT NOT NULL AUTO_INCREMENT,
  `homework_id` INT NOT NULL,
  `image_link` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`image_id`),
  CONSTRAINT `fk_image_homework`
    FOREIGN KEY (`homework_id`)
    REFERENCES `sb_homework`.`homework` (`homework_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SHOW WARNINGS;
CREATE INDEX `fk_image_homework_idx` ON `sb_homework`.`image` (`homework_id` ASC);

SHOW WARNINGS;

-- -----------------------------------------------------
-- Data for table `sb_homework`.`image`
-- -----------------------------------------------------
START TRANSACTION;
USE `sb_homework`;
INSERT INTO `sb_homework`.`image` (`image_id`, `homework_id`, `image_link`) VALUES (1, 1, 'image_link');
INSERT INTO `sb_homework`.`image` (`image_id`, `homework_id`, `image_link`) VALUES (2, 1, 'image_link');
INSERT INTO `sb_homework`.`image` (`image_id`, `homework_id`, `image_link`) VALUES (3, 2, 'image_link');
INSERT INTO `sb_homework`.`image` (`image_id`, `homework_id`, `image_link`) VALUES (4, 2, 'image_link');
INSERT INTO `sb_homework`.`image` (`image_id`, `homework_id`, `image_link`) VALUES (5, 3, 'image_link');
INSERT INTO `sb_homework`.`image` (`image_id`, `homework_id`, `image_link`) VALUES (6, 3, 'image_link');
INSERT INTO `sb_homework`.`image` (`image_id`, `homework_id`, `image_link`) VALUES (7, 4, 'image_link');
INSERT INTO `sb_homework`.`image` (`image_id`, `homework_id`, `image_link`) VALUES (8, 4, 'image_link');
INSERT INTO `sb_homework`.`image` (`image_id`, `homework_id`, `image_link`) VALUES (9, 5, 'image_link');

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
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (4, 2, 1, 5.50, 'Accepted');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (5, 2, 3, 6.00, 'Rejected');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (6, 2, 4, 6.50, 'Rejected');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (7, 3, 1, 6.00, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (8, 3, 4, 6.10, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (9, 3, 5, 6.50, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (10, 4, 3, 11.10, 'Rejected');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (11, 4, 5, 11.00, 'Rejected');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (12, 4, 1, 10.50, 'Accepted');

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
  `payment_code` VARCHAR(100) NOT NULL,
  `liaise_id` INT NOT NULL,
  `sender_id` INT NOT NULL,
  `receiver_id` INT NOT NULL,
  PRIMARY KEY (`payment_code`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Data for table `sb_payment`.`payment`
-- -----------------------------------------------------
START TRANSACTION;
USE `sb_payment`;
INSERT INTO `sb_payment`.`payment` (`payment_code`, `liaise_id`, `sender_id`, `receiver_id`) VALUES ('12345678', 12, 4, 0);
INSERT INTO `sb_payment`.`payment` (`payment_code`, `liaise_id`, `sender_id`, `receiver_id`) VALUES ('87654321', 12, 0, 4);
INSERT INTO `sb_payment`.`payment` (`payment_code`, `liaise_id`, `sender_id`, `receiver_id`) VALUES ('23456789', 4, 1, 0);

COMMIT;