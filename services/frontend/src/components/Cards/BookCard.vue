<template>
  <div
    @click="emitBookSelect"
    class="flex max-w-full bg-white rounded-semi overflow-hidden shadow-lg mt-2 mb-1 cursor-pointer"
  >
    <div class="w-1/3">
      <img
        class="object-cover mx-auto py-2 h-64 rounded-semi"
        :src="book.thumbnail_from_google"
        alt="Book Cover"
      />
    </div>

    <div class="w-2/3 px-6 py-4 flex flex-col justify-left">
      <div>
        <p class="font-bold text-lg">{{ book.title }}</p>
        <p class="font-light text-sm text-gray-500">by {{ book.authors }}</p>
        <span
          class="inline-block bg-gray-200 rounded-full mt-2 px-2 py-1 text-xs font-semibold text-gray-700 mr-1 mb-1"
          >{{ book.difficulty }}</span
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "BookCard",
  props: {
    book: {
      type: Object,
      required: true,
    },
  },
  methods: {
    toggleLike() {
      console.log("Like button clicked!");
    },
    emitBookSelect() {
      this.$emit("select", this.book);
    },
  },
};
</script>

<style scoped></style>
