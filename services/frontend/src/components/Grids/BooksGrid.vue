<template>
  <div class="container text-left mx-auto px-4 mb-10">
    <h3 class="text-lg font-semibold">
      Showing {{ total }} books for "{{ searchQuery }}"
    </h3>
    <div class="grid grid-cols-4 gap-4">
      <BookCard
        v-for="(book, index) in books"
        :key="index"
        :bookCover="book.cover"
        :title="book.title"
        :author="book.author"
        :rating="book.rating"
      />
    </div>
    <PaginationSimple
      class="flex justify-center mt-10 mb-15"
      :totalPages="totalPages"
      v-model="currentPage"
    ></PaginationSimple>
  </div>
</template>

<script>
import BookCard from "@/components/Cards/BookCard.vue";
import PaginationSimple from "@/components/Pagination/PaginationSimple.vue";

export default {
  name: "BooksGrid",
  components: {
    BookCard,
    PaginationSimple,
  },
  data() {
    return {
      books: [
        {
          cover:
            "https://m.media-amazon.com/images/I/A1GbblX7rOL._AC_UY218_.jpg",
          title: "Deep Learning",
          author: "Ian Goodfellow, Yoshua Bengio",
          rating: 4.6,
        },
        {
          cover:
            "https://m.media-amazon.com/images/I/61N9oTVT1IL._AC_UY218_.jpg",
          title: "Deep Learning with Python, Second Edition",
          author: "Francois Chollet",
          rating: 4.7,
        },
        {
          cover:
            "https://m.media-amazon.com/images/I/71WzAPykhHL._AC_UF350,350_QL50_.jpg",
          title:
            "The Principles of Deep Learning Theory: An Effective Theory...",
          author: " Daniel A. Roberts, Sho Yaida, Boris Hanin",
          rating: 4.8,
        },
        {
          cover:
            "https://m.media-amazon.com/images/I/A1GbblX7rOL._AC_UY218_.jpg",
          title: "Deep Learning",
          author: "Ian Goodfellow, Yoshua Bengio",
          rating: 4.6,
        },
        {
          cover:
            "https://m.media-amazon.com/images/I/61N9oTVT1IL._AC_UY218_.jpg",
          title: "Deep Learning with Python, Second Edition",
          author: "Francois Chollet",
          rating: 4.7,
        },
        {
          cover:
            "https://m.media-amazon.com/images/I/71WzAPykhHL._AC_UF350,350_QL50_.jpg",
          title:
            "The Principles of Deep Learning Theory: An Effective Theory...",
          author: " Daniel A. Roberts, Sho Yaida, Boris Hanin",
          rating: 4.8,
        },
      ],
      total: 6,
      searchQuery: "deep learning",
      currentPage: 1,
      itemsPerPage: 4,
    };
  },
  computed: {
    paginatedBooks() {
      let start = (this.currentPage - 1) * this.itemsPerPage;
      let end = start + this.itemsPerPage;
      return this.books.slice(start, end);
    },
    totalPages() {
      return Math.ceil(this.books.length / this.itemsPerPage);
    },
  },
  watch: {
    currentPage() {
      // Handle page change if necessary, e.g., fetch new data
    },
  },
};
</script>

<style scoped></style>
