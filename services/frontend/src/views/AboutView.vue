<template>
  <div class="flex flex-wrap">
    <div class="w-full">
      <ul class="flex mb-0 list-none flex-wrap pt-3 pb-4 flex-row">
        <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
          <a
            class="text-xs font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal"
            v-on:click="toggleTabs(1)"
            v-bind:class="{
              'text-emerald-600 bg-white': openTab !== 1,
              'text-white bg-emerald-600': openTab === 1,
            }"
          >
            <i class="fas fa-book text-base mr-1"></i> Books
          </a>
        </li>
        <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
          <a
            class="text-xs font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal"
            v-on:click="toggleTabs(2)"
            v-bind:class="{
              'text-emerald-600 bg-white': openTab !== 2,
              'text-white bg-emerald-600': openTab === 2,
            }"
          >
            <i class="fas fa-video text-base mr-1"></i> Single Youtube Videos
          </a>
        </li>
        <li class="-mb-px mr-2 last:mr-0 flex-auto text-center">
          <a
            class="text-xs font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal"
            v-on:click="toggleTabs(3)"
            v-bind:class="{
              'text-emerald-600 bg-white': openTab !== 3,
              'text-white bg-emerald-600': openTab === 3,
            }"
          >
            <i class="fas fa-certificate text-base mr-1"></i> Video Courses
          </a>
        </li>
      </ul>
      <div
        class="relative flex flex-col min-w-0 break-words bg-white w-full mb-6"
      >
        <div class="px-4 py-5 flex-auto">
          <div class="tab-content tab-space">
            <div v-bind:class="{ hidden: openTab !== 1, block: openTab === 1 }">
              <BooksGrid />
            </div>
            <div v-bind:class="{ hidden: openTab !== 2, block: openTab === 2 }">
              <SingleVideosGrid />
            </div>
            <div v-bind:class="{ hidden: openTab !== 3, block: openTab === 3 }">
              <YTVideoCoursesGrid />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import BooksGrid from "@/components/Grids/BooksGrid.vue";
import SingleVideosGrid from "@/components/Grids/SingleVideosGrid.vue";
import YTVideoCoursesGrid from "@/components/Grids/YTVideoCoursesGrid.vue";
export default {
  components: {
    BooksGrid,
    SingleVideosGrid,
    YTVideoCoursesGrid,
  },
  data() {
    return {
      openTab: 1,
    };
  },
  methods: {
    toggleTabs: function (tabNumber) {
      this.openTab = tabNumber;
    },
  },
};
</script>
