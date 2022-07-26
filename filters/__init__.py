from aiogram import Dispatcher
from . import AdminFilter,GroupFilter,PrivateFilter
from loader import dp
# from .is_admin import AdminFilter


if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter.IsAdmin)
    dp.filters_factory.bind(GroupFilter.IsGroup)
    dp.filters_factory.bind(PrivateFilter.IsPrivate)