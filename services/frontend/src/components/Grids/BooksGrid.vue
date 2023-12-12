<template>
  <div class="container text-left mx-auto px-4 mb-10">
    <h3 class="text-lg font-semibold">
      Showing {{ total }} books for "{{ searchQuery }}"
    </h3>
    <div class="grid grid-cols-2 gap-4">
      <BookCard
        v-for="(book, index) in paginatedBooks"
        :key="index"
        :book="book[3][1]"
        @select="selectBook"
      />
    </div>
    <PaginationSimple
      class="flex justify-center mt-10 mb-15"
      :totalPages="totalPages"
      v-model="currentPage"
    ></PaginationSimple>
  </div>
  <LargeModal :book="selectedBook" :show="showModal" @close="toggleModal" />
</template>

<script>
import axios from "axios";
import LargeModal from "@/components/Cards/LargeModal.vue";
import BookCard from "@/components/Cards/BookCard.vue";
import PaginationSimple from "@/components/Pagination/PaginationSimple.vue";

export default {
  name: "BooksGrid",
  components: {
    LargeModal,
    BookCard,
    PaginationSimple,
  },
  data() {
    return {
      books: [],
      total: 25,
      searchQuery: this.$route.query.q,
      currentPage: 1,
      itemsPerPage: 20,
      selectedBook: null,
      showModal: false,
    };
  },
  created() {
    this.fetchBooks();
  },
  watch: {
    $route: "fetchBooks",
    currentPage: "fetchBooks",
  },
  methods: {
    async fetchBooks() {
      console.log(this.searchQuery);
      try {
        const response = await axios.get(
          `http://localhost:8000/api/resource/search`,
          {
            params: {
              query: this.searchQuery,
              page: this.currentPage,
              type: "book",
            },
          }
        );
        this.books = response.data;
        this.total = response.data.length;
      } catch (error) {
        console.error("Error fetching books:", error);
      }
    },
    selectBook(book) {
      this.selectedBook = book;
      this.toggleModal();
    },
    toggleModal() {
      this.showModal = !this.showModal;
    },
  },
  computed: {
    paginatedBooks() {
      return this.books;
    },
    totalPages() {
      return Math.ceil(this.total / this.itemsPerPage);
    },
  },
};
</script>

<style scoped></style>
