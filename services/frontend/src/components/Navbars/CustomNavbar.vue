<template>
  <nav class="flex items-center justify-between py-3 px-40">
    <router-link to="/" class="text-2xl font-bold text-emerald-600">StudyLens</router-link>

    <!-- <div>
      <template v-if="!isAuthenticated">
        <router-link to="/signup" class="mr-4">Sign Up</router-link>
        <router-link to="/signin">Sign In</router-link>
      </template>
      <template v-else>
        <div class="relative" @click="toggleDropdown">
          <img
            src="https://gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50"
            alt="User"
            class="h-12 w-12 rounded-full cursor-pointer"
          />
          <div
            v-if="dropdownOpen"
            class="absolute right-0 mt-2 py-2 w-48 bg-white rounded-md shadow-xl z-50"
          >
            <a
              href="#"
              class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
              >Log Out</a
            >
          </div>
        </div>
      </template>
    </div> -->
  </nav>
</template>

<script>
export default {
  name: "CustomNavbar",
  data() {
    return {
      isAuthenticated: true,
      dropdownOpen: false,
    };
  },
  methods: {
    toggleDropdown() {
      this.dropdownOpen = !this.dropdownOpen;
    },
  },
};
</script>

<style scoped></style>
