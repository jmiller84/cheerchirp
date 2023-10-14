-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS posts CASCADE;
DROP SEQUENCE IF EXISTS posts_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(30),
    password VARCHAR(255),
    email VARCHAR(255),
    first_name VARCHAR(255),
    surname VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    content VARCHAR(255),
    user_id INT,
    CONSTRAINT fk_user foreign key(user_id)
    REFERENCES users(id)
    ON DELETE CASCADE
);



-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (username, password, email, first_name, surname) VALUES ('jmiller84', 'password123!', 'jmiller@hotmail.com', 'Joe', 'Miller');
INSERT INTO users (username, password, email, first_name, surname) VALUES ('alexm_2023', 'London123', 'alexm@hotmail.com', 'Alex', 'Martin');

INSERT INTO posts (title, content, user_id) VALUES ('Test Title', 'Test Content',  1);
INSERT INTO posts (title, content,   user_id) VALUES ('Test Post', 'Test Post Content', 2);