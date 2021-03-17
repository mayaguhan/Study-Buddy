-- MySQL Script generated by MySQL Workbench
-- 03/15/21 13:03:00
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema user
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `user` ;

-- -----------------------------------------------------
-- Schema user
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `user` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
SHOW WARNINGS;
USE `user` ;

-- -----------------------------------------------------
-- Table `user`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `user`.`user` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `user`.`user` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(20) NOT NULL,
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
-- Data for table `user`.`user`
-- -----------------------------------------------------
START TRANSACTION;
USE `user`;
INSERT INTO `user`.`user` (`user_id`, `username`, `contact`, `email`, `photo`) VALUES (1, 'yuquanyeo', 81254754, 'yuquanyeo@gmail.com', 'none.png');
INSERT INTO `user`.`user` (`user_id`, `username`, `contact`, `email`, `photo`) VALUES (2, 'student', 12345678, 'student@email.com', 'none.png');
INSERT INTO `user`.`user` (`user_id`, `username`, `contact`, `email`, `photo`) VALUES (3, 'tutor', 12345678, 'tutor@email.com', 'none.png');
INSERT INTO `user`.`user` (`user_id`, `username`, `contact`, `email`, `photo`) VALUES (4, 'eklum', 12345678, 'eklum@email.com', 'none.png');
INSERT INTO `user`.`user` (`user_id`, `username`, `contact`, `email`, `photo`) VALUES (5, 'randall', 12345678, 'randall@email.com', 'none.png');
INSERT INTO `user`.`user` (`user_id`, `username`, `contact`, `email`, `photo`) VALUES (6, 'durant', 12345678, 'durant@email.com', 'none.png');

COMMIT;



-- MySQL Script generated by MySQL Workbench
-- 03/15/21 16:44:44
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema homework
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `homework` ;

-- -----------------------------------------------------
-- Schema homework
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `homework` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
SHOW WARNINGS;
USE `homework` ;

-- -----------------------------------------------------
-- Table `homework`.`homework`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `homework`.`homework` ;

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
  `status` varchar(20) NOT NULL,
  PRIMARY KEY (`homework_id`)
) 
ENGINE=InnoDB;

SHOW WARNINGS;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `homework`.`homework`
-- -----------------------------------------------------
START TRANSACTION;
USE `homework`;
INSERT INTO `homework`.`homework` (`homework_id`, `student_id`, `subject`, `title`, `description`, `price`, `deadline`, `created`, `status`) VALUES (1, 1, 'Math', 'Help with Math Homework', 'Description of homework', 5.00, '2021-04-01 00:00:00', '2021-03-15 00:00:00', 'unsolved');
INSERT INTO `homework`.`homework` (`homework_id`, `student_id`, `subject`, `title`, `description`, `price`, `deadline`, `created`, `status`) VALUES (2, 2, 'English', 'English Homework', 'Description of homework', 5.00, '2021-04-01 00:00:00', '2021-03-15 00:00:00', 'unsolved');
INSERT INTO `homework`.`homework` (`homework_id`, `student_id`, `subject`, `title`, `description`, `price`, `deadline`, `created`, `status`) VALUES (3, 1, 'Science', 'HELP SCIENCE', 'Description of homework', 6.00, '2021-04-01 00:00:00', '2021-03-15 00:00:00', 'unsolved');
INSERT INTO `homework`.`homework` (`homework_id`, `student_id`, `subject`, `title`, `description`, `price`, `deadline`, `created`, `status`) VALUES (4, 3, 'English', 'English Assignment', 'Description of homework', 10.00, '2021-04-01 00:00:00', '2021-03-15 00:00:00', 'unsolved');
INSERT INTO `homework`.`homework` (`homework_id`, `student_id`, `subject`, `title`, `description`, `price`, `deadline`, `created`, `status`) VALUES (5, 2, 'Science', 'Science Labs', 'Description of homework', 6.50, '2021-04-01 00:00:00', '2021-03-15 00:00:00', 'unsolved');

COMMIT;




-- MySQL Script generated by MySQL Workbench
-- 03/18/21 02:27:51
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema liaise
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `liaise` ;

-- -----------------------------------------------------
-- Schema liaise
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `liaise` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
SHOW WARNINGS;
USE `liaise` ;

-- -----------------------------------------------------
-- Table `liaise`.`liaise`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `liaise`.`liaise` ;

SHOW WARNINGS;
CREATE TABLE IF NOT EXISTS `liaise`.`liaise` (
  `homework_id` INT NOT NULL,
  `tutor_id` INT NOT NULL,
  `offering` DECIMAL(10,2) NOT NULL,
  `status` VARCHAR(20) NOT NULL DEFAULT 'pending',
  PRIMARY KEY (`homework_id`, `tutor_id`))
ENGINE = InnoDB;

SHOW WARNINGS;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `liaise`.`liaise`
-- -----------------------------------------------------
START TRANSACTION;
USE `liaise`;
INSERT INTO `liaise`.`liaise` (`homework_id`, `tutor_id`, `offering`, `status`) VALUES (1, 2, 6.00, 'pending');
INSERT INTO `liaise`.`liaise` (`homework_id`, `tutor_id`, `offering`, `status`) VALUES (1, 3, 5.50, 'pending');
INSERT INTO `liaise`.`liaise` (`homework_id`, `tutor_id`, `offering`, `status`) VALUES (1, 4, 7.00, 'pending');
INSERT INTO `liaise`.`liaise` (`homework_id`, `tutor_id`, `offering`, `status`) VALUES (2, 1, 5.50, 'accepted');
INSERT INTO `liaise`.`liaise` (`homework_id`, `tutor_id`, `offering`, `status`) VALUES (2, 3, 6.00, 'rejected');
INSERT INTO `liaise`.`liaise` (`homework_id`, `tutor_id`, `offering`, `status`) VALUES (2, 4, 6.50, 'rejected');
INSERT INTO `liaise`.`liaise` (`homework_id`, `tutor_id`, `offering`, `status`) VALUES (3, 1, 6.00, 'pending');
INSERT INTO `liaise`.`liaise` (`homework_id`, `tutor_id`, `offering`, `status`) VALUES (3, 4, 6.10, 'pending');
INSERT INTO `liaise`.`liaise` (`homework_id`, `tutor_id`, `offering`, `status`) VALUES (3, 5, 6.50, 'pending');
INSERT INTO `liaise`.`liaise` (`homework_id`, `tutor_id`, `offering`, `status`) VALUES (4, 3, 11.10, 'pending');
INSERT INTO `liaise`.`liaise` (`homework_id`, `tutor_id`, `offering`, `status`) VALUES (4, 5, 11.00, 'pending');
INSERT INTO `liaise`.`liaise` (`homework_id`, `tutor_id`, `offering`, `status`) VALUES (4, 1, 10.50, 'pending');

COMMIT;

