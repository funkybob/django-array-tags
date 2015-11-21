from collections import Counter

from django.test import TestCase

from .models import TestModel

tags1 = ['one', 'two', 'three']
tags2 = ['one', 'five', 'eleven']
all_tags = set(tags1 + tags2)
tag_counts = Counter(tags1)
tag_counts.update(tags2)

class LazyTagTestCase(TestCase):

    def setUp(self):
        m = TestModel.objects.create(tags=tags1)
        n = TestModel.objects.create(tags=tags2)
        
    def test_all_values(self):
        v = TestModel.all_tags_values()
        self.assertEqual(set(v), all_tags)

    def test_count_values(self):
        v = TestModel.count_tags_values()
        for key, value in v.items():
            self.assertEqual(value, tag_counts[key])

    def test_cleanup(self):
        a = TestModel.objects.create(tags=['a', ' a ', 'b', ' b'])
        b = TestModel.objects.last()
        self.assertEqual(set(b.tags), set(['a', 'b']))

    def test_filtered_all(self):
        v = TestModel.objects.filter(tags__contains=['five']).all_tag_values('tags')
        self.assertEqual(set(v), set(tags2))

    def test_filtered_count(self):
        v = TestModel.objects.filter(tags__contains=['five']).count_tag_values('tags')
        for key, val in v.items():
            self.assertTrue(key in tags2)
            self.assertEqual(val, 1)
