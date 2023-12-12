<template>
  <div>
    <div
      v-if="show"
      class="fixed inset-0 z-50 flex items-center justify-center overflow-x-hidden overflow-y-auto outline-none focus:outline-none"
    >
      <div class="relative my-6 mx-auto w-11/12 md:w-3/4 xl:max-w-6xl">
        <div
          class="flex flex-col w-full bg-white rounded-lg shadow-lg outline-none focus:outline-none"
        >
          <div class="flex items-start justify-between p-5 border-b rounded-t">
            <h3 class="text-2xl font-semibold">
              {{ book.title }}
            </h3>
            <button
              class="p-1 ml-auto bg-transparent border-0 text-black float-right text-3xl leading-none font-semibold outline-none focus:outline-none"
              @click="toggleModal"
            >
              <span class="text-black h-6 w-6 text-2xl block"> × </span>
            </button>
          </div>

          <div class="relative p-6 flex-auto">
            <div class="flex">
              <div class="w-1/3">
                <img
                  :src="book.thumbnail_from_google"
                  alt="Book Cover"
                  class="object-contain w-full rounded"
                />
              </div>
              <div class="w-2/3 pl-4 text-left">
                <p class="text-lg leading-relaxed mb-1">
                  <strong>Author(s):</strong> {{ book.authors }}
                </p>
                <!-- <p class="text-lg leading-relaxed mb-1">
                  <strong>Rating:</strong> {{ book.rating.toFixed(1) }}
                </p> -->
                <p class="text-lg leading-relaxed mb-1">
                  <strong>Domains:</strong> {{ book.domains }}
                </p>
                <p class="text-lg leading-relaxed mb-4">
                  <strong>Difficulty Level:</strong>
                  {{ book.difficulty }}
                </p>
                <!-- <p class="text-lg leading-relaxed mb-4">
                  {{ book.rating.toFixed(1) }}
                </p> -->
              </div>
            </div>
          </div>

          <div
            class="flex items-center justify-end p-6 border-t border-solid border-blueGray-200 rounded-b"
          >
            <button
              class="text-red-500 background-transparent font-bold uppercase px-6 py-2 text-sm outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
              @click="toggleModal"
            >
              Close
            </button>
          </div>
        </div>
      </div>
    </div>
    <div v-if="show" class="fixed inset-0 z-40 bg-black opacity-25"></div>
  </div>
</template>

<script>
export default {
  name: "LargeModal",
  props: {
    book: Object,
    show: Boolean,
  },
  methods: {
    toggleModal: function () {
      this.$emit("close");
    },
  },
};
</script>
