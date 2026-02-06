from django.db.models import CharField, IntegerField, Model, ForeignKey,CASCADE

class StudentData(Model):
    name = CharField(max_length=200)
    age = IntegerField(default=0)
    

    def __str__(self):
        return self.name


class StudentTask(Model):
    student = ForeignKey(StudentData, on_delete=CASCADE)
    task = CharField(max_length=200)
    description = CharField(max_length=250)

    def __str__(self):
        return f"{self.task} - {self.student.name}"




