from django.db import models


class Program(models.Model):
    TYPES = [
        ("PREGRADO", "Pregrado"),
        ("POSGRADO", "Posgrado"),
        ("TECNOLOGO", "Tecnólogo"),
        ("ESPECIALIZACION", "Especialización"),
        ("MASTER", "Master"),
    ]

    name = models.CharField(max_length=120)
    type_program = models.CharField(
        max_length=20,
        choices=TYPES,
        default="PREGRADO"
    )

    def __str__(self):
        return self.name


class Course(models.Model):
    CATEGORIES = [
        ("PRESENCIAL", "Presencial"),
        ("VIRTUAL", "Virtual"),
        ("HIBRIDO", "Híbrido"),
    ]

    name = models.CharField(max_length=100)

    program = models.ForeignKey(
        Program,
        on_delete=models.CASCADE,
        related_name="courses"
    )

    quotas = models.IntegerField()
    credit_number = models.IntegerField()

    category = models.CharField(
        max_length=10,
        choices=CATEGORIES,
        default="PRESENCIAL"
    )

    def __str__(self):
        return f"{self.name} ({self.program.name})"


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Inscription(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="inscriptions"
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="inscriptions"
    )

    date = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["student", "course"],
                name="unique_student_course"
            )
        ]

    def __str__(self):
        return f"{self.student.name} → {self.course.name}"