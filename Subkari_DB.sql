
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
  `mail` VARCHAR(255) NOT NULL,
  `smoker` boolean NOT NULL,
  `introduction` TEXT  ,
  `money` INT,
  `newCreationDate` timestamp default current_timestamp,
  `updateDate` timestamp default current_timestamp on update current_timestamp,
  `updaterId` INT,
  `password` VARCHAR(255) NOT NULL,
  `identifyImg` varchar(255) NOT NULL,
  `apiFavoriteAnnounce` boolean,
  `apiFollowAnnounce` boolean,
  `apiSystemAnnounce` boolean,
  `mailFavoriteAnnounce` boolean,
  `mailFollowAnnounce` boolean,
  `mailSystemAnnounce` boolean,
  `autoLogin` boolean,
  
  PRIMARY KEY (`id`)
);

-- 住所テーブル -----------------------------------
CREATE TABLE `m_account` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `account_id` INT NOT NULL,
  `zip` CHAR(8) NOT NULL,
  `pref` VARCHAR NOT(255) NULL,
  `address1` VARCHAR(255) NOT NULL,
  `address2` VARCHAR(255) NOT NULL,
  `address3` VARCHAR(255) NOT NULL,
  
  PRIMARY KEY (`id`,`account_id`)
  FOREIGN KEY (`account_id`)
    REFERENCES `m_account`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE
);

-- 商品テーブル ------------------------------------
CREATE TABLE `m_product` (
  `id` INT AUTO_INCREMENT NOT NULL,
  `img` VARCHAR(255) NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `purchasePrice` INT NULL,
  `rentalPrice` INT NULL,
  `size` VARCHAR(255) NOT NULL,
  `upload` DATE NOT NULL,
  `showing` ENUM('公開','非公開','非表示') NOT NULL,
  `draft` boolean NOT NULL,
  `update` DATETIME NOT NULL,
  `purchaseFlg` boolean NOT NULL,
  `rentalFlg` boolean NOT NULL,
  `explanation` TEXT NULL,
  `account_id` INT NOT NULL,
  `brand_id` INT NOT NULL,
  `category_id` INT NOT NULL,
  `cleanNotes` TEXT ,
  `smokingFlg` boolean NOT NULL,

  PRIMARY KEY (`id`)
  FOREIGN KEY (`brand_id`)
    REFERENCES `m_brand`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE
  FOREIGN KEY (`category_id`)
    REFERENCES `m_category`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE
  FOREIGN KEY (`account_id`)
    REFERENCES `m_account`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE
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
  `level` ENUM('administrator','operator') NOT NULL,
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

-- トップステーブル --------------------------------
CREATE TABLE `m_topsSize` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `shoulderWidth` DECIMAL(5,2) NOT NULL,
  `bodyWidth` DECIMAL(5,2) NOT NULL,
  `sleeveLength` DECIMAL(5,2) NOT NULL,
  `bodyLength` DECIMAL(5,2) NOT NULL,
  `notes` VARCHAR(255) ,
  
  PRIMARY KEY (`id`)
);

-- ボトムステーブル --------------------------------
CREATE TABLE `m_bottomsSize` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `hip` DECIMAL(5,2) NOT NULL,
  `totalLength` DECIMAL(5,2) NOT NULL,
  `rise` DECIMAL(5,2) NOT NULL,
  `inseam` DECIMAL(5,2) NOT NULL,
  `waist` DECIMAL(5,2) NOT NULL,
  `thighWidth` DECIMAL(5,2) NOT NULL,
  `hemWidth` DECIMAL(5,2) NOT NULL,
  `skirtLength` DECIMAL(5,2) NOT NULL,
  `notes` VARCHAR(255),

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

-- レンタル期間テーブル ---------------------------------------
CREATE TABLE `t_rentalPeriod` (
  `id` INT NOT NULL,
  `product_id` INT NOT NULL,
  `rentalPeriod` ENUM('4日','7日','14日')  NOT NULL,

  PRIMARY KEY (`id`),
  FOREIGN KEY (`product_id`)
    REFERENCES `m_product`(`id`)
    ON DELETE RESTRICT ON UPDATE CASCADE,
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
  `type` ENUM('フォロー', 'ブロック') NOT NULL,

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
  `category` ENUM ('通報','警告') ,
  `reportDate` timestamp default current_timestamp ,
  `comments_id` INT,
  `account_id` INT,
  `transaction_id` INT,
  `adminAccount_id` INT,
  `manageDate` DATETIME,
  `reportMemo` TEXT,
  `situation` ENUM('未対応','対応中','対応済み'),
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
  `status` ENUM('支払い待ち','発送待ち','配達中','到着','レンタル中','クリーニング期間','発送待ち','取引完了') NOT NULL,
  `situation` ENUM('購入','レンタル') NOT NULL,
  `paymentMethod` ENUM('クレジットカード','PayPay','コンビニ払い') NOT NULL,
  `date` timestamp default current_timestamp ,
  `paymentDeadline` DATETIME NOT NULL,
  `shippingAddress` VARCHAR(255) NOT NULL,
  `shippingPhoto` VARCHAR(255) NOT NULL,
  `shippingFlg` boolean NOT NULL,
  `receivedPhoto` VARCHAR(255) NOT NULL,
  `receivedFlg` boolean NOT NULL,
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
  `situation` ENUM('未対応','対応中','対応済み'),

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
