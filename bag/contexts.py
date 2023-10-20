from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from courses.models import Course


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for course_id, quantity in bag.items():
        course = get_object_or_404(Course, pk=course_id)
        total += course.price
        product_count += quantity
        bag_items.append({
            'course_id': course_id,
            'quantity': quantity,
            'course': course,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }

    return context
