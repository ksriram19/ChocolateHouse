CREATE TABLE `chochouse`.`majorcategory` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));


CREATE TABLE `chochouse`.`subcategory` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));


CREATE TABLE `chochouse`.`variant` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `description` VARCHAR(45) NULL,
  `allergyid` INT NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `chochouse`.`ingredient` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `quantity` INT NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `chochouse`.`composition` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `variantid` INT NULL,
  `ingredientid` INT NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `chochouse`.`offering` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `majorcatid` INT NULL,
  `subcatid` INT NULL,
  `variantid` INT NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `chochouse`.`allergy` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));


CREATE TABLE `chochouse`.`customer` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `phone` VARCHAR(10) NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `chochouse`.`custpreference` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `custid` INT NULL,
  `variantid` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));

CREATE TABLE `chochouse`.`custallergy` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `custid` INT NULL,
  `allergyid` INT NULL,
  PRIMARY KEY (`id`));



