# Library-Management-System

The repository contains web pages using Django web development framework in python language. It contains
  a) Two Forms Students and Books 
  b) One Form to issue a book to particular student. (where multiple transaction require on one student).
 
## Getting Started
 

Open terminal using Ctrl + Alt + T. Run the following command <br>
```ruby 
   git clone https://github.com/Agha-Muqarib/Library-Management-System.git 
```

Create and activate virtual environment using <br>
```ruby
   virtualenv -p python3 venv
```
<br>

```ruby
    cd venv
``` 
<br>

```ruby 
   source bin/activate
``` 
<br>

### Run Steps:
```ruby 
   cd ..
```

```ruby 
   cd LMS
```


```ruby 
   python manage.py makemigrations
```

```ruby 
   python manage.py migrate
``` 

```ruby 
   python manage.py runserver
``` 
