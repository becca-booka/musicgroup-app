from django.db import models

# Create your models here.

# Post model
class Post(models.Model):
    """This class contains the post database table for the blog section of the app with fields for
       the following (which are class variables):

        * The unique id that is automatically assigned to each post entry - this is the primary key of the database
        * The title of the blog post - input method is a CharField with a max length of 140 characters
        * The body of the blog post - input method is a TextField
        * The signature of the writer that is automatically added at the bottom of each blog post - input method is
          a CharField with a max length of 140 characters, and is set to a default signature
        * The date that the blog post is published - input method is a DateTimeField
    """

    id= models.AutoField(primary_key=True)
    title = models.CharField(max_length=140)
    body=models.TextField()
    signature=models.CharField(max_length=140, default="Earth, Wind and Angelfire")
    date=models.DateTimeField()
    
    def __str__(self):
      """This method will return the details stored in the title field of the post database table
          
        :returns: The details stored in the title field of the post database table
             
        :rtype: str
      """
       
      return self.title


# Question model
class Question(models.Model):
    """This class contains the question database for the polls section of the app with fields for the following:
       
        * The questions details - method of input is a CharField with a max length of 200 characters
        * The date the question was published - method of input is a DateTimeField
    """
    
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """This method will return the details stored in the question_text field of the question database
            
            :return: The details stored in the question_text field of the question database
            
            :rtype: str
        """
        
        return self.question_text


# Choice model
class Choice(models.Model):
    """This class contains the database that stores the choices presented to the user in the poll section of the app
       with fields for the following:
        
        * The details of the question_text field that is stored in the question database - this field is the foreignkey
          that links the choice and question databases together
        * The details stored in the choice_text field - method of input is a CharField with a max length of 200 characters
        * This fields stores the counter that records how many times each choice is selected - method of input is a
          IntegerField that default setting is set to 0
    """
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """This method returns the details stored in the choice_text field of the choice database
        
           :returns: The details stored in the choice_text field of the choice database
           
           :rtype: str
        """
        
        return self.choice_text     