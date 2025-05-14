from django.db.models import Q
from .models import Product, Category


class ProductService:
    @staticmethod
    def search_products(
            search_query=None,
            sort_by=None,
            sort_direction='asc',
            categories=None,
            page=0,
            size=20
    ):
        """
        Search and filter products with sorting and pagination
        """

        queryset = Product.objects.all()

        # Search filter
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query)
            )

        # Category filter
        if categories:
            queryset = queryset.filter(category__in=categories)

        # Safe sort mapping
        # Sorting
        allowed_fields = ['price', 'title', 'rating']  # add more if needed

        if sort_by in allowed_fields:
            sort_field = sort_by
            if sort_direction == 'desc':
                sort_field = f'-{sort_by}'
            queryset = queryset.order_by(sort_field)
        else:
            # Default fallback (e.g., rating descending)
            queryset = queryset.order_by('-rating')

        # Pagination
        start = page * size
        end = start + size

        return queryset[start:end]
