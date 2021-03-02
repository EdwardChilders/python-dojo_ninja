from django.db import models


# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    # ninjas
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Ninja(models.Model):
    dojo_id = models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# from dojo_app.models import *
# Dojo.objects.create(
#   name="Coding",
#   city="San Jose",
#   state="CA"
# )

# Dojo.objects.create(
#   name="Bootcamp",
#   city="Seattle",
#   state="WA"
# )

# Dojo.objects.create(
#   name="The Dojo",
#   city="Los Angeles",
#   state="CA"
# )

# c = Dojo.objects.get(id=1)
# c.delete()

# c = Dojo.objects.get(id=2)
# c.delete()

# c = Dojo.objects.get(id=3)
# c.delete()

# Dojo.objects.create(
#   name="Coding",
#   city="San Jose",
#   state="CA"
# )

# Dojo.objects.create(
#   name="Bootcamp",
#   city="Seattle",
#   state="WA"
# )

# Dojo.objects.create(
#   name="The Dojo",
#   city="Los Angeles",
#   state="CA"
# )


# class1 = Dojo.objects.get(id=4)

# Ninja.objects.create(
#   dojo_id=class1,
#   first_name="JR",
#   last_name="Childers"
# )

# Ninja.objects.create(
#   dojo_id=class1,
#   first_name="Boss",
#   last_name="Mann"
# )

# Ninja.objects.create(
#   dojo_id=class1,
#   first_name="Marshawn",
#   last_name="Lynch"
# )

# class2 = Dojo.objects.get(id=5)

# Ninja.objects.create(
#   dojo_id=class2,
#   first_name="The",
#   last_name="Boss"
# )

# Ninja.objects.create(
#   dojo_id=class2,
#   first_name="Ya",
#   last_name="Boi"
# )

# Ninja.objects.create(
#   dojo_id=class2,
#   first_name="Derek",
#   last_name="Carr"
# )

# class3 = Dojo.objects.get(id=6)

# Ninja.objects.create(
#   dojo_id=class3,
#   first_name="My",
#   last_name="Homie"
# )

# Ninja.objects.create(
#   dojo_id=class3,
#   first_name="Rick",
#   last_name="Sanchez"
# )

# Ninja.objects.create(
#   dojo_id=class3,
#   first_name="Mr",
#   last_name="Robot"
# )

# Dojo.objects.all()[0].ninjas

# Dojo.objects.all()[2].ninjas

# Ninja.objects.all()[8].dojo_id

# Dojo.objects.create(
#   name="Codez",
#   city="Santa Cruz",
#   state="CA",
#   desc="The Desc"
# )

