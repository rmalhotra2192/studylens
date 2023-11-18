<template>
  <div
    class="max-w-sm rounded overflow-hidden shadow-lg mt-2 mb-1 bg-white relative"
  >
    <div class="relative">
      <!-- Overlay to darken the image -->
      <div class="absolute inset-0 bg-black opacity-25"></div>

      <img
        class="h-32 md:h-64 lg:h-96 object-fill w-full"
        :src="bookCover"
        alt="Book Cover"
      />
      <!-- Your buttons will now be more visible on the darkened cover -->
      <button
        class="absolute top-2 right-12 opacity-95 hover:opacity-100 bg-white hover:bg-white text-gray-500 hover:text-cyan-500 font-bold py-1 px-2 rounded shadow-md transition-all duration-200 ease-in-out delay-0"
        @click="toggleLike"
      >
        <i class="fas fa-plus"></i>
      </button>
      <button
        class="absolute top-2 right-2 opacity-95 hover:opacity-100 bg-white hover:bg-white text-gray-500 hover:text-cyan-500 font-bold py-1 px-2 rounded shadow-md transition-all duration-200 ease-in-out delay-0"
        @click="toggleLike"
      >
        <i class="fas fa-thumbs-up"></i>
      </button>
    </div>
    <div class="px-6 pt-4 pb-2">
      <div class="mb-2">
        <p class="font-bold text-lg text-left">{{ title }}</p>
        <p class="font-light text-sm text-gray-500 text-left">
          by {{ author }}
        </p>
      </div>
      <div class="flex items-center">
        <div class="flex text-left text-yellow-400">
          <template
            v-for="index in Math.floor(rating)"
            :key="'filled-' + index"
          >
            <i class="fas fa-star"></i>
          </template>
          <template v-if="!Number.isInteger(rating)">
            <i class="fas fa-star-half-alt" :key="Math.floor(rating)"></i>
          </template>
          <template
            v-for="index in 5 - Math.ceil(rating)"
            :key="'outlined-' + index"
          >
            <i class="far fa-star"></i>
          </template>
        </div>
        <span class="ml-2 text-gray-600 text-sm"
          >({{ rating.toFixed(1) }})</span
        >
      </div>
    </div>

    <div class="px-6 py-2 text-left">
      <span
        class="inline-block bg-gray-200 rounded-full px-2 py-1 text-sm font-semibold text-gray-700 mr-1 mb-1"
        >Amazon</span
      >
      <span
        class="inline-block bg-gray-200 rounded-full px-2 py-1 text-sm font-semibold text-gray-700 mr-1 mb-1"
        >Barnes & Noble</span
      >
      <span
        class="inline-block bg-gray-200 rounded-full px-2 py-1 text-sm font-semibold text-gray-700 mr-1 mb-1"
        >Goodreads</span
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
    rating: Number,
  },
  methods: {
    toggleLike() {
      console.log("Like button clicked!");
    },
  },
};
</script>

<style scoped></style>
