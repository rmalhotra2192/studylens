<template>
  <div class="max-w-sm rounded overflow-hidden shadow-lg my-2 bg-white">
    <img class="w-full" :src="bookCover" alt="Book Cover" />
    <div class="px-6 py-4">
      <div class="mb-2">
        <p class="font-bold text-xl text-left">{{ title }}</p>
        <p class="font-light text-sm text-gray-500 text-left">
          by {{ author }}
        </p>
      </div>
      <p class="text-gray-700 text-sm text-left">
        {{ description }}
      </p>
    </div>
    <div class="px-6 pt-4 pb-2">
      <span
        class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
        >#fiction</span
      >
      <span
        class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
        >#mystery</span
      >
    </div>
  </div>
</template>

<script>
export default {
  name: "BookCard",
  props: {
    bookCover: String,
    title: String,
    author: String,
    description: String,
  },
};
</script>

<style scoped>
/* You can add additional styles here if needed */
</style>
