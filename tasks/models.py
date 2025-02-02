# IMPORT BUILT-IN LIBRARIES
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# INFO
"""
    #== TO DO CATEGORIES IDEA FROM CHATGPT ==#

    1. Personal
        Tasks related to personal life and self-care, such as appointments, personal errands, or hobbies.
            Examples: "Call mom," "Buy groceries," "Go to the gym."
    2. Work/Professional
        Tasks related to the user's job, projects, or professional development.
            Examples: "Complete quarterly report," "Attend team meeting," "Respond to emails."
    3. Home
        Tasks related to household management, such as cleaning, maintenance, or organizing.
            Examples: "Mop the floor," "Fix leaking tap," "Organize closet."
    4. Urgent
        High-priority tasks that need immediate attention.
            Examples: "Submit project proposal by noon," "Respond to urgent client email."
    5. Study/School
        Tasks related to academic work or learning goals.
            Examples: "Study for math test," "Complete assignment," "Attend lecture."
    6. Health & Wellness
        Tasks related to maintaining physical and mental health.
            Examples: "Go for a walk," "Prepare healthy meals," "Meditate."
    7. Shopping
        Tasks for making purchases or tracking shopping lists.
            Examples: "Order new shoes," "Buy birthday gift," "Pick up office supplies."
    8. Finance
        Tasks related to managing money, budgeting, and financial planning.
            Examples: "Pay bills," "Review budget," "Check bank statements."
    9. Travel
        Tasks related to upcoming trips or travel planning.
            Examples: "Book flight tickets," "Pack for the trip," "Get travel insurance."
    10. Social/Events
        Tasks related to socializing, events, or gatherings.
            Examples: "RSVP to wedding," "Call friends," "Organize dinner party."
    11. Maintenance/Repairs
        Tasks for any maintenance or repair jobs, either at home or elsewhere.
            Examples: "Fix the car," "Service the AC unit," "Replace light bulb."
    12. Goals/Long-term Projects
        Tasks that contribute to achieving long-term personal or professional goals.
            Examples: "Write a book," "Launch new business," "Learn a new language."
    13. Miscellaneous
        A catch-all category for tasks that don’t fit neatly into other categories.
            Examples: "Read new book," "Clean out email inbox," "Explore new hobby."
    14. Team/Collaboration
        Tasks that involve working with others, such as group projects or team assignments.
            Examples: "Prepare presentation for team meeting," "Review teammate’s code," "Assign tasks to colleagues."
    15. Creative
        Tasks related to artistic or creative projects.
            Examples: "Design logo," "Write blog post," "Create video content."
    16. Learning & Development
        Tasks for developing new skills, reading, or training.
            Examples: "Complete online course," "Practice coding," "Watch educational video."
    17. Family
        Tasks related to family obligations and activities.
            Examples: "Pick up kids from school," "Family dinner," "Plan vacation."
    18. Technology/IT
        Tasks related to tech maintenance, updates, or IT-related work.
            Examples: "Update software," "Back up files," "Fix laptop issues."
    19. Volunteer/Charity
        Tasks related to giving back to the community or charitable causes.
            Examples: "Organize charity event," "Volunteer at food bank," "Donate clothes."
    20. Projects
        For specific ongoing projects, breaking them down into smaller tasks.
            Examples: "Design phase of project X," "Marketing plan for project Y," "Write research paper."
"""


# TASK CATEGORIES (home, workout, study, hobby, entertaintment, unset, ...)
class Category(models.Model):
    name = models.CharField(max_length=16)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


# TASK TYPE WILL DEFINE IS TASK WILL HAVE MILESTONES (0 > 3 > 15 ...) OR JUST WILL INCOMPLETE/DONE (0 or 1)
class TypeOfTask(models.Model):
    name = models.CharField(max_length=16)
    def __str__(self):
        return self.name


# LOG HISTORY OF USER'S
class LogHistory(models.Model):
    LOG_CATEGORIES = [('create','Create'), ('update','Update'), ('delete','Delete'), ('error','Error'), ('authentication','Authentication')]
    user = models.ForeignKey(User, on_delete=models.CASCADE) # related_name='user'
    category = models.CharField(choices=LOG_CATEGORIES, max_length=16)
    event = models.TextField()
    datentime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.id} • {self.category} • {self.event} • {self.datentime}'


# MODEL FOR TASK CARD
class Task(models.Model):
    PRIORITY_OPTIONS = [(1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), (10,10)]
    STATUS_OPTIONS = [(1,'1 → Incomplete'), (2,'2 → Work In Progress'), (3,'3 → Done')]
    category_of_task = models.ManyToManyField(Category, null=True, blank=True)
    type_of_task = models.ForeignKey(TypeOfTask, on_delete=models.CASCADE, null=True, blank=True) # related_name='tasks'
    todo = models.TextField(max_length=256, null=True, blank=True)
    priority_level = models.IntegerField(choices=PRIORITY_OPTIONS, default=1)
    todo_status = models.IntegerField(choices=STATUS_OPTIONS, default=1) # CONDITION IN HERE FOR SEPARATION, WHEN CHOOSE TYPE OF TASK, ONLY NECESSARY MODEL MUST BE VISIBLE
    progression_start = models.IntegerField(default=0)
    progression_end = models.IntegerField(default=1) # REQUIRES TRY EXCEPT OR ANY ERROR HANDLER, ONLY ALLOW START<END
    # is_starred = models.BooleanField(default=False)
    added_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='tasks', null=True)
    def __str__(self):
        all_categories_of_current_task = ''
        for category in self.category_of_task.all():
            all_categories_of_current_task += f'{(category.name)},'
        categ_str = all_categories_of_current_task[0:-1:1]

        return f'#{self.id} ▲▼ Categories: {categ_str} ←→ Type: {self.type_of_task} ▲▼ Task: {self.todo} ▲▼ Added: {self.added_time} ←→ Updated: {self.updated_time}'
