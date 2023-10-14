## MYSQL Advanced

This repository aims to demonstrate my understanding of advanced mysql concepts such as 

* creating tables with constaints
* optimizing queries by adding indexes
* implementing stored procedures and functions
* implementing views
* implementing triggers

### Creating tables with constraints
A constraint is a rule that defines the valid data for a table. It can be used to ensure that the data is accurate and consistent.

**Example**
This example creates a users table with a constraint that requires the username column be unique.
```SQL
CREATE TABLE users (
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);
```

### Optimizing queries by adding indexes
Indexes are data structures that help mysql find data quickly.
When an index is added to a column MYSQL creates a sorted list of the values in that column. Allowing mysql to quickly find rows where the value in that column matches a specific value.

**Example**
Adding an index to the username column in table users can be achieved as follows

```SQL
ALTER TABLE users ADD INDEX (username);
```
### Stored procedures and functions

Stored procedures and functions are pre-compiled SQL statements that can be stored in the database and executed on demand. They can be used to encapsulate complex SQL logic and make it easier to reuse code.

**Example**
To create a stored procedure or function, you can use the `CREATE PROCEDURE` or `CREATE FUNCTION` statement.
The following statement creates a stored procedure `get_user_by_username`
```SQL 
CREATE PROCEDURE get_user_by_username(username VARCHAR(255))
BEGIN
    SELECT * FROM users WHERE username = username;
END;
``` 
To execute a stored procedure or function, you can use the CALL statement. 

```SQL
CALL get_user_by_username('user_254');

SELECT * FROM @user;
```

### Implementing Views
Views are virtual tables that are based on one or more tables in the database. They can be used to simplify complex queries and restrict access to data.

**Example**
To create a view, you can use the `CREATE VIEW` statement. For example, the following statement creates a view called active_users that returns all users who have logged in within the past 24 hours

```SQL
CREATE VIEW active_users AS
SELECT * FROM users WHERE last_login_at > CURRENT_TIMESTAMP - INTERVAL 24 HOUR;
```
To query the view, we use the view name as if it were a table

```SQL
SELECT * FROM active_users;
```

### Implementing triggers
Triggers are special procedures that are automatically executed when certain events occur in the database, such as inserting, updating, or deleting data. Triggers can be used to enforce business rules and maintain data integrity.

To create a trigger, you can use the `CREATE TRIGGER` statement. For example, the following statement creates a trigger called `audit_user_changes` that logs all changes to the users table:

```SQL
CREATE TRIGGER audit_user_changes
AFTER INSERT, UPDATE, DELETE ON users
FOR EACH ROW
BEGIN
  INSERT INTO audit_log (event, table_name, row_data)
  VALUES (
    IF(NEW.id IS NULL, 'INSERT', IF(NEW.id <> OLD.id, 'UPDATE', 'DELETE')),
    'users',
    CONCAT('(', NEW.id, ', ', NEW.username, ', ', NEW.password, ')')
  );
END;
```

