# Test Task
## For setting up project: 
1. Clone the repository
2. Create your own virtual environment
3. Install requirements
4. Set up MySQL database
5. Make your migrations
6. Create a new superuser
7. python manage.py runserver

## Routers
1.  http://localhost:8000/doctors/ - get all doctors
2.  http://localhost:8000/categories/ - get all categories
3.  http://localhost:8000/doctors/x - get solo doctor (where x is doctor Id)
4. http://localhost:8000/doctors/?category=x - get all doctors with selected category (where x is category name)
5.  http://localhost:8000/doctors/?work_experience=x - get all doctors with work experience more than x in days
6. http://localhost:8000/doctors/?sorted_by=x - get all doctors sorted by x (name, birthday, work_experience, id for default)
