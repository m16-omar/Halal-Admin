from django.db import models

class Seeker(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    STATUS_CHOICES = [
        ('Verified', 'Verified'),
        ('Pending', 'Pending'),
        ('Unverified', 'Unverified'),
    ]
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    state = models.CharField(max_length=50)
    wali_name = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Unverified')
    join_date = models.DateField()

    def __str__(self):
        return self.full_name

class Wali(models.Model):
    name = models.CharField(max_length=100)
    seeker = models.ForeignKey(Seeker, on_delete=models.CASCADE, related_name='walis')
    relationship = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.relationship} of {self.seeker.full_name})"

class Imam(models.Model):
    name = models.CharField(max_length=100)
    mosque = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    is_verified = models.BooleanField(default=True)
    matches_supervised = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Match(models.Model):
    STATUS_CHOICES = [
        ('nikah', 'Nikah'),
        ('meeting planned', 'Meeting Planned'),
        ('active chat', 'Active Chat'),
        ('closed', 'Closed'),
    ]
    seeker_female = models.ForeignKey(Seeker, on_delete=models.CASCADE, related_name='matches_as_female')
    seeker_male = models.ForeignKey(Seeker, on_delete=models.CASCADE, related_name='matches_as_male')
    imam = models.ForeignKey(Imam, on_delete=models.SET_NULL, null=True, related_name='matches')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active chat')
    created_at = models.DateField()

    def __str__(self):
        return f"{self.seeker_male.full_name} & {self.seeker_female.full_name}"

class ChatMessage(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='chat_messages')
    sender = models.CharField(max_length=100)
    text = models.TextField()
    timestamp = models.DateTimeField()
    is_flagged = models.BooleanField(default=False)
    flag_reason = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.sender}: {self.text[:30]}"

class Report(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('reviewing', 'Reviewing'),
        ('resolved', 'Resolved'),
    ]
    reporter = models.CharField(max_length=100)
    reported_user = models.CharField(max_length=100)
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField()

    def __str__(self):
        return f"Report against {self.reported_user}"

class VerificationRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    user_name = models.CharField(max_length=100)
    document_type = models.CharField(max_length=50)
    document_preview_url = models.CharField(max_length=255)
    created_at = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Verification for {self.user_name}"

class RevenueTransaction(models.Model):
    STATUS_CHOICES = [
        ('success', 'Success'),
        ('failed', 'Failed'),
    ]
    user_name = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=50)  # e.g., 'Subscription', 'Match Fee', 'Donation'
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='success')
    created_at = models.DateField()

    def __str__(self):
        return f"{self.user_name} - {self.transaction_type} ({self.amount})"

class Mosque(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    chief_imam = models.CharField(max_length=100)
    active_users = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.state})"
