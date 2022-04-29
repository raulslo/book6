from django.shortcuts import get_object_or_404

from . import models, forma

from datetime import datetime, timedelta
from django.views import generic

start_date = datetime.today() - timedelta(days=365)


class BookListView(generic.ListView):
    template_name = "book_list.html"
    queryset = models.Book.objects.order_by("-id")

    def get_queryset(self):
        return self.queryset


class BookDetailView(generic.DetailView):
    template_name = "books_deteil.html"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=book_id)


class BookCreateView(generic.CreateView):
    template_name = "book_add.html"
    form_class = forma.BookForm
    queryset = models.Book.objects.all()
    success_url = "/book/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookCreateView, self).form_valid(form=form)


class BookUpdateView(generic.UpdateView):
    template_name = "book_update.html"
    form_class = forma.BookForm
    success_url = "/book/"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=book_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookUpdateView, self).form_valid(form=form)


class BookDeleteView(generic.DeleteView):
    success_url = "/book"
    template_name = "confirm_delete_book.html"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=book_id)
