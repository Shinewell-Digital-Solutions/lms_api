-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 22, 2025 at 03:25 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `lms_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `mobile` varchar(15) NOT NULL,
  `email` varchar(45) DEFAULT NULL,
  `usertype_id` int(11) NOT NULL,
  `password` varchar(45) DEFAULT NULL,
  `profile_pic` varchar(45) DEFAULT NULL,
  `acc_token` varchar(45) DEFAULT NULL,
  `status` tinyint(4) NOT NULL DEFAULT 0,
  `created_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `mobile`, `email`, `usertype_id`, `password`, `profile_pic`, `acc_token`, `status`, `created_at`, `deleted_at`, `updated_at`) VALUES
(1, 'Ayush', '62058', 'ayu@gmail.com', 2, '123', NULL, NULL, 0, NULL, NULL, NULL),
(2, 'Rachit', '852963741', 'rcahit@gmail.com', 1, '123@', NULL, NULL, 1, NULL, NULL, NULL),
(3, 'Rachit', '852963741', 'rcahit@gmail.com', 1, ' hashed_password', NULL, NULL, 1, NULL, NULL, NULL),
(4, 'Raman Sharma', '8545896', 'raman123@gmail.com', 2, 'scrypt:32768:8:1$E7Zsl1dQflJ1Q6Jo$96c73750277', NULL, NULL, 0, NULL, NULL, '2025-07-22 12:06:37'),
(6, 'Salman', '741258963', 'salaman@gmail.com', 1, 'scrypt:32768:8:1$nE90ACDR5hkvatYT$0926fa03b5d', NULL, NULL, 1, '2025-07-22 11:21:29', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `user_type`
--

CREATE TABLE `user_type` (
  `id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `deleted_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_type`
--

INSERT INTO `user_type` (`id`, `name`, `created_at`, `updated_at`, `deleted_at`) VALUES
(1, 'admin', NULL, NULL, NULL),
(2, 'student', NULL, NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`,`usertype_id`),
  ADD KEY `fk` (`usertype_id`);

--
-- Indexes for table `user_type`
--
ALTER TABLE `user_type`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `user_type`
--
ALTER TABLE `user_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `fk` FOREIGN KEY (`usertype_id`) REFERENCES `user_type` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
