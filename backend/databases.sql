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
  `email` VARCHAR(50) NOT NULL,
  `photo` VARCHAR(100) NOT NULL,
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
INSERT INTO `sb_user`.`user` (`user_id`, `username`, `telegram_id`, `contact`, `email`, `photo`, `account_num`, `account_type`, `bank_name`) VALUES (1, 'yuquanyeo', 'yuquanyeo', 81254754, 'yuquan.yeo.2019@sis.smu.edu.sg', 'https://i.imgur.com/cQlCJBi.jpg', '214748364711', 'Personal', 'POSB');
INSERT INTO `sb_user`.`user` (`user_id`, `username`, `telegram_id`, `contact`, `email`, `photo`, `account_num`, `account_type`, `bank_name`) VALUES (2, 'davidlyj', 'davidlyj', 98623227, 'david.lim.2019@sis.smu.edu.sg', 'https://i.imgur.com/bYC0VFF.jpg', '214748364712', 'Personal', 'POSB');
INSERT INTO `sb_user`.`user` (`user_id`, `username`, `telegram_id`, `contact`, `email`, `photo`, `account_num`, `account_type`, `bank_name`) VALUES (3, 'mayazhagug', 'Myz_ghn', 93805496, 'mayazhagug.2019@sis.smu.edu.sg', 'https://i.imgur.com/Me2bsCz.jpg', '214748364713', 'Personal', 'POSB');
INSERT INTO `sb_user`.`user` (`user_id`, `username`, `telegram_id`, `contact`, `email`, `photo`, `account_num`, `account_type`, `bank_name`) VALUES (4, 'avanthikaa', 'avan_thatgirl', 92345678, 'avanthikaa.2019@sis.smu.edu.sg', 'https://i.imgur.com/1hwNhh6.jpg', '214748364714', 'Personal', 'POSB');
INSERT INTO `sb_user`.`user` (`user_id`, `username`, `telegram_id`, `contact`, `email`, `photo`, `account_num`, `account_type`, `bank_name`) VALUES (5, 'ayeshass', 'shasha_123', 82345678, 'ayeshass.2019@sis.smu.edu.sg', 'https://i.imgur.com/nIiqi7E.jpg', '214748364715', 'Personal', 'POSB');
INSERT INTO `sb_user`.`user` (`user_id`, `username`, `telegram_id`, `contact`, `email`, `photo`, `account_num`, `account_type`, `bank_name`) VALUES (6, 'randallduran', 'rduran', 98345678, 'rduran@smu.edu.sg', 'https://i.imgur.com/VCOE8to.jpg', '214748364700', 'Personal', 'POSB');
INSERT INTO `sb_user`.`user` (`user_id`, `username`, `telegram_id`, `contact`, `email`, `photo`, `account_num`, `account_type`, `bank_name`) VALUES (7, 'engkitlum', 'eklum', 91234567, 'eklum@smu.edu.sg', 'https://i.imgur.com/PrEl2GA.png', '214748364700', 'Personal', 'POSB');
INSERT INTO `sb_user`.`user` (`user_id`, `username`, `telegram_id`, `contact`, `email`, `photo`, `account_num`, `account_type`, `bank_name`) VALUES (8, 'donaldtrump', 'donaldtrump', 91234567, 'donaldtrump@gmail.com', 'https://i.imgur.com/W2BW4uf.jpg', '214748364700', 'Personal', 'POSB');
INSERT INTO `sb_user`.`user` (`user_id`, `username`, `telegram_id`, `contact`, `email`, `photo`, `account_num`, `account_type`, `bank_name`) VALUES (9, 'stevenlim', 'stevenlim', 91234567, 'stevenlim@gmail.com', 'https://i.imgur.com/J2k0yKL.jpg', '214748364700', 'Personal', 'POSB');
INSERT INTO `sb_user`.`user` (`user_id`, `username`, `telegram_id`, `contact`, `email`, `photo`, `account_num`, `account_type`, `bank_name`) VALUES (10, 'johnny', 'johnny', 91234567, 'johnny@gmail.com', 'https://i.imgur.com/wVB6MwE.jpg', '214748364700', 'Personal', 'POSB');
INSERT INTO `sb_user`.`user` (`user_id`, `username`, `telegram_id`, `contact`, `email`, `photo`, `account_num`, `account_type`, `bank_name`) VALUES (100, 'studybuddy', 'studybuddy', 98765432, 'studybuddyapp@outlook.com', 'https://i.imgur.com/gWlJuOi.jpg', '214748364711', 'Personal', 'POSB');

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
  `homework_id` INT NOT NULL AUTO_INCREMENT,
  `student_id` INT NOT NULL,
  `subject` VARCHAR(20) NOT NULL,
  `meeting_type` VARCHAR(20) NOT NULL,
  `title` VARCHAR(50) NOT NULL,
  `description` VARCHAR(200) NOT NULL,
  `price` DECIMAL(10,2) NOT NULL,
  `image` VARCHAR(200) NOT NULL,
  `deadline` TIMESTAMP NOT NULL,
  `created` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
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
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (1, 1, 'Math', 'Virtual', 'Help with Math Homework', 'How do I find these angles?', 5.00, 'https://i.imgur.com/mrImm4u.jpg', '2021-04-30 00:00:00', '2021-03-29 08:10:21', 'Unsolve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (2, 2, 'English', 'Virtual', 'Fill in the word English Homework', 'Hello, I need help with this P5 English question, would be good if you can explain to me why those words are the answer', 5.00, 'https://i.imgur.com/VB9tG10.jpg', '2021-04-30 00:00:00', '2021-03-29 09:11:11', 'Unsolve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (3, 3, 'Science', 'Non-Virtual', 'Science Metals & Force', 'I have attached the homework question, please explain to me how this mechanism is able to separate metals and explain to me how the separator works', 6.00, 'https://i.imgur.com/dItYBN9.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Unsolve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (4, 4, 'Tamil', 'Virtual', 'Tamil Homework', 'Pls help, I am gonna fail my Tamil pretty soon', 10.00, 'https://i.imgur.com/mYgCv1w.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Unsolve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (5, 5, 'Social Studies', 'Non-Virtual', 'Reliability Question', 'Social Studies question on reliability, would require detailed explanation, willing to pay more', 6.50, 'https://i.imgur.com/FYwHAa9.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Unsolve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (6, 6, 'Math', 'Virtual', 'PSLE Math Question', 'Math question got me seeing cirlces', 5.00, 'https://i.imgur.com/1JFcXVy.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Unsolve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (7, 7, 'Literature', 'Virtual', 'Literature Review', 'What is a literature review?', 5.00, 'https://i.imgur.com/xUvfU9e.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Unsolve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (8, 8, 'Biology', 'Non-Virtual', 'Biology: Amino Acids', 'Is amino acid sour?', 6.00, 'https://i.imgur.com/bUBhXbu.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Unsolve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (9, 9, 'English', 'Virtual', 'English Assignment on eScooter', 'Please help me for my eng hw', 10.00, 'https://i.imgur.com/tVDmNcy.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Unsolve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (10, 10, 'Science', 'Non-Virtual', 'Anne Science Experiment', 'How to find the answer? Wth my school never teach', 6.50, 'https://i.imgur.com/HPGX9Qe.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Unsolve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (11, 1, 'Math', 'Virtual', 'Math Problem', 'Why is this so hard, how to find', 5.00, 'https://i.imgur.com/abyhHHC.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Unsolve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (12, 2, 'Literature', 'Virtual', 'Literature Assignment', 'Write for me and I will do anything', 10.00, 'https://i.imgur.com/cgdzMLI.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Unsolve');

INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (13, 3, 'Malay', 'Virtual', 'English Homework ASAP', 'Please see the image, I need help ASAP', 5.00, 'https://i.imgur.com/dKeNqhY.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Unsolve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (14, 1, 'Chinese', 'Virtual', 'Chinese Homework', 'MCQs', 5.00, 'https://i.imgur.com/QnGlfTx.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Progress');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (15, 1, 'Biology', 'Non-Virtual', 'HELP SCIENCE', 'How to find probability', 6.00, 'https://i.imgur.com/OIqszFl.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Progress');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (16, 2, 'Science', 'Non-Virtual', '[URGENT] Science Labs', 'Scienccceeee', 6.50, 'https://i.imgur.com/IJXsJVo.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Progress');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (17, 2, 'Math', 'Virtual', 'Help with Math Homework', 'Why is math so hard', 5.00, 'https://i.imgur.com/nym0HNY.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Progress');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (18, 3, 'Chinese', 'Non-Virtual', 'HELP SCIENCE', 'Please help me, if not my parents will kill me', 6.00, 'https://i.imgur.com/ZoGTP8W.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Progress');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (19, 4, 'Literature', 'Virtual', 'English Assignment due on 30th April', '[URGENT] Submission soon', 10.00, 'https://i.imgur.com/28ZHFmn.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Progress');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (20, 5, 'Science', 'Non-Virtual', 'Science Homework + Homework', 'Holiday homework need help ASAP', 6.50, 'https://i.imgur.com/hTmx0QJ.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Progress');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (21, 6, 'Accounting', 'Non-Virtual', 'Balance my sheet', 'Well... shit', 6.00, 'https://i.imgur.com/gSIzfFF.png', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Progress');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (22, 7, 'History', 'Virtual', 'History explanation', 'Provide me with answer, min words 1000', 10.00, 'https://i.imgur.com/AHAd8rY.png', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Progress');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (23, 8, 'Biology', 'Non-Virtual', 'Biology question', 'Can you do biology with me in my room', 6.50, 'https://i.imgur.com/eI8Wo8h.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Progress');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (24, 9, 'Tamil', 'Virtual', 'URGENT PLS HELP ME', '[URGENT] Submission soon', 10.00, 'https://i.imgur.com/3rO2pcz.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Progress');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (25, 10, 'Chemistry', 'Non-Virtual', 'Walter White Pls help', 'I want to make meth', 6.50, 'https://i.imgur.com/fJVIajd.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Progress');

INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (26, 1, 'Science', 'Non-Virtual', 'Science Labs', 'Open ended questions', 6.50, 'https://i.imgur.com/VJIPfTw.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Cancel');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (27, 2, 'Math', 'Virtual', 'Show me the working for this Math qn', 'Can you provide me with working', 5.00, 'https://i.imgur.com/ZnQRbPc.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Cancel');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (28, 3, 'Social Studies', 'Non-Virtual', 'Social studies essay', 'Write my essay for me', 6.00, 'https://i.imgur.com/bHL79QE.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Cancel');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (29, 4, 'Malay', 'Virtual', 'English Assignment URGENT', 'I need to finish so I can graduate', 10.00, 'https://i.imgur.com/dMdTYJX.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Cancel');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (30, 5, 'Chemistry', 'Non-Virtual', 'Science Labs', 'How to find the answer? Wth my school never teach', 6.50, 'https://i.imgur.com/gYuxMjp.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Cancel');

INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (31, 1, 'Math', 'Virtual', 'Math Homework Worksheet', 'Problem Sums', 5.00, 'https://i.imgur.com/HtZyAMP.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Solve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (32, 2, 'History', 'Virtual', 'English Assignment', 'Please help me, if not my parents will kill me', 10.00, 'https://i.imgur.com/ZwBKqeI.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Solve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (33, 3, 'Literature', 'Virtual', 'English Homework', 'Write my literature essay for me', 5.00, 'https://i.imgur.com/cOePfAb.png', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Solve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (34, 1, 'English', 'Virtual', 'English Homework', 'How to find the meaning of these words', 5.00, 'https://i.imgur.com/iYV6HTH.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Solve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (35, 1, 'Social Studies', 'Non-Virtual', 'Understanding the drawing', 'How to find out what the artist is trying to say', 6.00, 'https://i.imgur.com/35NJP7d.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Solve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (36, 2, 'Science', 'Non-Virtual', 'Science experiment', 'Help me conduct these experiments', 6.50, 'https://i.imgur.com/OWYDzzU.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Solve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (37, 2, 'Math', 'Virtual', '2+2=4-1=3 quick math', 'Why are we even learning math', 5.00, 'https://i.imgur.com/69Hu7ID.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Solve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (38, 3, 'Biology', 'Non-Virtual', 'Urgent... Science...', 'Why did I take bio...I need to finish so I can graduate', 6.00, 'https://i.imgur.com/6jz8QeL.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Solve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (39, 4, 'Chinese', 'Virtual', 'Ni Hao, qing ni bang wo', 'Hi can you help me? Idk how to read', 10.00, 'https://i.imgur.com/fsK3vN1.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Solve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (40, 5, 'Accounting', 'Non-Virtual', 'I cant count for nuts', 'How to find the answer? Wth my school never teach', 6.50, 'https://i.imgur.com/8hQwW4r.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Solve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (41, 6, 'Chemistry', 'Non-Virtual', 'I want to make meth', 'Breaking bad', 6.00, 'https://i.imgur.com/zVnOh6P.png', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Solve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (42, 7, 'English', 'Virtual', 'English Assignment', 'Willing to pay more if done well', 10.00, 'https://i.imgur.com/VI6eSWN.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Solve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (43, 8, 'Chinese', 'Non-Virtual', 'I HATE CHINESE', 'I am chinese and I cant even Chinese', 6.50, 'https://i.imgur.com/y8a6FIC.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Solve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (44, 9, 'Social Studies', 'Virtual', 'Social Studies help needed', 'Looking for tutor who will finish this assignment and present for me', 10.00, 'https://i.imgur.com/uzn9kad.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Solve');
INSERT INTO `sb_homework`.`homework` (`homework_id`, `student_id`, `subject`, `meeting_type`, `title`, `description`, `price`, `image`, `deadline`, `created`, `status`) VALUES (45, 10, 'Science', 'Non-Virtual', '[Urgent] Science question', 'Very difficult science question', 6.50, 'https://i.imgur.com/3xgqRgj.jpg', '2021-04-30 00:00:00', '2021-04-01 00:00:00', 'Solve');

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
  `tutor_remark` VARCHAR(200) NULL,
  PRIMARY KEY (`liaise_id`))
ENGINE = InnoDB;

SHOW WARNINGS;

-- -----------------------------------------------------
-- Data for table `sb_liaise`.`liaise`
-- -----------------------------------------------------
START TRANSACTION;
USE `sb_liaise`;
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (1, 1, 2, 6.00, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (2, 1, 3, 7.00, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (3, 1, 4, 7.50, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (4, 1, 10, 6.20, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (5, 2, 3, 6.00, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (6, 2, 4, 5.50, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (7, 2, 1, 7.50, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (8, 3, 1, 8.00, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (9, 3, 2, 8.50, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (10, 3, 4, 7.50, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (11, 4, 2, 8.50, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (12, 4, 3, 7.50, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (13, 5, 1, 8.50, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (14, 5, 2, 7.50, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (15, 6, 2, 8.50, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (16, 14, 2, 6.00, 'Accept');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (17, 14, 3, 7.00, 'Reject');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (18, 14, 4, 7.50, 'Reject');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (19, 15, 4, 6.00, 'Accept');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (20, 15, 6, 7.00, 'Reject');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (21, 15, 8, 7.50, 'Reject');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (22, 16, 3, 6.00, 'Accept');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (23, 16, 4, 7.00, 'Reject');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (24, 17, 5, 7.50, 'Reject');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (25, 17, 1, 6.00, 'Accept');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (26, 18, 1, 7.00, 'Accept');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (27, 18, 8, 7.50, 'Reject');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (28, 19, 3, 6.00, 'Accept');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (29, 20, 1, 7.00, 'Accept');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (30, 20, 8, 7.50, 'Reject');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (31, 21, 1, 7.00, 'Accept');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (32, 22, 2, 7.00, 'Accept');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (33, 23, 3, 7.00, 'Accept');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (34, 24, 4, 7.00, 'Accept');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (35, 25, 5, 7.00, 'Accept');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (36, 26, 2, 5.00, 'Reject');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (37, 27, 3, 5.00, 'Reject');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (38, 28, 4, 5.00, 'Reject');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (39, 29, 5, 5.00, 'Reject');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (40, 30, 1, 5.00, 'Reject');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`, `tutor_rating`, `tutor_remark`) VALUES (41, 31, 2, 10.50, 'Accept', 5, 'Tutor was very experienced');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`, `tutor_rating`, `tutor_remark`) VALUES (42, 32, 1, 10.50, 'Accept', 4, 'Good at Math');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`, `tutor_rating`, `tutor_remark`) VALUES (43, 33, 2, 10.50, 'Accept', 4, 'Very handsome');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`, `tutor_rating`, `tutor_remark`) VALUES (44, 34, 3, 10.50, 'Accept', 5, 'Very pretty');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (45, 35, 1, 10.50, 'Reject');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`, `tutor_rating`, `tutor_remark`) VALUES (46, 36, 4, 10.50, 'Accept', 5, 'Tutor was very smart');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`, `tutor_rating`, `tutor_remark`) VALUES (47, 37, 5, 10.50, 'Accept', 3, 'Explains well');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`, `tutor_rating`, `tutor_remark`) VALUES (48, 38, 2, 10.50, 'Accept', 5, 'If only this tutor was my teacher');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`, `tutor_rating`, `tutor_remark`) VALUES (49, 39, 1, 10.50, 'Accept', 2, 'Teaches well but rude');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`, `tutor_rating`, `tutor_remark`) VALUES (50, 40, 3, 10.50, 'Accept', 3, 'Patient');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`, `tutor_rating`, `tutor_remark`) VALUES (51, 41, 2, 10.50, 'Accept', 5, 'Approachable');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`, `tutor_rating`, `tutor_remark`) VALUES (52, 42, 4, 10.50, 'Accept', 3, 'Broke down question very meticulously');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`, `tutor_rating`, `tutor_remark`) VALUES (53, 43, 1, 10.50, 'Accept', 5, 'Will engage again');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`, `tutor_rating`, `tutor_remark`) VALUES (54, 44, 2, 10.50, 'Accept', 3, 'Tutor was very helpful');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`, `tutor_rating`, `tutor_remark`) VALUES (55, 45, 2, 10.50, 'Accept', 5, 'Very wise');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (56, 11, 2, 5.50, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (57, 11, 3, 6.50, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (58, 11, 4, 5.55, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (59, 11, 5, 4.50, 'Pending');
INSERT INTO `sb_liaise`.`liaise` (`liaise_id`, `homework_id`, `tutor_id`, `offering`, `status`) VALUES (60, 11, 6, 5.25, 'Pending');



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
  `created` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `status` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`payment_id`))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Data for table `sb_payment`.`payment`
-- -----------------------------------------------------
START TRANSACTION;
USE `sb_payment`;
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_1IZqxGmeqSxxgDRaS2Tdf312', 16, 1, 2, '2021-04-05 00:00:00', "Hold");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_1IYRi5DZqxGmeqS98DRaS2TA', 19, 1, 4, '2021-04-05 00:00:00', "Hold");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_1IYRi5DZqgDRaS2TGmeqSxSx', 22, 2, 3, '2021-04-05 00:00:00', "Hold");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_qDZqx01DZqxGmeqSxgDRaS2T', 25, 2, 1, '2021-04-05 00:00:00', "Hold");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_qDZqx016jkiGmeqSxgDRaS2T', 26, 3, 1, '2021-04-05 00:00:00', "Hold");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_1IYRi5DZqxGmqDZqxrAeqSxx', 28, 4, 3, '2021-04-05 00:00:00', "Hold");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_1IYRGmeqSxxgDRaS2gDRaS2T', 29, 5, 1, '2021-04-05 00:00:00', "Hold");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_1IYRi5DZqxGmeqSxxgDRaS2T', 31, 6, 1, '2021-04-05 00:00:00', "Hold");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_1IYSCqDZqxGmeqSx0rdDcv6a', 32, 6, 2, '2021-04-05 00:00:00', "Hold");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_1IYSfYDZ3VcxeqSxB8IwH2oA', 33, 8, 3, '2021-04-05 00:00:00', "Hold");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_1IYTJ1DZqxGmeqSx3mFdVb5N', 34, 9, 4, '2021-04-05 00:00:00', "Hold");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_1IYXImDZVb5NeqSxOYisxIpY', 35, 10, 5, '2021-04-05 00:00:00', "Hold");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_1Ibk2YDZqAG4B6OPemeqSAsT', 41, 1, 2, '2021-04-01 00:00:00', "Pending");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_1IYSeZDZqAG3VcAApmgageqS', 42, 2, 1, '2021-04-05 00:00:00', "Pending");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_1IYRi5GmeqDRaS2TSAAa2oIw', 43, 3, 2, '2021-04-05 00:00:00', "Pending");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_1IYSCqDZqA0rdDcv6aYtqSAd', 44, 1, 3, '2021-04-05 00:00:00', "Pending");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_1IYSfYDZqAGmDZqAeqSAHPes', 45, 1, 2, '2021-04-05 00:00:00', "Pending");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_6zbk9iDZqAG3VcAAB6OPesT4', 46, 2, 4, '2021-04-01 00:00:00', "Pending");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_Vb5NARDZqAGme05jiBYtqSAd', 47, 2, 5, '2021-04-01 00:00:00', "Pending");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_6zYSeZDZqAGmeqS3VcAAgagp', 48, 3, 2, '2021-04-01 00:00:00', "Pending");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_6zbjsKDZ3VcAmeqSA2ID1mbV', 49, 4, 1, '2021-04-01 00:00:00', "Pending");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_6zYS4RDZqAGmejJSAde3BYtq', 50, 5, 3, '2021-04-01 00:00:00', "Pending");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_6zbk9iDZqAG4B6OPemeqSAsT', 51, 6, 2, '2021-04-01 00:00:00', "Pending");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_6zYSeZDZqAG3VcAApmgageqS', 52, 7, 4, '2021-04-01 00:00:00', "Pending");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_6zYRi5DZqAGmeqDRaS2TSAAa', 53, 8, 1, '2021-04-01 00:00:00', "Pending");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_6zYSCqDZqA0rdDcv6aYtqSAd', 54, 9, 2, '2021-04-01 00:00:00', "Pending");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_6zYSfYDZqAGm2oIweqSAHPes', 55, 10, 3, '2021-04-01 00:00:00', "Pending");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_1Ibk2YDZqxG4B6OPemeqSxsT', 41, 1, 2, '2021-04-01 00:00:00', "Complete");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_1IYSeZDZqxG3VcxApmgageqS', 42, 2, 1, '2021-04-05 00:00:00', "Confirm");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_1IYRi5DZqxGmeqDRaS2TSxxa', 43, 3, 2, '2021-04-05 00:00:00', "Confirm");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_1IYSCqDZqx0rdDcv6aYtqSxd', 44, 1, 3, '2021-04-05 00:00:00', "Confirm");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_1IYSfYDZqxGm2oIweqSxHPes', 45, 1, 2, '2021-04-05 00:00:00', "Cancel");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_6zbk9iDZqxG3VcxxB6OPesT4', 46, 2, 4, '2021-04-01 00:00:00', "Complete");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_Vb5NARDZqxGme05jiBYtqSxd', 47, 2, 5, '2021-04-01 00:00:00', "Complete");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_6zYSeZDZqxGmeqS3VcxAgagp', 48, 3, 2, '2021-04-01 00:00:00', "Complete");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_6zbjsKDZ3VcxmeqSx2ID1mbV', 49, 4, 1, '2021-04-01 00:00:00', "Complete");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_6zYS4RDZqxGmejJSxde3BYtq', 50, 5, 3, '2021-04-01 00:00:00', "Complete");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_6zbk9iDZqxG4B6OPemeqSxsT', 51, 6, 2, '2021-04-01 00:00:00', "Complete");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_6zYSeZDZqxG3VcxApmgageqS', 52, 7, 4, '2021-04-01 00:00:00', "Complete");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_6zYRi5DZqxGmeqDRaS2TSxxa', 53, 8, 1, '2021-04-01 00:00:00', "Complete");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_6zYSCqDZqx0rdDcv6aYtqSxd', 54, 9, 2, '2021-04-01 00:00:00', "Complete");
INSERT INTO `sb_payment`.`payment` (`payment_id`, `liaise_id`, `sender_id`, `receiver_id`, `created`, `status`) VALUES ('pi_6zYSfYDZqxGm2oIweqSxHPes', 55, 10, 3, '2021-04-01 00:00:00', "Complete");

COMMIT;