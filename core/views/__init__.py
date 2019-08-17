from core.models import Tag


class UpdateCategoryMixin:

    TAG_CATEGORY_MAP = {}

    def _get_categories(self, tags):
        """
        Update category of item based upon tags
        :param items:
        :return:
        """
        return set(filter(None, [self.tag_category_map.get(t) for t in tags]))

    def _update_items(self, items):
        """
        Update category of items based upon tags
        :param items:
        :return:
        """
        for item in items:
            if not item.get('tags'):
                continue
            categories = self._get_categories(item['tags'])
            if categories:
                item['categories'] = item.get('categories', [])
                item['categories'].extend(categories)
        return items

    @property
    def tag_category_map(self):
        """
        # Cache Tag to Category mapping
        :return:
        """
        if not hasattr(self, '_tag_category_map'):
            queryset = Tag.objects.select_related('category').filter(category__isnull=False)
            self._tag_category_map = dict(queryset.values_list('name', 'category__name'))
        return self._tag_category_map


class ValidationMixin:

    items_key = 'events'

    def _validate(self):
        """
        Validate data
        :return:
        """
        errors = {}
        for i, item in enumerate(self.request.data.get(self.items_key)):
            serializer = self.serializer_class(data=item)
            if serializer.is_valid():
                continue
            errors[str(i)] = serializer.errors
        return errors
