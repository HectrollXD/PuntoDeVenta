create user sell_point_user with password '53ll!P01nt!U53r';
create database sell_point_database with owner sell_point_user encoding = 'UTF-8';
grant all privileges on database sell_point_database to sell_point_user;
grant all privileges on schema public to sell_point_user;
