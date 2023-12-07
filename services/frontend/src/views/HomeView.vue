<template>
  <CustomNavbar />
  <div
    class="relative w-full bg-cover bg-center bg-no-repeat"
    :style="{
      backgroundImage: 'url(' + homepageBackground + ')',
      minHeight: 'calc(100vh - 70px)',
    }"
  >
    <div
      class="absolute inset-0 bg-white bg-opacity-5 backdrop-blur z-10"
    ></div>
    <div class="container relative mx-auto pt-20 md:pt-32 lg:pt-64 z-20">
      <div class="items-center flex flex-wrap">
        <div class="w-full lg:w-10/12 px-4 ml-auto mr-auto text-center">
          <div class="pr-12">
            <h1 class="text-gray-700 font-semibold text-5xl">
              Tired of searching for Data Science resouces all over internet?
            </h1>
            <p class="mt-4 text-lg text-gray-500">
              Look no further! Dive into a vast ocean of knowledge with our
              curated selection. Discover an expansive library featuring over
              <b>5,000 books</b>, <b>1,500+ insightful videos</b>, and
              <b>250+ comprehensive courses</b>, all tailored to your Data
              Science learning needs. Your one-stop destination for top-tier
              Data Science resources is here.
            </p>
            <input
              id="search"
              ref="searchInput"
              v-model="searchQuery"
              type="text"
              placeholder="Enter search query"
              class="text-center w-7/12 display-block px-4 py-3 border-0 border-b-2 border-gray-700 outline-0 active:outline-none focus:outline-none placeholder-gray-400 text-xl"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
  <section class="pb-48">
    <div class="container mx-auto px-4 w-full">
      <div class="flex flex-wrap justify-center text-center mb-12">
        <div class="w-full lg:w-10/12 px-4">
          <h2 class="text-gray-700 font-semibold text-5xl">
            Our Data Partners
          </h2>
          <p class="mt-4 text-lg text-gray-500">
            We bring together a wide range of high-quality resources from
            trusted content platforms and data providers. Our goal is simple: to
            create an ever-growing, comprehensive list of the best data science
            materials available. Below are some of our valued data partners who
            play a key role in helping us achieve this mission.
          </p>
        </div>
      </div>
      <div class="flex flex-wrap">
        <div
          class="flex items-center justify-center w-full md:w-6/12 lg:w-2/12 lg:mb-0 mb-12 px-4"
        >
          <div class="flex items-center justify-center px-6">
            <img
              src="../assets/img/logo-google.svg"
              class="rounded-semi mx-auto max-w-250-px"
            />
          </div>
        </div>
        <div
          class="flex items-center justify-center w-full md:w-6/12 lg:w-2/12 lg:mb-0 mb-12 px-4"
        >
          <div class="flex items-center justify-center px-6">
            <img
              src="../assets/img/logo-open-library.svg"
              class="rounded-semi mx-auto max-w-250-px"
            />
          </div>
        </div>
        <div
          class="flex items-center justify-center w-full md:w-6/12 lg:w-2/12 lg:mb-0 mb-12 px-4"
        >
          <div class="flex items-center justify-center px-6">
            <img
              src="../assets/img/logo-youtube.svg"
              class="rounded-semi mx-auto max-w-250-px"
            />
          </div>
        </div>
        <div
          class="flex items-center justify-center w-full md:w-6/12 lg:w-2/12 lg:mb-0 mb-12 px-4"
        >
          <div class="flex items-center justify-center px-6">
            <img
              src="../assets/img/logo-amazon.svg"
              class="rounded-semi mx-auto max-w-250-px"
            />
          </div>
        </div>
        <div
          class="flex items-center justify-center w-full md:w-6/12 lg:w-2/12 lg:mb-0 mb-12 px-4"
        >
          <div class="flex items-center justify-center px-6">
            <img
              src="../assets/img/logo-udemy.svg"
              class="rounded-semi mx-auto max-w-250-px"
            />
          </div>
        </div>
        <div
          class="flex items-center justify-center w-full md:w-6/12 lg:w-2/12 lg:mb-0 mb-12 px-4"
        >
          <div class="flex items-center justify-center px-6">
            <img
              src="../assets/img/logo-coursera.svg"
              class="rounded-semi mx-auto max-w-250-px"
            />
          </div>
        </div>
      </div>
    </div>
  </section>
  <FooterSmall />
</template>

<script>
import homepageBackground from "@/assets/img/homepage_background.jpg";
import CustomNavbar from "@/components/Navbars/CustomNavbar.vue";
import FooterSmall from "@/components/Footers/FooterSmall.vue";
export default {
  data() {
    return {
      homepageBackground,
      searchQuery: "",
    };
  },
  mounted() {
    this.run();
  },
  components: {
    CustomNavbar,
    FooterSmall,
  },
  methods: {
    addToPlaceholder(toAdd, el) {
      const currentPlaceholder = el.getAttribute("placeholder") || "";
      el.setAttribute("placeholder", currentPlaceholder + toAdd);
      return new Promise((resolve) => setTimeout(resolve, 100));
    },
    clearPlaceholder(el) {
      el.setAttribute("placeholder", "");
    },
    printPhrase(phrase, el) {
      return new Promise((resolve) => {
        this.clearPlaceholder(el);
        let letters = phrase.split("");
        letters.reduce(
          (promise, letter, index) =>
            promise.then(() => {
              if (index === letters.length - 1) {
                setTimeout(resolve, 1000);
              }
              return this.addToPlaceholder(letter, el);
            }),
          Promise.resolve()
        );
      });
    },
    printPhrases(phrases, el) {
      phrases.reduce(
        (promise, phrase) => promise.then(() => this.printPhrase(phrase, el)),
        Promise.resolve()
      );
    },
    run() {
      let phrases = [
        "Beginner Resources on Python Programming",
        "I want to learn about Topic Modelling in Data Science",
      ];

      this.printPhrases(phrases, this.$refs.searchInput);
    },
  },
};
</script>

<style></style>
