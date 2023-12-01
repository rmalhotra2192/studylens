<template>
  <div class="container text-left mx-auto px-4">
    <h3 class="text-lg font-semibold">
      Showing {{ total }} courses for "{{ searchQuery }}"
    </h3>
    <div class="grid grid-cols-5 gap-4">
      <YTVideoCourseCard
        v-for="(course, index) in courses"
        :key="index"
        :courseThumbnail="course.thumbnail"
        :courseTitle="course.title"
        :channelName="course.channelName"
        :views="course.views"
        :uploadDate="course.uploadDate"
        :videoCount="course.videoCount"
        :courseLength="course.length"
      />
    </div>
  </div>
</template>

<script>
import YTVideoCourseCard from "@/components/Cards/YTVideoCourseCard.vue";

export default {
  name: "YTVideoCoursesGrid",
  components: {
    YTVideoCourseCard,
  },
  data() {
    return {
      courses: [
        {
          thumbnail: "https://i.ytimg.com/vi/xyVfLxV08I0/maxresdefault.jpg",
          title: "Some random video title",
          channelName: "Some channel",
          views: "351K",
          uploadDate: "3rd Oct 2021",
          videoCount: 14,
          length: "5h 37m",
        },
      ],
      total: 6,
      searchQuery: "deep learning",
    };
  },
};
</script>

<style scoped></style>
