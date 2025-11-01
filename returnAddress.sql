-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- ホスト: 127.0.0.1
-- 生成日時: 2025-10-31 08:01:17
-- サーバのバージョン： 10.4.32-MariaDB
-- PHP のバージョン: 8.2.12
DROP DATABASE db_subkari;
CREATE DATABASE db_subkari;
USE db_subkari;

DROP DATABASE db_subkari;
CREATE DATABASE db_subkari;
USE db_subkari;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- データベース: `db_subkari`
--

-- --------------------------------------------------------

--
-- テーブルの構造 `m_account`
--

CREATE TABLE `m_account` (
  `id` int(11) NOT NULL,
  `username` varchar(12) NOT NULL,
  `birthday` date NOT NULL,
  `tel` varchar(20) NOT NULL,
  `mail` varchar(255) NOT NULL,
  `smoker` tinyint(1) NOT NULL,
  `introduction` text DEFAULT NULL,
  `money` int(11) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updateDate` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `status` enum('未確認','本人確認済み','凍結','削除','強制削除') NOT NULL,
  `updaterId` int(11) DEFAULT NULL,
  `password` varchar(255) NOT NULL,
  `identifyImg` varchar(255) NOT NULL,
  `apiFavoriteAnnounce` tinyint(1) DEFAULT NULL,
  `apiFollowAnnounce` tinyint(1) DEFAULT NULL,
  `apiSystemAnnounce` tinyint(1) DEFAULT NULL,
  `mailFavoriteAnnounce` tinyint(1) DEFAULT NULL,
  `mailFollowAnnounce` tinyint(1) DEFAULT NULL,
  `mailSystemAnnounce` tinyint(1) DEFAULT NULL,
  `autoLogin` tinyint(1) DEFAULT NULL,
  `last_name` varchar(50) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name_kana` varchar(50) NOT NULL,
  `first_name_kana` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `m_account`
--

INSERT INTO `m_account` (`id`, `username`, `birthday`, `tel`, `mail`, `smoker`, `introduction`, `money`, `created_at`, `updateDate`, `status`, `updaterId`, `password`, `identifyImg`, `apiFavoriteAnnounce`, `apiFollowAnnounce`, `apiSystemAnnounce`, `mailFavoriteAnnounce`, `mailFollowAnnounce`, `mailSystemAnnounce`, `autoLogin`, `last_name`, `first_name`, `last_name_kana`, `first_name_kana`) VALUES
(1, 'nekamaware', '1990-03-15', '090-1111-1111', 'test@gmail.com', 0, 'ハチワレだいしゅき～', 12000, '2025-10-31 01:45:42', '2025-10-31 03:04:10', '本人確認済み', NULL, '12345678', 'image51.png', 1, 1, 1, 1, 0, 1, 0, '中村', '太郎', 'ナカムラ', 'タロウ'),
(2, 'hanako02', '1992-07-20', '090-2222-2222', 'hanako02@example.com', 0, '服が好きです。', 8000, '2025-10-31 01:45:42', '2025-10-31 01:45:42', '本人確認済み', NULL, 'hanako123', 'id02.jpg', 1, 0, 1, 1, 1, 1, 0, '佐藤', '花子', 'サトウ', 'ハナコ'),
(3, 'jiro03', '1988-02-11', '080-3333-3333', 'jiro03@example.com', 1, '古着を出品しています。', 3000, '2025-10-31 01:45:42', '2025-10-31 01:45:42', '本人確認済み', NULL, 'jiro_pass', 'id03.jpg', 0, 1, 1, 0, 1, 0, 1, '田中', '次郎', 'タナカ', 'ジロウ'),
(4, 'yuki04', '1995-12-01', '070-4444-4444', 'yuki04@example.com', 0, 'レンタル中心に使っています。', 5500, '2025-10-31 01:45:42', '2025-10-31 01:45:42', '未確認', NULL, 'yuki_pass', 'id04.jpg', 1, 1, 1, 0, 0, 1, 0, '鈴木', '悠希', 'スズキ', 'ユウキ'),
(5, 'mika05', '1998-09-25', '090-5555-5555', 'mika05@example.com', 0, 'よろしくお願いします！', 1000, '2025-10-31 01:45:42', '2025-10-31 01:45:42', '本人確認済み', NULL, 'mika_pass', 'id05.jpg', 1, 1, 1, 1, 1, 1, 0, '高橋', '美香', 'タカハシ', 'ミカ'),
(6, 'koji06', '1985-01-30', '080-6666-6666', 'koji06@example.com', 1, '喫煙者です。', 25000, '2025-10-31 01:45:42', '2025-10-31 01:45:42', '本人確認済み', NULL, 'koji_pass', 'id06.jpg', 0, 1, 0, 1, 0, 0, 1, '井上', '浩二', 'イノウエ', 'コウジ'),
(7, 'ayaka07', '1993-11-05', '070-7777-7777', 'ayaka07@example.com', 0, 'フォロバします！', 7200, '2025-10-31 01:45:42', '2025-10-31 01:45:42', '本人確認済み', NULL, 'ayaka_pass', 'id07.jpg', 1, 1, 1, 1, 1, 0, 0, '松本', '彩香', 'マツモト', 'アヤカ'),
(8, 'kenta08', '1991-06-10', '090-8888-8888', 'kenta08@example.com', 0, '出品中心で利用しています。', 4100, '2025-10-31 01:45:42', '2025-10-31 01:45:42', '未確認', NULL, 'kenta_pass', 'id08.jpg', 1, 0, 1, 1, 0, 1, 0, '山本', '健太', 'ヤマモト', 'ケンタ'),
(9, 'saki09', '1999-10-02', '080-9999-9999', 'saki09@example.com', 0, '新品も扱ってます。', 9300, '2025-10-31 01:45:42', '2025-10-31 01:45:42', '本人確認済み', NULL, 'saki_pass', 'id09.jpg', 1, 1, 1, 1, 1, 1, 1, '加藤', '咲', 'カトウ', 'サキ'),
(10, 'takumi10', '1987-08-08', '070-1010-1010', 'takumi10@example.com', 1, '古着コレクターです。', 12000, '2025-10-31 01:45:42', '2025-10-31 01:45:42', '本人確認済み', NULL, 'takumi_pass', 'id10.jpg', 0, 1, 1, 0, 0, 0, 1, '中島', '拓海', 'ナカジマ', 'タクミ'),
(11, 'rina11', '1996-04-18', '090-1111-2222', 'rina11@example.com', 0, 'かわいい服を探してます！', 7000, '2025-10-31 01:45:42', '2025-10-31 01:45:42', '本人確認済み', NULL, 'rina_pass', 'id11.jpg', 1, 1, 1, 1, 1, 1, 1, '森', '里奈', 'モリ', 'リナ'),
(12, 'kazu12', '1989-03-12', '080-2222-3333', 'kazu12@example.com', 0, '出品強化中！', 15500, '2025-10-31 01:45:42', '2025-10-31 01:45:42', '本人確認済み', NULL, 'kazu_pass', 'id12.jpg', 1, 0, 1, 1, 1, 1, 0, '藤田', '一', 'フジタ', 'カズ'),
(13, 'emi13', '1997-05-09', '070-3333-4444', 'emi13@example.com', 0, '日々出品中。', 4200, '2025-10-31 01:45:42', '2025-10-31 01:45:42', '本人確認済み', NULL, 'emi_pass', 'id13.jpg', 1, 1, 0, 1, 1, 1, 0, '長谷川', '恵美', 'ハセガワ', 'エミ'),
(14, 'ryota14', '1994-09-17', '090-4444-5555', 'ryota14@example.com', 1, 'よろしくお願いします。', 6000, '2025-10-31 01:45:42', '2025-10-31 01:45:42', '本人確認済み', NULL, 'ryota_pass', 'id14.jpg', 1, 1, 1, 1, 0, 0, 1, '小林', '亮太', 'コバヤシ', 'リョウタ'),
(15, 'mai15', '1993-12-03', '080-5555-6666', 'mai15@example.com', 0, 'フォロワー募集中！', 8600, '2025-10-31 01:45:42', '2025-10-31 01:45:42', '本人確認済み', NULL, 'mai_pass', 'id15.jpg', 1, 1, 1, 1, 1, 1, 0, '吉田', '舞', 'ヨシダ', 'マイ'),
(16, 'daisuke16', '1982-07-14', '070-6666-7777', 'daisuke16@example.com', 1, 'たまに出品してます。', 3000, '2025-10-31 01:45:42', '2025-10-31 01:45:42', '凍結', NULL, 'daisuke_pass', 'id16.jpg', 0, 0, 0, 1, 0, 0, 0, '佐々木', '大輔', 'ササキ', 'ダイスケ'),
(17, 'kana17', '1998-11-25', '090-7777-8888', 'kana17@example.com', 0, '初心者です。', 1800, '2025-10-31 01:45:42', '2025-10-31 01:45:42', '本人確認済み', NULL, 'kana_pass', 'id17.jpg', 1, 1, 1, 1, 1, 1, 0, '山田', '佳奈', 'ヤマダ', 'カナ'),
(18, 'yuto18', '1990-02-22', '080-8888-9999', 'yuto18@example.com', 1, '最近始めました。', 2000, '2025-10-31 01:45:42', '2025-10-31 01:45:42', '本人確認済み', NULL, 'yuto_pass', 'id18.jpg', 1, 0, 1, 1, 0, 1, 1, '岡田', '悠斗', 'オカダ', 'ユウト'),
(19, 'nana19', '1999-06-06', '070-9999-0000', 'nana19@example.com', 0, '洋服好きです。', 9700, '2025-10-31 01:45:42', '2025-10-31 01:45:42', '本人確認済み', NULL, 'nana_pass', 'id19.jpg', 1, 1, 1, 1, 1, 1, 0, '井上', '奈々', 'イノウエ', 'ナナ'),
(20, 'akira20', '1986-01-01', '090-0000-1111', 'akira20@example.com', 1, 'よろしく。', 500, '2025-10-31 01:45:42', '2025-10-31 01:45:42', '本人確認済み', NULL, 'akira_pass', 'id20.jpg', 0, 0, 1, 0, 0, 1, 1, '川口', '明', 'カワグチ', 'アキラ');

-- --------------------------------------------------------

--
-- テーブルの構造 `m_address`
--

CREATE TABLE `m_address` (
  `id` int(11) NOT NULL,
  `account_id` int(11) NOT NULL,
  `zip` char(7) NOT NULL,
  `pref` varchar(10) NOT NULL,
  `address1` varchar(20) NOT NULL,
  `address2` varchar(20) NOT NULL,
  `address3` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `m_address`
--

INSERT INTO `m_address` (`id`, `account_id`, `zip`, `pref`, `address1`, `address2`, `address3`) VALUES
(1, 1, '1000001', '東京都', '千代田区', '丸の内1-1', 'サンプルビル101'),
(2, 2, '5400002', '大阪府', '大阪市中央区', '大手前2-2', 'ABCマンション202'),
(3, 3, '4600001', '愛知県', '名古屋市中区', '三の丸3-3', ''),
(4, 4, '8100001', '福岡県', '福岡市中央区', '天神4-4', '天神ビル5F'),
(5, 5, '0600005', '北海道', '札幌市中央区', '北5条西5丁目', 'JRタワー'),
(6, 1, '1000002', '東京都', '千代田区', '皇居外苑', '1-1');

-- --------------------------------------------------------

--
-- テーブルの構造 `m_adminaccount`
--

CREATE TABLE `m_adminaccount` (
  `id` int(11) NOT NULL,
  `fullName` varchar(100) NOT NULL,
  `level` enum('administrator','operator') NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `lastLogin` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `m_adminaccount`
--

INSERT INTO `m_adminaccount` (`id`, `fullName`, `level`, `created_at`, `lastLogin`, `password`) VALUES
(1, '中村輝', 'administrator', '2023-01-01 01:00:00', '2025-10-15 00:30:00', '1234'),
(2, '佐藤健吾', 'operator', '2023-02-10 02:20:00', '2025-10-15 23:00:00', 'pass_sato'),
(3, '鈴木美穂', 'operator', '2023-03-15 05:00:00', '2025-10-14 06:10:00', 'pass_suzuki'),
(4, '高橋大輔', 'operator', '2023-04-20 00:00:00', '2025-10-31 01:45:42', 'pass_takahashi'),
(5, '田中祐子', 'administrator', '2023-05-01 07:45:00', '2025-10-16 02:05:00', 'pass_tanaka');

-- --------------------------------------------------------

--
-- テーブルの構造 `m_admin_contents`
--

CREATE TABLE `m_admin_contents` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_detail` text NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `m_admin_contents`
--

INSERT INTO `m_admin_contents` (`id`, `name`, `content_detail`, `created_at`, `updated_at`) VALUES
(1, '利用規約', '本利用規約（以下「本規約」といいます。）は、[サービス名]（以下「本サービス」といいます。）の利用条件を定めるものです。\n本サービスを利用するすべての方（以下「ユーザー」といいます。）は、本規約に同意のうえでご利用ください。\n\n第1条（適用）\n本規約は、ユーザーと運営者（以下「当社」といいます。）との間の本サービスの利用に関わる一切の関係に適用されます。\n当社は、本規約のほか、ガイドライン・ポリシー等を定める場合があります。これらは本規約の一部を構成します。\n\n第2条（会員登録）\n本サービスの利用を希望する者は、本規約に同意し、当社所定の方法により登録を申請するものとします。\n登録希望者が以下の事由に該当すると当社が判断した場合、登録を承認しないことがあります。\n・虚偽の情報を登録した場合\n・過去に規約違反等により利用停止となった場合\n・その他、当社が不適当と判断した場合\n\n第3条（アカウント管理）\nユーザーは、自己の責任においてアカウントを管理するものとします。\nアカウントを第三者に譲渡、貸与することはできません。\n\n第4条（サービス内容）\n本サービスは、ユーザー間で衣服をレンタル・貸出するためのプラットフォームを提供するものです。\n当社は、取引当事者ではなく、ユーザー間の契約・トラブル等について責任を負いません。\n\n第5条（禁止事項）\nユーザーは、以下の行為をしてはなりません。\n・法令または公序良俗に違反する行為\n・他のユーザーまたは第三者の権利を侵害する行為\n・虚偽の情報を登録または提供する行為\n・レンタル品の無断転貸・転売・改変\n・当社のサービス運営を妨害する行為\n\n第6条（レンタル取引）\nユーザーは、出品者と利用者の間でレンタル契約を締結するものとし、契約条件（レンタル料、期間、返却方法等）は当事者間で合意するものとします。\nレンタル品の紛失・破損が発生した場合、当事者間で誠実に解決を図るものとします。\n当社は取引の内容、品質、履行について一切の責任を負いません。\n\n第7条（料金・支払い）\n本サービス利用に際し、ユーザーは当社所定の手数料を支払うものとします。\n支払い方法・返金条件は別途定めます。\n\n第8条（延滞・未返却）\n借り手は、合意された返却期限を遵守するものとします。\n返却が遅延した場合、出品者は延滞料金を請求できるものとします。\n未返却が発生した場合、当社はアカウント停止や法的措置の補助を行う場合があります。\n\n第9条（免責事項）\n当社は、サービスに関してユーザー間で生じた損害・トラブルについて一切の責任を負いません。\n天災・通信障害・システム不具合等によりサービス提供が困難となった場合も、当社は責任を負いません。\n\n第10条（退会）\nユーザーは、当社所定の手続きによりいつでも退会できます。ただし、未完了の取引がある場合はその履行を優先するものとします。\n\n第11条（規約の変更）\n当社は必要に応じて本規約を変更することができます。変更後の規約は、本サービス上に掲示した時点から効力を生じます。\n\n第12条（準拠法・管轄）\n本規約は、日本法に準拠します。\n本サービスに関して紛争が生じた場合、当社本店所在地を管轄する裁判所を第一審の専属的合意管轄とします。\n以上', '2023-01-01 01:00:00', '2025-09-15 05:30:00'),
(2, 'プライバシーポリシー', '1. 個人情報の取得\n当社は、適法かつ公正な手段によって、個人情報を取得します。\n2. 個人情報の利用目的\n当社は、取得した個人情報を、本サービスの提供、お問い合わせ対応、サービス向上のために利用します。\n3. 個人情報の第三者提供\n当社は、法令に定める場合を除き、個人情報を事前に本人の同意を得ることなく、第三者に提供しません。', '2023-01-01 01:05:00', '2025-08-20 02:00:00'),
(3, '特定商取引法に基づく表記', '【事業者名】株式会社サンプル\n【所在地】〒100-0001 東京都千代田区〇〇\n【連絡先】電話番号：03-1234-5678, メールアドレス：support@example.com\n【販売価格】商品ごとに表示\n【支払方法】クレジットカード、銀行振込\n【商品の引渡し時期】注文確定後、3営業日以内に発送します。', '2023-01-05 06:00:00', '2025-07-01 09:00:00');

-- --------------------------------------------------------

--
-- テーブルの構造 `m_bottomssize`
--

CREATE TABLE `m_bottomssize` (
  `product_id` int(11) NOT NULL,
  `hip` decimal(5,2) NOT NULL,
  `totalLength` decimal(5,2) NOT NULL,
  `rise` decimal(5,2) NOT NULL,
  `inseam` decimal(5,2) NOT NULL,
  `waist` decimal(5,2) NOT NULL,
  `thighWidth` decimal(5,2) NOT NULL,
  `hemWidth` decimal(5,2) NOT NULL,
  `skirtLength` decimal(5,2) NOT NULL,
  `notes` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `m_bottomssize`
--

INSERT INTO `m_bottomssize` (`product_id`, `hip`, `totalLength`, `rise`, `inseam`, `waist`, `thighWidth`, `hemWidth`, `skirtLength`, `notes`) VALUES
(6, 98.50, 102.00, 25.50, 76.50, 82.00, 29.00, 18.50, 0.00, 'ストレッチ素材。ローライズ。'),
(7, 95.00, 88.00, 0.00, 0.00, 68.00, 0.00, 0.00, 88.00, 'ウエスト後ろ部分ゴム入り。裏地付き。'),
(8, 100.00, 100.00, 28.00, 72.00, 78.00, 30.00, 22.00, 0.00, 'センタープレス入り。'),
(9, 96.00, 45.00, 26.00, 19.00, 74.00, 31.00, 28.00, 0.00, NULL),
(10, 92.00, 65.00, 0.00, 0.00, 70.00, 0.00, 0.00, 65.00, 'バックスリット有り。伸縮性なし。');

-- --------------------------------------------------------

--
-- テーブルの構造 `m_brand`
--

CREATE TABLE `m_brand` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `m_brand`
--

INSERT INTO `m_brand` (`id`, `name`) VALUES
(1, 'TRAVAS TOKYO'),
(2, 'REFLEM'),
(3, 'CIVARIZE'),
(4, 'ililil'),
(5, 'Valerie'),
(6, 'THICC PSYNYXX'),
(7, 'KINGLYMASK'),
(8, 'Amlige'),
(9, 'Meltier'),
(10, 'OY'),
(11, 'LIZ LISA'),
(12, 'Ank Rouge'),
(13, 'other');

-- --------------------------------------------------------

--
-- テーブルの構造 `m_category`
--

CREATE TABLE `m_category` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `m_category`
--

INSERT INTO `m_category` (`id`, `name`) VALUES
(1, 'コーデ'),
(2, 'トップス'),
(3, 'ボトムス'),
(4, 'アクセサリー');

-- --------------------------------------------------------

--
-- テーブルの構造 `m_cleansign`
--

CREATE TABLE `m_cleansign` (
  `id` int(11) NOT NULL,
  `cleanName` varchar(255) NOT NULL,
  `cleanImg` varchar(255) DEFAULT NULL,
  `cleanDetail` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `m_cleansign`
--

INSERT INTO `m_cleansign` (`id`, `cleanName`, `cleanImg`, `cleanDetail`) VALUES
(100, '洗濯処理', 'sentaku_100.png', '家庭での洗濯禁止'),
(110, '洗濯処理', 'sentaku_110.png', '液温は40℃を限度とし、手洗いができる'),
(111, '洗濯処理', 'sentaku_111.png', '液温は30℃を限度とし、手洗いができる'),
(130, '洗濯処理', 'sentaku_130.png', '液温は30℃を限度とし、洗濯機で洗濯ができる'),
(131, '洗濯処理', 'sentaku_131.png', '液温は30℃を限度とし、洗濯機で弱い洗濯ができる'),
(132, '洗濯処理', 'sentaku_132.png', '液温は30℃を限度とし、洗濯機で非常に弱い洗濯ができる'),
(140, '洗濯処理', 'sentaku_140.png', '液温は40℃を限度とし、洗濯機で洗濯ができる'),
(141, '洗濯処理', 'sentaku_141.png', '液温は40℃を限度とし、洗濯機で弱い洗濯ができる'),
(142, '洗濯処理', 'sentaku_142.png', '液温は40℃を限度とし、洗濯機で非常に弱い洗濯ができる'),
(150, '洗濯処理', 'sentaku_150.png', '液温は50℃を限度とし、洗濯機で洗濯ができる'),
(151, '洗濯処理', 'sentaku_151.png', '液温は50℃を限度とし、洗濯機で弱い洗濯ができる'),
(160, '洗濯処理', 'sentaku_160.png', '液温は60℃を限度とし、洗濯機で洗濯ができる'),
(161, '洗濯処理', 'sentaku_161.png', '液温は60℃を限度とし、洗濯機で弱い洗濯ができる'),
(170, '洗濯処理', 'sentaku_170.png', '液温は70℃を限度とし、洗濯機で洗濯ができる'),
(190, '洗濯処理', 'sentaku_190.png', '液温は95℃を限度とし、洗濯機で洗濯ができる'),
(200, '漂白処理', 'hyohaku_200.png', '塩素系及び酸素系漂白剤の使用禁止'),
(210, '漂白処理', 'hyohaku_210.png', '酸素系漂白剤の使用はできるが、塩素系漂白剤は使用禁止'),
(220, '漂白処理', 'hyohaku_220.png', '塩素系及び酸素系の漂白剤を使用して漂白ができる'),
(300, 'タンブル乾燥', 'tumble_300.png', 'タンブル乾燥禁止'),
(310, 'タンブル乾燥', 'tumble_310.png', '低い温度でのタンブル乾燥ができる（排気温度上限60℃）'),
(320, 'タンブル乾燥', 'tumble_320.png', 'タンブル乾燥ができる（排気温度上限80℃）'),
(410, '自然乾燥', 'shizen_410.png', 'ぬれ平干しがよい'),
(415, '自然乾燥', 'shizen_415.png', '日陰のぬれ平干しがよい'),
(420, '自然乾燥', 'shizen_420.png', '平干しがよい'),
(425, '自然乾燥', 'shizen_425.png', '日陰の平干しがよい'),
(430, '自然乾燥', 'shizen_430.png', 'ぬれつり干しがよい'),
(435, '自然乾燥', 'shizen_435.png', '日陰のぬれつり干しがよい'),
(440, '自然乾燥', 'shizen_440.png', 'つり干しがよい'),
(445, '自然乾燥', 'shizen_445.png', '日陰のつり干しがよい'),
(500, 'アイロン仕上げ', 'iron_500.png', 'アイロン仕上げ禁止'),
(510, 'アイロン仕上げ', 'iron_510.png', '底面温度120℃を限度としてアイロン仕上げができる'),
(511, 'アイロン仕上げ', 'iron_511.png', '底面温度120℃を限度としてスチームなしでアイロン仕上げができる'),
(520, 'アイロン仕上げ', 'iron_520.png', '底面温度160℃を限度としてアイロン仕上げができる'),
(530, 'アイロン仕上げ', 'iron_530.png', '底面温度210℃を限度としてアイロン仕上げができる'),
(600, 'ドライクリーニング', 'dry_600.png', 'ドライクリーニング禁止'),
(610, 'ドライクリーニング', 'dry_610.png', '石油系溶剤によるドライクリーニングができる'),
(611, 'ドライクリーニング', 'dry_611.png', '石油系溶剤による弱いドライクリーニングができる'),
(620, 'ドライクリーニング', 'dry_620.png', 'パークロロエチレン又は石油系溶剤によるドライクリーニングができる'),
(621, 'ドライクリーニング', 'dry_621.png', 'パークロロエチレン又は石油系溶剤による弱いドライクリーニングができる'),
(700, 'ウエットクリーニング', 'wet_700.png', 'ウエットクリーニング禁止'),
(710, 'ウエットクリーニング', 'wet_710.png', 'ウエットクリーニングができる'),
(711, 'ウエットクリーニング', 'wet_711.png', '弱い操作によるウエットクリーニングができる'),
(712, 'ウエットクリーニング', 'wet_712.png', '非常に弱い操作によるウエットクリーニングができる');

-- --------------------------------------------------------

--
-- テーブルの構造 `m_product`
--

CREATE TABLE `m_product` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `purchasePrice` int(11) DEFAULT NULL,
  `rentalPrice` int(11) DEFAULT NULL,
  `size` varchar(255) NOT NULL,
  `color` enum('ブラック','ホワイト','イエロー','グレー','ブラウン','グリーン','ブルー','パープル','ピンク','レッド','オレンジ') DEFAULT NULL,
  `for` enum('レディース','ユニセックス') NOT NULL,
  `upload` date NOT NULL,
  `showing` enum('公開','非公開','非表示') NOT NULL,
  `draft` tinyint(1) NOT NULL,
  `updateDate` datetime NOT NULL,
  `purchaseFlg` tinyint(1) NOT NULL,
  `rentalFlg` tinyint(1) NOT NULL,
  `explanation` text DEFAULT NULL,
  `account_id` int(11) NOT NULL,
  `brand_id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  `cleanNotes` text DEFAULT NULL,
  `smokingFlg` tinyint(1) NOT NULL,
  `returnAddress` varchar(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `m_product`
--

INSERT INTO `m_product` (`id`, `name`, `purchasePrice`, `rentalPrice`, `size`, `color`, `for`, `upload`, `showing`, `draft`, `updateDate`, `purchaseFlg`, `rentalFlg`, `explanation`, `account_id`, `brand_id`, `category_id`, `cleanNotes`, `smokingFlg`) VALUES
(1, '地雷系フリルブラウス', 5800, 1200, 'M', 'ホワイト', 'レディース', '2025-09-28', '公開', 0, '2025-09-28 13:00:00', 1, 0, 'レースのついた甘めのブラウス。', 1, 2, 1, '手洗い推奨', 0),
(2, 'オーバーシャツ', 7200, 1500, 'L', 'ブルー', 'ユニセックス', '2025-09-15', '公開', 0, '2025-09-15 10:00:00', 1, 1, 'ゆったりとしたシルエット。', 2, 1, 2, 'ネット使用', 0),
(3, 'モードチェーンネックレス', 3200, 800, 'Free', '', 'ユニセックス', '2025-08-01', '公開', 0, '2025-08-01 15:00:00', 1, 0, 'シンプルで存在感あるデザイン。', 3, 3, 3, NULL, 0),
(4, 'くすみピンクカーディガン', 6400, 1300, 'M', 'ピンク', 'レディース', '2025-07-25', '非公開', 0, '2025-07-25 11:00:00', 1, 0, '淡いピンクで柔らかい印象に。', 4, 2, 1, NULL, 0),
(5, 'グランジダメージデニム', 8900, 1600, 'L', 'ブルー', 'ユニセックス', '2025-07-18', '公開', 0, '2025-07-18 09:30:00', 1, 1, '古着風のユーズド加工。', 5, 1, 1, '洗濯機OK', 0),
(6, '黒地レーススカート', 7800, 1500, 'M', 'ブラック', 'レディース', '2025-07-02', '公開', 0, '2025-07-02 12:00:00', 1, 0, '地雷系にぴったりのレーススカート。', 1, 2, 1, 'ドライ推奨', 0),
(7, 'ダークアシメトリートップス', 6100, 1200, 'M', 'グレー', 'レディース', '2025-06-25', '公開', 0, '2025-06-25 14:10:00', 1, 0, '片側ショルダーのモード系トップス。', 3, 4, 2, NULL, 0),
(8, 'オーバーサイズパーカー', 7800, 1700, 'XL', 'ブラック', 'ユニセックス', '2025-06-10', '公開', 0, '2025-06-10 09:00:00', 1, 1, 'ストリート感のあるゆったりパーカー。', 2, 5, 2, '乾燥機不可', 0),
(9, 'ゆるだぼ古着風Tシャツ', 4200, 900, 'L', 'ブラウン', 'ユニセックス', '2025-05-30', '非公開', 0, '2025-05-30 13:00:00', 1, 0, '味のあるくすみカラー。', 6, 3, 2, '手洗い可', 0),
(10, '地雷系リボンカチューシャ', 2800, 700, 'Free', 'ブラック', 'レディース', '2025-05-15', '公開', 0, '2025-05-15 16:30:00', 1, 0, 'ふんわりリボンがポイント。', 7, 2, 3, NULL, 0),
(11, 'チェック柄プリーツスカート', 6800, 1500, 'S', 'グレー', 'レディース', '2025-05-02', '公開', 0, '2025-05-02 09:45:00', 1, 0, 'スクール風で地雷にも量産にも合う。', 8, 1, 1, NULL, 0),
(12, 'パンクスタッズベルト', 3500, 800, 'Free', 'ブラック', 'ユニセックス', '2025-04-18', '公開', 0, '2025-04-18 11:00:00', 1, 0, 'シルバースタッズが印象的。', 9, 4, 3, NULL, 0),
(13, 'スモーキーグレーニット', 7200, 1400, 'M', 'グレー', 'ユニセックス', '2025-04-05', '非公開', 0, '2025-04-05 10:00:00', 1, 1, 'くすみカラーの柔らかいニット。', 10, 2, 2, 'ネット洗い', 0),
(14, 'レトロ刺繍ブラウス', 6500, 1300, 'M', 'ホワイト', 'レディース', '2025-03-25', '公開', 0, '2025-03-25 13:00:00', 1, 0, 'アンティーク調の刺繍デザイン。', 11, 3, 1, NULL, 0),
(15, 'クラッシュデニムパンツ', 8400, 1600, 'L', 'ブルー', 'ユニセックス', '2025-03-10', '公開', 0, '2025-03-10 14:30:00', 1, 1, 'ラフなクラッシュ加工入り。', 12, 1, 1, '裏返し洗い', 0),
(16, '黒蝶ネックレス', 3900, 850, 'Free', 'ブラック', 'レディース', '2025-02-28', '公開', 0, '2025-02-28 12:10:00', 1, 0, '地雷系の定番黒蝶モチーフ。', 13, 4, 3, NULL, 0),
(17, 'ゆめかわハートイヤリング', 3100, 750, 'Free', 'ピンク', 'レディース', '2025-02-20', '非公開', 0, '2025-02-20 11:30:00', 1, 0, '量産型に人気のアクセ。', 14, 2, 3, NULL, 0),
(18, 'グラデーションスウェット', 7600, 1600, 'L', 'パープル', 'ユニセックス', '2025-02-05', '公開', 0, '2025-02-05 13:00:00', 1, 1, '淡いグラデが特徴のストリート風。', 15, 5, 2, NULL, 0),
(19, 'フェイクレザージャケット', 9500, 2000, 'M', 'ブラック', 'ユニセックス', '2025-01-28', '公開', 0, '2025-01-28 09:00:00', 1, 1, '韓国風のシンプルなレザージャケット。', 16, 1, 1, '乾燥機不可', 0),
(20, 'ダークフリルワンピース', 8800, 1700, 'M', 'ブラック', 'レディース', '2025-01-15', '公開', 0, '2025-01-15 12:00:00', 1, 0, 'ゴシック地雷系に人気のワンピース。', 17, 3, 1, 'ドライ推奨', 0);

--
-- トリガ `m_product`
--
DELIMITER $$
CREATE TRIGGER `trg_product_price_change` AFTER UPDATE ON `m_product` FOR EACH ROW BEGIN

    
    
    
    IF NOT (NEW.purchasePrice <=> OLD.purchasePrice) OR 
       NOT (NEW.rentalPrice <=> OLD.rentalPrice) THEN
        
        
        
        
        INSERT INTO `t_time` (
            `account_id`,       
            `product_id`,       
            `product_change`    
        )
        VALUES (
            NEW.account_id,     
            NEW.id,             
            '料金変更'
        );
        
    END IF;
    
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- テーブルの構造 `m_productimg`
--

CREATE TABLE `m_productimg` (
  `id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `img` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `m_productimg`
--

INSERT INTO `m_productimg` (`id`, `product_id`, `img`) VALUES
(1, 1, 'img/00000000001_01.png'),
(2, 1, 'img/00000000001_02.png'),
(3, 1, 'img/00000000001_03.png'),
(4, 2, 'img/00000000002_01.png'),
(5, 2, 'img/00000000002_02.png'),
(6, 2, 'img/00000000002_03.png'),
(7, 3, 'img/00000000003_01.png'),
(8, 3, 'img/00000000003_02.png'),
(9, 3, 'img/00000000003_03.png'),
(10, 4, 'img/00000000001_01.png'),
(11, 4, 'img/00000000001_02.png'),
(12, 4, 'img/00000000001_03.png'),
(13, 5, 'img/00000000002_01.png'),
(14, 5, 'img/00000000002_02.png'),
(15, 5, 'img/00000000002_03.png'),
(16, 6, 'img/00000000003_01.png'),
(17, 6, 'img/00000000003_02.png'),
(18, 6, 'img/00000000003_03.png'),
(19, 7, 'img/00000000001_01.png'),
(20, 7, 'img/00000000001_02.png'),
(21, 7, 'img/00000000001_03.png'),
(22, 8, 'img/00000000002_01.png'),
(23, 8, 'img/00000000002_02.png'),
(24, 8, 'img/00000000002_03.png'),
(25, 9, 'img/00000000003_01.png'),
(26, 9, 'img/00000000003_02.png'),
(27, 9, 'img/00000000003_03.png'),
(28, 10, 'img/00000000001_01.png'),
(29, 10, 'img/00000000001_02.png'),
(30, 10, 'img/00000000001_03.png'),
(31, 11, 'img/00000000002_01.png'),
(32, 11, 'img/00000000002_02.png'),
(33, 11, 'img/00000000002_03.png'),
(34, 12, 'img/00000000003_01.png'),
(35, 12, 'img/00000000003_02.png'),
(36, 12, 'img/00000000003_03.png'),
(37, 13, 'img/00000000001_01.png'),
(38, 13, 'img/00000000001_02.png'),
(39, 13, 'img/00000000001_03.png'),
(40, 14, 'img/00000000002_01.png'),
(41, 14, 'img/00000000002_02.png'),
(42, 14, 'img/00000000002_03.png'),
(43, 15, 'img/00000000003_01.png'),
(44, 15, 'img/00000000003_02.png'),
(45, 15, 'img/00000000003_03.png'),
(46, 16, 'img/00000000001_01.png'),
(47, 16, 'img/00000000001_02.png'),
(48, 16, 'img/00000000001_03.png'),
(49, 17, 'img/00000000002_01.png'),
(50, 17, 'img/00000000002_02.png'),
(51, 17, 'img/00000000002_03.png'),
(52, 18, 'img/00000000003_01.png'),
(53, 18, 'img/00000000003_02.png'),
(54, 18, 'img/00000000003_03.png'),
(55, 19, 'img/00000000001_01.png'),
(56, 19, 'img/00000000001_02.png'),
(57, 19, 'img/00000000001_03.png'),
(58, 20, 'img/00000000002_01.png'),
(59, 20, 'img/00000000002_02.png'),
(60, 20, 'img/00000000002_03.png');

-- --------------------------------------------------------

--
-- テーブルの構造 `m_topssize`
--

CREATE TABLE `m_topssize` (
  `product_id` int(11) NOT NULL,
  `shoulderWidth` decimal(5,2) NOT NULL,
  `bodyWidth` decimal(5,2) NOT NULL,
  `sleeveLength` decimal(5,2) NOT NULL,
  `bodyLength` decimal(5,2) NOT NULL,
  `notes` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `m_topssize`
--

INSERT INTO `m_topssize` (`product_id`, `shoulderWidth`, `bodyWidth`, `sleeveLength`, `bodyLength`, `notes`) VALUES
(1, 48.00, 55.00, 22.00, 72.00, 'Lサイズ相当 (80s ヴィンテージTシャツ)'),
(2, 45.50, 52.00, 60.50, 70.00, 'Mサイズ相当 (デニムジャケット)'),
(5, 46.00, 54.00, 61.00, 90.00, 'Mサイズ (ウールロングコート)');

-- --------------------------------------------------------

--
-- テーブルの構造 `t_adminlogin`
--

CREATE TABLE `t_adminlogin` (
  `id` int(11) NOT NULL,
  `adminAccount_id` int(11) NOT NULL,
  `loginDatetime` datetime DEFAULT NULL,
  `logoutDatetime` datetime DEFAULT NULL,
  `flag` tinyint(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `t_adminlogin`
--

INSERT INTO `t_adminlogin` (`id`, `adminAccount_id`, `loginDatetime`, `logoutDatetime`, `flag`) VALUES
(1, 1, '2025-10-15 09:30:00', '2025-10-15 18:00:00', 1),
(2, 2, '2025-10-16 08:00:00', '2025-10-16 12:30:00', 1),
(3, 3, '2025-10-14 15:10:00', '2025-10-14 19:00:00', 1),
(4, 5, '2025-10-16 11:05:00', '2025-10-16 11:30:00', 1),
(5, 4, '2025-10-18 10:00:00', NULL, 0),
(6, 4, '2025-10-18 10:01:00', '2025-10-18 15:00:00', 1),
(7, 1, '2025-10-20 09:00:00', NULL, 0),
(8, 1, '2025-10-20 09:01:00', NULL, 1),
(9, 2, '2025-10-25 14:00:00', NULL, 1),
(10, 5, '2025-10-26 10:00:00', '2025-10-26 18:00:00', 1);

-- --------------------------------------------------------

--
-- テーブルの構造 `t_alert`
--

CREATE TABLE `t_alert` (
  `id` int(11) NOT NULL,
  `product_id` int(11) DEFAULT NULL,
  `content` text DEFAULT NULL,
  `category` enum('通報','警告') DEFAULT NULL,
  `reportDate` datetime DEFAULT NULL,
  `comment_id` int(11) DEFAULT NULL,
  `sender_id` int(11) DEFAULT NULL,
  `recipient_id` int(11) DEFAULT NULL,
  `transaction_id` int(11) DEFAULT NULL,
  `adminAccount_id` int(11) DEFAULT NULL,
  `manageDate` datetime DEFAULT NULL,
  `reportMemo` text DEFAULT NULL,
  `situation` enum('未対応','対応中','対応済み') DEFAULT NULL,
  `reportType` enum('商品','ユーザー','取引','その他') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `t_alert`
--

INSERT INTO `t_alert` (`id`, `product_id`, `content`, `category`, `reportDate`, `comment_id`, `sender_id`, `recipient_id`, `transaction_id`, `adminAccount_id`, `manageDate`, `reportMemo`, `situation`, `reportType`) VALUES
(1, 1, '商品説明に「レア」とありますが、根拠が不明です。虚偽の可能性があります。', '通報', '2025-10-21 10:00:00', NULL, 2, 1, NULL, NULL, NULL, NULL, '未対応', '商品'),
(2, NULL, '過度な値下げ交渉です。', '通報', '2025-10-21 14:05:00', 3, 2, 5, NULL, 1, NULL, '値下げ交渉のレベルを精査中。', '対応中', 'ユーザー'),
(3, NULL, '発送通知があったのに、追跡番号が反映されません。', '通報', '2025-10-24 18:00:00', NULL, 2, 4, 5, 2, '2025-10-25 10:00:00', '出品者に連絡。入力ミスと判明。取引メッセージで謝罪済み。クローズ。', '対応済み', '取引'),
(4, NULL, '利用規約第X条に基づき、過度な値下げ交渉はお控えください。', '警告', '2025-10-21 18:00:00', NULL, NULL, 5, NULL, 1, '2025-10-21 18:00:00', '通報(ID 2)に基づき、警告を実施。', '対応済み', 'ユーザー'),
(5, 3, '偽ブランド品の可能性があります。', '通報', '2025-10-25 15:00:00', NULL, 4, 3, NULL, 5, '2025-10-26 10:00:00', '鑑定の結果、規約違反品と断定。商品(ID 3)を削除。', '対応済み', '商品'),
(6, NULL, '出品禁止物（偽ブランド品）の出品を確認しました。アカウントを一時停止します。', '警告', '2025-10-26 10:05:00', NULL, NULL, 3, NULL, 5, '2025-10-26 10:05:00', '通報(ID 5)に基づき対応。', '対応済み', 'ユーザー'),
(7, NULL, '返却期限を過ぎても返送されません。', '通報', '2025-11-02 10:00:00', NULL, 1, 3, 2, NULL, NULL, NULL, '未対応', '取引'),
(8, NULL, 'アプリの動作が不安定です。カテゴリ検索がうまく動きません。', '通報', '2025-10-27 10:00:00', NULL, 5, NULL, NULL, NULL, NULL, NULL, '未対応', 'その他'),
(9, NULL, 'プロフィール画像が不適切です。', '通報', '2025-10-26 13:00:00', NULL, 1, 4, NULL, 3, NULL, 'ガイドラインと照合中。', '対応中', 'ユーザー'),
(10, NULL, '返信の態度が高圧的で不快です。', '通報', '2025-10-23 19:30:00', 8, 3, 1, NULL, 2, '2025-10-24 10:00:00', 'コメント(ID 8)を確認。高圧的とは判断できず。介入不要と判断しクローズ。', '対応済み', 'ユーザー');

--
-- トリガ `t_alert`
--
DELIMITER $$
CREATE TRIGGER `trg_alert_warning_to_timeline` AFTER INSERT ON `t_alert` FOR EACH ROW BEGIN
    
    
    
    
    IF NEW.category = '警告' AND NEW.recipient_id IS NOT NULL THEN
    
        
        INSERT INTO `t_time` (
            `account_id`,   
            `alert_id`      
        )
        VALUES (
            NEW.recipient_id, 
            NEW.id            
        );
        
    END IF;
    
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- テーブルの構造 `t_clean`
--

CREATE TABLE `t_clean` (
  `product_id` int(11) NOT NULL,
  `cleanSign_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `t_clean`
--

INSERT INTO `t_clean` (`product_id`, `cleanSign_id`) VALUES
(1, 141),
(1, 200),
(1, 300),
(1, 445),
(1, 520),
(1, 600),
(1, 711),
(2, 130),
(2, 200),
(2, 300),
(2, 440),
(2, 520),
(3, 100),
(3, 200),
(3, 300),
(3, 440),
(3, 500),
(3, 600),
(4, 110),
(4, 200),
(4, 300),
(4, 445),
(5, 100),
(5, 200),
(5, 300),
(5, 510),
(5, 611),
(5, 700);

-- --------------------------------------------------------

--
-- テーブルの構造 `t_comments`
--

CREATE TABLE `t_comments` (
  `id` int(11) NOT NULL,
  `account_id` int(11) NOT NULL,
  `content` text NOT NULL,
  `createdDate` timestamp NOT NULL DEFAULT current_timestamp(),
  `product_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `t_comments`
--

INSERT INTO `t_comments` (`id`, `account_id`, `content`, `createdDate`, `product_id`) VALUES
(1, 2, 'コメント失礼します。こちら着丈と身幅を教えていただけますでしょうか？', '2025-10-20 01:00:00', 1),
(2, 1, '鈴木様 コメントありがとうございます。着丈70cm、身幅55cmとなります。ご検討ください。', '2025-10-20 02:30:00', 1),
(3, 5, '13000円で即決させていただけないでしょうか？', '2025-10-21 05:00:00', 2),
(4, 2, '伊藤様 コメントありがとうございます。出品したばかりですので、そこまでのお値下げは考えておりません。申し訳ありません。', '2025-10-21 06:00:00', 2),
(5, 1, '購入を検討しています。出品者様は喫煙者とのことですが、商品に匂いはついていますでしょうか？', '2025-10-22 00:15:00', 5),
(6, 4, '谷口様 コメントありがとうございます。別室で保管しておりましたが、敏感な方は気になるかもしれません。クリーニング後の発送となります。', '2025-10-22 01:00:00', 5),
(7, 3, '箱は付属しますか？', '2025-10-23 09:00:00', 4),
(8, 1, '佐藤様 付属しません。現品のみとなります。', '2025-10-23 10:00:00', 4),
(9, 2, 'こちらの商品、まだ購入可能でしょうか？', '2025-10-24 03:00:00', 3),
(10, 1, '運営です。利用規約が変更されましたのでご確認ください。', '2025-10-24 15:00:00', NULL);

--
-- トリガ `t_comments`
--
DELIMITER $$
CREATE TRIGGER `trg_notify_favorite_users_on_comment` AFTER INSERT ON `t_comments` FOR EACH ROW BEGIN
    
    
    
    
    
    
    INSERT INTO `t_time` (
        `account_id`,       
        `comments_id`,      
        `product_id`,       
        `product_change`    
    )
    SELECT
        tf.account_id,      
        NEW.id,             
        NEW.product_id,     
        'コメント'            
    FROM
        `t_favorite` AS tf
    WHERE
        tf.product_id = NEW.product_id  
        
        
        AND tf.account_id != NEW.account_id;

END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- テーブルの構造 `t_connection`
--

CREATE TABLE `t_connection` (
  `id` int(11) NOT NULL,
  `execution_id` int(11) NOT NULL,
  `target_id` int(11) NOT NULL,
  `Datetime` timestamp NOT NULL DEFAULT current_timestamp(),
  `type` enum('フォロー','ブロック') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `t_connection`
--

INSERT INTO `t_connection` (`id`, `execution_id`, `target_id`, `Datetime`, `type`) VALUES
(1, 1, 2, '2025-01-15 01:30:00', 'フォロー'),
(2, 1, 3, '2025-01-16 02:00:00', 'フォロー'),
(3, 1, 5, '2025-05-20 00:15:00', 'ブロック'),
(4, 2, 1, '2025-01-15 03:00:00', 'フォロー'),
(5, 2, 4, '2025-03-10 09:00:00', 'フォロー'),
(6, 3, 1, '2025-02-01 05:20:00', 'フォロー'),
(7, 3, 4, '2025-08-05 13:00:00', 'ブロック'),
(8, 4, 3, '2025-08-05 23:00:00', 'ブロック'),
(9, 4, 1, '2025-09-01 10:30:00', 'フォロー'),
(10, 5, 1, '2025-05-19 01:00:00', 'フォロー');

-- --------------------------------------------------------

--
-- テーブルの構造 `t_creditcard`
--

CREATE TABLE `t_creditcard` (
  `id` int(11) NOT NULL,
  `account_id` int(11) NOT NULL,
  `number` varchar(20) NOT NULL,
  `expiry` char(5) NOT NULL,
  `holderName` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `t_creditcard`
--

INSERT INTO `t_creditcard` (`id`, `account_id`, `number`, `expiry`, `holderName`) VALUES
(1, 1, '4980123456789012', '12/26', 'MASAYA TANIGUCHI'),
(2, 1, '5100987654321098', '05/28', 'MASAYA TANIGUCHI'),
(3, 1, '3560111122223333', '09/27', 'MASAYA TANIGUCHI'),
(4, 2, '4200123456780000', '01/29', 'HANAKO SUZUKI'),
(5, 2, '5500987654329999', '11/25', 'HANAKO SUZUKI'),
(6, 3, '4980888877776666', '07/26', 'JIRO SATO'),
(7, 4, '5200111122223333', '03/28', 'SABURO TAKAHASHI'),
(8, 4, '4900123456781111', '06/27', 'SABURO TAKAHASHI'),
(9, 4, '3750999988887777', '10/29', 'SABURO TAKAHASHI'),
(10, 5, '5100444455556666', '08/25', 'SHIRO ITO');

-- --------------------------------------------------------

--
-- テーブルの構造 `t_evaluation`
--

CREATE TABLE `t_evaluation` (
  `id` int(11) NOT NULL,
  `transaction_id` int(11) NOT NULL,
  `score` int(11) NOT NULL,
  `comment` text DEFAULT NULL,
  `evaluationTime` timestamp NOT NULL DEFAULT current_timestamp(),
  `productCheck` tinyint(1) NOT NULL,
  `recipient_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `t_evaluation`
--

INSERT INTO `t_evaluation` (`id`, `transaction_id`, `score`, `comment`, `evaluationTime`, `productCheck`, `recipient_id`) VALUES
(1, 1, 5, 'スムーズな取引ありがとうございました。商品も綺麗でした。', '2025-09-04 01:00:00', 1, 2),
(2, 1, 5, '受け取り連絡ありがとうございました。', '2025-09-04 02:00:00', 0, 1),
(3, 8, 2, '商品説明と少し色が違いました。', '2025-08-18 00:15:00', 0, 1),
(4, 8, 5, 'ありがとうございました。', '2025-08-18 01:00:00', 0, 4),
(5, 7, 5, NULL, '2025-10-26 04:00:00', 1, 4),
(6, 7, 5, NULL, '2025-10-26 04:05:00', 0, 3),
(7, 6, 3, '商品は良かったですが、発送が少し遅かったです。', '2025-09-23 09:00:00', 1, 3),
(8, 6, 5, 'ご返却ありがとうございました。', '2025-09-24 00:00:00', 0, 1),
(9, 10, 5, '素敵な商品をありがとうございました！', '2025-10-28 01:00:00', 1, 1),
(10, 10, 5, 'またのご利用をお待ちしております。', '2025-10-28 01:30:00', 0, 2);

--
-- トリガ `t_evaluation`
--
DELIMITER $$
CREATE TRIGGER `trg_evaluation_to_timeline` AFTER INSERT ON `t_evaluation` FOR EACH ROW BEGIN
    
    
    
    
    INSERT INTO `t_time` (
        `account_id`,       
        `evaluation_id`,    
        `transaction_id`    
    )
    VALUES (
        NEW.recipient_id,   
        NEW.id,             
        NEW.transaction_id  
    );

END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- テーブルの構造 `t_favorite`
--

CREATE TABLE `t_favorite` (
  `id` int(11) NOT NULL,
  `account_id` int(11) NOT NULL,
  `product_id` int(11) DEFAULT NULL,
  `brand_id` int(11) DEFAULT NULL,
  `resisterTime` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `t_favorite`
--

INSERT INTO `t_favorite` (`id`, `account_id`, `product_id`, `brand_id`, `resisterTime`) VALUES
(1, 1, 5, NULL, '2025-10-31 01:45:43'),
(2, 1, 2, NULL, '2025-10-31 01:45:43'),
(3, 2, 1, NULL, '2025-10-31 01:45:43'),
(4, 2, 3, NULL, '2025-10-31 01:45:43'),
(5, 3, 1, NULL, '2025-10-31 01:45:43'),
(6, 4, 4, NULL, '2025-10-31 01:45:43'),
(7, 5, 3, NULL, '2025-10-31 01:45:43'),
(8, 1, NULL, 1, '2025-10-31 01:45:43'),
(9, 2, NULL, 3, '2025-10-31 01:45:43'),
(10, 4, NULL, 12, '2025-10-31 01:45:43');

-- --------------------------------------------------------

--
-- テーブルの構造 `t_history`
--

CREATE TABLE `t_history` (
  `id` int(11) NOT NULL,
  `account_id` int(11) NOT NULL,
  `transaction_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `datetime` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `t_history`
--

INSERT INTO `t_history` (`id`, `account_id`, `transaction_id`, `product_id`, `datetime`) VALUES
(1, 1, NULL, 1, '2025-10-31 01:45:43'),
(2, 1, NULL, 2, '2025-10-31 01:45:43'),
(3, 2, NULL, 3, '2025-10-31 01:45:43'),
(4, 2, NULL, 5, '2025-10-31 01:45:43'),
(5, 3, NULL, 1, '2025-10-31 01:45:43'),
(6, 4, NULL, 4, '2025-10-31 01:45:43'),
(7, 5, NULL, 3, '2025-10-31 01:45:43'),
(8, 1, 1, NULL, '2025-10-31 01:45:43'),
(9, 2, 5, NULL, '2025-10-31 01:45:43'),
(10, 4, 3, NULL, '2025-10-31 01:45:43');

-- --------------------------------------------------------

--
-- テーブルの構造 `t_inquiry`
--

CREATE TABLE `t_inquiry` (
  `id` int(11) NOT NULL,
  `sender_id` int(11) NOT NULL,
  `content` text NOT NULL,
  `timeSent` timestamp NOT NULL DEFAULT current_timestamp(),
  `product_id` int(11) DEFAULT NULL,
  `adminAccount_id` int(11) DEFAULT NULL,
  `replyDetail` text NOT NULL,
  `replyDate` datetime DEFAULT NULL,
  `situation` enum('未対応','対応中','対応済み') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `t_inquiry`
--

INSERT INTO `t_inquiry` (`id`, `sender_id`, `content`, `timeSent`, `product_id`, `adminAccount_id`, `replyDetail`, `replyDate`, `situation`) VALUES
(1, 1, '退会方法を教えてください。', '2025-10-27 01:00:00', NULL, NULL, '', NULL, '未対応'),
(2, 2, '商品ID 4 のスニーカーは正規品ですか？', '2025-10-27 02:00:00', 4, NULL, '', NULL, '未対応'),
(3, 3, '本人確認書類を再提出したいです。', '2025-10-26 06:00:00', NULL, 1, '担当部署に確認中です。', NULL, '対応中'),
(4, 4, 'パスワードを忘れました。', '2025-10-25 00:00:00', NULL, 2, 'ログイン画面の「パスワードを忘れた場合」より再設定をお願いいたします。', '2025-10-25 09:30:00', '対応済み'),
(5, 5, '商品ID 2 のジャケットの送料はいくらですか？', '2025-10-24 01:00:00', 2, 3, 'お問い合わせありがとうございます。送料は出品者様の設定によりますが、当該商品は「送料込み」となっております。', '2025-10-24 11:00:00', '対応済み'),
(6, 1, '取引(ID 8)で悪い評価を付けられましたが、納得いきません。', '2025-08-20 01:00:00', NULL, 5, 'ご連絡ありがとうございます。恐れ入りますが、一度投稿された評価の変更は、双方の合意がない限り運営側では介入できかねます。', '2025-08-20 14:00:00', '対応済み'),
(7, 2, '売上金の振込申請をしましたが、まだ振り込まれません。', '2025-10-27 05:00:00', NULL, NULL, '', NULL, '未対応'),
(8, 4, 'アプリが頻繁にクラッシュします。 (OS: iOS 19.0)', '2025-10-26 11:00:00', NULL, 1, '開発チームに報告し、調査中です。ご迷惑をおかけしております。', '2025-10-27 09:00:00', '対応中'),
(9, 3, '商品ID 5 のコートのレンタルを延長したいです。', '2025-10-22 01:00:00', 5, 2, 'レンタル期間の延長は、一度商品を返却いただいた後の再注文となります。', '2025-10-22 11:30:00', '対応済み'),
(10, 5, 'こんにちは', '2025-10-20 01:00:00', NULL, 3, 'お問い合わせありがとうございます。具体的なご用件をお伺いできますでしょうか。 ※本件は一旦クローズいたします。', '2025-10-20 10:05:00', '対応済み');

--
-- トリガ `t_inquiry`
--
DELIMITER $$
CREATE TRIGGER `trg_inquiry_admin_assigned_update` AFTER UPDATE ON `t_inquiry` FOR EACH ROW BEGIN
    
    
    IF OLD.adminAccount_id IS NULL AND NEW.adminAccount_id IS NOT NULL THEN
    
        
        INSERT INTO `t_time` (
            `account_id`,   
            `inquiry_id`,
            `product_id`
        )
        VALUES (
            NEW.sender_id,  
            NEW.id,
            NEW.product_id
        );
        
    END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- テーブルの構造 `t_login`
--

CREATE TABLE `t_login` (
  `id` int(11) NOT NULL,
  `account_id` int(11) NOT NULL,
  `loginDatetime` datetime DEFAULT NULL,
  `logoutDatetime` datetime DEFAULT NULL,
  `notice` tinyint(1) DEFAULT NULL,
  `flag` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `t_login`
--

INSERT INTO `t_login` (`id`, `account_id`, `loginDatetime`, `logoutDatetime`, `notice`, `flag`) VALUES
(1, 1, '2025-10-26 10:00:00', '2025-10-26 11:00:00', 1, 0),
(2, 2, '2025-10-25 15:30:00', '2025-10-25 16:00:00', 0, 0),
(3, 3, '2025-10-24 09:15:00', NULL, 1, 1),
(4, 4, '2025-10-20 20:05:00', '2025-10-20 22:30:00', 0, 1),
(5, 5, '2025-10-15 11:00:00', '2025-10-15 11:30:00', 1, 0),
(6, 6, '2025-10-10 08:00:00', NULL, 0, 0),
(7, 7, '2025-09-30 18:45:00', '2025-09-30 19:00:00', 1, 0),
(8, 8, '2025-09-15 14:20:00', '2025-09-15 18:00:00', 0, 1),
(9, 9, '2025-09-05 23:00:00', '2025-09-06 01:00:00', 1, 0),
(10, 10, '2025-08-28 07:30:00', NULL, 1, 1);

--
-- トリガ `t_login`
--
DELIMITER $$
CREATE TRIGGER `trg_after_insert_login` AFTER INSERT ON `t_login` FOR EACH ROW BEGIN
    
    INSERT INTO t_time (
        account_id,  
        login_id     
    )
    VALUES (
        NEW.account_id,  
        NEW.id           
    );
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- テーブルの構造 `t_message`
--

CREATE TABLE `t_message` (
  `id` int(11) NOT NULL,
  `sender_id` int(11) NOT NULL,
  `recipient_id` int(11) NOT NULL,
  `transaction_id` int(11) NOT NULL,
  `content` varchar(255) NOT NULL,
  `sendingTime` timestamp NOT NULL DEFAULT current_timestamp(),
  `readStatus` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `t_message`
--

INSERT INTO `t_message` (`id`, `sender_id`, `recipient_id`, `transaction_id`, `content`, `sendingTime`, `readStatus`) VALUES
(1, 2, 1, 1, 'ご購入ありがとうございます。本日発送いたします。', '2025-09-01 01:30:00', 1),
(2, 1, 2, 1, 'ありがとうございます。商品受け取りました。', '2025-09-03 06:00:00', 1),
(3, 1, 3, 2, '発送しました。到着まで今しばらくお待ちください。', '2025-10-25 06:00:00', 1),
(4, 3, 1, 2, '本日受け取りました。ありがとうございました。', '2025-10-26 09:00:00', 1),
(5, 5, 1, 4, '購入しました。いつ頃発送予定でしょうか？', '2025-10-26 10:00:00', 1),
(6, 1, 5, 4, '伊藤様 ご購入ありがとうございます。明日発送予定です。', '2025-10-27 00:00:00', 0),
(7, 4, 2, 5, '発送いたしました。追跡番号はXXX-XXXX-XXXXです。', '2025-10-24 03:00:00', 1),
(8, 2, 4, 5, '承知いたしました。よろしくお願いいたします。', '2025-10-24 04:00:00', 1),
(9, 4, 3, 7, '発送しました。2日ほどで到着予定です。', '2025-10-20 00:00:00', 1),
(10, 4, 3, 7, '商品は到着していますでしょうか？お手数ですが受取評価をお願いします。', '2025-10-25 01:00:00', 0);

--
-- トリガ `t_message`
--
DELIMITER $$
CREATE TRIGGER `trg_message_to_timeline` AFTER INSERT ON `t_message` FOR EACH ROW BEGIN
    
    
    
    
    INSERT INTO `t_time` (
        `account_id`,       
        `message_id`,       
        `transaction_id`    
    )
    VALUES (
        NEW.recipient_id,   
        NEW.id,             
        NEW.transaction_id  
    );

END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- テーブルの構造 `t_rentalperiod`
--

CREATE TABLE `t_rentalperiod` (
  `id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `rentalPeriod` enum('4日','7日','14日') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `t_rentalperiod`
--

INSERT INTO `t_rentalperiod` (`id`, `product_id`, `rentalPeriod`) VALUES
(1, 1, '4日'),
(2, 1, '7日'),
(3, 3, '7日'),
(4, 3, '14日'),
(5, 4, '4日'),
(6, 4, '7日'),
(7, 4, '14日'),
(8, 5, '14日');

-- --------------------------------------------------------

--
-- テーブルの構造 `t_time`
--

CREATE TABLE `t_time` (
  `id` int(11) NOT NULL,
  `account_id` int(11) NOT NULL,
  `login_id` int(11) DEFAULT NULL,
  `comments_id` int(11) DEFAULT NULL,
  `alert_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `message_id` int(11) DEFAULT NULL,
  `inquiry_id` int(11) DEFAULT NULL,
  `transaction_id` int(11) DEFAULT NULL,
  `transaction_status` enum('支払い待ち','発送待ち','配達中','到着','レンタル中','クリーニング期間','発送待ち','取引完了') DEFAULT NULL,
  `evaluation_id` int(11) DEFAULT NULL,
  `product_change` enum('料金変更','取引状態遷移','コメント') DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `t_time`
--

INSERT INTO `t_time` (`id`, `account_id`, `login_id`, `comments_id`, `alert_id`, `product_id`, `message_id`, `inquiry_id`, `transaction_id`, `transaction_status`, `evaluation_id`, `product_change`, `created_at`) VALUES
(1, 1, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2025-10-31 01:45:43'),
(2, 2, 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2025-10-31 01:45:43'),
(3, 3, 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2025-10-31 01:45:43'),
(4, 4, 4, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2025-10-31 01:45:43'),
(5, 5, 5, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2025-10-31 01:45:43'),
(6, 6, 6, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2025-10-31 01:45:43'),
(7, 7, 7, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2025-10-31 01:45:43'),
(8, 8, 8, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2025-10-31 01:45:43'),
(9, 9, 9, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2025-10-31 01:45:43'),
(10, 10, 10, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2025-10-31 01:45:43'),
(11, 3, NULL, 1, NULL, 1, NULL, NULL, NULL, NULL, NULL, 'コメント', '2025-10-31 01:45:43'),
(12, 2, NULL, 2, NULL, 1, NULL, NULL, NULL, NULL, NULL, 'コメント', '2025-10-31 01:45:43'),
(13, 3, NULL, 2, NULL, 1, NULL, NULL, NULL, NULL, NULL, 'コメント', '2025-10-31 01:45:43'),
(15, 1, NULL, 3, NULL, 2, NULL, NULL, NULL, NULL, NULL, 'コメント', '2025-10-31 01:45:43'),
(16, 1, NULL, 4, NULL, 2, NULL, NULL, NULL, NULL, NULL, 'コメント', '2025-10-31 01:45:43'),
(17, 1, NULL, 6, NULL, 5, NULL, NULL, NULL, NULL, NULL, 'コメント', '2025-10-31 01:45:43'),
(18, 4, NULL, 7, NULL, 4, NULL, NULL, NULL, NULL, NULL, 'コメント', '2025-10-31 01:45:43'),
(19, 4, NULL, 8, NULL, 4, NULL, NULL, NULL, NULL, NULL, 'コメント', '2025-10-31 01:45:43'),
(20, 5, NULL, 9, NULL, 3, NULL, NULL, NULL, NULL, NULL, 'コメント', '2025-10-31 01:45:43'),
(21, 5, NULL, NULL, 4, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2025-10-31 01:45:43'),
(22, 3, NULL, NULL, 6, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2025-10-31 01:45:43'),
(23, 1, NULL, NULL, NULL, NULL, 1, NULL, 1, NULL, NULL, NULL, '2025-10-31 01:45:43'),
(24, 2, NULL, NULL, NULL, NULL, 2, NULL, 1, NULL, NULL, NULL, '2025-10-31 01:45:43'),
(25, 3, NULL, NULL, NULL, NULL, 3, NULL, 2, NULL, NULL, NULL, '2025-10-31 01:45:43'),
(26, 1, NULL, NULL, NULL, NULL, 4, NULL, 2, NULL, NULL, NULL, '2025-10-31 01:45:43'),
(27, 1, NULL, NULL, NULL, NULL, 5, NULL, 4, NULL, NULL, NULL, '2025-10-31 01:45:43'),
(28, 5, NULL, NULL, NULL, NULL, 6, NULL, 4, NULL, NULL, NULL, '2025-10-31 01:45:43'),
(29, 2, NULL, NULL, NULL, NULL, 7, NULL, 5, NULL, NULL, NULL, '2025-10-31 01:45:43'),
(30, 4, NULL, NULL, NULL, NULL, 8, NULL, 5, NULL, NULL, NULL, '2025-10-31 01:45:43'),
(31, 3, NULL, NULL, NULL, NULL, 9, NULL, 7, NULL, NULL, NULL, '2025-10-31 01:45:43'),
(32, 3, NULL, NULL, NULL, NULL, 10, NULL, 7, NULL, NULL, NULL, '2025-10-31 01:45:43'),
(33, 2, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, 1, NULL, '2025-10-31 01:45:43'),
(34, 1, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, 2, NULL, '2025-10-31 01:45:43'),
(35, 1, NULL, NULL, NULL, NULL, NULL, NULL, 8, NULL, 3, NULL, '2025-10-31 01:45:43'),
(36, 4, NULL, NULL, NULL, NULL, NULL, NULL, 8, NULL, 4, NULL, '2025-10-31 01:45:43'),
(37, 4, NULL, NULL, NULL, NULL, NULL, NULL, 7, NULL, 5, NULL, '2025-10-31 01:45:43'),
(38, 3, NULL, NULL, NULL, NULL, NULL, NULL, 7, NULL, 6, NULL, '2025-10-31 01:45:43'),
(39, 3, NULL, NULL, NULL, NULL, NULL, NULL, 6, NULL, 7, NULL, '2025-10-31 01:45:43'),
(40, 1, NULL, NULL, NULL, NULL, NULL, NULL, 6, NULL, 8, NULL, '2025-10-31 01:45:43'),
(41, 1, NULL, NULL, NULL, NULL, NULL, NULL, 10, NULL, 9, NULL, '2025-10-31 01:45:43'),
(42, 2, NULL, NULL, NULL, NULL, NULL, NULL, 10, NULL, 10, NULL, '2025-10-31 01:45:43');

-- --------------------------------------------------------

--
-- テーブルの構造 `t_transaction`
--

CREATE TABLE `t_transaction` (
  `id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `seller_id` int(11) NOT NULL,
  `status` enum('支払い待ち','発送待ち','配達中','到着','レンタル中','クリーニング期間','発送待ち','取引完了') NOT NULL,
  `situation` enum('購入','レンタル') NOT NULL,
  `paymentMethod` enum('クレジットカード','PayPay','コンビニ払い') NOT NULL,
  `date` timestamp NOT NULL DEFAULT current_timestamp(),
  `paymentDeadline` datetime NOT NULL,
  `shippingAddress` varchar(255) NOT NULL,
  `shippingPhoto` varchar(255) NOT NULL,
  `shippingFlg` tinyint(1) NOT NULL,
  `receivedPhoto` varchar(255) NOT NULL,
  `receivedFlg` tinyint(1) NOT NULL,
  `rentalPeriod` datetime NOT NULL,
  `creditcard_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `t_transaction`
--

INSERT INTO `t_transaction` (`id`, `product_id`, `customer_id`, `seller_id`, `status`, `situation`, `paymentMethod`, `date`, `paymentDeadline`, `shippingAddress`, `shippingPhoto`, `shippingFlg`, `receivedPhoto`, `receivedFlg`, `rentalPeriod`, `creditcard_id`) VALUES
(1, 2, 1, 2, '取引完了', '購入', 'クレジットカード', '2025-09-01 01:00:00', '2025-09-01 10:00:00', '東京都渋谷区... 谷口様', 'img/shipping/ship_001.jpg', 1, 'img/received/recv_001.jpg', 1, '2025-09-05 00:00:00', 1),
(2, 1, 3, 1, 'レンタル中', 'レンタル', 'PayPay', '2025-10-25 05:00:00', '2025-10-25 14:00:00', '神奈川県横浜市... 佐藤様', 'img/shipping/ship_002.jpg', 1, 'img/received/recv_002.jpg', 1, '2025-11-01 23:59:59', NULL),
(3, 3, 4, 3, '支払い待ち', '購入', 'コンビニ払い', '2025-10-27 01:00:00', '2025-10-30 23:59:59', '埼玉県さいたま市... 高橋様', 'img/shipping/default.jpg', 0, 'img/received/default.jpg', 0, '2025-10-31 00:00:00', NULL),
(4, 4, 5, 1, '発送待ち', 'レンタル', 'クレジットカード', '2025-10-26 09:00:00', '2025-10-26 18:00:00', '北海道札幌市... 伊藤様', 'img/shipping/default.jpg', 0, 'img/received/default.jpg', 0, '2025-11-05 23:59:59', 10),
(5, 5, 2, 4, '配達中', '購入', 'クレジットカード', '2025-10-24 02:00:00', '2025-10-24 11:00:00', '東京都新宿区... 鈴木様', 'img/shipping/ship_003.jpg', 1, 'img/received/default.jpg', 0, '2025-10-28 00:00:00', 4),
(6, 3, 1, 3, 'クリーニング期間', 'レンタル', 'クレジットカード', '2025-09-15 01:00:00', '2025-09-15 10:00:00', '東京都渋谷区... 谷口様', 'img/shipping/ship_004.jpg', 1, 'img/received/recv_004.jpg', 1, '2025-09-22 23:59:59', 2),
(7, 5, 3, 4, '到着', '購入', 'PayPay', '2025-10-19 23:00:00', '2025-10-20 08:00:00', '神奈川県横浜市... 佐藤様', 'img/shipping/ship_005.jpg', 1, 'img/received/default.jpg', 0, '2025-10-27 00:00:00', NULL),
(8, 1, 4, 1, '取引完了', 'レンタル', 'クレジットカード', '2025-08-10 03:00:00', '2025-08-10 12:00:00', '埼玉県さいたま市... 高橋様', 'img/shipping/ship_006.jpg', 1, 'img/received/recv_006.jpg', 1, '2025-08-17 23:59:59', 7),
(9, 5, 1, 4, '発送待ち', '購入', 'クレジットカード', '2025-10-27 03:00:00', '2025-10-27 12:00:00', '東京都渋谷区... 谷口様', 'img/shipping/default.jpg', 0, 'img/received/default.jpg', 0, '2025-11-03 00:00:00', 3),
(10, 1, 2, 1, '配達中', 'レンタル', 'クレジットカード', '2025-10-25 01:00:00', '2025-10-25 10:00:00', '東京都新宿区... 鈴木様', 'img/shipping/ship_007.jpg', 1, 'img/received/default.jpg', 0, '2025-11-04 23:59:59', 5);

--
-- トリガ `t_transaction`
--
DELIMITER $$
CREATE TRIGGER `trg_transaction_status_change` AFTER UPDATE ON `t_transaction` FOR EACH ROW BEGIN

    
    IF OLD.status != NEW.status THEN
    
        
        INSERT INTO `t_time` (
            `account_id`,       
            `transaction_id`,   
            `transaction_status`, 
            `product_change`    
        )
        VALUES (
            NEW.customer_id,    
            NEW.id,             
            OLD.status,         
            '取引状態遷移'
        );
        
        
        
        IF NEW.customer_id != NEW.seller_id THEN
            INSERT INTO `t_time` (
                `account_id`,       
                `transaction_id`,   
                `transaction_status`, 
                `product_change`    
            )
            VALUES (
                NEW.seller_id,      
                NEW.id,             
                OLD.status,         
                '取引状態遷移'
            );
        END IF;
        
    END IF;
    
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- テーブルの構造 `t_transfer`
--

CREATE TABLE `t_transfer` (
  `id` int(11) NOT NULL,
  `account_id` int(11) NOT NULL,
  `bankName` varchar(100) NOT NULL,
  `accountType` varchar(20) NOT NULL,
  `branchCode` char(3) NOT NULL,
  `accountNumber` varchar(20) NOT NULL,
  `accountHolder` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- テーブルのデータのダンプ `t_transfer`
--

INSERT INTO `t_transfer` (`id`, `account_id`, `bankName`, `accountType`, `branchCode`, `accountNumber`, `accountHolder`) VALUES
(2, 1, 'ゆうちょ銀行', '普通', '456', '123487654', 'タニグチ マサヤ'),
(3, 2, '三井住友銀行', '普通', '444', '2223333', 'スズキ ハナコ'),
(4, 2, 'みずほ銀行', '普通', '222', '4445555', 'スズキ ハナコ'),
(5, 2, '楽天銀行', '普通', '566', '1000001', 'カ）スズキショウテン'),
(6, 3, 'りそな銀行', '普通', '222', '6667777', 'サトウ ジロウ'),
(7, 4, 'PayPay銀行', '普通', '169', '8888888', 'タカハシ サブロウ'),
(8, 4, '新生銀行', '普通', '257', '9999999', 'タカハシ サブロウ'),
(9, 5, '北洋銀行', '当座', '678', '0001234', 'イトウ シロウ'),
(10, 5, 'ソニー銀行', '普通', '244', '1112222', 'イトウ シロウ'),
(11, 1, 'ゆうちょ銀行', '貯蓄', '677', '3567234', 'タジリトトクラ');

-- --------------------------------------------------------

--
-- ビュー用の代替構造 `v_age_group_new_users`
-- (実際のビューを参照するには下にあります)
--
CREATE TABLE `v_age_group_new_users` (
`month` varchar(7)
,`0?19歳` decimal(22,0)
,`20代` decimal(22,0)
,`30代` decimal(22,0)
,`40代` decimal(22,0)
,`50代` decimal(22,0)
,`60代以上` decimal(22,0)
);

-- --------------------------------------------------------

--
-- ビュー用の代替構造 `v_alert_unchecked`
-- (実際のビューを参照するには下にあります)
--
CREATE TABLE `v_alert_unchecked` (
`未対応通報` bigint(21)
);

-- --------------------------------------------------------

--
-- ビュー用の代替構造 `v_compare_1_week_ago_listing`
-- (実際のビューを参照するには下にあります)
--
CREATE TABLE `v_compare_1_week_ago_listing` (
`先週比` decimal(27,1)
);

-- --------------------------------------------------------

--
-- ビュー用の代替構造 `v_compare_1_week_ago_new_users`
-- (実際のビューを参照するには下にあります)
--
CREATE TABLE `v_compare_1_week_ago_new_users` (
`先週比` decimal(27,1)
);

-- --------------------------------------------------------

--
-- ビュー用の代替構造 `v_identify_offer`
-- (実際のビューを参照するには下にあります)
--
CREATE TABLE `v_identify_offer` (
`count(*)` bigint(21)
);

-- --------------------------------------------------------

--
-- ビュー用の代替構造 `v_inquiry_unchecked`
-- (実際のビューを参照するには下にあります)
--
CREATE TABLE `v_inquiry_unchecked` (
`count(*)` bigint(21)
);

-- --------------------------------------------------------

--
-- ビュー用の代替構造 `v_monthly_active_users`
-- (実際のビューを参照するには下にあります)
--
CREATE TABLE `v_monthly_active_users` (
`month` varchar(7)
,`MAU` bigint(21)
);

-- --------------------------------------------------------

--
-- ビュー用の代替構造 `v_notice`
-- (実際のビューを参照するには下にあります)
--
CREATE TABLE `v_notice` (
`created_at` timestamp
,`transaction_status` enum('支払い待ち','発送待ち','配達中','到着','レンタル中','クリーニング期間','発送待ち','取引完了')
,`product_change` enum('料金変更','取引状態遷移','コメント')
,`transaction_date` timestamp
,`paymentDeadline` datetime
,`rentalPeriod` datetime
,`alert_category` enum('通報','警告')
,`purchasePrice` int(11)
,`rentalPrice` int(11)
,`user_account_id` int(11)
,`time_id` int(11)
,`transaction_id` int(11)
,`alert_id` int(11)
,`comments_id` int(11)
,`product_id` int(11)
);

-- --------------------------------------------------------

--
-- ビュー用の代替構造 `v_region_new_users`
-- (実際のビューを参照するには下にあります)
--
CREATE TABLE `v_region_new_users` (
`month` varchar(7)
,`北海道` decimal(22,0)
,`東北` decimal(22,0)
,`関東` decimal(22,0)
,`中部` decimal(22,0)
,`近畿` decimal(22,0)
,`中国` decimal(22,0)
,`四国` decimal(22,0)
,`九州` decimal(22,0)
);

-- --------------------------------------------------------

--
-- ビュー用の代替構造 `v_weekly_active_users`
-- (実際のビューを参照するには下にあります)
--
CREATE TABLE `v_weekly_active_users` (
`今週のアクティブユーザー数` bigint(21)
);

-- --------------------------------------------------------

--
-- ビュー用の代替構造 `v_weekly_listing`
-- (実際のビューを参照するには下にあります)
--
CREATE TABLE `v_weekly_listing` (
`今週の出品数` bigint(21)
);

-- --------------------------------------------------------

--
-- ビュー用の代替構造 `v_weekly_new_users`
-- (実際のビューを参照するには下にあります)
--
CREATE TABLE `v_weekly_new_users` (
`今週の新規ユーザー数` bigint(21)
);

-- --------------------------------------------------------

--
-- ビュー用の構造 `v_age_group_new_users`
--
DROP TABLE IF EXISTS `v_age_group_new_users`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_age_group_new_users`  AS SELECT date_format(`a`.`created_at`,'%Y-%m') AS `month`, sum(case when timestampdiff(YEAR,`a`.`birthday`,curdate()) < 20 then 1 else 0 end) AS `0?19歳`, sum(case when timestampdiff(YEAR,`a`.`birthday`,curdate()) between 20 and 29 then 1 else 0 end) AS `20代`, sum(case when timestampdiff(YEAR,`a`.`birthday`,curdate()) between 30 and 39 then 1 else 0 end) AS `30代`, sum(case when timestampdiff(YEAR,`a`.`birthday`,curdate()) between 40 and 49 then 1 else 0 end) AS `40代`, sum(case when timestampdiff(YEAR,`a`.`birthday`,curdate()) between 50 and 59 then 1 else 0 end) AS `50代`, sum(case when timestampdiff(YEAR,`a`.`birthday`,curdate()) >= 60 then 1 else 0 end) AS `60代以上` FROM `m_account` AS `a` WHERE `a`.`status` not in ('削除','強制削除') AND `a`.`created_at` >= date_format(curdate() - interval 6 month,'%Y-%m-01') GROUP BY date_format(`a`.`created_at`,'%Y-%m') ORDER BY date_format(`a`.`created_at`,'%Y-%m') ASC ;

-- --------------------------------------------------------

--
-- ビュー用の構造 `v_alert_unchecked`
--
DROP TABLE IF EXISTS `v_alert_unchecked`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_alert_unchecked`  AS SELECT count(0) AS `未対応通報` FROM `t_alert` WHERE `t_alert`.`category` = '通報' AND `t_alert`.`situation` = '未対応' ;

-- --------------------------------------------------------

--
-- ビュー用の構造 `v_compare_1_week_ago_listing`
--
DROP TABLE IF EXISTS `v_compare_1_week_ago_listing`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_compare_1_week_ago_listing`  AS SELECT round(sum(case when yearweek(`m_product`.`upload`,1) = yearweek(curdate(),1) then 1 else 0 end) / nullif(sum(case when yearweek(`m_product`.`upload`,1) = yearweek(curdate(),1) - 1 then 1 else 0 end),0) * 100,1) AS `先週比` FROM `m_product` ;

-- --------------------------------------------------------

--
-- ビュー用の構造 `v_compare_1_week_ago_new_users`
--
DROP TABLE IF EXISTS `v_compare_1_week_ago_new_users`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_compare_1_week_ago_new_users`  AS SELECT round(sum(case when yearweek(`m_account`.`created_at`,1) = yearweek(curdate(),1) then 1 else 0 end) / nullif(sum(case when yearweek(`m_account`.`created_at`,1) = yearweek(curdate(),1) - 1 then 1 else 0 end),0) * 100,1) AS `先週比` FROM `m_account` ;

-- --------------------------------------------------------

--
-- ビュー用の構造 `v_identify_offer`
--
DROP TABLE IF EXISTS `v_identify_offer`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_identify_offer`  AS SELECT count(0) AS `count(*)` FROM `m_account` WHERE `m_account`.`status` = '未確認' ;

-- --------------------------------------------------------

--
-- ビュー用の構造 `v_inquiry_unchecked`
--
DROP TABLE IF EXISTS `v_inquiry_unchecked`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_inquiry_unchecked`  AS SELECT count(0) AS `count(*)` FROM `t_inquiry` WHERE `t_inquiry`.`situation` = '未対応' ;

-- --------------------------------------------------------

--
-- ビュー用の構造 `v_monthly_active_users`
--
DROP TABLE IF EXISTS `v_monthly_active_users`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_monthly_active_users`  AS SELECT date_format(`t_login`.`loginDatetime`,'%Y-%m') AS `month`, count(distinct `t_login`.`account_id`) AS `MAU` FROM `t_login` WHERE `t_login`.`loginDatetime` >= date_format(curdate() - interval 6 month,'%Y-%m-01') GROUP BY date_format(`t_login`.`loginDatetime`,'%Y-%m') ORDER BY date_format(`t_login`.`loginDatetime`,'%Y-%m') ASC ;

-- --------------------------------------------------------

--
-- ビュー用の構造 `v_notice`
--
DROP TABLE IF EXISTS `v_notice`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_notice`  AS SELECT `ttm`.`created_at` AS `created_at`, `ttm`.`transaction_status` AS `transaction_status`, `ttm`.`product_change` AS `product_change`, `ttr`.`date` AS `transaction_date`, `ttr`.`paymentDeadline` AS `paymentDeadline`, `ttr`.`rentalPeriod` AS `rentalPeriod`, `ta`.`category` AS `alert_category`, `mp`.`purchasePrice` AS `purchasePrice`, `mp`.`rentalPrice` AS `rentalPrice`, `ma`.`id` AS `user_account_id`, `ttm`.`id` AS `time_id`, `ttm`.`transaction_id` AS `transaction_id`, `ttm`.`alert_id` AS `alert_id`, `ttm`.`comments_id` AS `comments_id`, `ttm`.`product_id` AS `product_id` FROM (((((`t_time` `ttm` left join `m_account` `ma` on(`ttm`.`account_id` = `ma`.`id`)) left join `t_transaction` `ttr` on(`ttm`.`transaction_id` = `ttr`.`id`)) left join `t_alert` `ta` on(`ttm`.`alert_id` = `ta`.`id`)) left join `t_comments` `tc` on(`ttm`.`comments_id` = `tc`.`id`)) left join `m_product` `mp` on(`ttm`.`product_id` = `mp`.`id`)) WHERE `ttm`.`account_id` = 123 ORDER BY `ttm`.`created_at` DESC ;

-- --------------------------------------------------------

--
-- ビュー用の構造 `v_region_new_users`
--
DROP TABLE IF EXISTS `v_region_new_users`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_region_new_users`  AS SELECT date_format(`region_data`.`created_at`,'%Y-%m') AS `month`, sum(case when `region_data`.`region` = '北海道' then 1 else 0 end) AS `北海道`, sum(case when `region_data`.`region` = '東北' then 1 else 0 end) AS `東北`, sum(case when `region_data`.`region` = '関東' then 1 else 0 end) AS `関東`, sum(case when `region_data`.`region` = '中部' then 1 else 0 end) AS `中部`, sum(case when `region_data`.`region` = '近畿' then 1 else 0 end) AS `近畿`, sum(case when `region_data`.`region` = '中国' then 1 else 0 end) AS `中国`, sum(case when `region_data`.`region` = '四国' then 1 else 0 end) AS `四国`, sum(case when `region_data`.`region` = '九州' then 1 else 0 end) AS `九州` FROM (select `a`.`id` AS `id`,`a`.`created_at` AS `created_at`,case when `addr`.`pref` = '北海道' then '北海道' when `addr`.`pref` in ('青森県','岩手県','宮城県','秋田県','山形県','福島県') then '東北' when `addr`.`pref` in ('茨城県','栃木県','群馬県','埼玉県','千葉県','東京都','神奈川県') then '関東' when `addr`.`pref` in ('新潟県','富山県','石川県','福井県','山梨県','長野県','岐阜県','静岡県','愛知県') then '中部' when `addr`.`pref` in ('三重県','滋賀県','京都府','大阪府','兵庫県','奈良県','和歌山県') then '近畿' when `addr`.`pref` in ('鳥取県','島根県','岡山県','広島県','山口県') then '中国' when `addr`.`pref` in ('徳島県','香川県','愛媛県','高知県') then '四国' when `addr`.`pref` in ('福岡県','佐賀県','長崎県','熊本県','大分県','宮崎県','鹿児島県','沖縄県') then '九州' else '不明' end AS `region` from (`m_account` `a` join `m_address` `addr` on(`a`.`id` = `addr`.`account_id`)) where `a`.`status` not in ('削除','強制削除') and `a`.`created_at` >= date_format(curdate() - interval 6 month,'%Y-%m-01')) AS `region_data` GROUP BY date_format(`region_data`.`created_at`,'%Y-%m') ORDER BY date_format(`region_data`.`created_at`,'%Y-%m') ASC ;

-- --------------------------------------------------------

--
-- ビュー用の構造 `v_weekly_active_users`
--
DROP TABLE IF EXISTS `v_weekly_active_users`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_weekly_active_users`  AS SELECT count(0) AS `今週のアクティブユーザー数` FROM `t_login` WHERE to_days(curdate() - interval weekday(curdate()) day) - to_days(`t_login`.`loginDatetime`) < 7 ;

-- --------------------------------------------------------

--
-- ビュー用の構造 `v_weekly_listing`
--
DROP TABLE IF EXISTS `v_weekly_listing`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_weekly_listing`  AS SELECT count(0) AS `今週の出品数` FROM `m_product` WHERE to_days(curdate() - interval weekday(curdate()) day) - to_days(`m_product`.`upload`) < 7 ;

-- --------------------------------------------------------

--
-- ビュー用の構造 `v_weekly_new_users`
--
DROP TABLE IF EXISTS `v_weekly_new_users`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_weekly_new_users`  AS SELECT count(0) AS `今週の新規ユーザー数` FROM `m_account` WHERE to_days(curdate() - interval weekday(curdate()) day) - to_days(`m_account`.`created_at`) < 7 ;

--
-- ダンプしたテーブルのインデックス
--

--
-- テーブルのインデックス `m_account`
--
ALTER TABLE `m_account`
  ADD PRIMARY KEY (`id`);

--
-- テーブルのインデックス `m_address`
--
ALTER TABLE `m_address`
  ADD PRIMARY KEY (`id`,`account_id`),
  ADD KEY `account_id` (`account_id`);

--
-- テーブルのインデックス `m_adminaccount`
--
ALTER TABLE `m_adminaccount`
  ADD PRIMARY KEY (`id`);

--
-- テーブルのインデックス `m_admin_contents`
--
ALTER TABLE `m_admin_contents`
  ADD PRIMARY KEY (`id`);

--
-- テーブルのインデックス `m_bottomssize`
--
ALTER TABLE `m_bottomssize`
  ADD PRIMARY KEY (`product_id`);

--
-- テーブルのインデックス `m_brand`
--
ALTER TABLE `m_brand`
  ADD PRIMARY KEY (`id`);

--
-- テーブルのインデックス `m_category`
--
ALTER TABLE `m_category`
  ADD PRIMARY KEY (`id`);

--
-- テーブルのインデックス `m_cleansign`
--
ALTER TABLE `m_cleansign`
  ADD PRIMARY KEY (`id`);

--
-- テーブルのインデックス `m_product`
--
ALTER TABLE `m_product`
  ADD PRIMARY KEY (`id`),
  ADD KEY `brand_id` (`brand_id`),
  ADD KEY `category_id` (`category_id`),
  ADD KEY `account_id` (`account_id`);

--
-- テーブルのインデックス `m_productimg`
--
ALTER TABLE `m_productimg`
  ADD PRIMARY KEY (`id`),
  ADD KEY `product_id` (`product_id`);

--
-- テーブルのインデックス `m_topssize`
--
ALTER TABLE `m_topssize`
  ADD PRIMARY KEY (`product_id`);

--
-- テーブルのインデックス `t_adminlogin`
--
ALTER TABLE `t_adminlogin`
  ADD PRIMARY KEY (`id`),
  ADD KEY `adminAccount_id` (`adminAccount_id`);

--
-- テーブルのインデックス `t_alert`
--
ALTER TABLE `t_alert`
  ADD PRIMARY KEY (`id`),
  ADD KEY `sender_id` (`sender_id`),
  ADD KEY `comment_id` (`comment_id`),
  ADD KEY `transaction_id` (`transaction_id`),
  ADD KEY `adminAccount_id` (`adminAccount_id`),
  ADD KEY `recipient_id` (`recipient_id`);

--
-- テーブルのインデックス `t_clean`
--
ALTER TABLE `t_clean`
  ADD PRIMARY KEY (`product_id`,`cleanSign_id`),
  ADD KEY `cleanSign_id` (`cleanSign_id`);

--
-- テーブルのインデックス `t_comments`
--
ALTER TABLE `t_comments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `account_id` (`account_id`),
  ADD KEY `product_id` (`product_id`);

--
-- テーブルのインデックス `t_connection`
--
ALTER TABLE `t_connection`
  ADD PRIMARY KEY (`id`),
  ADD KEY `execution_id` (`execution_id`),
  ADD KEY `target_id` (`target_id`);

--
-- テーブルのインデックス `t_creditcard`
--
ALTER TABLE `t_creditcard`
  ADD PRIMARY KEY (`id`),
  ADD KEY `account_id` (`account_id`);

--
-- テーブルのインデックス `t_evaluation`
--
ALTER TABLE `t_evaluation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `transaction_id` (`transaction_id`),
  ADD KEY `recipient_id` (`recipient_id`);

--
-- テーブルのインデックス `t_favorite`
--
ALTER TABLE `t_favorite`
  ADD PRIMARY KEY (`id`),
  ADD KEY `account_id` (`account_id`),
  ADD KEY `product_id` (`product_id`),
  ADD KEY `brand_id` (`brand_id`);

--
-- テーブルのインデックス `t_history`
--
ALTER TABLE `t_history`
  ADD PRIMARY KEY (`id`),
  ADD KEY `account_id` (`account_id`),
  ADD KEY `transaction_id` (`transaction_id`),
  ADD KEY `product_id` (`product_id`);

--
-- テーブルのインデックス `t_inquiry`
--
ALTER TABLE `t_inquiry`
  ADD PRIMARY KEY (`id`),
  ADD KEY `sender_id` (`sender_id`),
  ADD KEY `product_id` (`product_id`),
  ADD KEY `adminAccount_id` (`adminAccount_id`);

--
-- テーブルのインデックス `t_login`
--
ALTER TABLE `t_login`
  ADD PRIMARY KEY (`id`),
  ADD KEY `account_id` (`account_id`);

--
-- テーブルのインデックス `t_message`
--
ALTER TABLE `t_message`
  ADD PRIMARY KEY (`id`),
  ADD KEY `sender_id` (`sender_id`),
  ADD KEY `recipient_id` (`recipient_id`),
  ADD KEY `transaction_id` (`transaction_id`);

--
-- テーブルのインデックス `t_rentalperiod`
--
ALTER TABLE `t_rentalperiod`
  ADD PRIMARY KEY (`id`),
  ADD KEY `product_id` (`product_id`);

--
-- テーブルのインデックス `t_time`
--
ALTER TABLE `t_time`
  ADD PRIMARY KEY (`id`),
  ADD KEY `account_id` (`account_id`),
  ADD KEY `login_id` (`login_id`),
  ADD KEY `comments_id` (`comments_id`),
  ADD KEY `alert_id` (`alert_id`),
  ADD KEY `product_id` (`product_id`),
  ADD KEY `message_id` (`message_id`),
  ADD KEY `inquiry_id` (`inquiry_id`),
  ADD KEY `transaction_id` (`transaction_id`),
  ADD KEY `evaluation_id` (`evaluation_id`);

--
-- テーブルのインデックス `t_transaction`
--
ALTER TABLE `t_transaction`
  ADD PRIMARY KEY (`id`),
  ADD KEY `product_id` (`product_id`),
  ADD KEY `customer_id` (`customer_id`),
  ADD KEY `seller_id` (`seller_id`),
  ADD KEY `creditcard_id` (`creditcard_id`);

--
-- テーブルのインデックス `t_transfer`
--
ALTER TABLE `t_transfer`
  ADD PRIMARY KEY (`id`),
  ADD KEY `account_id` (`account_id`);

--
-- ダンプしたテーブルの AUTO_INCREMENT
--

--
-- テーブルの AUTO_INCREMENT `m_account`
--
ALTER TABLE `m_account`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- テーブルの AUTO_INCREMENT `m_address`
--
ALTER TABLE `m_address`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- テーブルの AUTO_INCREMENT `m_adminaccount`
--
ALTER TABLE `m_adminaccount`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- テーブルの AUTO_INCREMENT `m_admin_contents`
--
ALTER TABLE `m_admin_contents`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- テーブルの AUTO_INCREMENT `m_brand`
--
ALTER TABLE `m_brand`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- テーブルの AUTO_INCREMENT `m_category`
--
ALTER TABLE `m_category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- テーブルの AUTO_INCREMENT `m_cleansign`
--
ALTER TABLE `m_cleansign`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=713;

--
-- テーブルの AUTO_INCREMENT `m_product`
--
ALTER TABLE `m_product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- テーブルの AUTO_INCREMENT `m_productimg`
--
ALTER TABLE `m_productimg`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- テーブルの AUTO_INCREMENT `t_adminlogin`
--
ALTER TABLE `t_adminlogin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- テーブルの AUTO_INCREMENT `t_alert`
--
ALTER TABLE `t_alert`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- テーブルの AUTO_INCREMENT `t_comments`
--
ALTER TABLE `t_comments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- テーブルの AUTO_INCREMENT `t_connection`
--
ALTER TABLE `t_connection`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- テーブルの AUTO_INCREMENT `t_creditcard`
--
ALTER TABLE `t_creditcard`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- テーブルの AUTO_INCREMENT `t_evaluation`
--
ALTER TABLE `t_evaluation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- テーブルの AUTO_INCREMENT `t_favorite`
--
ALTER TABLE `t_favorite`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- テーブルの AUTO_INCREMENT `t_history`
--
ALTER TABLE `t_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- テーブルの AUTO_INCREMENT `t_inquiry`
--
ALTER TABLE `t_inquiry`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- テーブルの AUTO_INCREMENT `t_login`
--
ALTER TABLE `t_login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- テーブルの AUTO_INCREMENT `t_message`
--
ALTER TABLE `t_message`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- テーブルの AUTO_INCREMENT `t_time`
--
ALTER TABLE `t_time`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- テーブルの AUTO_INCREMENT `t_transaction`
--
ALTER TABLE `t_transaction`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- テーブルの AUTO_INCREMENT `t_transfer`
--
ALTER TABLE `t_transfer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- ダンプしたテーブルの制約
--

--
-- テーブルの制約 `m_address`
--
ALTER TABLE `m_address`
  ADD CONSTRAINT `m_address_ibfk_1` FOREIGN KEY (`account_id`) REFERENCES `m_account` (`id`) ON UPDATE CASCADE;

--
-- テーブルの制約 `m_bottomssize`
--
ALTER TABLE `m_bottomssize`
  ADD CONSTRAINT `m_bottomssize_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `m_product` (`id`) ON UPDATE CASCADE;

--
-- テーブルの制約 `m_product`
--
ALTER TABLE `m_product`
  ADD CONSTRAINT `m_product_ibfk_1` FOREIGN KEY (`brand_id`) REFERENCES `m_brand` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `m_product_ibfk_2` FOREIGN KEY (`category_id`) REFERENCES `m_category` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `m_product_ibfk_3` FOREIGN KEY (`account_id`) REFERENCES `m_account` (`id`) ON UPDATE CASCADE;

--
-- テーブルの制約 `m_productimg`
--
ALTER TABLE `m_productimg`
  ADD CONSTRAINT `m_productimg_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `m_product` (`id`) ON UPDATE CASCADE;

--
-- テーブルの制約 `m_topssize`
--
ALTER TABLE `m_topssize`
  ADD CONSTRAINT `m_topssize_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `m_product` (`id`) ON UPDATE CASCADE;

--
-- テーブルの制約 `t_adminlogin`
--
ALTER TABLE `t_adminlogin`
  ADD CONSTRAINT `t_adminlogin_ibfk_1` FOREIGN KEY (`adminAccount_id`) REFERENCES `m_adminaccount` (`id`) ON UPDATE CASCADE;

--
-- テーブルの制約 `t_alert`
--
ALTER TABLE `t_alert`
  ADD CONSTRAINT `t_alert_ibfk_1` FOREIGN KEY (`sender_id`) REFERENCES `m_account` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_alert_ibfk_2` FOREIGN KEY (`comment_id`) REFERENCES `t_comments` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_alert_ibfk_3` FOREIGN KEY (`transaction_id`) REFERENCES `t_transaction` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_alert_ibfk_4` FOREIGN KEY (`adminAccount_id`) REFERENCES `m_adminaccount` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_alert_ibfk_5` FOREIGN KEY (`recipient_id`) REFERENCES `m_account` (`id`) ON UPDATE CASCADE;

--
-- テーブルの制約 `t_clean`
--
ALTER TABLE `t_clean`
  ADD CONSTRAINT `t_clean_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `m_product` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_clean_ibfk_2` FOREIGN KEY (`cleanSign_id`) REFERENCES `m_cleansign` (`id`) ON UPDATE CASCADE;

--
-- テーブルの制約 `t_comments`
--
ALTER TABLE `t_comments`
  ADD CONSTRAINT `t_comments_ibfk_1` FOREIGN KEY (`account_id`) REFERENCES `m_account` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_comments_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `m_product` (`id`) ON UPDATE CASCADE;

--
-- テーブルの制約 `t_connection`
--
ALTER TABLE `t_connection`
  ADD CONSTRAINT `t_connection_ibfk_1` FOREIGN KEY (`execution_id`) REFERENCES `m_account` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_connection_ibfk_2` FOREIGN KEY (`target_id`) REFERENCES `m_account` (`id`) ON UPDATE CASCADE;

--
-- テーブルの制約 `t_creditcard`
--
ALTER TABLE `t_creditcard`
  ADD CONSTRAINT `t_creditcard_ibfk_1` FOREIGN KEY (`account_id`) REFERENCES `m_account` (`id`) ON UPDATE CASCADE;

--
-- テーブルの制約 `t_evaluation`
--
ALTER TABLE `t_evaluation`
  ADD CONSTRAINT `t_evaluation_ibfk_1` FOREIGN KEY (`transaction_id`) REFERENCES `t_transaction` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_evaluation_ibfk_2` FOREIGN KEY (`recipient_id`) REFERENCES `m_account` (`id`) ON UPDATE CASCADE;

--
-- テーブルの制約 `t_favorite`
--
ALTER TABLE `t_favorite`
  ADD CONSTRAINT `t_favorite_ibfk_1` FOREIGN KEY (`account_id`) REFERENCES `m_account` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_favorite_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `m_product` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_favorite_ibfk_3` FOREIGN KEY (`brand_id`) REFERENCES `m_brand` (`id`) ON UPDATE CASCADE;

--
-- テーブルの制約 `t_history`
--
ALTER TABLE `t_history`
  ADD CONSTRAINT `t_history_ibfk_1` FOREIGN KEY (`account_id`) REFERENCES `m_account` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_history_ibfk_2` FOREIGN KEY (`transaction_id`) REFERENCES `t_transaction` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_history_ibfk_3` FOREIGN KEY (`product_id`) REFERENCES `m_product` (`id`) ON UPDATE CASCADE;

--
-- テーブルの制約 `t_inquiry`
--
ALTER TABLE `t_inquiry`
  ADD CONSTRAINT `t_inquiry_ibfk_1` FOREIGN KEY (`sender_id`) REFERENCES `m_account` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_inquiry_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `m_product` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_inquiry_ibfk_3` FOREIGN KEY (`adminAccount_id`) REFERENCES `m_adminaccount` (`id`) ON UPDATE CASCADE;

--
-- テーブルの制約 `t_login`
--
ALTER TABLE `t_login`
  ADD CONSTRAINT `t_login_ibfk_1` FOREIGN KEY (`account_id`) REFERENCES `m_account` (`id`) ON UPDATE CASCADE;

--
-- テーブルの制約 `t_message`
--
ALTER TABLE `t_message`
  ADD CONSTRAINT `t_message_ibfk_1` FOREIGN KEY (`sender_id`) REFERENCES `m_account` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_message_ibfk_2` FOREIGN KEY (`recipient_id`) REFERENCES `m_account` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_message_ibfk_3` FOREIGN KEY (`transaction_id`) REFERENCES `t_transaction` (`id`) ON UPDATE CASCADE;

--
-- テーブルの制約 `t_rentalperiod`
--
ALTER TABLE `t_rentalperiod`
  ADD CONSTRAINT `t_rentalperiod_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `m_product` (`id`) ON UPDATE CASCADE;

--
-- テーブルの制約 `t_time`
--
ALTER TABLE `t_time`
  ADD CONSTRAINT `t_time_ibfk_1` FOREIGN KEY (`account_id`) REFERENCES `m_account` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_time_ibfk_2` FOREIGN KEY (`login_id`) REFERENCES `t_login` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_time_ibfk_3` FOREIGN KEY (`comments_id`) REFERENCES `t_comments` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_time_ibfk_4` FOREIGN KEY (`alert_id`) REFERENCES `t_alert` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_time_ibfk_5` FOREIGN KEY (`product_id`) REFERENCES `m_product` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_time_ibfk_6` FOREIGN KEY (`message_id`) REFERENCES `t_message` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_time_ibfk_7` FOREIGN KEY (`inquiry_id`) REFERENCES `t_inquiry` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_time_ibfk_8` FOREIGN KEY (`transaction_id`) REFERENCES `t_transaction` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_time_ibfk_9` FOREIGN KEY (`evaluation_id`) REFERENCES `t_evaluation` (`id`) ON UPDATE CASCADE;

--
-- テーブルの制約 `t_transaction`
--
ALTER TABLE `t_transaction`
  ADD CONSTRAINT `t_transaction_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `m_product` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_transaction_ibfk_2` FOREIGN KEY (`customer_id`) REFERENCES `m_account` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_transaction_ibfk_3` FOREIGN KEY (`seller_id`) REFERENCES `m_account` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `t_transaction_ibfk_4` FOREIGN KEY (`creditcard_id`) REFERENCES `t_creditcard` (`id`) ON UPDATE CASCADE;

--
-- テーブルの制約 `t_transfer`
--
ALTER TABLE `t_transfer`
  ADD CONSTRAINT `t_transfer_ibfk_1` FOREIGN KEY (`account_id`) REFERENCES `m_account` (`id`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
