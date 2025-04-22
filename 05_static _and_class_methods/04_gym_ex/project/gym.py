from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.trainer import Trainer
from project.subscription import Subscription


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = [subscription for subscription in self.subscriptions if subscription.id == subscription_id][0]
        customer = [customer for customer in self.customers if customer.id == subscription.customer_id][0]
        trainer = [trainer for trainer in self.trainers if trainer.id == subscription.trainer_id][0]
        exercise_plan = [plan for plan in self.plans if plan.id == subscription.exercise_id][0]
        equipment = [equipment for equipment in self.equipment if equipment.id == exercise_plan.equipment_id][0]

        return f"{subscription}\n{customer}\n{trainer}\n{equipment}\n{exercise_plan}"



