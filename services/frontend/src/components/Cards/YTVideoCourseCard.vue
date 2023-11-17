<template>
  <div class="max-w-full rounded overflow-hidden shadow-lg my-2 bg-white">
    <div class="aspect-w-16 aspect-h-9 w-full bg-black">
      <div
        class="w-full h-full bg-center bg-cover"
        :style="{ backgroundImage: `url('${courseThumbnail}')` }"
      >
        <div class="absolute inset-0 flex justify-end items-start p-2">
          <button
            class="opacity-95 hover:opacity-100 bg-white hover:bg-white text-gray-500 hover:text-cyan-500 font-bold py-0 px-1 mr-2 rounded shadow-md transition-all duration-200 ease-in-out delay-0"
            @click="toggleLike"
          >
            <i class="fas fa-plus text-sm"></i>
          </button>
          <button
            class="opacity-95 hover:opacity-100 bg-white hover:bg-white text-gray-500 hover:text-cyan-500 font-bold py-0 px-1 rounded shadow-md transition-all duration-200 ease-in-out delay-0"
            @click="toggleLike"
          >
            <i class="fas fa-thumbs-up text-sm"></i>
          </button>
        </div>
      </div>
    </div>
    <div class="p-4">
      <div class="text-left">
        <p class="font-bold text-md">{{ courseTitle }}</p>
        <p class="text-gray-500 text-sm text-left mb-1">{{ channelName }}</p>
        <p class="text-gray-500 text-sm">
          {{ videoCount }} videos • {{ courseLength }}
        </p>
        <p class="text-gray-500 text-sm">
          {{ views }} views • {{ uploadDate }}
        </p>
      </div>
    </div>
    <div class="px-4 text-left mb-2">
      <span
        class="inline-block bg-gray-200 rounded-full px-2 py-1 text-xs font-semibold text-gray-700 mr-1 mb-1"
        >Beginner</span
      >
    </div>
  </div>
</template>

<script>
export default {
  name: "YTVideoCourseCard",
  props: {
    courseThumbnail: String,
    courseTitle: String,
    channelName: String,
    views: String,
    videoCount: Number,
    courseLength: String,
    uploadDate: String,
  },
  methods: {
    toggleLike() {
      console.log("Like button clicked!");
    },
    addToPlaylist() {
      console.log("Add to playlist button clicked!");
    },
  },
};
</script>

<style scoped></style>
