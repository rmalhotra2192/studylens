<template>
  <CustomNavbar />
  <div class="flex justify-center mt-10">
    <div class="max-w-80">
      <ul class="flex mb-0 list-none flex-wrap pt-3 pb-4 flex-row">
        <li class="-mb-px mr-2 last:mr-0 flex-auto text-center cursor-pointer">
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
        <li class="-mb-px mr-2 last:mr-0 flex-auto text-center cursor-pointer">
          <a
            class="text-xs font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal"
            v-bind:class="{
              'text-emerald-600 bg-white': openTab !== 2,
              'text-white bg-emerald-600': openTab === 2,
            }"
          >
            <div class="relative">
              <i class="fas fa-video text-base mr-1"></i>Videos

              <span
                class="absolute lowercase top-0 right-0 inline-block rounded px-1 py-1 text-xs font-semibold mr-1"
                v-bind:class="{
                  'text-white bg-emerald-600': openTab !== 2,
                  'text-emerald-600 bg-white': openTab === 2,
                }"
              >
                Coming Soon
              </span>
            </div>
          </a>
        </li>
        <li class="-mb-px mr-2 last:mr-0 flex-auto text-center cursor-pointer">
          <a
            class="text-xs font-bold uppercase px-5 py-3 shadow-lg rounded block leading-normal"
            v-bind:class="{
              'text-emerald-600 bg-white': openTab !== 3,
              'text-white bg-emerald-600': openTab === 3,
            }"
          >
            <div class="relative">
              <i class="fas fa-certificate text-base mr-1"></i>Courses

              <span
                class="absolute lowercase top-0 right-0 inline-block rounded px-1 py-1 text-xs font-semibold mr-1"
                v-bind:class="{
                  'text-white bg-emerald-600': openTab !== 3,
                  'text-emerald-600 bg-white': openTab === 3,
                }"
              >
                Coming Soon
              </span>
            </div>
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
          </div>
        </div>
      </div>
    </div>
  </div>
  <FooterSmall />
</template>

<script>
import CustomNavbar from "@/components/Navbars/CustomNavbar.vue";
import BooksGrid from "@/components/Grids/BooksGrid.vue";
import FooterSmall from "@/components/Footers/FooterSmall.vue";
export default {
  components: {
    CustomNavbar,
    BooksGrid,
    FooterSmall,
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
