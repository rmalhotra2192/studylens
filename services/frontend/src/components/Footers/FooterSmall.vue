<template>
  <footer
    class="pb-6"
    :class="[
      absolute ? 'absolute w-full bottom-0 bg-blueGray-800' : 'relative',
    ]"
  >
    <div class="container mx-auto px-4">
      <hr class="mb-6 border-b-1 border-blueGray-600" />
      <div
        class="flex flex-wrap items-center md:justify-between justify-center"
      >
        <div class="w-full md:w-4/12 px-4">
          <div
            class="text-sm text-blueGray-500 font-semibold py-1 text-center md:text-left"
          >
            Copyright © {{ date }}
            <a
              href="https://www.creative-tim.com?ref=vn-footer-small"
              class="text-white hover:text-blueGray-300 text-sm font-semibold py-1"
            >
              Study Lens
            </a>
          </div>
        </div>
        <div class="w-full md:w-8/12 px-4">
          <div
            class="text-sm text-blueGray-500 font-semibold py-1 text-right md:text-right"
          >
            Engineered by
            <a
              href="https://github.com/rmalhotra2192/"
              target="_blank"
              class="text-blueGray-500 hover:text-blue-400 text-sm font-semibold py-1 underline"
            >
              Rishabh Malhotra
            </a>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  data() {
    return {
      date: new Date().getFullYear(),
    };
  },
  props: {
    absolute: {
      type: Boolean,
      default: false,
    },
  },
};
</script>
