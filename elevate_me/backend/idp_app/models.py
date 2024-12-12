from django.db import models

from django.contrib.auth.models import User

# UserProfile
# User model (supplement to the standard user model). 
# This model allows you to store additional information about the user, 
# including their level of knowledge in a particular area.
# UserProfile — One user can have only one profile that stores their level of knowledge.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Communication/Relationship/Connection (зв'язок) with the user
    knowledge_level = models.CharField(
        max_length=20, choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default='Beginner'
    ) # User knowledge level 

    def __str__(self):
        return f"{self.user.username} - {self.knowledge_level}"



# Topic
# Model of the topic the user will be learning
# This model contains information about each topic the user needs to learn, including a description, 
# priority, estimated time, and resources for learning.
# Topic — Each topic can be associated with multiple test results and development plans.
class Topic(models.Model):
    title = models.CharField(max_length=200) # Topic name
    description = models.TextField() # Description of topics
    resources = models.TextField()  # Resources for learning (links to courses can be added)
    priority = models.CharField(
        max_length=10, choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='Medium'
    )
    duration = models.CharField(max_length=100)  # Study duration

    def __str__(self):
        return self.title




# TestResult
# Model of test results
# This model stores the user's test results for each topic. It contains fields for the score, 
# whether the test passed or failed, and the relationship to the specific topic.
# TestResult — Each test is associated with a user and a topic.
class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Communication/Relationship (зв'язок) with the user
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # Communication/Relationship/Connection to the topic
    score = models.IntegerField()  # Evaluation/Test result in points (for example, from 0 to 100 or from 1 to 5 )
    passed = models.BooleanField(default=False) # Did the test pass?

    def __str__(self):
        return f"Test Result for {self.user.username} on {self.topic.title}"



# LearningPlan / DevelopmentPlan
# A model of an individual development plan
# This model is created for each user based on test results. 
# It includes the topic, learning status, and learning recommendations.
# LearningPlan — This is a model that stores each user's individual development plan for each topic.
class LearningPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Communication/Relationship (зв'язок) with the user
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # Communication/Relationship/Connection to the topic
    status = models.CharField(
        max_length=20, choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Not Started'
    ) # Learning status (e.g. "Not started", "In progress", "Completed")
    priority = models.CharField(
        max_length=10, choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='Medium'
    ) # Priority of topics for learning
    estimated_duration = models.CharField(max_length=100)  # # Estimated study duration
    resources = models.TextField()  # Recommended resources for study (courses, articles, books)

    def __str__(self):
        return f"Learning Plan for {self.user.username} - {self.topic.title}"





# Recommendation
# Model for course and training recommendations by topic
# This model includes specific recommendations for each topic (e.g., courses or articles to study). 
# Recommendation — Recommendations for each topic for further study.
class Recommendation(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # Communication/Relationship/Connection to the topic
    recommendation_text = models.TextField() # Text recommendation for study

    def __str__(self):
        return f"Recommendation for {self.topic.title}"

