Two Tables Design Recipe Template
Copy this recipe template to design and create two related database tables from a specification.

1. Extract nouns from the user stories or specification
# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

As a blogger
So I can write interesting stuff
I want to write posts having a title.

As a blogger
So I can write interesting stuff
I want to write posts having a content.

As a blogger
So I can let people comment on interesting stuff
I want to allow comments on my posts.

As a blogger
So I can let people comment on interesting stuff
I want the comments to have a content.

As a blogger
So I can let people comment on interesting stuff
I want the author to include their name in comments.



post title, post content, comments, authors` names


2. Infer the Table Name and Columns
Put the different nouns in this table. Replace the example with your own nouns.

Record	Properties
posts	name, name, starting_dates year
comments	name
Name of the first table (always plural): posts

Column names: post titles

Name of the second table (always plural): cohorts

Column names: name, starting_date

3. Decide the column types
Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.

# EXAMPLE:

Table: posts
id: SERIAL
title: text
content: text


Table: comments
id: SERIAL
post id: SERIAL
author_name: text
content: text

4. Decide on The Tables Relationship
Most of the time, you'll be using a one-to-many relationship, and will need a foreign key on one of the two tables.

To decide on which one, answer these two questions:

Can one [TABLE ONE] have many [TABLE TWO]? (Yes/No)
Can one [TABLE TWO] have many [TABLE ONE]? (Yes/No)
You'll then be able to say that:

Can a student have many cohorts? No 
Can a cohort have many students? Yes

Student -> many yo one -> Cohort

The foreign key is on studetns (cohort_id)

[A] has many [B]
And on the other side, [B] belongs to [A]
In that case, the foreign key is in the table [B]
Replace the relevant bits in this example with your own:

# EXAMPLE

1. Can one artist have many albums? YES
2. Can one album have many artists? NO

-> Therefore,
-> An artist HAS MANY albums
-> An album BELONGS TO an artist

-> Therefore, the foreign key is on the albums table.
If you can answer YES to the two questions, you'll probably have to implement a Many-to-Many relationship, which is more complex and needs a third table (called a join table).

4. Write the SQL
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, columm names and types.

-- Create the table without the foreign key first.
CREATE TABLE post (
  post_id SERIAL PRIMARY KEY,
  title text,
  content text
);

-- Then the table with the foreign key second.
CREATE TABLE comments (
  comment_id SERIAL PRIMARY KEY,
  post_id SERIAL PRIMARY KEY,
  author_name text
  content text

-- The foreign key name is always {other_table_singular}venue_id
  post_id int,
  constraint fk_post foreign key(post_id)
    references post(id)
);
5. Create the tables
psql -h 127.0.0.1 database_name < albums_table.sql