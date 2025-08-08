from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    """
    A project has the following information:
        - Project name
        - Project code
        - Project description
        - Employer
        - Project start date
        - Project end date
        - Project progress
        - Project status
        - Latitude
        - Longitude
    """
    name = models.CharField(max_length=255, verbose_name="نام پروژه")
    code = models.CharField(max_length=50, unique=True, verbose_name="کد پروژه")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    employer = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="کارفرما")
    start_date = models.DateField(verbose_name="تاریخ شروع")
    end_date = models.DateField(verbose_name="تاریخ پایان")
    progress = models.PositiveIntegerField(default=0, help_text="درصد پیشرفت", verbose_name="پیشرفت")
    status = models.CharField(
        max_length=20,
        choices=[
            ('planning', 'برنامه‌ریزی'),
            ('in_progress', 'در حال اجرا'),
            ('completed', 'تکمیل شده'),
            ('on_hold', 'متوقف شده'),
            ('cancelled', 'لغو شده')
        ],
        default='planning',
        verbose_name="وضعیت"
    )
    lat = models.FloatField(null=True, blank=True, verbose_name="عرض جغرافیایی")
    lng = models.FloatField(null=True, blank=True, verbose_name="طول جغرافیایی")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ به‌روزرسانی")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه‌ها"
        ordering = ['-created_at']


class Phase(models.Model):
    """
    A project phase has the following information:
        - Phase name
        - Phase code
        - Phase description
        - Project
        - Phase start date
        - Phase end date
        - Phase progress
        - Phase status
    """
    name = models.CharField(max_length=255, verbose_name="نام فاز")
    code = models.CharField(max_length=50, unique=True, verbose_name="کد فاز")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="phases", verbose_name="پروژه")
    start_date = models.DateField(verbose_name="تاریخ شروع")
    end_date = models.DateField(verbose_name="تاریخ پایان")
    progress = models.PositiveIntegerField(default=0, help_text="درصد پیشرفت", verbose_name="پیشرفت")
    status = models.CharField(
        max_length=20,
        choices=[
            ('planning', 'برنامه‌ریزی'),
            ('in_progress', 'در حال اجرا'),
            ('completed', 'تکمیل شده'),
            ('on_hold', 'متوقف شده'),
            ('cancelled', 'لغو شده')
        ],
        default='planning',
        verbose_name="وضعیت"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ به‌روزرسانی")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "فاز"
        verbose_name_plural = "فازها"
        unique_together = ('name', 'project')
        ordering = ['-created_at']


class Activity(models.Model):
    """
    An activity has the following information:
        - Activity name
        - Activity code
        - Activity description
        - Phase
        - Activity start date
        - Activity end date
        - Activity progress
        - Activity status
    """
    name = models.CharField(max_length=255, verbose_name="نام فعالیت")
    code = models.CharField(max_length=50, unique=True, verbose_name="کد فعالیت")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE, related_name="activities", verbose_name="فاز")
    parent_activity = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE, related_name="sub_activities", verbose_name="فعالیت والد")
    start_date = models.DateField(verbose_name="تاریخ شروع")
    end_date = models.DateField(verbose_name="تاریخ پایان")
    progress = models.PositiveIntegerField(default=0, help_text="درصد پیشرفت", verbose_name="پیشرفت")
    status = models.CharField(
        max_length=20,
        choices=[
            ('planning', 'برنامه‌ریزی'),
            ('in_progress', 'در حال اجرا'),
            ('completed', 'تکمیل شده'),
            ('on_hold', 'متوقف شده'),
            ('cancelled', 'لغو شده')
        ],
        default='planning',
        verbose_name="وضعیت"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ به‌روزرسانی")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "فعالیت"
        verbose_name_plural = "فعالیت‌ها"
        unique_together = ('name', 'phase')
        ordering = ['-created_at']


class Dependency(models.Model):
    """
    A dependency between two activities:
        - Main activity
        - Dependent activity
        - Dependency type
    """
    activity = models.ForeignKey(
        Activity, 
        on_delete=models.CASCADE, 
        related_name="dependencies",
        verbose_name="فعالیت اصلی"
    )
    depends_on = models.ForeignKey(
        Activity, 
        on_delete=models.CASCADE, 
        related_name="dependents",
        verbose_name="فعالیت وابسته"
    )
    dependency_type = models.CharField(
        max_length=20,
        choices=[
            ('finish_to_start', 'فعالیت وابسته بعد از تمام شدن فعالیت اصلی شروع می‌شود'), 
            ('start_to_start', 'فعالیت وابسته همزمان با فعالیت اصلی شروع میشود'), 
            ('finish_to_finish', 'فعالیت وابسته همزمان با فعالیت اصلی تمام میشود'),
            ('start_to_finish', 'فعالیت وابسته بعد از شروع فعالیت اصلی تمام میشود')
        ],
        verbose_name="نوع وابستگی"
    )
    
    def __str__(self):
        return f"{self.activity.name} -> {self.depends_on.name} ({self.dependency_type})"

    class Meta:
        verbose_name = "وابستگی"
        verbose_name_plural = "وابستگی‌ها"
        unique_together = ('activity', 'depends_on', 'dependency_type')
        ordering = ['activity__name', 'depends_on__name']