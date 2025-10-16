
-- データベース作成
create database db_subkari
default character set utf8;


-- テーブル作成 
-- アカウントテーブル ------------------------------
CREATE TABLE `m_account` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `username` VARCHAR(100) NOT NULL,
  `fullName` VARCHAR(100) NOT NULL,
  `birthday` DATE NOT NULL,
  `zip` CHAR(7) NOT NULL,
  `pref` VARCHAR(50) NOT NULL,
  `address1` VARCHAR(50) NOT NULL,
  `address2` VARCHAR(50) NOT NULL,
  `address3` VARCHAR(50) NOT NULL,
  `mail` VARCHAR(255) NOT NULL,
  `smoker` boolean NOT NULL,
  `introduction` TEXT  ,
  `money` INT,
  `newCreationDate` timestamp default current_timestamp,
  `updateDate` timestamp default current_timestamp on update current_timestamp,
  `updaterId` INT,
  `password` VARCHAR(255) NOT NULL,
  `identifyOffer` boolean,
  `apiFavoriteAnnounce` boolean,
  `apiFollowAnnounce` boolean,
  `apiSystemAnnounce` boolean,
  `mailFavoriteAnnounce` boolean,
  `mailFollowAnnounce` boolean,
  `mailSystemAnnounce` boolean,
  `autoLogin` boolean,
  
  PRIMARY KEY (`id`)
);


-- 商品テーブル ------------------------------------
CREATE TABLE `m_product` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `img` VARCHAR(255) NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `price` INT NOT NULL,
  `size` VARCHAR(255) NOT NULL,
  `clean_id` INT NOT NULL,
  `upload` timestamp default current_timestamp,
  `sellRental` VARCHAR(255) NOT NULL,
  `showing` VARCHAR(255) NOT NULL,
  `draft` VARCHAR(255) NULL,
  `update` timestamp default current_timestamp on update current_timestamp,
  `account_id` INT NOT NULL,
  `brand_id` INT NULL,
  `category_id` INT NULL,
  `visible` VARCHAR(255) NOT NULL,
  `rentalDuration` DATE NOT NULL,
  `explanation` VARCHAR(255) NULL,
  PRIMARY KEY (`id`)
);


-- 洗濯表示テーブル --------------------------------------------
CREATE TABLE `m_cleanSign` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `cleanName` VARCHAR(255) NOT NULL,
  `cleanImg` VARCHAR(255),
  `cleanDetail` TEXT,
  
  PRIMARY KEY (`id`)
);


-- 管理者アカウントテーブル --------------------------------
CREATE TABLE `m_adminAccount` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `fullName` VARCHAR(100) NOT NULL,
  `level` ENUM NOT NULL,
  `creationDate` timestamp default current_timestamp ,
  `lastLogin` timestamp default current_timestamp on update current_timestamp,
  `password` VARCHAR(255) NOT NULL,
  
  PRIMARY KEY (`id`)
);


-- コンテンツテーブル ---------------------------------
CREATE TABLE `m_admin_contents` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `content_detail` TEXT NOT NULL,                       --この形式後で要調査
  `created_at` timestamp default current_timestamp ,
  `updated_at` timestamp default current_timestamp on update current_timestamp,
  
  
  PRIMARY KEY (`id`)
);


-- ブランドテーブル -------------------------------------
CREATE TABLE `m_brand` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  
  PRIMARY KEY (`id`)
);

-- カテゴリテーブル -------------------------------------
CREATE TABLE `m_category` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  
  PRIMARY KEY (`id`)
);

-- ログインテーブル --------------------------------
CREATE TABLE `t_login` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `account_id` INT NOT NULL,
  `loginDatetime` timestamp default current_timestamp on update current_timestamp ,
  `logoutDatetime` timestamp default current_timestamp on update current_timestamp,
  `notice` boolean,

  PRIMARY KEY (`id`),
  FOREIGN KEY (`account_id`)
    REFERENCES `m_account`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE
);



-- お気に入りテーブル --------------------------------
CREATE TABLE `t_favorite` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `account_id` INT NOT NULL,
  `product_id` INT,
  `brand_id` INT,
  `resisterTime` timestamp default current_timestamp ,
  
  PRIMARY KEY (`id`),
  FOREIGN KEY (`account_id`)
    REFERENCES `m_account`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (`product_id`)
    REFERENCES `m_product`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (`brand_id`)
    REFERENCES `m_brand`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE
);

-- 振り込みテーブル --------------------------------
CREATE TABLE `t_transfer` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `account_id` INT NOT NULL,
  `bankName` VARCHAR(100) NOT NULL,
  `accountType` VARCHAR(20) NOT NULL,
  `branchName` VARCHAR(10) NOT NULL,
  `accountNumber` VARCHAR(20) NOT NULL,
  `accountHolder` VARCHAR(20) NOT NULL,
  
  PRIMARY KEY (`id`),
  FOREIGN KEY (`account_id`)
    REFERENCES `m_account`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE
);

-- クレジットカードテーブル --------------------------------
CREATE TABLE `t_creditCard` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `account_id` INT NOT NULL,
  `number` VARCHAR(20) NOT NULL,
  `expiry` CHAR(5) NOT NULL,                              --有効期限これで大丈夫？
  `holderName` VARCHAR(100) NOT NULL,
  
  PRIMARY KEY (`id`),
  FOREIGN KEY (`account_id`)
    REFERENCES `m_account`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE
);


-- 履歴テーブル --------------------------------
CREATE TABLE `t_history` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `account_id` INT NOT NULL,
  `transaction_id` INT,
  `product_id` INT,
  `datetime` timestamp default current_timestamp,

  PRIMARY KEY (`id`),
  FOREIGN KEY (`account_id`)
    REFERENCES `m_account`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (`transaction_id`)
    REFERENCES `t_transaction`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (`product_id`)
    REFERENCES `m_product`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE
);

-- コメントテーブル --------------------------------
CREATE TABLE `t_comments` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `account_id` INT NOT NULL,
  `content` TEXT NOT NULL,
  `createdDate` timestamp default current_timestamp ,
  `product_id` INT,
  
  PRIMARY KEY (`id`),
  FOREIGN KEY (`account_id`)
    REFERENCES `m_account`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (`product_id`)
    REFERENCES `m_product`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE
);

-- コネクションテーブル --------------------------------
CREATE TABLE `t_connection` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `execution_id` INT NOT NULL,
  `target_id` INT NOT NULL,
  `Datetime` timestamp default current_timestamp ,
  `type` ENUM NOT NULL,

  PRIMARY KEY (`id`),
  FOREIGN KEY (`execution_id`)
    REFERENCES `m_account`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (`target_id`)
    REFERENCES `m_account`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE
);


-- アラートテーブル --------------------------------
CREATE TABLE `t_alert` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `product_id` INT,
  `content` TEXT ,
  `category` ENUM ,
  `reportDate` timestamp default current_timestamp ,
  `comments_id` INT,
  `account_id` INT,
  `transaction_id` INT,
  `adminAccount_id` INT,
  `manageDate` DATETIME,
  `reportMemo` TEXT,
  `situation` ENUM,
  `reportType` ENUM,
  `notice` boolean,
  
  PRIMARY KEY (`id`),
  FOREIGN KEY (`account_id`)
    REFERENCES `m_account`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (`comments_id`)
    REFERENCES `t_comments`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (`account_id`)
    REFERENCES `m_account`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (`transaction_id`)
    REFERENCES `t_transaction`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (`adminAccount_id`)
    REFERENCES `m_adminAccount`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE
);



-- 取引テーブル ---------------------------------
CREATE TABLE `t_transaction` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `product_id` INT NOT NULL,
  `customer_id` INT NOT NULL,
  `seller_id` INT NOT NULL,
  `status` VARCHAR(255) NOT NULL,
  `situation` boolean NOT NULL,
  `paymentMethod` ENUM NOT NULL,
  `date` timestamp default current_timestamp ,
  `paymentDeadline` DATETIME NOT NULL,
  `shippingAddress` VARCHAR(255) NOT NULL,
  `shippingPhoto` VARCHAR(255) NOT NULL,
  `receivedPhoto` VARCHAR(255) NOT NULL,
  `rentalPeriod` DATETIME NOT NULL,
  `creditcards_id` INT NOT NULL,

  PRIMARY KEY (`id`),
  FOREIGN KEY (`product_id`)
    REFERENCES `m_product`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (`customer_id`)
    REFERENCES `m_account`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (`seller_id`)
    REFERENCES `m_account`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (`creditcards_id`)
    REFERENCES `m_creditcards`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE
);

-- 取引メッセージ ------------------------------------
CREATE TABLE `t_message` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `sender_id` INT NOT NULL,
  `recipient_id` INT NOT NULL,
  `t_transaction_id` INT NOT NULL,
  `content` VARCHAR(255) NOT NULL,
  `sendingTime` timestamp default current_timestamp ,
  `readStatus` VARCHAR(255) NOT NULL,

  PRIMARY KEY (`id`),
  FOREIGN KEY (`sender_id`)
    REFERENCES `m_account`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (`recipient_id`)
    REFERENCES `m_account`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (`t_transaction_id`)
    REFERENCES `t_transaction`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE
);


-- 評価テーブル ---------------------------------------
CREATE TABLE `t_evaluation` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `transaction_id` INT NOT NULL,
  `score` INT NOT NULL,
  `comment` TEXT ,
  `evaluationTime` timestamp default current_timestamp ,
  `productCheck` boolean NOT NULL,

  PRIMARY KEY (`id`),
  FOREIGN KEY (`t_transaction_id`)
    REFERENCES `t_transaction`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (`m_account_id`)
    REFERENCES `m_account`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE
);


-- 洗濯テーブル --------------------------------------------
CREATE TABLE `t_clean` (
  `product_id` INT NOT NULL,
  `cleanSign_id` INT NOT NULL,

  PRIMARY KEY (`product_id`,`cleanSign_id`)
  FOREIGN KEY (`product_id`)
    REFERENCES `m_product`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY (`cleanSign_id`)
    REFERENCES `m_cleanSign`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE,
);



-- お問い合わせテーブル ------------------------------------------
CREATE TABLE `t_inquiry` (
  `id` INT NOT NULL,
  `sender_id` INT NOT NULL,
  `content` TEXT NOT NULL,
  `timeSent` timestamp default current_timestamp ,
  `product_id` INT,
  `adminAccount_id` INT,
  `replyDetail` TEXT NOT NULL,
  `replyDate` DATETIME ,
  `situation` ENUM,

  PRIMARY KEY (`id`),
  FOREIGN KEY (`sender_id`)
    REFERENCES `m_account`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (`product_id`)
    REFERENCES `m_product`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (`adminAccount_id`)
    REFERENCES `m_adminAccount`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE
);

-- 通報テーブル -------------------------------------------------
CREATE TABLE `t_report` (
  `id` INT NOT NULL,
  `product_id` INT NOT NULL,
  `content` TEXT NOT NULL,
  `category` VARCHAR(255) NOT NULL,
  `reportDate` timestamp default current_timestamp ,
  `status` ENUM NOT NULL,
  `comment_id` INT,
  `sender_id` INT,
  `adminAccount_id` INT,
  `commitDate` timestamp default current_timestamp ,

  
  PRIMARY KEY (`id`),
  FOREIGN KEY (`sender_id`)
    REFERENCES `m_account`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (`comment_id`)
    REFERENCES `t_comments`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (`adminAccount_id`)
    REFERENCES `m_adminAccount`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE
  FOREIGN KEY (`product_id`)
    REFERENCES `m_product`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE
);





