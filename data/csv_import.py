import csv
import os

from django.utils.dateparse import parse_datetime
from users.models import User
from artworks.models import Category, Genre, Title
from reviews.models import Review, Comment


with open('data/users.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == 'id':
            continue
        obj, created = User.objects.get_or_create(
            id=int(row[0]),
            username=row[1],
            email=row[2],
            role=row[3],
            bio=row[4],
            first_name=row[5],
            last_name=row[6]
        )

with open('data/category2.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == 'id':
            continue
        obj, created = Category.objects.get_or_create(
            id=int(row[0]),
            name=row[1],
            slug=row[2],
        )

with open('data/genre2.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == 'id':
            continue
        obj, created = Genre.objects.get_or_create(
            id=int(row[0]),
            name=row[1],
            slug=row[2]
        )

with open('data/titles2.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == 'id':
            continue
        obj, created = Title.objects.get_or_create(
            id=int(row[0]),
            name=row[1],
            year=int(row[2]),
            category=Category.objects.get(id=int(row[3]))
        )

with open('data/genre_title.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == 'id':
            continue
        title = Title.objects.get(id=int(row[1]))
        print(title)
        genre = Genre.objects.get(id=int(row[2]))
        print(genre)
        title.genre.add(genre)


with open('data/review2.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == 'id':
            continue
        obj, created = Review.objects.get_or_create(
            id=int(row[0]),
            title_id=Title.objects.get(id=int(row[1])),
            text=row[2],
            author=User.objects.get(id=int(row[3])),
            score=int(row[4]),
            pub_date=parse_datetime(row[5])
        )

with open('data/comments2.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == 'id':
            continue
        obj, created = Comment.objects.get_or_create(
            id=int(row[0]),
            review_id=Review.objects.get(id=int(row[1])),
            text=row[2],
            author=User.objects.get(id=int(row[3])),
            pub_date=parse_datetime(row[4])
        )
