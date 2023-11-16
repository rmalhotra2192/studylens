<template>
  <div class="container mx-auto px-4">
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
    };
  },
};
</script>

<style scoped></style>
