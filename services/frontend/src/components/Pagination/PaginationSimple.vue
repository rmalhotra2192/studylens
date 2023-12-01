<template>
  <div>
    <button
      class="mx-1 px-4 py-2 bg-gray-200 text-gray-800 rounded"
      @click="prevPage"
      :disabled="currentPage === 1"
    >
      Prev
    </button>
    <button
      class="mx-1 px-4 py-2 bg-gray-200 text-gray-800 rounded"
      v-for="page in totalPages"
      :key="page"
      :class="{ 'bg-blue-500 text-white': page === currentPage }"
      @click="goToPage(page)"
    >
      {{ page }}
    </button>
    <button
      class="mx-1 px-4 py-2 bg-gray-200 text-gray-800 rounded"
      @click="nextPage"
      :disabled="currentPage === totalPages"
    >
      Next
    </button>
  </div>
</template>

<script>
export default {
  name: "PaginationSimple",
  props: {
    totalPages: {
      type: Number,
      required: true,
    },
    value: {
      type: Number,
      default: 1,
    },
  },
  methods: {
    prevPage() {
      if (this.value > 1) this.$emit("input", this.value - 1);
    },
    nextPage() {
      if (this.value < this.totalPages) this.$emit("input", this.value + 1);
    },
    goToPage(page) {
      this.$emit("input", page);
    },
  },
};
</script>

<style scoped></style>
