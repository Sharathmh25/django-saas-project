from django.core.management.base import BaseCommand
from faker import Faker
from account.models import User
from tenant.models import Tenant
from task.models import Task
import random

fake = Faker()

class Command(BaseCommand):
    help = "Generate fake data"

    def handle(self, *args, **kwargs):
        
        # 🔷 Create Tenants
        tenants = []
        for _ in range(3):
            tenant = Tenant.objects.create(
                name=fake.company(),
                domain=fake.domain_name()
            )
            tenants.append(tenant)

        # 🔷 Create Users
        users = []
        for _ in range(5):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password="1234",
                tenant=random.choice(tenants),
                is_admin=random.choice([True, False]),
                is_customer=True
            )
            users.append(user)

        # 🔷 Create Tasks
        for _ in range(20):
            Task.objects.create(
                title=fake.sentence(),
                description=fake.text(),
                tenant=random.choice(tenants),
                created_by=random.choice(users),
                status=random.choice(['Pending', 'Done'])
            )

        self.stdout.write(self.style.SUCCESS("Fake data generated successfully!"))