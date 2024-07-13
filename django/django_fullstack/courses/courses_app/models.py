from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self , postData):
        errors = {}
        if len(postData['name']) < 5 : 
            errors['name'] = "Name must be at least 5 characters"
        if len(postData['text_area']) < 15 :
            errors['text_area'] = 'Description must be at least 15 characters'
        return errors


class Course(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()


class Description(models.Model):
    desc = models.TextField()
    course = models.OneToOneField(Course , related_name='description' , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comments = models.TextField(null=True)
    course = models.ForeignKey(Course , related_name='comments' , on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



def view_courses():
    return Course.objects.all()

def create_course(name  ,description):
    new_course = Course.objects.create(name = name )
    new_description = Description.objects.create(desc = description , course = new_course)
    return new_course , new_description

def view_course_info(id):
    thecourse = Course.objects.get(id=id)
    return thecourse

def destroy_course(id):
    thecourse = Course.objects.get(id=id)
    return thecourse.delete()

def create_comment(id , com):
    return Comment.objects.create(comments = com , course = Course.objects.get(id=id))

#def view_comments(id):
    thecourse = Course.objects.get(id=id)
    return thecourse.comments.all()