<template>
  <div class="container mx-auto px-4">
    <div class="grid grid-cols-5 gap-4">
      <BookCard
        v-for="(book, index) in books"
        :key="index"
        :bookCover="book.cover"
        :title="book.title"
        :author="book.author"
        :description="book.description"
      />
    </div>
  </div>
</template>

<script>
import BookCard from "@/components/Cards/BookCard.vue";

export default {
  name: "BooksGrid",
  components: {
    BookCard,
  },
  data() {
    return {
      books: [
        // Populate this array with objects containing cover, title, and description for each book
        // Example:
        {
          cover:
            "https://images.qloo.com/i/fffff616-b9ef-455e-9336-deec744dfcc8-360x504-outside.webp",
          title: "Book Title 1",
          author: "Someone Famous",
          description:
            "When Carley Sutherland receives a frantic call for help, she races to a desolate park to meet her best friend. On a dimly-lit park bench, Carley's friend fumbles in her handbag for her",
        },
        {
          cover:
            "https://images.qloo.com/i/ffffe0f9-1773-4d87-b6e2-d24041fe94f5-360x504-outside.webp",
          title: "Book Title 2",
          author: "Someone Famous",
          description:
            "A new adult story about breaking out, moving on, and learning that some loves never die…It’s been almost a year since that night in the attic, since something inside me died, and a new",
        },
        {
          cover:
            "https://images.qloo.com/i/fffff616-b9ef-455e-9336-deec744dfcc8-360x504-outside.webp",
          title: "Book Title 1",
          author: "Someone Famous",
          description:
            "When Carley Sutherland receives a frantic call for help, she races to a desolate park to meet her best friend. On a dimly-lit park bench, Carley's friend fumbles in her handbag for her",
        },
        {
          cover:
            "https://images.qloo.com/i/ffffe0f9-1773-4d87-b6e2-d24041fe94f5-360x504-outside.webp",
          title: "Book Title 2",
          author: "Someone Famous",
          description:
            "A new adult story about breaking out, moving on, and learning that some loves never die…It’s been almost a year since that night in the attic, since something inside me died, and a new",
        },
        {
          cover:
            "https://images.qloo.com/i/fffff616-b9ef-455e-9336-deec744dfcc8-360x504-outside.webp",
          title: "Book Title 1",
          author: "Someone Famous",
          description:
            "When Carley Sutherland receives a frantic call for help, she races to a desolate park to meet her best friend. On a dimly-lit park bench, Carley's friend fumbles in her handbag for her",
        },
        {
          cover:
            "https://images.qloo.com/i/ffffe0f9-1773-4d87-b6e2-d24041fe94f5-360x504-outside.webp",
          title: "Book Title 2",
          author: "Someone Famous",
          description:
            "A new adult story about breaking out, moving on, and learning that some loves never die…It’s been almost a year since that night in the attic, since something inside me died, and a new",
        },
        {
          cover:
            "https://images.qloo.com/i/fffff616-b9ef-455e-9336-deec744dfcc8-360x504-outside.webp",
          title: "Book Title 1",
          author: "Someone Famous",
          description:
            "When Carley Sutherland receives a frantic call for help, she races to a desolate park to meet her best friend. On a dimly-lit park bench, Carley's friend fumbles in her handbag for her",
        },
        {
          cover:
            "https://images.qloo.com/i/ffffe0f9-1773-4d87-b6e2-d24041fe94f5-360x504-outside.webp",
          title: "Book Title 2",
          author: "Someone Famous",
          description:
            "A new adult story about breaking out, moving on, and learning that some loves never die…It’s been almost a year since that night in the attic, since something inside me died, and a new",
        },
        {
          cover:
            "https://images.qloo.com/i/fffff616-b9ef-455e-9336-deec744dfcc8-360x504-outside.webp",
          title: "Book Title 1",
          author: "Someone Famous",
          description:
            "When Carley Sutherland receives a frantic call for help, she races to a desolate park to meet her best friend. On a dimly-lit park bench, Carley's friend fumbles in her handbag for her",
        },
        {
          cover:
            "https://images.qloo.com/i/ffffe0f9-1773-4d87-b6e2-d24041fe94f5-360x504-outside.webp",
          title: "Book Title 2",
          author: "Someone Famous",
          description:
            "A new adult story about breaking out, moving on, and learning that some loves never die…It’s been almost a year since that night in the attic, since something inside me died, and a new",
        },
        {
          cover:
            "https://images.qloo.com/i/fffff616-b9ef-455e-9336-deec744dfcc8-360x504-outside.webp",
          title: "Book Title 1",
          author: "Someone Famous",
          description:
            "When Carley Sutherland receives a frantic call for help, she races to a desolate park to meet her best friend. On a dimly-lit park bench, Carley's friend fumbles in her handbag for her",
        },
        {
          cover:
            "https://images.qloo.com/i/ffffe0f9-1773-4d87-b6e2-d24041fe94f5-360x504-outside.webp",
          title: "Book Title 2",
          author: "Someone Famous",
          description:
            "A new adult story about breaking out, moving on, and learning that some loves never die…It’s been almost a year since that night in the attic, since something inside me died, and a new",
        },
        {
          cover:
            "https://images.qloo.com/i/fffff616-b9ef-455e-9336-deec744dfcc8-360x504-outside.webp",
          title: "Book Title 1",
          author: "Someone Famous",
          description:
            "When Carley Sutherland receives a frantic call for help, she races to a desolate park to meet her best friend. On a dimly-lit park bench, Carley's friend fumbles in her handbag for her",
        },
        {
          cover:
            "https://images.qloo.com/i/ffffe0f9-1773-4d87-b6e2-d24041fe94f5-360x504-outside.webp",
          title: "Book Title 2",
          author: "Someone Famous",
          description:
            "A new adult story about breaking out, moving on, and learning that some loves never die…It’s been almost a year since that night in the attic, since something inside me died, and a new",
        },
        // ...and so on for each book
      ],
    };
  },
};
</script>

<style scoped>
/* Styles specific to this component */
</style>
