from django.db import models
from django.utils.text import slugify
from root.models import Tags, LearningTopics

class ProgDSA(models.Model):
    COMPLEXITIES = [
        (1,'O(1)'),
        (2,'O(log n)'),
        (3,'O(sqrt(n))'),
        (4,'O(n)'),
        (5,'O(n logn)'),
        (6,'O(n^2)'),
        (7,'O(n^3)'),
        (8,'O(n^k)'),
        (9,'O(2^n)'),
        (10,'O(n!)'),
    ]

    DIFFICULTY_LEVEL = [
        (1,'Lowest Difficulty'),
        (2,'Low Difficulty'),
        (3,'Moderate Difficulty'),
        (4,'High Difficulty'),
        (5,'Highest Difficulty'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=128, null=True)
    link = models.CharField(max_length=128, null=True, blank=True)
    learning_topics = models.ManyToManyField(LearningTopics, related_name="dsa_topic", blank=True)
    slvd = models.BooleanField(default=False, help_text="was the problem solved?")
    tts = models.IntegerField(default=0, help_text="time to solve the problem")
    best_tc = models.IntegerField(choices=COMPLEXITIES, help_text="best time complexity possible")
    achieved_tc = models.IntegerField(choices=COMPLEXITIES, help_text="achieved time complexity")
    best_sc = models.IntegerField(choices=COMPLEXITIES, help_text="best space complexity possible")
    achieved_sc = models.IntegerField(choices=COMPLEXITIES, help_text="achieved space complexity")
    self_msg = models.TextField(blank=True)
    perc_diff = models.IntegerField(choices=DIFFICULTY_LEVEL, help_text="precieved difficulty")
    tags = models.ManyToManyField(
        Tags,
        related_name='dsa_tags',
        blank=True
    )

class ProgSQL(models.Model):
    DIFFICULTY_LEVEL = [
        (1,'Lowest Difficulty'),
        (2,'Low Difficulty'),
        (3,'Moderate Difficulty'),
        (4,'High Difficulty'),
        (5,'Highest Difficulty'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=128, null=True)
    link = models.CharField(max_length=128, null=True, blank=True)
    learning_topics = models.ManyToManyField(LearningTopics, related_name="sql_topic", blank=True)
    slvd = models.BooleanField(default=False, help_text="was the problem solved?")
    tts = models.IntegerField(default=0, help_text="time to solve the problem")
    self_msg = models.TextField(blank=True)
    perc_diff = models.IntegerField(choices=DIFFICULTY_LEVEL, help_text="precieved difficulty")
    tags = models.ManyToManyField(
        Tags,
        related_name='sql_tags',
        blank=True
    )

class ResearchPaper(models.Model):
    DIFFICULTY_LEVEL = [
        (1,'Lowest Difficulty'),
        (2,'Low Difficulty'),
        (3,'Moderate Difficulty'),
        (4,'High Difficulty'),
        (5,'Highest Difficulty'),
    ]

    UNDERSTANDING_LEVEL = [
        (1,'What did I just read?'),
        (2,'I kind of get it, but not really'),
        (3,'Yeah, I think I understand this.'),
        (4,'I am quite confident about this.'),
        (5,'I can explain this to most people I know.'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=128)
    link = models.CharField(max_length=128, null=True, blank=True)
    link_summarization = models.CharField(max_length=128, null=True, blank=True)
    learning_topics = models.ManyToManyField(LearningTopics, related_name="research_topic", blank=True)
    first_read_time = models.IntegerField(default=0, help_text="time to read for first pass")
    final_read_time = models.IntegerField(default=0, help_text="total time to read for including all passes")
    perc_unde = models.IntegerField(choices=UNDERSTANDING_LEVEL, help_text="percieved level of understanding after final pass and summarization")
    self_msg = models.TextField(blank=True)
    perc_diff = models.IntegerField(choices=DIFFICULTY_LEVEL, help_text="precieved difficulty")
    tags = models.ManyToManyField(
        Tags,
        related_name='research_paper_tags',
        blank=True
    )

class MockInterview(models.Model):
    INTERVIEW_MODE = [
        ('With Single Person','With Single Person'),
        ('With a Group of People (like a Panel)','With a Group of People (like a Panel)'),
        ('On a Website with Collection of Interview Questions','On a Website with Collection of Interview Questions'),
        ('I am quite confident about this.','I am quite confident about this.'),
        ('I can explain this to most people I know.','I can explain this to most people I know.'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mode = models.CharField(choices=INTERVIEW_MODE,max_length=128, null=True, blank=True)
    learning_topics = models.ManyToManyField(LearningTopics, related_name="interview_topic", blank=True)
    high_confidence_question_count = models.IntegerField(default=0, help_text = "number of questions where you had high perceived confidence")
    medium_confidence_question_count = models.IntegerField(default=0, help_text = "number of questions where you had medium perceived confidence")
    low_confidence_question_count = models.IntegerField(default=0, help_text = "number of questions where you had low perceived confidence")
    no_clue_question_count = models.IntegerField(default=0, help_text="number of questions where you had no clue, what was happening.")
    total_question_count = models.IntegerField(default=0, help_text="total questions")
    tti= models.CharField(default=0,help_text="")
    self_msg = models.TextField(blank=True)
    tags = models.ManyToManyField(
        Tags,
        related_name='mock_interview_tags',
        blank=True
    )
