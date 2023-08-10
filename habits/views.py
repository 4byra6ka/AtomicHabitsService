from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.serializers import HabitSerializer
from habits.services import create_periodic_task
from users.models import User


class HabitListView(ListAPIView):
    """Контроллер списка привычек"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    # permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = HabitPaginator

    # def get_queryset(self):
    #     # check_habit_time()
    #     user = self.request.user
    #     search_owners = []
    #     owners = Habit.objects.filter()
    #     # find and filter users habits
    #     for find_owner in owners:
    #         if find_owner.is_public is True:
    #             search_owners.append(find_owner)
    #         else:
    #             if find_owner.owner == user:
    #                 search_owners.append(find_owner)
    #     return search_owners


class HabitDetailView(RetrieveAPIView):
    """Контроллер описания привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    # permission_classes = [IsAuthenticated, IsOwner]


class HabitCreateView(CreateAPIView):
    """Контроллер создания привычки"""
    # queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    # permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        # new_habit.owner = self.request.user
        new_habit.owner = User.objects.get(username="admin")
        new_habit.task = create_periodic_task(new_habit.frequency, new_habit.pk, new_habit.time)
        new_habit.save()



class HabitUpdateView(UpdateAPIView):
    """Контроллер обновления привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    # permission_classes = [IsAuthenticated, IsOwner]


class HabitDeleteView(DestroyAPIView):
    """Контроллер удаления привычки"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    # permission_classes = [IsAuthenticated, IsOwner]


class PublicHabitListView(ListAPIView):
    """Контроллер списка публичных привычек"""
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
