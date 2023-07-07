-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    email text
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (username, email) VALUES ('kay', 'kay@lack.net');
INSERT INTO users (username, email) VALUES ('leo', 'leo@leohetsch.net');

-- INSERT INTO users (title, author_name) VALUES ('Nineteen Eighty-Four', 'George Orwell');
-- INSERT INTO users (title, author_name) VALUES ('Mrs Dalloway', 'Virginia Woolf');
-- INSERT INTO users (title, author_name) VALUES ('Emma', 'Jane Austen');
-- INSERT INTO users (title, author_name) VALUES ('Dracula', 'Bram Stoker');
-- INSERT INTO users (title, author_name) VALUES ('The Age of Innocence', 'Edith Wharton');

DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    views text,
    user_id int
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO posts (title, content, views, user_id) VALUES ('My Title 1', 'My Content 1', 0, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('My Title 2', 'My Content 2', 0, 2);