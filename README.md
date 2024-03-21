Simple Blog System using Django
This is a simple blog system built using Django. It allows users to read blog posts, create new posts, and edit existing ones.

Features
View all blog posts
Create new blog posts
Edit existing blog posts
Installation
Clone the repository to your local machine:

bash
Copy code
git clone <repository_url>
Navigate to the project directory:

bash
Copy code
cd <project_directory>
Install the required dependencies using pip:

bash
Copy code
pip install -r requirements.txt
Apply database migrations:

bash
Copy code
python manage.py migrate
Usage
Run the development server:

bash
Copy code
python manage.py runserver
Open your web browser and navigate to http://127.0.0.1:8000/ to access the blog system.

Use the following URLs to perform different actions:

/: View all blog posts.
/post/new/: Create a new blog post.
/post/<int:pk>/edit/: Edit an existing blog post.
Testing
You can run the test suite to ensure that the application is functioning correctly:

bash
Copy code
python manage.py test
Contributing
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

License
This project is licensed under the MIT License.
